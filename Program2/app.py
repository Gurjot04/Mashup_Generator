from flask import Flask, request, render_template_string
import os
import yt_dlp
from pydub import AudioSegment
import zipfile
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

HTML = """
<h2>Mashup Generator</h2>
<form method="POST">
Singer Name: <input name="singer"><br><br>
# of Videos: <input name="videos"><br><br>
Duration (sec): <input name="duration"><br><br>
Email: <input name="email"><br><br>
<input type="submit">
</form>
"""

def create_mashup(singer, num_videos, duration):
    if not os.path.exists("downloads"):
        os.makedirs("downloads")

    ydl_opts = {
        'format': 'bestaudio',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'quiet': True,
        'noplaylist': True
    }

    search_query = f"ytsearch{num_videos}:{singer} official video"

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([search_query])

    final_audio = AudioSegment.empty()

    for file in os.listdir("downloads"):
        filepath = os.path.join("downloads", file)
        audio = AudioSegment.from_file(filepath)
        clip = audio[:duration * 1000]
        final_audio += clip

    output_file = "mashup.mp3"
    final_audio.export(output_file, format="mp3")

    return output_file


def zip_file(file_name):
    zip_name = "mashup.zip"
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        zipf.write(file_name)
    return zip_name


def send_email(receiver_email, zip_file_name):
    sender_email = "gurjotkdeol06@gmail.com"
    app_password = "nyas fygt llxy rlvn"

    msg = EmailMessage()
    msg["Subject"] = "Your Mashup"
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.set_content("Your mashup is attached!")

    with open(zip_file_name, "rb") as f:
        file_data = f.read()

    msg.add_attachment(file_data, maintype="application",
                       subtype="zip", filename=zip_file_name)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(sender_email, app_password)
        smtp.send_message(msg)


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        singer = request.form["singer"]
        videos = int(request.form["videos"])
        duration = int(request.form["duration"])
        email = request.form["email"]

        mashup = create_mashup(singer, videos, duration)
        zip_name = zip_file(mashup)
        send_email(email, zip_name)

        return "Mashup created and emailed successfully!"

    return render_template_string(HTML)


if __name__ == "__main__":
    app.run(debug=True)
