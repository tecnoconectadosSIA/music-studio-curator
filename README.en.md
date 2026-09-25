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

> **Created and maintained by:** **Ricardo Montero** ([@tecnoconectadosSIA](https://github.com/tecnoconectadosSIA))  
> *Broadcaster, Broadcast Automation Consultant & Audio Engineer.*

---

## 🎙️ The Broadcaster's Manifesto: Why This Tool Exists

In professional terrestrial and digital broadcasting (FM, DAB+, Satellite, and Web Radio), audio metadata is not a decorative tag—**it is mission-critical broadcast infrastructure**.

When tracks are ingested into commercial broadcast playout systems (**RCS Master Control, Dalet, WideOrbit, RadioDJ, ZaraRadio, or Dinesat**):
1. **Dynamic RDS & Web Streams** feed artist and title information in real-time to vehicle dashboards, DAB+ receiver screens, and mobile streaming apps. An inverted title like `Lrad - Knife Party` or noisy tags like `(Official Video HD)` destroys the station's on-air credibility.
2. **Performance Rights Organizations** (ASCAP, BMI, SESAC, PRS for Music, SGAE, SIAE) audit transmission logs generated from ID3 tags and ISRC metadata. Inaccurate, truncated, or misattributed files lead to compliance penalties, misallocated royalties, and failed audits.
3. **On-Air Broadcast Audio Processors** (Orban Optimod, Omnia, Telos Alliance) brutally expose and exaggerate compression artifacts present in low-bitrate files (< 192 kbps). Airing a 32 kbps or 64 kbps MP3 squashes modulation dynamics and creates severe listener fatigue.
4. **Zero Dead Air & Zero Identity Hallucinations**: Playout engines cannot afford to broadcast a mislabeled track like `Makj - Generic` when the audio is actually an iconic Progressive Trance record by `Kyau & Albert`.

Legacy desktop taggers (**MusicBrainz Picard**, **beets**) were engineered for domestic music enthusiasts managing retail studio CD albums. When confronted with live concert recordings, exclusive studio sessions (*Free Cover*), festival bootlegs, in-studio acoustic takes, or stream captures, these programs **stall, fail, or demand tedious manual track-by-track intervention**.

To solve this fundamentally, I engineered **Music Studio Curator**: a broadcast-standard pipeline combining **spectral acoustic fingerprinting (Chromaprint / AcoustID)**, **AI-assisted phonetic lyric transcription (Speech-to-Text)**, and a **non-destructive bitrate-hierarchy quarantine protocol**.

---

## 🏛️ The 5-Phase Broadcast Curation Pipeline

```mermaid
flowchart TD
    A["Master Audio Repository (Playout / Music Bank)"] --> B["Phase 1: Broadcast Audit & Parasite Purge"]
    B --> C{"Spectral Match in MusicBrainz?"}
    C -->|Yes (Score ≥ 0.90)| D["Phase 2A: Acoustic Identification (Chromaprint / AcoustID)"]
    C -->|No / Custom Session| E["Phase 2B: AI Phonetic Lyric Transcription (Speech-to-Text)"]
    D --> F["Phase 3: On-Air Standardization & Collaboration Cleanup"]
    E --> F
    F --> G["Phase 4: Hierarchical Playout Bitrate Deduplication"]
    G --> H{"Identical Takes (|Δt| ≤ 3s)?"}
    H -->|Yes: Technical Duplicate| I["Safe Isolation in _Duplicados_Eliminados/"]
    H -->|No: Alternate Legitimate Version| J["Protect & Retain (Live, Acoustic, Free Cover, Remix)"]
    G --> K["Phase 5: Broadcast-Ready ID3v2.3 Injection & CSV Audit Log"]
```

### 1. Broadcast Audit & Inversion Detection
- **Bidirectional Inversion Detection (`Title - Artist` ➡️ `Artist - Title`)**: Cross-references against a broadcast canonical artist database to reverse misordered files without losing metadata.
- **Soundtrack Prefix Stripping**: Unpacks generic compilation tags (`Various Artists - Artist – Title`) and restores true original authorship.
- **Parasitic Noise Purge**: Strips out video junk like `(Official Video)`, `(Prod. By ...)`, `(Audio Original)`, YouTube channel tags, uploader slugs, and stray release years.

### 2. Hybrid Identification Engine (Spectral + Phonetic)
- **Tier 1 (Chromaprint / AcoustID Fingerprinting)**: Mathematical spectral analysis powered by the native `fpcalc.exe` 1.6.1 binary. Identifies the real audio content regardless of false or blank metadata.
- **Tier 2 (Multilingual AI Speech Recognition)**: When unreleased Latin music, bootlegs, or live regional concert takes lack commercial catalog indexing, a 25-second excerpt is transcribed using Speech-to-Text (Google Speech in English, Spanish, or Italian) to identify verified lyrics and restore official titles.

### 3. Editorial Standardization for Playout Engines
- Enforces broadcast-safe UTF-8 and Windows Media ID3v2.3 standards:
  * Normalized collaboration syntaxes: `con`, `ft.`, `feat`, `,`, `x`, `vs.` ➡️ `feat.` or `&`.
  * Preserves diacritical marks and proper nouns (`Mägo de Oz`, `OneRepublic`, `Qué Quieres de Mí`, `Abrázame`).
  * Enforces Windows filesystem compliance (stripping illegal chars `: , " ? * < > |` and balancing broken brackets).

### 4. Zero Data Loss Bitrate Hierarchy
- **Golden Rule**: No original master track is ever deleted.
- If two files share identical musical audio ($| \Delta \text{duration} | \le 3.0\,\text{s}$), the highest-fidelity file (320 kbps > 256 kbps > 192 kbps > 128 kbps) is retained in the active playout bank, while the inferior copy is quarantined into `_Duplicados_Eliminados/`.
- **Alternate Take Protection**: Live recordings, acoustic booth takes, *Free Cover* concerts, and official remixes are strictly preserved as distinct assets.

### 5. Automated Master Upgrading
- When legacy tracks exhibit sub-broadcast quality (< 96 kbps) or corrupted truncations, the pipeline queries YouTube Music via `yt-dlp`, fetches the full 320 kbps master audio, sets broadcast tags, and quarantines the degraded copy.

---

## 🤖 Multi-Agent AI Compatibility Matrix

Designed to operate natively within world-class autonomous coding agents:

| AI Platform / Agent | Integration Type | Installation Target |
|---|---|---|
| **Google Antigravity** | Native Skill | `~/.gemini/config/skills/music-studio-curator/SKILL.md` |
| **Claude Code** (Anthropic) | System Skill / `CLAUDE.md` | `.claude/skills/music-studio-curator/` or within `CLAUDE.md` |
| **OpenCode** | Agent Skill | `.opencode/skills/music-studio-curator/` |
| **OpenAI Codex / ChatGPT Operator** | Custom Instructions / Action | Embed directives from `SKILL.md` |
| **Cursor & Windsurf** | Rule File | `.cursorrules` / `.windsurfrules` |
| **Aider & Roo Code** | Contextual Prompt | `.aider.conf.yml` / System Prompt |
| **Headless Linux / Windows Server** | Standalone Python CLI | `python curate_music.py --dir /var/broadcast/music` |

---

## 📦 Installation & Setup

### Prerequisites
* **Python 3.10** or higher.
* **FFmpeg** installed and accessible in the system `PATH`.
* **Chromaprint (`fpcalc.exe`)**: Included under `bin/` for Windows 64-bit or downloadable for Linux/macOS from [acoustid.org/chromaprint](https://acoustid.org/chromaprint).

```bash
# 1. Clone the repository
git clone https://github.com/tecnoconectadosSIA/music-studio-curator.git
cd music-studio-curator

# 2. Install dependencies
pip install -r requirements.txt
```

---

## 💻 CLI Operations Guide

### 1. Pre-Broadcast Dry Run Audit (No Files Modified)
```bash
python curate_music.py --dir "E:\Musica" --dry-run
```

### 2. Identify Mystery or Forged Track via Acoustic Fingerprint
```bash
python acoustid_identify.py "E:\Musica\Lrad - Knife Party.mp3"
```
*Sample Output:*
```text
Analyzing: Lrad - Knife Party.mp3
IDENTIFIED (Score 0.98):
  Artist: Knife Party
  Title:  LRAD
```

### 3. Full Playout Curation & Quarantine Execution
```bash
python curate_music.py --dir "E:\Musica" --fix-id3 --quarantine-dupes
```

---

## 📄 License

Distributed under the open-source **MIT License**. Free for commercial and non-commercial implementation across community radio stations, national broadcast networks, DJ digital record pools, and private music vaults.
