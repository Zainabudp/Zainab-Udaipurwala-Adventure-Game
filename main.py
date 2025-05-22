###############################
# Mid-Term Project - ANA1001
# Zainab Udaipurwala
###############################

# importing required modules
from os import system, name 
from sys import exit 
import time
import random


#Declaring variables
health = 100
wallet = 0
backpack = []
code = []

#Clear screen code
def clear():
    
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

#Display summary code
def summary():
    #Calling the global variables
    global health
    global wallet
    global backpack

    #Print the summary of the total coins and lives and items
    print(f'''
          SUMMARY BOARD
    _____________________________
    Wallet balance - {wallet}
    Health meter   - {health}%
    Backpack Items  - {backpack}
    -----------------------------''')

#health check code
def health_check():
    global health #calling global variable

    #Print message if out of health
    if health == 0:
      print("Sorry you ran out of health.")
      print('''
__   __                            ______               _   _ _ _ 
\ \ / /                            |  _  \             | | | | | |
 \ V /___  _   _    __ _ _ __ ___  | | | |___  __ _  __| | | | | |
  \ // _ \| | | |  / _` | '__/ _ \ | | | / _ \/ _` |/ _` | | | | |
  | | (_) | |_| | | (_| | | |  __/ | |/ /  __/ (_| | (_| | |_|_|_|
  \_/\___/ \__,_|  \__,_|_|  \___| |___/ \___|\__,_|\__,_| (_|_|_)
''')
      time.sleep(2)
      exit()
    elif health < 20:
      print("You are running low on Health. Consume the Energy Drink to increase your health by 20%")
      print("Enter [1] for Yes, Enter [2] for No")
      useranswer = int(input('>>>'))
      if useranswer == 1:
        health += 20

      #Print Game Name
print('''

    _    _      _                            _            ___                             _ _   _ _ _ 
   | |  | |    | |                          | |          |_  |                           (_(_) | | | |
   | |  | | ___| | ___ ___  _ __ ___   ___  | |_ ___       | |_   _ _ __ ___   __ _ _ __  _ _  | | | |
   | |/\| |/ _ | |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \      | | | | | '_ ` _ \ / _` | '_ \| | | | | | |
   \  /\  |  __| | (_| (_) | | | | | |  __/ | || (_) | /\__/ | |_| | | | | | | (_| | | | | | | |_|_|_|
    \/  \/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/  \____/ \__,_|_| |_| |_|\__,_|_| |_| |_| (_(_(_)
                                                                                        _/ |          
                                                                                       |__/           
    

''')
time.sleep(1.5)
clear()
# Scene Introduction
def scene():
    global backpack
    print("You are currently in a dense foggy Jungle surrounded by long trees.")
    print("You will need to complete the Quest in order to free yourself from this Jungle.")
    print("You start walking a little into the forest and see that there is a Cave to your Left and a River flowing to your right.")
    print("The Cave is pitch dark and the River has many Sharks swimming in it. Where would you go")
    print("Press [1] - Go into the Cave")
    print("Press [2] - Go into the River")
    print("Press [3] - To Quit Game")

    while True:       #Setting a while loop untill broken
        caveorriver = input('>>>')   #Asking for Player input
        clear()
        if int(caveorriver) == 1:
                print("You enter the Cave but cannot see anything. You stumble upon a torch and light it. You now see 2 Doors at the far end of the cave.")
                print("One Door says Room 1 and the other door says Escape with a message over it which reads:")
                print('''
    "The door to escape the cave contains a code padlock with a three digit code. You will find the code hidden in each room you enter, and must solve it
    to get coins. You shall find three numbers, and must order them correctly. For every code you collect you get 50 coins and with each passing room your
    health will keep reducing by 10%.
    Good Luck on your Quest!!"
    ''')
                print('''You look around the cave and find:
A Backpack
An Axe
Energy Drinks''')
                print('You took the items, kept them inside the backpack and entered the Door that said Room 1.')
                backpack.append('Axe')
                backpack.append('Energy drinks')
                input('''
                Press [Enter] to Visit Room 1.  >>> ''')
                roomone()     #Takes you to the next room or function
                break
        elif int(caveorriver) == 2:
                print("You were eaten by the Sharks.")
                steplose()    #Takes you to the said function
                
                break
        elif int(caveorriver) == 3:
                quit()
                break
        else:
                print("Enter either 1, 2 or 3:")
        
