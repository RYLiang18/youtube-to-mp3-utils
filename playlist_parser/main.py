from pytube import Playlist

import sys

playlist_url = sys.argv[1]
file_name = f"./playlist/{sys.argv[2]}"

playlist = Playlist(playlist_url)

f = open(file_name, "w")

for url in playlist:
    print("writing...")
    f.write(f"{url}\n")