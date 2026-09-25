# 📻 Music Studio Curator
### Curatela Audio di Grado Broadcast, Impronta Acustica e Automazione dei Metadati On-Air

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

> **Sviluppato e curato da:** **Ricardo Montero** ([@tecnoconectadosSIA](https://github.com/tecnoconectadosSIA))  
> *Broadcaster, Consulente per l'Automazione Radiofonica e Ingegnere del Suono.*

---

## 🎙️ Il Manifesto del Broadcaster: Perché nasce questo strumento

Nel mondo dell'emittenza radiofonica professionale (FM, DAB+, Web Radio e reti satellitari), i metadati audio **non sono un dettaglio decorativo: rappresentano un'infrastruttura critica di trasmissione**.

Quando un brano viene inserito nei software di automazione e regia di emissione (**MB Studio, Dalet, RCS Master Control, RadioDJ, ZaraRadio, WideOrbit o Dinesat**):
1. **L'RDS Dinamico e i Flussi Web Streaming** trasmettono in tempo reale artista e titolo agli schermi delle autoradio, ai sintonizzatori DAB+ e alle app mobili. Un titolo invertito come `Lrad - Knife Party` o sporcato da diciture tipo `(Video Ufficiale HD)` danneggia gravemente l'immagine della stazione.
2. **Le Società di Gestione dei Diritti d'Autore** (SIAE, SCF, SGAE, BMI, ASCAP) controllano i registri di trasmissione estratti dai tag ID3 e codici ISRC. Tracce errate o non identificate generano sanzioni, mancato riconoscimento dei diritti e report respinti.
3. **I Processori Audio On-Air** (Orban Optimod, Omnia, Telos) enfatizzano in modo spietato qualsiasi artefatto di compressione al di sotto dei 192 kbps. Trasmettere in onda un file compresso a 32 o 64 kbps distrugge la dinamica di modulazione e affatica istantaneamente l'ascoltatore.
4. **Nessun Falso Titolo On-Air**: Una regia automatica non può mandare in onda un file etichettato come `Makj - Generic` quando in realtà l'audio corrisponde a un classico Progressive Trance di `Kyau & Albert`.

I tradizionali software di tagging desktop (**MusicBrainz Picard**, **beets**) sono stati pensati per utenti consumer che gestiscono CD fisici ufficiali. Quando un broadcaster si trova a gestire registrazioni dal vivo, sessioni acustiche in studio (*Free Cover*), bootleg radiofonici o estratti da trasmissioni web, questi strumenti **falliscono, si bloccano o richiedono estenuanti correzioni manuali brano per brano**.

Per superare definitivamente questi limiti ho progettato **Music Studio Curator**: una pipeline di standard radiofonico che combina **impronta acustica spettrale (Chromaprint / AcoustID)**, **de-offuscamento fonetico tramite intelligenza artificiale vocale (Speech-to-Text)** e un **protocollo di quarantena non distruttivo basato sulla fedeltà del bitrate**.

---

## 🏛️ Pipeline di Curatela in 5 Fasi

```mermaid
flowchart TD
    A["Archivio Audio Master (Regia Radiofonica / Playout)"] --> B["Fase 1: Audit di Trasmissione & Pulizia Parassiti"]
    B --> C{"Corrispondenza Spettrale in MusicBrainz?"}
    C -->|Sì (Score ≥ 0.90)| D["Fase 2A: Risoluzione Acustica (Chromaprint / AcoustID)"]
    C -->|No / Sessione Speciale| E["Fase 2B: Trascrizione Fonetica Lirica con IA (Speech-to-Text)"]
    D --> F["Fase 3: Standardizzazione On-Air & Normalizzazione Feat"]
    E --> F
    F --> G["Fase 4: Deduplicazione Gerarchica per Bitrate di Emissione"]
    G --> H{"Tracce Identiche (|Δt| ≤ 3s)?"}
    H -->|Sì: Duplicato Tecnico| I["Isolamento Sicuro in _Duplicados_Eliminados/"]
    H -->|No: Versione Alternativa| J["Preservare e Proteggere (Live, Acustico, Free Cover, Remix)"]
    G --> K["Fase 5: Iniezione ID3v2.3 Broadcast Ready & Report CSV"]
```

### 1. Audit di Trasmissione e Rilevamento Inversioni
- **Riconoscimento Inversioni (`Titolo - Artista` ➡️ `Artista - Titolo`)**: Verifica automatica contro un database di artisti canonici per riordinare la nomenclatura senza perdere metadati.
- **Bonifica di Prefissi da Colonna Sonora**: Rimozione di etichette generiche da compilation (`Various Artists - Artista – Titolo`) per ripristinare la paternità originaria dell'artista.
- **Eliminazione Rumore Tecnico**: Rimozione di stringhe parassite quali `(Video Ufficiale)`, `(Prod. By ...)`, `(by Gabrielpauta)`, canali YouTube, nomi di uploader e anni superflui.

### 2. Motore Ibrido di Identificazione (Spettrale + Fonetico)
- **Livello 1 (Impronta Acustica Chromaprint / AcoustID)**: Analisi matematica della frequenza con il binario nativo `fpcalc.exe` 1.6.1. Riconosce il vero brano anche in presenza di metadati totalmente errati o assenti.
- **Livello 2 (IA Vocale Multilingue)**: Per brani regionali, bootleg da consolle o esibizioni dal vivo non censite nei cataloghi commerciali, estrae un frammento di 25 secondi e trascrive il testo cantato con l'IA (Google Speech in italiano, spagnolo o inglese), ricavando il titolo esatto dal testo.

### 3. Normalizzazione Editoriale per Sistemi di Regia
- Standardizzazione ID3v2.3 conforme a UTF-8 e sistemi Windows Media:
  * Collaborazioni uniformate: `con`, `ft.`, `feat`, `,`, `x`, `vs.` ➡️ `feat.` o `&`.
  * Rispetto rigoroso di accenti e nomi d'arte (`Mägo de Oz`, `OneRepublic`, `Qué Quieres de Mí`, `Abrázame`).
  * Eliminazione dei caratteri non consentiti nei file system Windows (`: , " ? * < > |`) e bilanciamento di parentesi e quadre.

### 4. Gerarchia di Fedeltà Sonora (Zero Perdita di Dati)
- **Regola Fondamentale**: Nessun brano originale viene cancellato.
- Se due file presentano la medesima traccia audio ($| \Delta \text{durata} | \le 3.0\,\text{s}$), la copia a risoluzione superiore (320 kbps > 256 kbps > 192 kbps > 128 kbps) rimane nel catalogo attivo di trasmissione, mentre la versione a bitrate inferiore viene spostata in sicurezza nella cartella `_Duplicados_Eliminados/`.
- **Protezione Versioni Alternative**: Registrazioni live, versioni acustiche in studio, concerti *Free Cover* e remix ufficiali sono preservati come asset indipendenti.

### 5. Upgrade Automatico di Master Danneggiati
- Se vengono rilevate tracce a qualità inaccettabile per l'etere (< 96 kbps) o brani troncati, il sistema interroga automaticamente YouTube Music tramite `yt-dlp`, scarica il master a 320 kbps con FFmpeg, riscrive i tag ID3 conformi e sposta la copia degradata in quarantena.

---

## 🤖 Compatibilità Multi-Agente (Ecosistema AI)

Ottimizzato per funzionare nativamente all'interno dei principali agenti di intelligenza artificiale per lo sviluppo e l'automazione:

| Piattaforma / Assistente AI | Tipo di Integrazione | Percorso di Installazione |
|---|---|---|
| **Google Antigravity** | Native Skill | `~/.gemini/config/skills/music-studio-curator/SKILL.md` |
| **Claude Code** (Anthropic) | System Skill / `CLAUDE.md` | `.claude/skills/music-studio-curator/` o all'interno di `CLAUDE.md` |
| **OpenCode** | Agent Skill | `.opencode/skills/music-studio-curator/` |
| **OpenAI Codex / ChatGPT Operator** | Custom Instructions / Action | Copiare le regole da `SKILL.md` |
| **Cursor & Windsurf** | Rule File | `.cursorrules` / `.windsurfrules` |
| **Aider & Roo Code** | Contextual Prompt | `.aider.conf.yml` / System Prompt |
| **Server Linux / Windows Playout** | Standalone Python CLI | `python curate_music.py --dir /var/broadcast/music` |

---

## 📦 Installazione e Configurazione

### Prerequisiti
* **Python 3.10** o superiore.
* **FFmpeg** installato e configurato nelle variabili d'ambiente (`PATH`).
* **Chromaprint (`fpcalc.exe`)**: Già incluso nella cartella `bin/` per Windows a 64 bit o scaricabile per Linux/macOS da [acoustid.org/chromaprint](https://acoustid.org/chromaprint).

```bash
# 1. Clonare il repository
git clone https://github.com/tecnoconectadosSIA/music-studio-curator.git
cd music-studio-curator

# 2. Installare i pacchetti richiesti
pip install -r requirements.txt
```

---

## 💻 Manuale Operativo CLI

### 1. Verifica Preventiva senza Modifiche (Dry-Run di Regia)
```bash
python curate_music.py --dir "E:\Musica" --dry-run
```

### 2. Riconoscimento Traccia Ignota o Falsificata tramite Impronta Acustica
```bash
python acoustid_identify.py "E:\Musica\Lrad - Knife Party.mp3"
```
*Output di esempio:*
```text
Analyzing: Lrad - Knife Party.mp3
IDENTIFIED (Score 0.98):
  Artist: Knife Party
  Title:  LRAD
```

### 3. Esecuzione Completa di Curatela, Correzione Tag e Quarantena
```bash
python curate_music.py --dir "E:\Musica" --fix-id3 --quarantine-dupes
```

---

## 📄 Licenza

Rilasciato sotto licenza open source **MIT**. Adottabile liberamente per emittenti radiofoniche comunitarie, stazioni commerciali, studi di post-produzione e collezioni musicali per DJ e collezionisti.

---

## ⚖️ Note Legali ed Esclusione di Responsabilità

### Esclusione di Responsabilità (Disclaimer Legale)
Questo software è stato sviluppato a fini di gestione tecnica, catalogazione e preparazione dell'archivio audio per emittenti radiofoniche, broadcaster, sound engineer e collezionisti in possesso di copie regolarmente licenziate o acquisite. L'autore e i collaboratori **non incoraggiano, non promuovono e non facilitano in alcun modo la violazione dei diritti d'autore o la pirateria informatica**.
* Il software **non ospita, non ritrasmette in streaming e non distribuisce materiale coperto da copyright**.
* È responsabilità esclusiva dell'utente verificare la conformità con la normativa vigente in materia di proprietà intellettuale (Direttiva UE 2019/790, Legge sul Diritto d'Autore L. 633/1941, SIAE, SCF, SGAE, ASCAP, BMI) e con le condizioni d'uso delle piattaforme collegate.

### Licenze di Terze Parti e Crediti Open Source
* **Chromaprint (pcalc.exe)**: Copyright © Lukáš Lalinský. Distribuito secondo i termini della licenza **GNU Lesser General Public License (LGPL) v2.1**. Il codice sorgente integrale è reperibile su [github.com/acoustid/chromaprint](https://github.com/acoustid/chromaprint).
* **AcoustID & MusicBrainz**: Si ringraziano la MetaBrainz Foundation e AcoustID.org per il supporto alla banca dati aperta di impronte acustiche.
* **Mutagen**: Copyright © Joe Wreschnig e collaboratori (GPL v2+).
