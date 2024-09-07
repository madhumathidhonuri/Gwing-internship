print("Hello!! Welcome to computer quiz game")
name=input("enter your name:")
play=input("do you want to play {} ? ".format(name))
if play.lower()=='yes':
    print("let's start the game {}".format(name))
    print("In this quiz you will be given 5 questions,for every correct answer you will get one mark")
else:
    exit()
questions=("1.What is the color of blood when it's inside your body?",           
"2.Which is the fastest bird in the world?",
"3.What is the tallest waterfall in the world?",
"4.Which planet is known as the Red Planet?",
"5.Which element is known as the building block of life?")

options=(("a.yellow","b.white","c.Red","d.Green"),
         ("a.Bald Eagle","b.peregrine Falcon","c.Humming Bird","d.Raven"),
         ("a.Angel Falls,venezuela","b.Niagara Falls,New York","c.Wailua Falls,Hawaii","d.Sutherland Falls,New Zealand"),
         ("a.Venus","b.Saturn","c.Mars","d.Mercury"),
         ("a.Oxygen","b.Carbon","c.Hydrogen","d.Nitrogen"))

Feedback=("(c) The color of blood when inside the body is red. This is due to hemoglobin, a protein that binds with oxygen and gives blood its red hue. The presence of oxygenated or deoxygenated blood determines its shade of red.",
          "(b) Renowned for its remarkable flight speed, the peregrine falcon is distinguished as the fastest bird globally, capable of reaching speeds exceeding 300 km (186 miles) per hour during dives. This exceptional velocity also earns it the title of the fastest animal on Earth.",
          "(a) The tallest waterfall in the world is Angel Falls in Venezuela. With a height of 3,212 feet (979 meters) and a continuous drop, Angel Falls holds the title as the highest waterfall on the planet.",
          "(c) Mars is commonly referred to as the Red Planet due to its reddish appearance, which is visible from Earth. This characteristic color comes from iron oxide, or rust, that covers much of the planet's surface. Mars' distinct hue makes it a visually distinctive object in the night sky and has also influenced a significant amount of scientific research focused on its geology and potential for supporting life.",
          "(b) Carbon is often referred to as the building block of life due to its unparalleled ability to form stable bonds with many elements, including itself. This property allows carbon to form a diverse array of complex organic molecules, which are fundamental components of biological organisms. Carbon's versatile bonding makes it central in the chemistry of almost all living creatures and is thus critical to the study and understanding of biochemistry.")


answers=("c","b","a","c","b")

guesses=[]

score=0

question_num=0

for question in questions:
    print()
    print(question)
    for option in options[question_num]:
        print()
        print(option)
    guess=input("enter (a,b,c,d):").lower()
    guesses.append(guess)
    if guess==answers[question_num]:
        print("correct")
        score+=1
    else:
        print("incorrect")
        print("{} is the correct answer".format(answers[question_num]))
        for feed in Feedback[question_num]:
            print(feed,end="")
    question_num+=1
    print()
print("you answered"+" "+str(score)+" "+"out of 5")
if score==(4,5):
    print("excellent")
else:
    print("well played")
print("your score is"+" "+str(score))
            
        
        

