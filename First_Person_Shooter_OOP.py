class First_Person_Shooter_Game:
    def __init__(self, player1, player2, rounds=3):
        self.player1 = player1       
        self.player2 = player2
        self.rounds = rounds
        self.current_round = 0

    def play_round(self):
        if self.current_round < self.rounds:
            print(f"Round {self.current_round + 1}")
            self.player1.shoot()
            self.player2.take_damage(self.player1.weapon.damage)

            self.player2.shoot()
            self.player1.take_damage(self.player2.weapon.damage)

            self.current_round += 1
        else:
            self.end_game()

    def end_game(self):
        print("Game over!")
        if self.player1.health > self.player2.health:
            print(f"{self.player1.name} wins!")
        elif self.player2.health > self.player1.health:
            print(f"{self.player2.name} wins!")
        else:
            print("It's a draw!")

if __name__ == "__main__":
    # Create weapons
    assault_rifle = Weapon("Assault Rifle", damage=10, ammo_capacity=30)
    shotgun = Weapon("Shotgun", damage=30, ammo_capacity=8)

    # Create players
    player1 = Player("Player 1", health=100)
    player2 = Player("Player 2", health=100)

    # Equip weapons
    player1.equip_weapon(assault_rifle)
    player2.equip_weapon(shotgun)

    # Create the game with a specified number of rounds
    fps_game = First_Person_Shooter_Game(player1, player2, rounds=3)

    # Continue the game until all rounds are played
    while fps_game.current_round < fps_game.rounds:
        fps_game.play_round()
