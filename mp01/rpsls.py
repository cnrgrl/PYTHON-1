import random
def rpsls(player_choice,computer_choice):
    d=(computer_choice-player_choice)%5
    if d==1 or d==2:
        print("computer wins")
    elif d==0:
        print("Spiel zieht")
    else:
        print("player wins")

def name_to_number(name):

    if name == "rock":
        number=0
    elif name=="paper":
        number=2
    elif name=="scissor":
        number=4    
    elif name=="lizard":
        number=3
    elif name=="spock":
        number=1    
    else :
        number=""
        print("Sie haben einen falsche Auswahl eingegeben!")
    return number


def number_to_name(num):
    nam=""
    
    if num==0:
        nam="rock"
    elif num==1:
        nam="spock"
    elif num==2:
        nam="paper"
    elif num==3:
        nam="lizard"
    elif num==4:
        nam="scissor"
    else :
        nam=""
        print("Error!")
    return nam

name=input("Player Choice  :").lower()
#comp_number=name_to_number(name)
print(name.upper())
p_choice=name_to_number(name)



#num=int(input("Computer's Guess"))

comp_number=random.randrange(0,4)

computer_choice=number_to_name(comp_number).upper()
print(computer_choice)

rpsls(p_choice,comp_number)