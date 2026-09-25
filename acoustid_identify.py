#!/usr/bin/env python3
"""
Universal AcoustID / Chromaprint music identifier using local fpcalc binary and AcoustID API.
Author: Ricardo Montero (@tecnoconectadosSIA)
License: MIT
"""
import os, sys, shutil, subprocess, json, urllib.request, urllib.parse, argparse

def find_fpcalc():
    """Dynamically locate the fpcalc binary across Windows, macOS, and Linux."""
    # 1. Custom environment variable
    custom = os.environ.get("FPCALC_PATH")
    if custom and os.path.isfile(custom):
        return custom

    # 2. Bundled bin/ directory relative to this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    candidates = [
        os.path.join(script_dir, "bin", "fpcalc.exe"),
        os.path.join(script_dir, "bin", "fpcalc"),
        os.path.join(script_dir, "fpcalc.exe"),
        os.path.join(script_dir, "fpcalc"),
    ]
    for c in candidates:
        if os.path.isfile(c) and os.access(c, os.X_OK):
            return c

    # 3. System PATH
    system_path = shutil.which("fpcalc")
    if system_path:
        return system_path

    return None

def identify_file(audio_path, client_key="cSpUJKpD", fpcalc_bin=None):
    """Generates acoustic fingerprint and queries the AcoustID web service."""
    if not os.path.isfile(audio_path):
        print(f"Error: File not found -> '{audio_path}'", file=sys.stderr)
        return None

    fpcalc = fpcalc_bin or find_fpcalc()
    if not fpcalc:
        print("Error: 'fpcalc' binary not found. Please install Chromaprint or set FPCALC_PATH.", file=sys.stderr)
        return None

    try:
        out = subprocess.run([fpcalc, "-json", audio_path], capture_output=True, text=True, timeout=30)
        if out.returncode != 0:
            print(f"fpcalc error: {out.stderr.strip()}", file=sys.stderr)
            return None

        data = json.loads(out.stdout)
        dur = int(float(data['duration']))
        fp = data['fingerprint']

        params = {
            'client': client_key,
            'meta': 'recordings releasegroups releases tracks',
            'duration': dur,
            'fingerprint': fp
        }
        data_enc = urllib.parse.urlencode(params).encode('utf-8')
        req = urllib.request.Request(
            'https://api.acoustid.org/v2/lookup',
            data=data_enc,
            headers={'User-Agent': 'MusicStudioCurator/1.0.0 (https://github.com/tecnoconectadosSIA/music-studio-curator)'}
        )
        with urllib.request.urlopen(req, timeout=15) as resp:
            res = json.loads(resp.read().decode('utf-8'))
            results = res.get('results', [])
            candidates = []
            for r in results:
                score = r.get('score', 0)
                for rec in r.get('recordings', []):
                    title = rec.get('title')
                    artists = [a.get('name') for a in rec.get('artists', []) if a.get('name')]
                    candidates.append({
                        'score': score,
                        'artist': ', '.join(artists),
                        'title': title
                    })
            if candidates:
                candidates.sort(key=lambda x: -x['score'])
                return candidates[0]
    except Exception as e:
        print(f"Identification failed for '{os.path.basename(audio_path)}': {e}", file=sys.stderr)
    return None

def main():
    parser = argparse.ArgumentParser(description="Identify audio track using AcoustID acoustic fingerprinting.")
    parser.add_argument("file", help="Path to audio file (.mp3, .m4a, .flac, .wav)")
    parser.add_argument("--key", default=os.environ.get("ACOUSTID_API_KEY", "cSpUJKpD"), help="AcoustID client API key")
    parser.add_argument("--fpcalc", default=None, help="Custom path to fpcalc binary")

    args = parser.parse_args()

    print(f"Analyzing: {os.path.basename(args.file)}")
    result = identify_file(args.file, client_key=args.key, fpcalc_bin=args.fpcalc)
    if result:
        print(f"\nIDENTIFIED (Confidence: {result['score'] * 100:.1f}%):")
        print(f"  Artist: {result['artist']}")
        print(f"  Title:  {result['title']}")
    else:
        print("\nNo acoustic match found in the AcoustID database.")

if __name__ == "__main__":
    main()
