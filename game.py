from generator import Generator
from controler import Controler

class Game:
    def __init__(self):
        pass

    def play_game(self):
        magic_number = Generator()
        x = magic_number.generate()
        new_flow = Controler()
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
                    x = magic_number.generate()
                    y = new_flow.welcome()
                else:
                    break