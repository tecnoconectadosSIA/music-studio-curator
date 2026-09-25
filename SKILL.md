---
name: music-studio-curator
description: Automatización y curaduría de bibliotecas musicales con calidad de estudio profesional. Repara etiquetas ID3 (v2.3/v2.4), limpia ruido de títulos/artistas (VEVO, Official Video, track numbers, webs), detecta duplicados por huella acústica/metadatos y conserva siempre la copia de máxima fidelidad (bitrate, formato, frecuencia de muestreo) con archivado seguro en cuarentena.
---

# 🎵 Music Studio Curator (Skill de Curaduría de Audio Profesional)

Este skill proporciona un pipeline industrial de grado de estudio para la auditoría, desofuscación, normalización de metadatos ID3 y deduplicación certificada de bibliotecas musicales masivas sin pérdida de fidelidad sonora.

---

## 🏛️ Principios Fundamentales y Reglas de Oro

1. **Integridad de Contenido (No Destructivo)**:
   - **NUNCA borrar pistas originales**. Todo duplicado o archivo degradado debe ser trasladado a `_Duplicados_Eliminados/` con bitácora auditable.
   - Antes de retirar o sustituir una pista, **certificar rigurosamente** que una copia idéntica o de calidad superior (mayor bitrate / formato) permanece activa en la biblioteca.

2. **Diferenciación de Versiones Legítimas vs. Duplicados Técnicos**:
   - **Son versiones independientes y legítimas**: Pistas en vivo (`En Vivo`, `Live`), acústicas, duetos, remixes oficiales, mini-conciertos (`Free Cover`), sesiones de estudio alternativas (`MTV Unplugged`, `Corona Music Sessions`), tomas instrumentales y versiones extendidas/de video con intros narrativos.
   - **Criterio de Duplicado Técnico Real**: Mismo contenido musical donde $| \text{duración}_A - \text{duración}_B | \le 3.0\,\text{s}$ y ambas representan la misma toma sonora.
   - **Resolución de Duplicados**: El archivo con mayor bitrate o formato superior (.flac > .m4a > .mp3 320k > 192k > 128k) retiene el nombre canónico y las etiquetas completas; la copia inferior se archiva en cuarentena.

3. **Sintaxis de Archivo y Compatibilidad con Windows**:
   - Estructura universal obligatoria: `Artista - Título.ext`.
   - Prohibición absoluta de caracteres ilegales en Windows (`:`, `*`, `?`, `"`, `<`, `>`, `|`, `/`, `\`). Los medleys o subtítulos deben usar comas o guiones (ej. `Guaco - Medley - Noche Sensacional, El Billetero (En Vivo).mp3`).
   - Detección y corrección obligatoria de paréntesis o corchetes no balanceados o truncados (`(` sin `)`, `]` sin `[`).

---

## 🛠️ Pipeline de Ejecución de 5 Fases

```mermaid
flowchart TD
    A["Fase 1: Escaneo y Detección de Anomalías"] --> B["Fase 2: Desofuscación y Fonética (Speech / AudD)"]
    B --> C["Fase 3: Normalización de Colaboraciones y Tipografía"]
    C --> D["Fase 4: Deduplicación Cruzada por Fidelidad Técnica"]
    D --> E["Fase 5: Inyección ID3v2.3 y Certificación Final"]
```

### Fase 1: Escaneo de Patrones Parásitos y Estructuras Invertidas
- **Detección de Títulos Invertidos**: Archivos donde el artista aparece en la segunda mitad (`Título - Artista`). Se cotejan contra el diccionario canónico de artistas (`KNOWN_ARTISTS`).
- **Eliminación de Prefijos de Bandas Sonoras**: Desmontar etiquetas genéricas como `Various Artists - Artista – Título` y restaurar la autoría original.
- **Purgado de Ruido Residual**: Remover `[OFFICIAL VIDEO]`, `(Video Oficial)`, `(Letra / Lyrics)`, `(Prod. By ...)`, `(Audio Original)`, canales de YouTube, nombres de uploaders (`by Gabrielpauta`, `Lanzamientosmp3`) y años residuales en sufijos (`(reggaeton 2016)`).

### Fase 2: Desofuscación Fonética y Huella Acústica
- **Prohibición de Nombres Genéricos**: Prohibir nombres como `Track X`, `Pista X`, `Video Oficial`, `Salsa Baúl` o códigos alfanuméricos (`Mtrr`, hashes).
- **Extracción Fonética**: Si la huella acústica no tiene match (música latina regional o medleys):
  1. Extraer clip de 25–30 segundos con `ffmpeg` a 16 kHz mono.
  2. Transcribir letra mediante `speech_recognition` (Google Speech API en español o inglés).
  3. Identificar lírica oficial y reconstruir el título y artista auténticos.

### Fase 3: Estandarización de Colaboraciones y Tipografía
- Unificar todas las fórmulas de colaboración al estándar canónico:
  - `con X`, `ft. X`, `ft X`, `feat X`, `, X`, `x X`, `a Dúo con X` ➡️ `feat. X` o `& X`.
- Formateo editorial con tildes y diéresis correctas (ej. `Mägo de Oz`, `OneRepublic`, `Qué Quieres de Mí`, `Abrázame`, `Corazón Abierto`).

### Fase 4: Deduplicación Cruzada
- Agrupar por clave canónica normalizada (NFKD: minúsculas, sin tildes, sin signos de puntuación).
- Comparar duraciones y tasas de bits:
  * Si $\Delta \text{duración} \le 3.0\,\text{s}$: Conservar el archivo de máxima tasa de bits y trasladar el inferior a `_Duplicados_Eliminados/`.
  * Si $\Delta \text{duración} > 5.0\,\text{s}$: Mantener ambas versiones, asignando sufijos descriptivos claros (`(Versión Radio)`, `(Versión Extendida)`, `(En Vivo)`).

### Fase 5: Inyección de Metadatos ID3v2.3
- Inyectar etiquetas limpias y exactas compatibles universalmente:
  * `TPE1` (Artista principal y colaboradores)
  * `TIT2` (Título limpio sin parásitos)
  * `TALB` (Álbum oficial con tildes)
  * `TRCK` (Número de pista en álbumes y conciertos estructurados)
