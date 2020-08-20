from colorama import Fore
from greet import greeting_msg
import pyttsx3
import os
from help_module import helping
from games import play_game
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

def speak(text):
	engine.say(text)
	engine.runAndWait()

os.system("cls")

name = "Enter Command: "

msg = greeting_msg()
print(Fore.GREEN + msg + Fore.RESET)
speak(msg)
print(Fore.GREEN + "What can I help for you." + Fore.RESET)
speak("What can I help for you.")

thank = ["My pleasure", "Anytime", "Anything for you", "Mention Not", "Welcome"]

while(True):
    x = input(Fore.RED + name + Fore.RESET)

    if len(x) <= 0:
        print(Fore.CYAN + "Please Enter a command" + Fore.RESET)
        speak("Please Enter a command")

    if "bye" in x or "quit" in x or "cya" in x or "exit" in x:
        print(Fore.CYAN + "Bye!! See You Soon" + Fore.RESET)
        speak("Bye!! See You Soon")
        exit() 

    if "help" in x:
        helping()
        speak("I can help you with above things")

    elif "thank you" in x or "thanks" in x:
        p = random.choice(thank)
        print(Fore.CYAN + p + Fore.RESET)
        speak(p)

    elif "games" in x or "game" in x:
        print(Fore.CYAN + play_game() + Fore.RESET)
        speak("Opening game")

    elif ( "run" in x or "execute" in x or "open" in x ) and "chrome" in x:
        print(Fore.CYAN + "Opening Chrome" + Fore.RESET)
        speak("Opening Chrome")
        os.system("chrome")

    elif ( "run" in x or "execute" in x or "open" in x ) and ( "code" in x or "vs code" in x or "vscode" in x ):
        print(Fore.CYAN + "Opening VS Code" + Fore.RESET)
        speak("Opening VS Code")
        os.system("code")

    elif ( "run" in x or "execute" in x or "open" in x ) and ( "editor" in x or "notepad" in x or "text" in x ):
        print(Fore.CYAN + "Opening Notepad" + Fore.RESET)
        speak("Opening Notepad")
        os.system("notepad")

    elif ( "run" in x or "execute" in x or "open" in x ) and ( "editor" in x or "sublime" in x or "text" in x ):
        print(Fore.CYAN + "Opening Sublime" + Fore.RESET)
        speak("Opening Sublime")
        os.system("sublime_text")
    
    elif "do not" in x or "don't" in x or "not" in x:
        print(Fore.CYAN + "Okay!! I will not run this" + Fore.RESET)
        speak("Okay!! I will not run this")

    else:
        print(Fore.CYAN + "Right Now Not Supported!! Will be availabe in future" + Fore.RESET)
        speak("Right Now Not Supported!! Will be availabe in future")