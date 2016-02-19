from sys import exit
import random

prompt = "> "

def initial(mp, hp):
    mp = random.random() * 100
    hp = 100
    return mp, hp

def check_status(mp, hp):
    print "Now you have %d money, and %d health. Cheer!" % (mp, hp)
    raw_input("Press Enter key to continue...")

def game_choose(mp, hp):
    print "Which game you want to play now? "
    print "1. Shooter"
    print "2. Fighter"
    print "3. Quit"
    game_choice = raw_input(prompt)

    if game_choice == "1":
        mp, hp = shooter(mp, hp)
    elif game_choice == "2":
        mp, hp = fighter(mp, hp)
    else:
        fail()

    return mp, hp

def fail():
    print "Bad luck, you are quit!"
    exit(0)

def new_game():
    print "Restarting... After restart, all your record will be erased."
    raw_input("Press Enter to start a new game... ")
    start()

def shooter(mp, hp):
    debt = 6
    print "Shooting game is starting, get ready......"
    target = random.random() * 10
    aim_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print "Target is ready, choose your aim timing..."
    choice = int(raw_input("1 ~ 9: "))
    aim = aim_list[choice]

    if abs(aim - target) <= 3:
        print "Got it!! You won, contratulation! You have already gain %d MP!" % (debt * 1.2)
        mp += debt * 1.2
        print "You now have %d money." % mp

    else :
        print "Missed!! You lost."
        mp -= debt

    if mp >= 0:
        print "You now have %d money." % mp
        print "Do you want to play again?"
        print "1. play again."
        print "2. choose another game."
        print "3. quit."
        play_again = raw_input(prompt)

        if play_again == '1':
            shooter(mp, hp)
        elif play_again == '2':
            game_choose(mp, hp)
        elif play_again == '3':
            exit(0)
        else:
            print "Do not understand. Let's choose a game to play again."

    else:
        print "You are out of Money, now quiting..."
        exit(0)

    return mp, hp

def fighter(mp, hp):
    print "This is example code of fighter function"
    mp += 3

    return mp, hp

def start():
    mp = 0
    hp = 0
    print "Welcome to Sidney's game tour, please tell me what's your name?"
    name = raw_input(prompt)
    print "Hi %s, now we are initializing your role..." % name
    mp, hp = initial(mp, hp)
    print "Done! What you want to do now?"

    while True:
        print "1. Choose a game."
        print "2. Check my status."
        print "3. Quit the game."
        choice = raw_input(prompt)

        if choice == "1":
            mp, hp = game_choose(mp, hp)
        elif choice == "2":
            check_status(mp, hp)
        elif choice == "3":
            fail()
        else:
            print "Can`t understand that, choose again!"


start()
