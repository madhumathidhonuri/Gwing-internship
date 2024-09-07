import random

name=input("enter your name:")
game=input("do you want to play {} ? ".format(name))
if game.lower()=='yes':
    print("come on {} lets play".format(name))
else:
    quit()

options = ("rock", "paper", "scissors")
player_score=0
computer_score=0
running = True

while running:

    computer = random.choice(options)
    player = input("Enter a choice (rock, paper, scissors): ")

    print("computer choosed:",computer)

    if player == computer:
        print("It's a tie!")
    elif player=="rock" and computer=="scissors":
        print("You win!")
        player_score+=1
    elif player=="paper" and computer=="rock":
        print("You win!")
        player_score+=1
    elif player=="scissors" and computer=="paper":
        print("You win!")
        player_score+=1
    else:
        print("You lose!")
        computer_score+=1
        print("{} scored:".format(name),player_score)
        print("computer_score:",computer_score)
    play_again=input("do you want to play {} :".format(name))
    if play_again.lower()=='yes':
        continue
    else:
        break
print("{} scored:".format(name),player_score)
print("computer score:",computer_score)
print("Thanks for playing!")