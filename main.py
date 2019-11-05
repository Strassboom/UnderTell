from flask import Flask, render_template
from pydub import AudioSegment
from pydub.silence import split_on_silence

app = Flask(__name__)

@app.route('/')
def home(text="You're gonna have a bad time"):
    if len(text.strip()) == 0:
        return render_template("index.html",message="")
    return render_template("index.html")

if __name__=="__main__":
    app.run()