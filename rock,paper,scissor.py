from random import randint
import time

print("                       ROCK  PAPER  SCISSOR","\n")
time.sleep(2)
#instruction-----------------------------------------------------------------------------
print("""Instruction:
~give the option(rock,paper,scissor)
~if your choice is rock and computer choice is scissor then you win else you lose.
~if your choice is paper and computer choice is rock then you win else you lose.
~if your choice is scissor and computer choice is paper the you win else you lose.
~five round will be conduct and the scores will be calculated.
~finally the scores are displayed""","\n")

time.sleep(1)

print("Loading.......","\n")
time.sleep(3)

#random choice-----------------------------------------------------------------------------
t = ["rock","paper","scissor"]
computer = t[randint(0,2)]

#score--------------------------------------------------------------------------------------
s1=0
s2=0

#match start--------------------------------------------------------------------------------
def again():
    #random choice-----------------------------------------------------------------------------
    t = ["rock","paper","scissor"]
    computer = t[randint(0,2)]
    #score--------------------------------------------------------------------------------------
    s1=0
    s2=0
    #match start--------------------------------------------------------------------------------
    for i in range(1,6):
        player=str(input("Enter your choice:"))
        if player == computer:
            print("tie...")
            s1 = s1 + 1
            s2 = s2 + 1
            print("player score = ",s1," computer score = ",s2)
        elif player == "rock":
            if computer == "paper":
                print("you lose.... ",computer," covers ",player)
                s2 = s2 + 1
                print("player score = ",s1," computer score = ",s2)
            else:
                print("you win.....! ",player," breaks ",computer)
                s1 = s1 + 1
                print("player score = ",s1," computer score = ",s2)        
        elif player == "paper":
            if computer == "scissor":
                print("you lose...... , ",computer," cuts ",player)
                s2 = s2 + 1
                print("player score = ",s1," computer score = ",s2)
            else:
                print("you win.......! , ",player," covers ",computer)
                s1 = s1 + 1
                print("player score = ",s1," computer score = ",s2)
        elif player == "scissor":
            if computer == "rock":
                print("you lose....... , ",computer," breaks ",player)
                s2 = s2 + 1
                print("player score = ",s1," computer score = ",s2)
            else:
                print("you win..........! , ",player," cuts ",computer)
                s1 = s1 + 1
                print("player score = ",s1," computer score = ",s2)
    time.sleep(1)
    print("Wait for a result","\n")
    time.sleep(2)

#desicion making-------------------------------------------------------
    if(s1>s2):
        print("CONGRATULATION,YOU WIN THE MATCH","\n")
    elif(s1<s2):
        print("SORRY,YOU LOSE THE MATCH TRY AGAIN","\n")
    else:
        print("MATCH DRAW","\n")
print(again())

#rematch----------------------------------------------------------------
rematch=str(input("If you want to play again(yes/no):"))
if(rematch == "yes"):
    print(again())
else:
    print("THANK YOU.......!")


    
  


           

