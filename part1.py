import time
loose="The computer wins"
win="You win"
lives=5
score=0
draw=0
computer_lives=7
password_list=[]
while True:
    print("Fill the following information")
    username=input("Enter your Name : ")
    password=input("Enter your password : ")
    searchfile=open("accounts.txt","r")
    for line in searchfile:
        password_list.append(line.strip())
        if username and password in password_list:
            print("Access Granted")
            time.sleep(0.5)
            print("Loading....")
            time.sleep(0.5)
            print("Loading....")
            time.sleep(0.5)
            print("Loading....")
            while True:
                rps=input("rock paper scissors ?")
                computer=("rock","paper","scissors")
                import random
                computer=random.choice(computer)
                #rock if statement
                if rps=="rock" and computer=="paper":
                    print("The computer choose",computer)
                    print("")
                    print(loose)
                    print("")
                    lives-=1
                if rps=="rock" and computer=="scissors":
                    print("The computer choose",computer)
                    print("")
                    print(win)
                    print("")
                    score+=1
                    computer_lives-=1
                
                #paper if statement
                if rps=="paper" and computer=="scissors":
                    print("The computer choose",computer)
                    print("")
                    print(loose)
                    print("")
                    lives-=1
                if rps=="paper" and computer=="rock":
                    print("The computer choose",computer)
                    print("")
                    print(win)
                    print("")
                    score+=1
                    computer_lives-=1
                
                #scissors if statement
                if rps=="scissors" and computer=="rock":
                    print("The computer choose",computer)
                    print("")
                    print(loose)
                    print("")
                    lives-=1
                if rps=="scissors" and computer=="paper":
                    print("The computer choose",computer)
                    print("")
                    print(win)
                    print("")
                    score+=1
                    computer_lives-=1

                #rock draw
                if rps=="rock" and computer=="rock":
                    print("The computer choose",computer)
                    print("")
                    print("Draw")
                    print("")
                    draw+=1
                
                #paper draw
                if rps=="paper" and computer=="paper":
                    print("The computer choose",computer)
                    print("")
                    print("Draw")
                    print("")
                    draw+=1
                
                #scissors darw
                if rps=="scissors" and computer=="scissors":
                    print("The computer choose",computer)
                    print("")
                    print("Draw")
                    print("")
                    draw+=1
                
                # Rules
                
                if rps == "rules":
                    print("**********************************************")
                    print("Rules")
                    print("**********************************************")
                    print("-Rock looses against Paper")
                    print("-Rock beats Scissors")
                    print("-Paper beats Rock")
                    print("-Paper looses against Scissors")
                    print("-Scissors beats Paper")
                    print("-Scissors looses against Rock")
                    print("**********************************************")
                if rps=="display lives":
                    print(lives)
                if rps=="display score":
                    print(score)
                if rps=="display draw":
                    print(draw)
                
                # your lives
                if lives==0:
                    print("Thanks for playing")
                    print("You have run out of lives")
                    print("Your score is",score)
                    print("You darw",draw,"times")
                    stop=input("Enter to exit")
                    exit()
                
                # computer lives
                if computer_lives==0:
                    print("Thanks for playing")
                    print("Computer lost all its lives, You win...!!!!")
                    print("Your score is",score)
                    print("You darw",draw,"times")
                    stop=input("Enter to exit")
                    exit()
                
                # if you wan to exit
                if rps=="exit":
                    break
        
        else:
            print("Username and password is incorrect")
            exit()


