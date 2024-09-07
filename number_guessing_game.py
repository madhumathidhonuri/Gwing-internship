import random
name=input("enter your name:")
game=input("do you want play {} ".format(name))
if game.lower()=='yes':
  print("come on start guessing the numbers {} ".format(name))
else:
  exit()

number=input("enter a number: ")
if number.isdigit():
    number=int(number)
    if number<=0:
        print("enter a number larger than 0")
        exit()
else:
    print("enter a number next time")
    exit()

random_number=random.randint(0,number)
guesses=0
while True:
    guesses+=1
    guess=input("guess the number: ")
    if guess.isdigit():
        guess=int(guess)
    else:
        print("enter the number next time")
        continue
    if guess==random_number:
        print("You got it! {}".format(name))
        break
    elif guess>random_number:
        print("You guessed above the number!")
    else:
        print("You guessed below the number!")
print("You guessed the number in"+" "+str(guesses)+" "+"guesses")