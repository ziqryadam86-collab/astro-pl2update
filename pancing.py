import requests
import re

url = "https://www.kds.tw/tv/sports-tv-live-streaming/astro-pl-2/"
headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 11)", "Referer": "https://www.kds.tw/"}

def get_link():
    try:
        res = requests.get(url, headers=headers, timeout=15)
        found = re.search(r'(https?[:\/\\]+[^"\']+\.m3u8[^"\']*)', res.text)
        if found:
            return found.group(1).replace('\\/', '/').replace('\\', '')
    extra_headers = {}
    return None

link = get_link()
if link:
    # Ini isi fail .m3u8 yang akan dihasilkan
    print("#EXTM3U")
    print("#EXT-X-VERSION:3")
    print("#EXT-X-STREAM-INF:BANDWIDTH=500000,RESOLUTION=1920x1080")
    print(link)
  
