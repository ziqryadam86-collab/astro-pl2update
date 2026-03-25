import requests
import re
import sys

# URL target Astro PL 2
url = "https://www.kds.tw/tv/sports-tv-live-streaming/astro-pl-2/"
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 11)", 
    "Referer": "https://www.kds.tw/"
}

def get_link():
    try:
        # Guna timeout 20 saat supaya GitHub tak sangkut lama
        res = requests.get(url, headers=headers, timeout=20)
        # Cari link m3u8 yang ada token
        found = re.search(r'(https?[:\/\\]+[^"\']+\.m3u8[^"\']*)', res.text)
        if found:
            # Bersihkan URL daripada backslash (\/)
            return found.group(1).replace('\\/', '/').replace('\\', '')
    except Exception as e:
        # Jika error, kita tulis dalam log GitHub
        print(f"# Error: {e}", file=sys.stderr)
    return None

link = get_link()

if link:
    # Print format Master Playlist yang awak nak
    print("#EXTM3U")
    print("#EXT-X-VERSION:3")
    print("#EXT-X-STREAM-INF:BANDWIDTH=500000,RESOLUTION=1920x1080")
    print(link)
else:
    # Jika gagal dapat link, kita bagi exit code 1 supaya GitHub tahu ada masalah
    sys.exit(1)
    