#Room 1 code
def roomone():     #Definig a another function
    #declare variables
    global wallet
    global health
    global code
    flag = 1
    codeValue = random.randint(0,9)   #Variable for generating a random integer for the code.

    health_check()
    clear()
    print("You are in ROOM 1. There is a beautiful painting on one wall, a net trap on the floor and another door behind you.")
    summary()
    
    while flag != 0:      #Giving a command of printing if variable is not equest to
        print('''
Press[1] - Examine the Painting
Press[2] - Step on the net Trap
Press[3] - Go through the Door
Press[4] - To Quit Game
''')
        choiceone = int(input('>>>'))
        clear()
        if choiceone == 1:
            print("")
            print("While you are studying the painting you notice the number " + str(codeValue) + " painted on the corner.")
            print("You start feeling out of breath. You health is decreased by 5%")
            code.append(str(codeValue))
            wallet += 50     #Adding/deducting value into the variable
            health -= 5      #Adding/deducting value into the variable
        elif choiceone == 2:
            flag = 0
            steplose()
        elif choiceone == 3:
            flag = 0
            health -= 10
            roomthree()
        elif choiceone == 4:
            quit()
            break

#Room 2 code
def roomtwo():    #Definig a another function
    #declare variables
    global wallet
    global health
    global code
    flag = 1
    codeValue = random.randint(0,9)
    
    health_check()   #Checking for Health meter to declare if dead or not.
    clear()
    print("You find yourself in a small Cabin. There is a man sitting on a chair, a Net Trap on the floor and an exit board.")
    summary()
    
    while flag != 0:
        print('''
Press[1] - Talk to the man
Press[2] - Step on the Net Trap
Press[3] - Follow the exit board
Press[4] - To Quit Game
''')
        choiceone = int(input('>>>'))
        if choiceone == 1:
            clear()
            print("")
            print("Hi! I am Joe. I like asking riddles and if you crack the answer the correctly, I will give what you need to escape from here!")
            print("I will give you 3 chances to guess the answer. Each wrong answer will reduce your health by 10% and you also loose 10 coins, on failing to crack the answer your health will reduce to 0 and you will die.")
            time.sleep(2)
            print("Here you go..\nI’m hot and I live in the sky. I’m bright; don’t look directly at me. I will disappear at night. What am I?")
            active = 2
            while active != -1:
                answer = input("\nEnter your answer here: ")
                if answer.lower() == 'sun' and active != -1:
                    print(f"Awesome! Here is your number clue {codeValue}, and a 100 coins")
                    wallet += 100
                    code.append(str(codeValue))
                    active = -1
                elif answer.lower() != 'sun' and active != 0:
                    active -= 1
                    print("Sorry wrong answer, try again!")
                    health -= 10
                    wallet -= 10
                elif answer.lower() != 'sun' and active == 0:
                    print("Sorry, you did not guess the answer within the given chances.\nYour health is now at 0%")
                    health -= health
                    summary()
                    time.sleep(4)
                    clear()
                    health_check()
                    time.sleep(2)
                    
        elif choiceone == 2:
            flag = 0
            steplose()
        elif choiceone == 3:
            flag = 0
            health -= 10
            clear()
            roomfive()
        elif choiceone == 4:
            quit()  
            break
          
