from googletrans import Translator
from gtts import gTTS
import os
import time, pyperclip 

translator = Translator()

def choose_language():
    target = input('Which language do you want to translate to? ')
    return target

target = choose_language()

phrase = ''

while phrase != 'quit':
    phrase = input('Enter text: ')
    if phrase == 'quit':
        break 
    elif phrase == 'cl':
        target = choose_language()
        continue
    result = translator.translate(phrase, dest = target)
    print(result.text)
    pyperclip.copy(result.text)
    speech = gTTS(text=result.text, lang=target, slow=False)
    filename = 'speech.mp3'
    speech.save(filename)
    os.system(f"afplay {filename}")
    os.remove(filename)
    #time.sleep(2)


print('Thanks for using!')