import speech_recognition

# Get audio from microphone
recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Say something!")
    audio = recognizer.listen(source)

# Recognize speech using Google
words = recognizer.recognize_google(audio)

# Respond
if "hello" in words:
    print("Hello there!")
elif "how are you" in words:
    print("I'm fine, thanks!")
elif "goodbye" in words:
    print("Goodbye to you too!")
else:
    print("No capisco")
