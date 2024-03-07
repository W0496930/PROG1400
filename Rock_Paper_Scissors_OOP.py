import random
options_list = ("rock", "paper", "scissors")

#Define base class
class Player:
 
    def __init__(self,name):
        self.name = name
    
    def choose_move(self):
        pass

#Create a derived class (Human_Player) that inherits from the base class
class Human_Player(Player):
    def choose_move(self):
        move = input(f"{self.name}, Enter your move (Rock, Paper, Scissors): ").lower()
        while move not in (options_list):
            print("Invalid Input. Please select rock, paper, or scissors.")
            move = input(f"{self.name}, Enter your move (Rock, Paper, Scissors): ").lower()
        return move

#Create another derived class (Computer_Player) that inherits from the base class
class Computer_Player(Player):
    def choose_move(self):
        return random.choice(options_list)
    
#Create a Game Class
class Rock_Paper_Scissors_Game:
    #Create the Characters
    def __init__(self):
        self.player1 = Human_Player("Player 1")
        self.player2 = Computer_Player("Computer")
    def determine_winner(self, move1, move2):
        if move1 == move2:
            return "It's a tie."
        elif (move1 == "rock" and move2 == "scissors") or \
             (move1 == "scissors" and move2 == "paper")or \
             (move1 == "paper" and move2 == "rock"):
            return f"{self.player1.name} wins!"
        else:
            return f"{self.player2.name} wins!"
    
    def play_game(self):
        #intro
        print("Welcome to Rock Paper Scissors!")
        #Call the choose move method on Player 1 And 2
        move1 = self.player1.choose_move()
        move2 = self.player2.choose_move()
        #Inform the player the moves
        print(f"{self.player1.name} chose {move1}")
        print(f"{self.player2.name} chose {move2}")

        result = self.determine_winner(move1, move2)
        print(result)
#Instantiate the game class and play the game
if __name__ == "__main__":
        game = Rock_Paper_Scissors_Game()
        game.play_game()
        

      

       

        