#Room 3 code
def roomthree():
    #declare variables
    global wallet
    global health
    global backbag
    global code
    flag = 1
    codeValue = random.randint(0,9)

    health_check()
    clear()
    print("You now find yourself on barren land of the Jungle with just one Big Tree. There is a huge Wooden Trunk near the tree, a Net Trap on the floor and a Secret passage way in the Tree trunk.")
    summary()

    while flag != 0:
        print('''
Press[1] - Open The Trunk
Press[2] - Step on the Net Trap
Press[3] - Enter the Secret Passageway
Press[4] - To Quit Game''')

        choicethree = int(input('>>>'))

        if choicethree == 1 and 'Axe' in backpack:
            clear()
            print("You cut open the wooden trunk using the Axe in your backpack.")
            print("Inside the trunk you notice the number " + str(codeValue) + ".")
            print("You are now tired and hungry and your health has reduces by another 10%")
            code.append(str(codeValue))
            wallet += 50
            health -= 10
            backpack.remove('Axe')     #Removing the items from the list
        elif choicethree == 1 and 'Axe' not in backpack:      #Giving a conditional statement
            print(f"You have already opened the wooden trunk, so go to another place")
        elif choicethree == 2:
            flag = 0
            steplose()
        elif choicethree == 3:
            flag = 0
            health -= 10
            roomfour()
        elif choicethree == 4:
            quit()
            break

def roomfour():   #Definig a another function
    #declare variables
    global wallet
    global health
    global backbag
    flag = 1

    health_check()
    clear()
    print("The Secret Passageway lead you to an old House Boat. There is a talking cat, a Net Trap on the floor and lockless door at one end.")
    summary()

    while flag != 0:
        print('''
Press[1] - Talk to the cat
Press[2] - Step on the Net Trap
Press[3] - Enter lockless door
Press[4] - To Quit Game
''')

        choicethree = int(input('>>>'))
        clear()
        if choicethree == 1:
            print("Hi I am Tommy, now I will show a number and it will vanish in seconds. Let me check your memory power...")
            print("I will give you 3 chances to guess the answer. With each wrong answer you loose 10 coins, on failing to crack the answer your health will reduce to 0 and you will die.")
            time.sleep(5)
            value = random.randint(10000, 99999)
            print(f"Here you go..\n\n{value}")
            time.sleep(4)
            clear()
            active = 2
            while active != -1:
                answer = int(input("\nEnter your answer here: "))
                if answer == value and active != -1:
                    print("Well done! You really have great memory! Here is the cookie to boost your energy and this cake is my gift for your memory power!")
                    health += 30
                    backpack.append('Cake')    #Adding the item in the list
                    active = -1
                elif answer != value and active != 0:    #Giving a conditional statement
                    wallet -= 10
                    print("Sorry wrong answer, try again!")
                    active -= 1
                elif answer != value and active == 0:
                    print("Sorry, you did not guess the answer within the given chances.\nYour health is now at 0%")
                    health -= health
                    summary()
                    time.sleep(4)
                    clear()
                    health_check()
                    time.sleep(2)
        elif choicethree == 2:
            flag = 0
            steplose()
        elif choicethree == 3:
            flag = 0
            health -= 10
            roomtwo()
        elif choicethree == 4:
            quit()
            break

