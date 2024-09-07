from colorama import Back,Fore,Style
print(Fore.YELLOW,Back.BLUE)
print(10*"    ","WELCOME TO CHOOSE YOUR OWN WAY",10*"    ")
print(Style.RESET_ALL)
print(10*"    ","------------------------------")
print(10*"    ","")
print(Fore.MAGENTA)
name=input("Enter your name: ")
print(Style.RESET_ALL+f"Welcome {name} to Adventure game ")
q0=input("==>>>can you make a plan or help in to some one in this game? (yes/no) ")
if q0=="yes":
    q=input("""==>>>A man is running towords you and asked that, i am new to this place please give me shelter . Do you want to give shelter ?(yes/no)  """)
    if q=="yes":
        print("After some time a police man come to you and asked that a theif ran toward you did you see ? you relised that he is a theft and say   (yes/no)  ")
        q1=input("==>>>")
        if q1=="yes":
            print("honestly you said that 'i know and he is in my house' and the police man catch him."+Fore.GREEN+ "YOU WON !!"+Style.RESET_ALL)    
        elif q1!="yes":
            print("You supported to the theif and you want to Jail"+Fore.RED+" YOU LOSS"+Style.RESET_ALL)
        else:
            print("WRONG INPUT YOU ENTERED")
    elif q!="yes":
        print("Thief is tring to kill you,do you oppose and knock him ? (yes/no) ")
        q2=input("==>>>")
        if q2=="yes":
            print("Theif catched by police man and" +Fore.GREEN+ "YOU WON !!"+Style.RESET_ALL)
        elif q2!="yes":
            print("Thief killed you and "+Fore.RED + "YOU LOSS"+Style.RESET_ALL) 
        else:
            print("enter the correct input")  
    else:
        print("enter  the correct input ")   
else:
    print(Fore.YELLOW+"OK, Try again"+Style.RESET_ALL)