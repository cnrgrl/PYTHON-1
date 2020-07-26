import random

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

#num=int(input("Computer's Guess"))

comp_choice=random.randrange(0,4)

player_number=number_to_name(comp_choice).upper()
print(player_number)






def rpsls(player_choice): 
    
    
    
    return comp_choice
