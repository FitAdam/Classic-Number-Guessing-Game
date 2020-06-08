class Controler:
    def __init__(self):
        pass

    def welcome(self):
        y = int(float(input("I'm thinking of a number! Try to guess the number I'm thinking of: ")))
        return y 

    def get_input(self):
        y = int(input('Guess again: '))
        return y

    def play_again(self):
        game = str(input("That's it! Would like to play again? (yes/no) "))
        if game == 'yes':
            return True
        else:
            return False