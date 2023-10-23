import speech_recognition as sr
import shelve

languages = shelve.open("langs_data")["langs"]

def getTextFromSpeech(language):
    recognizer = sr.Recognizer()

    while True:
       
        try:
            with sr.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=1.5)
                print("Listening for text in", language)
                audio = recognizer.listen(mic)

                text = recognizer.recognize_google(audio, language=languages[language]["value"])

                text = text.lower()
                print(f"Recognized {text}")
                return text

        except Exception as e:
            recognizer = sr.Recognizer()
            print(e)



