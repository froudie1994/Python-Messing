import random
import time
attackpower = 5
defensepower = 5
specialattack = 5
nopointsavailable = 15
gamelength = 2

def gamemenu():
    global name
    global attackpower
    global defensepower
    global specialattack
    print ('Welcome to Adventure, ' + name + '! Your objective is to traverse the forest to save the princess, without being defeated by the forest creatures.')
    print ('These creatures may attack you at any time, so always be on your guard.')
    print ("Before we begin our quest, let's make sure you are suitably equipped for what lies ahead.")
    print ("Attack Power:" + str(attackpower))
    print ("Defense Power:" + str(defensepower))
    print ("Special Attack:" + str(specialattack))
    print (' ')
    print ("Would you like to change these? Don't forget, you can only use" + str(nopointsavailable) + " points in total.")
    print ('1. Yes')
    print ('2. No')
    changepoints = input()

def options():
    global name
    global gamelength
    print ('Welcome to the options menu. Please choose a setting to amend:')
    print ('1. Game Length')
    print ('2. Change Name')
    print ('3. Main Menu')
    settingselect = input()
    if settingselect == '1':
        print ('Thanks, how long a game would you like? Please select between one and three.')
        gamelength = int(input())
        print ('Thanks, you have changed the game length to ' + str(gamelength))
        print (' ')
        options()
    elif settingselect == '2':
        print ('Thanks, please input your player name.')
        name = input()
        print ('Thanks, ' + name + '.')
        options()
    elif settingselect == '3':
        mainmenu()
    

def mainmenu():
    global name
    print ('Thanks ' + name + ", let's see what you want to do. Please select an option:")
    print ('1. Start Game')
    print ('2. Options')
    print ('3. How to play')
    print ('4. Exit')
    menuoption = input()
    if menuoption == '1':
        gamemenu()
    elif menuoption == '2':
        options()
    elif menuoption == '3':
        howtoplay()
    elif menuoption =='4':
        print ('Thanks for playing!')
    else:
        print ("That's a wrong selection, please try again.")
        mainmenu()


print ('Hello, and welcome to Adventure! What is your player name?')
global name
name = input()
time.sleep(1)
mainmenu()


