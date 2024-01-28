import os
from transcribe import Transcriber
from youtube_downloader import YouTubeDownloader

link = ""

yt = YouTubeDownloader(link)
video_path = yt.download()

transcriber = Transcriber("openai/whisper-large-v3")
result = transcriber.convert(video_path)
transcriber.save(result, f"{yt.title}.json")
