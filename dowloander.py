from pathlib import Path

from pytube import YouTube, streams
from pytube.cli import on_progress


def dowloander(url):
    Path('./videos').mkdir(exist_ok=True)
    for link in url:

        yt = YouTube(link, on_progress_callback = on_progress)

        print(f"Titulo: {yt.title}, realizando o dowloand Por favor aguarde...")

        ys = yt.streams.get_highest_resolution()
        ys.download('videos')