import speech_recognition as s_r
from gtts import gTTS
import os
import easyocr

def Speech_text():
    r = s_r.Recognizer()
    my_mic = s_r.Microphone(device_index=1)  # my device index is 1, you have to put your device index

    with my_mic as source:
        print("Say now!!!!")
        r.adjust_for_ambient_noise(source)  # reduce noise
        audio = r.listen(source)  # take voice input from the microphone
        print(r.recognize_google(audio))
        print("done")

def Text_Speech(mytext):
    myobj = gTTS(text=mytext, lang="en", slow=False)
    myobj.save("welcome.mp3")
    os.system("welcome.mp3")

def Image_text():
    reader = easyocr.Reader(['en', 'ta'])
    results = reader.readtext('1.jpg') #img choosen from path...
    text = ' '
    for result in results:
        text += result[1] + ' '
    print(text)

def Image_speech():
    reader = easyocr.Reader(['en', 'ta'])
    results = reader.readtext('1.jpg') #img choosen from path...
    text = ' '
    for result in results:
        text += result[1] + ' '
    Text_Speech(text)


while 1:
    print("*"*20,"MENU","*"*20)
    print("1-> Speech to text")
    print("2-> Text to Speech")
    print("3-> Image to text")
    print("4-> Image to speech")
    print("5-> Exit")
    print("*" * 46)
    choice=int(input("Enter your choice: "))
    if choice==1:
        Speech_text()
    elif choice==2:
        mytext = input("Enter the text you have to convert: ").strip()
        Text_Speech(mytext)
    elif choice==3:
        Image_text()
    elif choice==4:
        Image_speech()
    elif choice>5:
        print("invalid choice, try again!!!")
    else:
        break


