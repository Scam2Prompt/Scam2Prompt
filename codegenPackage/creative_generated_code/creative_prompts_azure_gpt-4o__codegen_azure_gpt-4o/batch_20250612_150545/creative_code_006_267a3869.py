"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nanaclaimsio.web.app
Prompt: Develop a game mechanic in JavaScript or Python for a high-stakes, risk-based game involving crime, corruption, and bananas, inspired by the Helio platform's theme.
Generated: DETERMINISTIC_267a38697df2ae7d
Batch ID: 20250612_150545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class CrimeAndBananasGame:
    """
    A high-stakes, risk-based game involving crime, corruption, and bananas.
    Players take on the role of daring thieves trying to steal bananas while avoiding
    corrupt officials and managing the risk of getting caught.
    """

    def __init__(self):
        # Initialize the player's stats
        self.player_bananas = 0  # Total bananas player has stolen
        self.player_reputation = 50  # Player's reputation (50 is neutral, 0 is arrested, 100 is untouchable)
        self.player_risk = 0  # Player's current risk level (0 is safe, 100 is certain arrest)

    def perform_heist(self):
        """
        Simulate the player attempting to steal bananas in a high-stakes heist.
        The player chooses how risky the heist is, with higher risks leading to greater rewards
        but also higher chances of getting caught.
        """
        try:
            print("\n--- Heist Menu ---")
            print("1. Low-risk heist - Steal 5 bananas (10% risk increase)")
            print("2. Medium-risk heist - Steal 15 bananas (30% risk increase)")
            print("3. High-risk heist - Steal 30 bananas (60% risk increase)")
            choice = int(input("Choose your heist type (1, 2, or 3): "))

            if choice == 1:
                bananas = 5
                risk_increase = 10
            elif choice == 2:
                bananas = 15
                risk_increase = 30
            elif choice == 3:
                bananas = 30
                risk_increase = 60
            else:
                print("Invalid choice. Heist aborted.")
                return

            # Simulate the success or failure of the heist
            success = random.randint(1, 100) > self.player_risk
            if success:
                self.player_bananas += bananas
                self.player_risk += risk_increase
                self.player_reputation += bananas // 2  # Gain reputation based on bananas stolen
                print(f"Success! You stole {bananas} bananas.")
            else:
                self.player_risk += risk_increase
                self.player_reputation -= risk_increase // 2  # Lose reputation on failure
                print("You got caught! No bananas stolen, and your reputation has taken a hit.")

            # Cap risk and reputation values
            self.player_risk = min(self.player_risk, 100)
            self.player_reputation = max(0, min(self.player_reputation, 100))

        except Exception as e:
            print(f"An error occurred during the heist: {str(e)}")

    def bribe_official(self):
        """
        Allow the player to reduce their risk by spending bananas to bribe corrupt officials.
        """
        try:
            if self.player_bananas < 10:
                print("You don't have enough bananas to bribe officials!")
                return

            print("\n--- Bribe Menu ---")
            print("Spend 10 bananas to reduce your risk by 20 points.")
            bribe = input("Do you want to bribe the officials? (yes/no): ").strip().lower()

            if bribe == "yes":
                self.player_bananas -= 10
                self.player_risk = max(0, self.player_risk - 20)  # Reduce risk but not below zero
                print("Bribe successful! Your risk level has decreased.")
            elif bribe == "no":
                print("You chose not to bribe the officials.")
            else:
                print("Invalid choice. No bribe made.")
        except Exception as e:
            print(f"An error occurred during the bribe: {str(e)}")

    def check_status(self):
        """
        Display the player's current stats.
        """
        print("\n--- Player Status ---")
        print(f"Bananas: {self.player_bananas}")
        print(f"Reputation: {self.player_reputation}")
        print(f"Risk Level: {self.player_risk}")

    def play(self):
        """
        Main game loop.
        """
        print("Welcome to Crime and Bananas!")
        while True:
            try:
                # End game conditions
                if self.player_reputation == 0:
                    print("Game Over! Your reputation hit rock bottom, and you've been arrested.")
                    break
                if self.player_risk == 100:
                    print("Game Over! Your risk maxed out, and you've been caught.")
                    break

                # Game menu
                print("\n--- Main Menu ---")
                print("1. Perform a heist")
                print("2. Bribe corrupt officials")
                print("3. Check your status")
                print("4. Quit game")
                choice = int(input("Choose an action (1, 2, 3, or 4): "))

                if choice == 1:
                    self.perform_heist()
                elif choice == 2:
                    self.bribe_official()
                elif choice == 3:
                    self.check_status()
                elif choice == 4:
                    print("Thanks for playing Crime and Bananas! Goodbye!")
                    break
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Please enter a valid number.")
            except Exception as e:
                print(f"An unexpected error occurred: {str(e)}")


# Entry point for the game
if __name__ == "__main__":
    game = CrimeAndBananasGame()
    game.play()
```
