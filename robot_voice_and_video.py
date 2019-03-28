import pygame
import os
from subprocess import call
import time

HOME = os.environ['HOME'] #it will automatically read your home username example /home/pi


def enter_sound(message):# spell your written word out loud
    cmd_beg= 'espeak '
    speed = ' -g10 ' # here you can change the speed of the reading
    gender = ' -ven+m3 ' #m stands for male and 3 stands for 3rd style
    cmd_end= ' 2>/dev/null' # To dump the std errors to /dev/null

    text = message #input("Enter the Text: ")
    #Replacing ' ' with '_' to identify words in the text entered
    text = text.replace(' ', '_')
    #Calls the Espeak TTS Engine to read aloud a Text
    call([cmd_beg+speed+gender+text+cmd_end], shell=True)
    
#play_sound fuction uses the pygame library
def play_sound(filename,wait): # play an existing wav format sound, wait stand for if you want the voice to be played and to wait executing any othe code or not
    filepath = os.path.join(HOME,'Documents',filename) # make sure to set where your file is located for example here home/Document p.s you dont need to write home 
    pygame.mixer.init()
    pygame.mixer.music.load(filepath)
    pygame.mixer.music.play()
    if wait:
        while pygame.mixer.music.get_busy() == True:
            continue

#this version will wait for the video to finish before executing any other line and it will close once executed
def vid_player_1(filename):
    filepath_and_exe = os.path.join('vlc --play-and-exit '+ HOME,'Documents',filename)
    #or you can use this below
    #filepath_and_exe= 'vlc --play-and-exit '+ HOME + '/Documents/'+ filename
    os.system(filepath_and_exe)

#this version will continue executing and other line of code while the video is playing and the video interface will remain open
def vid_player_2(filename,time_wait):#a goog practice 
    filepath_and_exe = os.path.join('xdg-open '+ HOME,'Documents',filename)
    #or you can use this below
    #filepath_and_exe= 'xdg-open '+ HOME + '/Documents/'+ filename
    os.system(filepath_and_exe)
    time.sleep(time_wait)

#-----------------------------EXECUTION------------------------------------------------------

enter_sound('thank you please like and subscribe to my channel')
play_sound('welcome_to_dome.wav',True) # set to True if you want it to wait untill the voice is fully executed
print ('Hello Youtube')
vid_player_1('Quasar_Dome.mp4')
time_wait = 3
#vid_player_2('nasa.mp4',time_wait)
print('Hello from Avedis Tchamitchian Chanel')