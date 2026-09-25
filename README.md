# 📻 Music Studio Curator
### Broadcast-Grade Audio Curation, Acoustic Fingerprinting & On-Air Metadata Automation

<p align="center">
  <a href="README.md"><b>Español</b></a> •
  <a href="README.en.md"><b>English</b></a> •
  <a href="README.it.md"><b>Italiano</b></a>
</p>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![AcoustID](https://img.shields.io/badge/AcoustID-Chromaprint%201.6.1-green.svg)](https://acoustid.org/)
[![Broadcast Standard](https://img.shields.io/badge/Broadcast-EBU%20R128%20%2F%20RDS%20Ready-red.svg)]()
[![AI Agent Ready](https://img.shields.io/badge/AI%20Agent-Antigravity%20%7C%20Claude%20%7C%20OpenCode%20%7C%20Codex-purple.svg)]()

> **Desarrollado y mantenido por:** **Ricardo Montero** ([@tecnoconectadosSIA](https://github.com/tecnoconectadosSIA))  
> *Broadcaster, Consultor de Automatización Radial e Ingeniero de Audio.*

---

## 🎙️ Manifiesto del Broadcaster: Por qué nació esta herramienta

En la radiodifusión profesional (FM, DAB+, Web Radio y cadenas satelitales), los metadatos **no son un adorno cosmético: son infraestructura crítica de emisión**.

Cuando una pista se inserta en un sistema de automatización y *playout* comercial (**RCS Master Control, Dalet, WideOrbit, RadioDJ, ZaraRadio o Dinesat**):
1. **El RDS dinámico y el Stream Web** transmiten el artista y el título en tiempo real a las pantallas de los receptores en automóviles, sintonizadores digitales y apps móviles. Un tema invertido como `Lrad - Knife Party` o con sufijos como `(Video Oficial HD)` arruina la imagen corporativa de la estación.
2. **Las Sociedades de Gestión Colectiva de Derechos** (SGAE, BMI, ASCAP, SACVEN, SIAE) auditan los registros de emisión basados en los códigos ISRC y metadatos ID3. Si un archivo está mal etiquetado, la emisora incurre en multas, regalías erróneas o reportes rechazados.
3. **El Procesamiento de Audio On-Air** (Orban Optimod, Omnia) amplifica de forma brutal cualquier artefacto de compresión por debajo de 192 kbps. Transmitir un archivo de 32 kbps o 64 kbps por aire destruye la cadena de modulación y genera fatiga auditiva inmediata en la audiencia.
4. **Cero Aire Muerto y Cero Falsos Nombres**: No se puede emitir una pista como `Makj - Generic` cuando en realidad suena un clásico de Progressive Trance de `Kyau & Albert`.

Las herramientas tradicionales de tagging de escritorio (**MusicBrainz Picard**, **beets**) fueron creadas para usuarios domésticos con álbumes comerciales de estudio en CD. Cuando un broadcaster se enfrenta a grabaciones en vivo, sesiones exclusivas (*Free Cover*), bootlegs de festivales, temas acústicos de cabina o extracciones de transmisiones, esos programas **fallan, se detienen o exigen intervención manual archivo por archivo**.

Por esta razón diseñé **Music Studio Curator**: un estándar de grado de radiodifusión que unifica **huella acústica espectral (Chromaprint / AcoustID)**, **desofuscación lírica fonética asistida por IA (Speech-to-Text)** y un **pipeline de deduplicación no destructiva con preservación estricta de fidelidad acústica**.

---

## 🏛️ Pipeline de Curaduría en 5 Fases

```mermaid
flowchart TD
    A["Directorio Maestro de Audio (Playout / Music Bank)"] --> B["Fase 1: Auditoría Broadcast & Limpieza de Parásitos"]
    B --> C{"¿Coincidencia Espectral en MusicBrainz?"}
    C -->|Sí (Score ≥ 0.90)| D["Fase 2A: Resolución Acústica (Chromaprint / AcoustID)"]
    C -->|No / Sesión Especial| E["Fase 2B: Desofuscación Fonética Lírica por IA (Speech-to-Text)"]
    D --> F["Fase 3: Estandarización On-Air & Normalización de Feats"]
    E --> F
    F --> G["Fase 4: Deduplicación Jerárquica por Bitrate de Emisión"]
    G --> H{"¿Pistas Idénticas (|Δt| ≤ 3s)?"}
    H -->|Sí: Duplicado Técnico| I["Aislamiento Seguro en _Duplicados_Eliminados/"]
    H -->|No: Versión Alterna| J["Certificar y Preservar (Live, Acústico, Free Cover, Remix)"]
    G --> K["Fase 5: Inyección ID3v2.3 Broadcast Ready & Reporte CSV"]
```

### 1. Auditoría Broadcast y Detección de Inversiones
- **Detección Inversa Bidireccional (`Título - Artista` ➡️ `Artista - Título`)**: Cotejo contra base de datos canónica de radiodifusión para revertir pistas erradas sin perder metadatos.
- **Purga de Prefijos de Compilación**: Desmonta etiquetas genéricas de bandas sonoras (`Various Artists - Artista – Título`) y restaura la autoría original.
- **Eliminación de Ruido Técnico**: Suprime parásitos como `(Video Oficial)`, `(Prod. By ...)`, `(by Gabrielpauta)`, `(Audio Original)`, canales de YouTube, nombres de uploaders y menciones web.

### 2. Motor Híbrido de Identificación (Espectral + Fonético)
- **Nivel 1 (Huella Acústica Chromaprint / AcoustID)**: Análisis espectral mediante el binario nativo `fpcalc.exe` 1.6.1. Identifica el audio real aunque el nombre sea falso o una pista huérfana.
- **Nivel 2 (IA Fonética Multilingüe)**: Para gaitas, piezas regionales, bootlegs de cabina o temas no indexados comercialmente, extrae un fragmento de 25 segundos y transcribe la letra cantada mediante IA (Google Speech en español, inglés o italiano) para recuperar la identidad original.

### 3. Normalización Editorial para Sistemas Playout
- Formateo tipográfico canónico compatible con RDS y codificación UTF-8 / Windows Media:
  * Estandarización de colaboradores: `con`, `ft.`, `feat`, `,`, `x`, `vs.` ➡️ `feat.` o `&`.
  * Preservación estricta de ortografía y diacríticos (`Mägo de Oz`, `OneRepublic`, `Qué Quieres de Mí`, `Abrázame`).
  * Eliminación de caracteres ilegales en Windows (`: , " ? * < > |`) y balanceo obligatorio de paréntesis y corchetes.

### 4. Deduplicación Jerárquica de Fidelidad (Cero Pérdida de Datos)
- **Regla de Oro**: Ninguna pista original se elimina.
- Si dos archivos poseen la misma señal ($| \Delta \text{duración} | \le 3.0\,\text{s}$), la copia con mayor tasa de bits (320 kbps > 256 kbps > 192 kbps > 128 kbps) se mantiene en el banco activo de emisión y la versión inferior se traslada a `_Duplicados_Eliminados/`.
- **Protección de Tomas Alternas**: Conciertos en vivo (`En Vivo`, `Live`), acústicos de cabina, sesiones *Free Cover* y remixes se protegen como piezas únicas independientes.

### 5. Auto-Upgrade de Masters Degradados
- Si se detectan pistas en tasas de bits críticas (< 96 kbps) o fragmentos cortados, el pipeline busca automáticamente la versión original de estudio en YouTube Music a través de `yt-dlp`, la compila a 320 kbps con FFmpeg y reemplaza el master defectuoso.

---

## 🤖 Compatibilidad Multi-Agente (AI Ecosystem)

Este framework está optimizado para integrarse de forma nativa en los principales asistentes y agentes de código del mundo:

| Plataforma / Entorno | Tipo de Integración | Ubicación de Instalación |
|---|---|---|
| **Google Antigravity** | Native Skill | `~/.gemini/config/skills/music-studio-curator/SKILL.md` |
| **Claude Code** (Anthropic) | System Skill / `CLAUDE.md` | `.claude/skills/music-studio-curator/` o en `CLAUDE.md` |
| **OpenCode** | Agent Skill | `.opencode/skills/music-studio-curator/` |
| **OpenAI Codex / ChatGPT Operator** | Custom Instructions / Action | Copiar directivas de `SKILL.md` |
| **Cursor & Windsurf** | Rule File | `.cursorrules` / `.windsurfrules` |
| **Aider & Roo Code** | Contexual Prompt | `.aider.conf.yml` / System Prompt |
| **Headless Linux / Windows Server** | Standalone Python CLI | `python curate_music.py --dir /var/music` |

---

## 📦 Instalación y Puesta en Marcha

### Prerrequisitos de Emisión
* **Python 3.10** o superior.
* **FFmpeg** configurado en el `PATH` del sistema.
* **Chromaprint (`fpcalc.exe`)**: Incluido en la carpeta `bin/` para Windows 64-bit o descargable para Linux/macOS desde [acoustid.org/chromaprint](https://acoustid.org/chromaprint).

```bash
# 1. Clonar el repositorio
git clone https://github.com/tecnoconectadosSIA/music-studio-curator.git
cd music-studio-curator

# 2. Instalar dependencias
pip install -r requirements.txt
```

---

## 💻 Guía de Operaciones CLI

### 1. Auditoría Rápida sin Alterar Archivos (Dry-Run de Cabina)
```bash
python curate_music.py --dir "E:\Musica" --dry-run
```

### 2. Identificación de Pista Huérfana o Falsificada vía Huella Acústica
```bash
python acoustid_identify.py "E:\Musica\Lrad - Knife Party.mp3"
```
*Salida en consola:*
```text
Analyzing: Lrad - Knife Party.mp3
IDENTIFIED (Score 0.98):
  Artist: Knife Party
  Title:  LRAD
```

### 3. Ejecutar Curaduría Playout Completa y Aislamiento en Cuarentena
```bash
python curate_music.py --dir "E:\Musica" --fix-id3 --quarantine-dupes
```

---

## 📄 Licencia

Publicado bajo licencia abierta **MIT**. Diseñado para libre implementación en emisoras de radio comunitarias, comerciales, estudios de post-producción y discotecas digitales personales.
