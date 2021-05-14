class player:
    #do guess only allows h or l and repeats if invalid answer given
<<<<<<< HEAD
    def __init__(self) -> None:
        pass
=======
>>>>>>> 6257f76f979c9954a2b6d35422d747c8234245f2
    def do_guess(self):
        while True:
            guess = input("Higher or Lower? [h/l]: ")
            if guess == 'h' or guess == 'l':
                return guess
                
            else:
                print("Please only give H or L for higher or lower.")
    #is hilo will call guess and compare the 2 cards given from dealer. Will return point totals
    #specified by the requirements
    def is_hilo(self, old_card, new_card):
        guess = self.do_guess()
        if guess == 'h':
            if new_card > old_card:
                return 100
            else:
                return -75
        elif guess == 'l':
            if new_card < old_card:
                return 100
            else: 
                return -75

#This is to test if things are working right uncomment if you want to make sure player class works
#x = player()
#print(x.is_hilo(10,11))
#print("done")
        
