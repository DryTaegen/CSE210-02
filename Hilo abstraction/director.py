from cards import Cards
import random

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        cards (List[Cards]): A list of Die instances.
        total_points (int): The score for the entire game.
    """
    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.cards = []
        self.is_playing = True
        self.total_points = 300

        for i in range(13):
            cards = Cards()
            self.cards.append(cards)

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        self.higher_or_lower()
        self.do_updates()
        self.do_outputs()

    def higher_or_lower(self):
        '''Ask the user if the next card is higher or lower
        Args:
        self(Director): An instance of Director
        ''' 
        number = random.randint(1,13)
        print(f'The card is {number}')       
        h_or_l = input('Higher or Lower [h/l]: ')
        print(h_or_l)

    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        for i in range(len(self.cards)):
            card = self.cards[i]
            card.select_card()
            self.total_points == card.points

    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """

        for i in range(len(self.cards)):
            card = self.cards[i]
            value = f'{card.value}'
        print(f'The next card was: {value}')
        print(f"Your score is: {self.total_points}\n")
        self.is_playing == (self.score > 0)
        y_n = input('Play again? [y/n]: ')
