import os
import random
from colorama import Fore

music_path = 'Music'
musics = os.listdir(music_path)

def play_music():
    
    p = random.choice(musics)
    os.startfile("Music\\" + p)
    return("Playing one of my favourite song")