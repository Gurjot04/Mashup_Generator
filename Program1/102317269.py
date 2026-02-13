import sys
import os
import yt_dlp
from pydub import AudioSegment

def download_videos(singer, num_videos):
    if not os.path.exists("downloads"):
        os.makedirs("downloads")

    ydl_opts = {
        'format': 'bestaudio',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'quiet': False,
        'extractaudio': True,
        'audioformat': 'mp3',
        'noplaylist': True
    }

    search_query = f"ytsearch{num_videos}:{singer} official video"

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([search_query])


def trim_and_merge(duration, output_file):
    final_audio = AudioSegment.empty()

    for file in os.listdir("downloads"):
        filepath = os.path.join("downloads", file)
        try:
            audio = AudioSegment.from_file(filepath)
            clip = audio[:duration * 1000]
            final_audio += clip
        except:
            print("Error processing:", file)

    final_audio.export(output_file, format="mp3")
    print("Mashup created successfully:", output_file)


def main():
    if len(sys.argv) != 5:
        print("Usage: python <program.py> <SingerName> <NumberOfVideos> <Duration> <OutputFileName>")
        sys.exit()

    singer = sys.argv[1]

    try:
        num_videos = int(sys.argv[2])
        duration = int(sys.argv[3])
    except:
        print("Number of videos and duration must be integers.")
        sys.exit()

    output_file = sys.argv[4]

    if num_videos < 10:
        print("Number of videos must be greater than 10.")
        sys.exit()

    if duration < 20:
        print("Duration must be greater than 20 seconds.")
        sys.exit()

    download_videos(singer, num_videos)
    trim_and_merge(duration, output_file)


if __name__ == "__main__":
    main()
