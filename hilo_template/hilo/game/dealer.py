from game.player import Player
import random

class Dealer:
    def __init__(self):
        self.keep_playing = True
        self.score = 75
        self.cards = []
        self.player = Player()
        self.choice = ''

    def draw_card(self):
        return random.randint(1,13)

    def score_count(self,point_change):
        self.score += point_change

    def start(self):
        self.cards.append(self.draw_card())
        
        while self.keep_playing:
            print(f"The card is: {self.cards[0]}")
            self.cards.append(self.draw_card())
            self.playing()
            self.display()


    def playing(self):
        self.score_count(self.player.is_hilo(self.cards[0], self.cards[1]))
   
    def display(self):
        print(f"The next card was: {self.cards[1]}")
        print(f"Your score: {self.score}")
        del self.cards[0]
        if self.score <= 0:
            self.keep_playing = False
            print("Game Over! Thanks for Playing")
        else:
            choice = input("Keep playing? [y/n] ")
            if choice == 'n':
                print("Thanks for Playing")
                self.keep_playing = False
            
            

