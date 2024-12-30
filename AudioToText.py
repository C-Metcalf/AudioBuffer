import speech_recognition as sr
# ToDo: When the banned words are said beep them out from the audio.
r = sr.Recognizer()
banned_list = ['fuck', 'bitch', 'queer', 'fagot']

with sr.AudioFile('audio_logs/recording.wav') as source:
    audio = r.record(source)

    try:
        text = r.recognize_google(audio)
        for word in text.split():
            if word in banned_list:
                continue
            print(word)
        # print(text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))