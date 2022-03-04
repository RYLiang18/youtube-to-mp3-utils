from pytube import YouTube, Playlist
import os
import sys
from moviepy.editor import *

def mp4_to_mp3(mp4, mp3):
    mp4_without_frames = AudioFileClip(mp4)
    mp4_without_frames.write_audiofile(mp3)
    mp4_without_frames.close()

def get_mp3_filename(file, track_number=-1):
    base, ext = os.path.splitext(file)
    
    if track_number == -1:
        return base + '.mp3'
    else:
        # 012345678901234567
        # /home/appuser/mp3/
        new_base = base[0:18] + f"{track_number} " + base[18:len(base)]
        return new_base + '.mp3'

class Youtube_Video:
    def __init__(self, url, track_number=-1) -> None:
        self.url = url
        self.track_number = track_number

    def to_mp4(self):
        yt = YouTube(self.url)
        audio = yt.streams.filter(only_audio=True).first()
        out_file = audio.download(output_path="/home/appuser/mp3")
        return out_file


# main
wants_playlist = input("Do you want to convert a playlist? (Y/n) ")

if wants_playlist == 'Y':
    playlist_url = input("Enter youtube playlist URL: ")
    playlist = Playlist(playlist_url)

    want_track_number = input("Do you want to add a track number to the beginning of the file? (y/N) ")
    
    for i, youtube_url in enumerate(playlist):
        track_number = i + 1

        video = None
        if want_track_number:
            video = Youtube_Video(youtube_url, track_number)
        else:
            video = Youtube_Video(youtube_url)
        
        video_mp4 = video.to_mp4()

        if want_track_number:
            mp4_to_mp3(
                video_mp4,
                get_mp3_filename(video_mp4, track_number)
            )
        else:
            mp4_to_mp3(
                video_mp4,
                get_mp3_filename(video_mp4)
            )
        # delete the original mp4
        os.remove(f"/home/appuser/mp3/{video_mp4}")

elif wants_playlist == 'n':
    youtube_url = input("Enter youtube URL: ")
    video = Youtube_Video(youtube_url)
    video_mp4 = video.to_mp4()
    mp4_to_mp3(
        video_mp4,
        get_mp3_filename(video_mp4)
    )

    # delete the original mp4
    os.remove(f"/home/appuser/mp3/{video_mp4}")

# ///// deprecated ////////////////////////////////////////////////

if False:
    filename = f"/mp3/{sys.argv[1]}"

    file = open(filename, 'r')
    urls = file.readlines()

    for i, url in enumerate(urls):
        print("converting...")
        url = url.strip()
        
        yt = YouTube(url)
        audio = yt.streams.filter(only_audio=True).first()

        out_file = audio.download(output_path="/mp3")

        base,ext = os.path.splitext(out_file)
    
        # convert mp4 file to mp3
        # creating name for mp3
        track_number = i+1
        new_base = base[0:5] + f"{track_number} " + base[5:len(base)]
        new_file = new_base + '.mp3'
        mp4_to_mp3(out_file, new_file)

        # delete the original mp4
        if os.path.exists(f"/mp3/{out_file}"):
            os.remove(f"/mp3/{out_file}")

        print(f"{yt.title} has been successfully downloaded")
        print(f"saving into {new_file}")