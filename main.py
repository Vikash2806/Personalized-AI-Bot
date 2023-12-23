import webbrowser
import speech_recognition as sr
import pyttsx3
import os
import datetime
from bardapi import Bard
import time
from bardapi import BardCookies
import re

os.environ['_BARD_API_KEY']="eQjJYsg27bEBZMh7yAPBp6WHVLBkmUaFD7mIZQv03frM4_copNOcQN2SmzfnXZtxZ_eWbA."

cookie_dict = {
    "__Secure-1PSID": "egjJYkzJspDFcKx8heu87IXOzDJoTMR_GGAd0Alpq6A6xz9LMDsTUMke2bYl0IO8FusbNA.",
    "__Secure-1PSIDTS": "sidts-CjEBPVxjSqTtfou9ygb_8MQjrmGygIU7BH_dJVl8L30LMwbkbMJPYQDO8qA1M2l57H6FEAA",
    "__Secure-1PSIDCC": "ABTWhQGxetmQ2cjS3s82rgvsI9qvBfaQeh-gSV0RBgOK_WsBbHykPNEOL28CfF3Q_Bml35hC"
}

def say(text, rate=150):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)  # Adjust the speech rate here
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said : {query}")
            return query
        except Exception as e:
            return "Some error had occured! Sorry from jarvis"


if __name__ == '__main__':

    print('PyCharm')
    say(" Hello I am Jarvis AI ")

    while True:
        print("Listening...")
        query=takeCommand()
        #say(query)
        site = [["youtube","https://youtube.com"],["google","https://www.google.com/"]]

        res=False

        if f"open {site[0][0]}".lower() in query.lower():
            say(f"Opening {site[0][0]} Sir...")
            webbrowser.open(site[0][1])
            res=True

        if f"open {site[1][0]}".lower() in query.lower():
            say(f"Opening {site[1][0]} Sir...")
            webbrowser.open(site[1][1])
            res = True


        if "open my website".lower() in query.lower():
            say("Opening your Sir...")
            webbrowser.open("https://vikash2806.github.io/Portfolio-Website/")
            res = True

        if "open brave browser".lower() in query.lower():
            say("Opening brave browser Sir...")
            os.startfile(r"C:\Users\VIKASH\AppData\Local\BraveSoftware\Brave-Browser\Application\brave")
            res = True

        if "open Telegram".lower() in query.lower():
            say("Opening Telegram Sir...")
            os.startfile(r"C:\Users\VIKASH\AppData\Roaming\Telegram Desktop\Telegram")
            res = True

        if "open my college website".lower() in query.lower():
            say("Opening your college website Sir...")
            webbrowser.open("https://sastra.edu/")
            res = True

        if "created you".lower() in query.lower():
            say("I am AI assistant created by Vikash")
            res = True

        if "built you".lower() in query.lower():
            say("I am AI assistant created by Vikash")
            res = True

        if "is vikas".lower() in query.lower():
            say("he created me!")
            res = True

        if "Stop".lower() in query.lower():
            say("Good Bye Sir")
            res = True
            break

        if "time".lower() in query.lower():
            strftime=datetime.datetime.now().strftime("%I:%M %p")
            say(f"Sir the time is {strftime}")
            res = True

        if query == "":
            continue

        if res == False:

            bard = BardCookies(cookie_dict=cookie_dict)
            response = bard.get_answer(query)

            cleaned_response = re.sub(r'\*\*|[\*]+', '', response['content'])
            cleaned_response = re.sub(r'\n+', '\n', cleaned_response)
            cleaned_response = re.sub(r'[\r\n]+', '\n', cleaned_response)
            cleaned_response = cleaned_response.strip()

            print(cleaned_response)
            say(cleaned_response)















