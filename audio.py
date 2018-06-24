import speech_recognition as sr

r = sr.Recognizer()


## Our Yanny vs Laurel Audio File.
audio = 'audio.wav'

with sr.AudioFile(audio) as source:
    audio = r.record(source)



## GOOGLE
print ("Google Speech API:\n" + r.recognize_google(audio) + "\n")

## WIT
print ("WIT Recognizer thinks you said:\n" + r.recognize_wit(audio, 'RY63TZSC7YXLRAGMPNQKMPAWFETDISVU') + "\n")

## Bing
print ("Bing thinks you said:\n" + r.recognize_bing(audio, "29db94d248a843aa9095e61a993558b8") + "\n")

## Houndify
print ("Houndify Speech Recognizer:\n" + r.recognize_houndify(audio, "iYLhbpiJvLwsY0jp_GttKw==", "QDK28RbpPFJoXe54xHNso2WySh77coJNlbJ4G_8LyykJLNNBz5GkFFGAuxyUnlDHnbLADiW4x5f8MIIuf7Zfyg==") + "\n")

## Sphinx
print ("Sphinx Speech Recognizer:\n" + r.recognize_sphinx(audio))

