import speech_recognition as sr


def live_voice_to_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio, show_all=False)
        print("You said: {}".format(text))
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
    except sr.RequestError as e:
        print("Error: {}".format(e))


live_voice_to_text()
