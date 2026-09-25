"""
Universal AcoustID / Chromaprint music identifier using local fpcalc.exe and AcoustID API.
Usage: python acoustid_identify.py "path/to/song.mp3"
"""
import os, sys, subprocess, json, urllib.request, urllib.parse
sys.stdout.reconfigure(encoding='utf-8')

FPCALC = r"e:\dev\Antigravity\Fix pc\bin\fpcalc.exe"
CLIENT_KEY = "cSpUJKpD"

def identify_file(audio_path):
    if not os.path.exists(audio_path):
        return None
    try:
        out = subprocess.run([FPCALC, "-json", audio_path], capture_output=True, text=True)
        data = json.loads(out.stdout)
        dur = int(float(data['duration']))
        fp = data['fingerprint']

        params = {
            'client': CLIENT_KEY,
            'meta': 'recordings releasegroups releases tracks',
            'duration': dur,
            'fingerprint': fp
        }
        data_enc = urllib.parse.urlencode(params).encode('utf-8')
        req = urllib.request.Request('https://api.acoustid.org/v2/lookup', data=data_enc)
        with urllib.request.urlopen(req, timeout=12) as resp:
            res = json.loads(resp.read().decode('utf-8'))
            results = res.get('results', [])
            candidates = []
            for r in results:
                score = r.get('score', 0)
                for rec in r.get('recordings', []):
                    title = rec.get('title')
                    artists = [a.get('name') for a in rec.get('artists', [])]
                    candidates.append({
                        'score': score,
                        'artist': ', '.join(artists),
                        'title': title
                    })
            if candidates:
                candidates.sort(key=lambda x: -x['score'])
                return candidates[0]
    except Exception as e:
        print(f"Error identifying {audio_path}: {e}")
    return None

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else r"E:\Musica\Makj - Generic.mp3"
    print(f"Analyzing: {os.path.basename(path)}")
    res = identify_file(path)
    if res:
        print(f"IDENTIFIED (Score {res['score']:.2f}):")
        print(f"  Artist: {res['artist']}")
        print(f"  Title:  {res['title']}")
    else:
        print("No acoustic match found in database.")
