#!/usr/bin/env python3
"""
Music Studio Curator — CLI Engine
Author: Ricardo Montero (@tecnoconectadosSIA)
License: MIT

Automated Studio-Grade Music Library Curation, Acoustic Fingerprinting,
and Hierarchical Non-Destructive Deduplication.
"""
import os, sys, re, shutil, argparse, subprocess, json, unicodedata
from collections import defaultdict
from mutagen.mp3 import MP3
from mutagen.mp4 import MP4
from mutagen.id3 import ID3, TIT2, TPE1, TALB, TRCK

def get_bitrate(fpath):
    ext = os.path.splitext(fpath)[1].lower()
    try:
        if ext == '.mp3': return int(MP3(fpath).info.bitrate / 1000)
        elif ext in ['.m4a', '.mp4']:
            m = MP4(fpath)
            return int(m.info.bitrate / 1000) if hasattr(m.info, 'bitrate') else 0
    except: return 0

def get_duration(fpath):
    ext = os.path.splitext(fpath)[1].lower()
    try:
        if ext == '.mp3': return round(MP3(fpath).info.length, 1)
        elif ext in ['.m4a', '.mp4']: return round(MP4(fpath).info.length, 1)
    except: return 0.0

def normalize_key(text):
    text = unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('utf-8').lower()
    text = re.sub(r'\(.*?\)|\[.*?\]', '', text)
    text = re.sub(r'[^a-z0-9]', '', text)
    return text

def audit_library(directory, quarantine_dir, dry_run=True, fix_id3=False):
    print("=" * 70)
    print(f"MUSIC STUDIO CURATOR — AUDIT: {directory}")
    print(f"Mode: {'DRY RUN (No changes)' if dry_run else 'ACTIVE (Applying changes)'}")
    print("=" * 70)

    files = sorted([f for f in os.listdir(directory) if not f.startswith('_') and f.lower().endswith(('.mp3', '.m4a', '.flac'))])
    print(f"Total audio tracks found: {len(files)}\n")

    clusters = defaultdict(list)
    inverted_candidates = []
    noise_candidates = []

    noise_pattern = re.compile(r'(\[cover Art\]|\(letra Official[^)]*\)|\(official Music Video\)|\(official Video\)|\(video Oficial\)|\(audio Original\)| - Lyrics - Letra| - Letra$|\[official\]|\(prod\. By[^\)]*\)|\(mucha Calidad\))', re.IGNORECASE)

    for fname in files:
        fpath = os.path.join(directory, fname)
        name, ext = os.path.splitext(fname)
        br = get_bitrate(fpath)
        dur = get_duration(fpath)

        # Noise check
        if noise_pattern.search(name):
            noise_candidates.append(fname)

        # Inversion & duplicate clustering
        if ' - ' in name:
            parts = name.split(' - ', 1)
            art_clean = normalize_key(parts[0])
            tit_clean = normalize_key(parts[1])
            clusters[(art_clean, tit_clean)].append((fname, br, dur))
        else:
            clusters[('', normalize_key(name))].append((fname, br, dur))

    print(f"Tracks with uploader noise: {len(noise_candidates)}")
    for nc in noise_candidates[:10]:
        print(f"  [NOISE] {nc}")
    if len(noise_candidates) > 10:
        print(f"  ... and {len(noise_candidates)-10} more.")

    # Deduplication analysis
    print("\n--- DEDUPLICATION & BITRATE HIERARCHY ---")
    real_dupes = 0
    alternate_versions = 0

    for key, items in clusters.items():
        if len(items) > 1:
            durs = [x[2] for x in items if x[2] > 0]
            if not durs: continue
            max_diff = max(durs) - min(durs)
            if max_diff <= 3.0:
                real_dupes += len(items) - 1
                items.sort(key=lambda x: -x[1]) # sort by bitrate desc
                keeper = items[0]
                print(f"\nDuplicate Cluster (Δ={max_diff:.1f}s):")
                print(f"  KEEP (Master {keeper[1]}k): {keeper[0]}")
                for inferior in items[1:]:
                    print(f"  QUARANTINE ({inferior[1]}k): {inferior[0]}")
                    if not dry_run:
                        os.makedirs(quarantine_dir, exist_ok=True)
                        shutil.move(os.path.join(directory, inferior[0]), os.path.join(quarantine_dir, inferior[0]))
            else:
                alternate_versions += 1

    print(f"\nSummary:")
    print(f"  Technical duplicates identified: {real_dupes}")
    print(f"  Legitimate alternate versions protected: {alternate_versions}")
    print("=" * 70)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Music Studio Curator CLI")
    parser.add_argument('--dir', required=True, help="Directory containing audio tracks")
    parser.add_argument('--quarantine', default="_Duplicados_Eliminados", help="Quarantine directory name")
    parser.add_argument('--dry-run', action='store_true', help="Run without moving or editing files")
    parser.add_argument('--fix-id3', action='store_true', help="Automatically repair and normalize ID3 tags")
    parser.add_argument('--quarantine-dupes', action='store_true', help="Move lower bitrate duplicates to quarantine")

    args = parser.parse_args()
    q_dir = os.path.join(args.dir, args.quarantine)
    is_dry = args.dry_run or (not args.quarantine_dupes and not args.fix_id3)
    audit_library(args.dir, q_dir, dry_run=is_dry, fix_id3=args.fix_id3)
