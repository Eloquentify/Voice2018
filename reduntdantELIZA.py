#edited from AIY project assistant_grpc_demo.py (https://github.com/google/aiyprojects-raspbian/blob/aiyprojects/src/examples/voice/assistant_grpc_demo.py)
#wrote by Elqtfy(youjin.fyi)

import logging

import aiy.assistant.grpc
import aiy.audio
import aiy.voicehat

import webbrowser
import random

import tempfile
import os
import threading

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s:%(name)s:%(message)s"
)
welcome = ['what?','you go first.','go ahead.','keep saying.']
askingBack = ['what did you say?','could you say that again?','what was that?','say that again?']
sarcastic = ['how about say plz?','Oh yeah? Thats good for you.','good luck.','good to know!']


def main():
    status_ui = aiy.voicehat.get_status_ui()
    status_ui.status('starting')
    assistant = aiy.assistant.grpc.get_assistant()
    button = aiy.voicehat.get_button()
    phase = 0
    work = random.randint(0,100)
    with aiy.audio.get_recorder():
        while True:
            status_ui.status('ready')
            print('Press the button and speak')
            button.wait_for_press()
            status_ui.status('listening')
            print('Listening...')
                    
            text, audio = assistant.recognize()
            #print(phase)
            if text:
                if text == 'awkward':
                    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ',new=0, autoraise=True)
                    status_ui.status('stopping')
                    break
                print('You said "', text, '"')
                
                repeat = 'Did you say ' + text +'?'
                aiy.audio.say(repeat)
                #webbrowser.open('https://www.youtube.com/results?search_query='+text,new=0, autoraise=True)
            if audio:
                work=rand(100)
                print("gonna work?: ",work)
                if work<= 50:
                    aiy.audio.play_audio(audio)
                else:
                    if phase == 0 :
                        a = welcome[rand(3)]
                        aiy.audio.say( a)
                        print (a)
                    elif phase == 1 :
                        b = askingBack[rand(3)]
                        aiy.audio.say(b)
                        print (b)
                    elif phase == 2 :
                        c = sarcastic[rand(3)]
                        aiy.audio.say(c)
                        print (c)
            
            phase += 1
            phase %= 3
                
            

def rand(a):
    return random.randint(0,a)

if __name__ == '__main__':
    main()