def roomfive():      #Definig a another function
    #declare variables
    global health
    global code
    if len(code) != 3 :
      print("\n\tYou did not collect the Code. Go back and start over")
      time.sleep(2)
      clear()
      roomone()
    else:
      final_code = int(str(code[0]) + str(code[1]) + str(code[2]))    #creating variable to store the codes generating during the game
      chance = 1

      clear()
      print("You are back in the cave and you see the Escape door with the Code padlock.")
      summary()
      print("You walk to the door. You enter a code you collected up till now\nNote: You have only 2 chances to unlock, if you fail then you'll be dead!")

      while chance != -1:
          health_check()
          while True:
              try:
                  option1 = int(input("Digit one: "))
                  break
              except:
                  print("Digit one must be a whole number between 0-9:")
        
          while True:
              try:
                  option2 = int(input("Digit two: "))
                  break
              except:
                  print("Digit two must be a whole number between 0-9:")
        
          while True:
              try:
                  option3 = int(input("Digit three: "))
                  break
              except:
                  print("Digit three must be a whole number between 0-9:")
        
          chosenCode = int(str(option1) + str(option2) + str(option3))

          if chosenCode == final_code and chance != -1:
              clear()
              print("You hear a click, and the padlock shifts. As you press open the door a rush of fresh, warm air caresses your face as you step out to a now Beautiful Jungle. At last,")
              print('''
                 
__   _______ _   _    ___ ______ _____  ____________ _____ _____   _ _ 
\ \ / |  _  | | | |  / _ \| ___ |  ___| |  ___| ___ |  ___|  ___| | | |
 \ V /| | | | | | | / /_\ | |_/ | |__   | |_  | |_/ | |__ | |__   | | |
  \ / | | | | | | | |  _  |    /|  __|  |  _| |    /|  __||  __|  | | |
  | | \ \_/ | |_| | | | | | |\ \| |___  | |   | |\ \| |___| |___  |_|_|
  \_/  \___/ \___/  \_| |_\_| \_\____/  \_|   \_| \_\____/\____/  (_(_)
                                                                       
                                                                       
''')
              chance = -1
          elif chosenCode != final_code and chance != 0:
              health -= 5 
              print("You jiggle the padlock, but to no avail. The code is incorrect.Try Again!")
              chance -= 1
          elif chosenCode != final_code and chance == 0:
              chance = -1
              print("Chances are over! You were very close to be free")
              print('''                  
__   _______ _   _    ___ ______ _____  ______ _____ ___ ______   _ 
\ \ / |  _  | | | |  / _ \| ___ |  ___| |  _  |  ___/ _ \|  _  \ | |
 \ V /| | | | | | | / /_\ | |_/ | |__   | | | | |__/ /_\ | | | | | |
  \ / | | | | | | | |  _  |    /|  __|  | | | |  __|  _  | | | | | |
  | | \ \_/ | |_| | | | | | |\ \| |___  | |/ /| |__| | | | |/ /  |_|
  \_/__\___/ \___/__\_|_|_\_|_\_\____/ _|___/_\____\_| |_|___/   (_)
 |  __ \/ _ \|  \/  |  ___| |  _  | | | |  ___| ___ \ | | |         
 | |  \/ /_\ | .  . | |__   | | | | | | | |__ | |_/ / | | |         
 | | __|  _  | |\/| |  __|  | | | | | | |  __||    /  | | |         
 | |_\ | | | | |  | | |___  \ \_/ \ \_/ | |___| |\ \  |_|_|         
  \____\_| |_\_|  |_\____/   \___/ \___/\____/\_| \_| (_(_)         

''')

def steplose():
  print("Oops! Not a smart Choice.")
  print('''                    
__   _______ _   _    ___ ______ _____  ______ _____ ___ ______   _ 
\ \ / |  _  | | | |  / _ \| ___ |  ___| |  _  |  ___/ _ \|  _  \ | |
 \ V /| | | | | | | / /_\ | |_/ | |__   | | | | |__/ /_\ | | | | | |
  \ / | | | | | | | |  _  |    /|  __|  | | | |  __|  _  | | | | | |
  | | \ \_/ | |_| | | | | | |\ \| |___  | |/ /| |__| | | | |/ /  |_|
  \_/__\___/ \___/__\_|_|_\_|_\_\____/ _|___/_\____\_| |_|___/   (_)
 |  __ \/ _ \|  \/  |  ___| |  _  | | | |  ___| ___ \ | | |         
 | |  \/ /_\ | .  . | |__   | | | | | | | |__ | |_/ / | | |         
 | | __|  _  | |\/| |  __|  | | | | | | |  __||    /  | | |         
 | |_\ | | | | |  | | |___  \ \_/ \ \_/ | |___| |\ \  |_|_|         
  \____\_| |_\_|  |_\____/   \___/ \___/\____/\_| \_| (_(_)         ''')

def quit():
  print("\t\tWe are Sorry to see you go.")
  print("\t\tUntill Next Time!!!!")
  time.sleep(1)

scene()    #Calling out the main function to start the game