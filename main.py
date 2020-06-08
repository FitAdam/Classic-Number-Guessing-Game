"""
import random


def generate():
    x = random.randrange(100)
    return x

"""
from generator import Generator
from controler import Controler

magic_number = Generator()
x = magic_number.generate()
new_flow = Controler()

def game():
    #x = generate()
    y = new_flow.welcome()
    gameOn = True
    while gameOn:
        if y < x:
            print('Too low!')
            y = new_flow.get_input()
        elif y > x:
            print('Too High')
            y = new_flow.get_input()    
        else:
            gameOn = new_flow.play_again()
            if gameOn:
                y = new_flow.welcome()
            else:
                break


game()