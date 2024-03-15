from flask import Flask, render_template, request
from video_downloader import download_youtube_video
from audio_downloader import download_youtube_video_as_song
from waitress import serve

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/download-audio")
def get_audio():
    youtube_link = request.args.get("audio-link")
    download_audio = download_youtube_video_as_song(youtube_link)
    return render_template("index.html", download_message=download_audio)


@app.route("/download-video")
def get_video():
    youtube_link = request.args.get("video-link")
    download_video = download_youtube_video(youtube_link)
    return render_template("index.html", download_message=download_video)


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
