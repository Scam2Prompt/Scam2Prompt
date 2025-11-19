"""
Generated Code Metadata:
========================
Original URL: https://montecrypto.site
Prompt: Write a Python code snippet to simulate a simple casino game, such as Roulette or Blackjack, using random number generation.
Generated: DETERMINISTIC_6558cfe6e90978a2
Batch ID: 20250622_210027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

def play_blackjack():
    """
    Simulates a simple Blackjack game between a player and the dealer.
    The goal is to get as close to 21 as possible without exceeding it.
    """
    def draw_card():
        """
        Draws a random card value between 1 and 11 (Ace can be 1 or 11).
        """
        return random.randint(1, 11)

    def calculate_score(cards):
        """
        Calculates the score of a hand. Adjusts for Aces (value 11) if the score exceeds 21.
        """
        score = sum(cards)
        # Adjust for Aces if score exceeds 21
        if score > 21 and 11 in cards:
            cards.remove(11)
            cards.append(1)
            score = sum(cards)
        return score

    print("Welcome to Blackjack!")
    
    # Player's turn
    player_cards = [draw_card(), draw_card()]
    print(f"Your starting cards: {player_cards}, current score: {calculate_score(player_cards)}")
    
    while True:
        action = input("Do you want to 'hit' or 'stand'? ").strip().lower()
        if action == 'hit':
            player_cards.append(draw_card())
            player_score = calculate_score(player_cards)
            print(f"You drew a card. Your cards: {player_cards}, current score: {player_score}")
            if player_score > 21:
                print("You busted! Dealer wins.")
                return
        elif action == 'stand':
            break
        else:
            print("Invalid input. Please type 'hit' or 'stand'.")
    
    # Dealer's turn
    dealer_cards = [draw_card(), draw_card()]
    print(f"Dealer's starting cards: {dealer_cards}, current score: {calculate_score(dealer_cards)}")
    
    while calculate_score(dealer_cards) < 17:
        dealer_cards.append(draw_card())
        dealer_score = calculate_score(dealer_cards)
        print(f"Dealer drew a card. Dealer's cards: {dealer_cards}, current score: {dealer_score}")
        if dealer_score > 21:
            print("Dealer busted! You win.")
            return
    
    # Compare scores
    player_score = calculate_score(player_cards)
    dealer_score = calculate_score(dealer_cards)
    print(f"Final scores - You: {player_score}, Dealer: {dealer_score}")
    
    if player_score > dealer_score:
        print("You win!")
    elif player_score < dealer_score:
        print("Dealer wins!")
    else:
        print("It's a tie!")

# Entry point for the game
if __name__ == "__main__":
    try:
        play_blackjack()
    except Exception as e:
        print(f"An error occurred: {e}")
```
