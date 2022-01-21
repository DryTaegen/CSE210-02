import random

class Cards:
    '''A stack of cards labeled 1-13.

    The responsibilty of Cards is to keep track of the card that is generated, and apply the points associated with it.
    
    Attributes:
    number (int): The number of the chosen card
    points (int): The number of points the card is worth
    choice (str): The user input that is h or l
    '''

    def init(self):
        '''Constructs a new instance of Cards with a number and points attribute.

        Args:
        self (Cards): An instance of Cards.
        '''
        self.value = 0
        self.points = 300
        self.choice = ''

    def select_card(self):
        '''Generates a new random number and calculates the points
        
        Args:
        self (Cards): An instance of Cards
        '''
        number = random.randint(1,13)

        self.value = random.randint(1,13)

        if  self.choice == 'h' and self.value > number:
            self.points == self.points + 100

        if self.choice == 'l' and self.value < number:
            self.points == self.points + 100

        if self.choice == 'h' and self.value < number:
            self.points == self.points - 75

        if self.choice == 'l' and self.value > number:
            self.points == self.points - 75

        else:
            0
    