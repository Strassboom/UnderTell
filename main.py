from flask import Flask, render_template
from pydub import AudioSegment
from pydub.silence import split_on_silence

app = Flask(__name__)

@app.route('/')
def home(text="You're gonna have a bad time"):
    if len(text.strip()) == 0:
        return render_template("underteller.html",message="")
    
    inSound = "static/voice_sans.wav"
    outSound = "static/result.wav"

    # create 1 sec of silence audio segment
    space_segment = AudioSegment.silent(duration=100)  #duration in milliseconds

    #read wav file to an audio segment
    song = AudioSegment.from_wav(inSound)
    
    #Add above two audio segments    
    #final_song = one_sec_segment + song

    #Either save modified audio
    #final_song.export(audio_out_file, format="wav")

    outVoice = AudioSegment.silent(duration=10)

    for character in text:
        if not character.isalnum():
            outVoice = outVoice + space_segment
        else:
            outVoice = outVoice + song

    outVoice.export(outSound, format="wav")

    aich = AudioSegment.from_wav(outSound)
    #play(aich)
    return render_template("underteller.html")

if __name__=="__main__":
    app.run()