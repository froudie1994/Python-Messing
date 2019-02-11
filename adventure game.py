import random
import time
attackpower = 5
defensepower = 5
specialattack = 5
nopointsavailable = 15
gamelength = 2
currentpoints = attackpower + defensepower + specialattack

def game(): #this is the actual game. dont cock this up
    print ("We begin our quest in the castle of the tempest thieves, a deserted and horrible place.")
    print ("Before we leave, we should choose our weapon.")
    print ("Please see the weapons below, and make your choice by selecting the corresponding number. Choose carefully, once chosen you cannot change your weapon!")
    print ("1. Sword")
    print ("2. Bow & Arrow")
    print ("3. Mace")
    print (' ')
    playerweapon = int(input('Make your choice...'))
    if playerweapon == 1:
        print ("You have chosen the sword, the weapon of the noble. Use it wisely...")
    elif playerweapon == 2:
        print ("Aah the bow and arrow, range is on your side.")
    elif playerweapon == 3:
        print ("The mace, the finest weapon of them all. This will devour your enemies but be careful, you can also damage yourself...")

def changepoints():
    global attackpower
    global defensepower
    global specialattack
    global nopointsavailable
    print ('Which power would you like to change?')
    print ('1. Attack (Currently ' + str(attackpower) + ')')
    print ('2. Defense(Currently ' + str(defensepower) + ')')
    print ('3. Special Attack(Currently ' + str(specialattack) + ')')
    changepower = input()
    if changepower == '1':
        print ('What would you like your new attack power to be?')
        attackpower = int(input())
        currentpoints = attackpower + defensepower + specialattack
        print ('Thanks, did you want to change any other powers?')
        print ('1. Yes')
        print ('2. No')
        attackchange = input()
        if attackchange == '1':
            changepoints()
        elif attackchange == '2':
            if attackpower + defensepower + specialattack <= 15:
                gamemenu()
            else:
                print ('Sorry, your total game points need to be less than ' + str(nopointsavailable) + ', and your current points are ' + str(currentpoints) + '. Please amend your powers.')
                time.sleep(1)
                changepoints()
    elif changepower == '2':
        print ('What would you like your new defense power to be?')
        defensepower = int(input())
        currentpoints = attackpower + defensepower + specialattack
        print ('Thanks, did you want to change any other powers?')
        print ('1. Yes')
        print ('2. No')
        attackchange = input()
        if attackchange == '1':
            changepoints()
        elif attackchange == '2':
            if attackpower + defensepower + specialattack <= 15:
                gamemenu()
            else:
                print ('Sorry, your total game points need to be less than ' + str(nopointsavailable) + ', and your current points are ' + str(currentpoints) + '. Please amend your powers.')
                changepoints()
    elif changepower == '3':
        print ('What would you like your new special attack to be?')
        specialattack = int(input())
        currentpoints = attackpower + defensepower + specialattack
        print ('Thanks, did you want to change any other powers?')
        print ('1. Yes')
        print ('2. No')
        attackchange = input()
        if attackchange == '1':
            changepoints()
        elif attackchange == '2':
            if attackpower + defensepower + specialattack <= 15:
                gamemenu()
            else:
                print ('Sorry, your total game points need to be less than ' + str(nopointsavailable) + ', and your current points are ' + str(currentpoints) + '. Please amend your powers.')
                changepoints()
    else:
        changepoints()
           
    

def gamemenu():
    global name
    global attackpower
    global defensepower
    global specialattack
    print ("Before we begin our quest, let's make sure you are suitably equipped for what lies ahead.")
    print ("Attack Power:" + str(attackpower))
    print ("Defense Power:" + str(defensepower))
    print ("Special Attack:" + str(specialattack))
    print (' ')
    print ("Would you like to change these? Don't forget, you can only use " + str(nopointsavailable) + " points in total.")
    print ('1. Yes')
    print ('2. No')
    changepointsind = input()
    if changepointsind == '1':
        changepoints()
    elif changepointsind == '2':
        game()

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
        print ('Welcome to Adventure, ' + name + '! Your objective is to traverse the forest to save the princess, without being defeated by the forest creatures.')
        print ('These creatures may attack you at any time, so always be on your guard.')
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


