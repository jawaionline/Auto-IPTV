import requests

SOURCE = "https://www.mana2.my/channel/tvs"
OUTPUT = "tvs_auto.m3u"

headers = {
    "User-Agent": "Mozilla/5.0"
}

r = requests.get(SOURCE, headers=headers, timeout=20)
r.raise_for_status()

with open(OUTPUT, "w", encoding="utf-8") as f:
    f.write(r.text)

print("Playlist berhasil diperbarui.")
