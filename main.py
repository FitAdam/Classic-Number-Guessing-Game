import random


def generate():
    x = random.randrange(100)
    return x

def welcome():
    y = int(input("I'm thinking of a number! Try to guess the number I'm thinking of: "))
    return y 

def get_input():
    y = int(input('Guess again: '))
    return y

def play_again():
    game = str(input("That's it! Would like to play again? (yes/no) "))
    if game == 'yes':
        return True
    else:
        return False
    
def game():
    x = generate()
    y = welcome()
    gameOn = True
    while gameOn:
        if y < x:
            print('Too low!')
            y = get_input()
        elif y > x:
            print('Too High')
            y = get_input()    
        else:
            gameOn = play_again()
            if gameOn:
                y = welcome()
            else:
                break


game()