from threading import Thread
from flask import Flask, request, redirect
from flask.templating import render_template

import speech_recognition as sr

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def index():
    transcript=''
    if request.method =='POST':
        print('data received')
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)
        if file:
            recog = sr.Recognizer()
            audioFile = sr.AudioFile(file)
            with audioFile as source:
                data = recog.record(source)
            transcript = recog.recognize_google(data, key=None)

    return render_template('index.html', transcript = transcript)

if __name__=="__main__":
    app.run(debug=True, Threaded=True)