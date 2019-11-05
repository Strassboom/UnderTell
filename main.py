from flask import Flask, render_template, request
from pydub import AudioSegment
import simpleaudio as sa
from pydub.effects import speedup

app = Flask(__name__)

<<<<<<< HEAD
@app.route('/')
def home(text="You're gonna have a bad time"):
    if len(text.strip()) == 0:
        return render_template("index.html",message="")
    return render_template("index.html")
=======
@app.route('/',methods=["GET","POST"])
def home():
    if request.method == 'GET':
        text = "Heya"
    else:
        text = request.form["words"]
    inSound = "static/voice_sans.wav"
    outSound = "static/result.wav"

    # create 0.1 sec of silence audio segment
    space_segment = AudioSegment.silent(duration=100)  #duration in milliseconds

    #read wav file to an audio segment
    song = AudioSegment.from_wav(inSound)
    speedy_song = speedup(song * 6,10.0,crossfade=5)
    outVoice = AudioSegment.silent(duration=10)

    for character in text:
        if not character.isalnum():
            if character == " ":
                outVoice = outVoice + song + space_segment
        else:
            outVoice = outVoice + speedy_song

    outVoice = speedup(outVoice,8.0)
    outVoice.export(outSound, format="wav")

    wave_obj = sa.WaveObject.from_wave_file("static/result.wav")
    wave_obj.play()
    return render_template("underteller.html",message=text)
>>>>>>> e02b5e9... Cleaned up underteller.html. Implemented first fully working sans version for Windows 10.

if __name__=="__main__":
    app.run(host="localhost", port=8080)