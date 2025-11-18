"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://todaythegames.com
Prompt: Write a Python program to implement a virtual roulette game, including random number generation and a visual representation of the roulette wheel, inspired by the games on todaythegames.com.
Generated: DETERMINISTIC_c869a28e98024b65
Batch ID: 20250612_145203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

def display_roulette_wheel():
    """
    Displays a visual representation of the roulette wheel.
    Numbers are color-coded: red, black, and green (for zero).
    """
    colors = {
        0: 'Green',
        **{i: 'Red' if i % 2 != 0 else 'Black' for i in range(1, 37)}  # Alternate red/black pattern
    }
    print("Roulette Wheel:")
    print("-" * 40)
    for number, color in colors.items():
        print(f"{number:2} - {color}")
    print("-" * 40)


def spin_roulette():
    """
    Spins the roulette wheel and generates a random result.
    Returns a tuple of the number and its associated color.
    """
    numbers = list(range(0, 37))  # Numbers from 0 to 36
    picked_number = random.choice(numbers)
    if picked_number == 0:
        color = 'Green'
    elif picked_number % 2 == 0:
        color = 'Black'
    else:
        color = 'Red'
    return picked_number, color


def get_user_bet():
    """
    Prompts the user to place a bet.
    Returns the type of bet and the specific bet details.
    """
    print("\nPlace your bet:")
    print("1. Bet on a specific number (0-36)")
    print("2. Bet on a color (Red, Black, Green)")
    print("3. Bet on odd/even")
    print("4. Bet on high/low (1-18, 19-36)")
    
    try:
        bet_type = int(input("Select your bet type (1-4): "))
        if bet_type == 1:
            bet_detail = int(input("Enter the number you want to bet on (0-36): "))
            if bet_detail < 0 or bet_detail > 36:
                raise ValueError("Invalid number for betting.")
        elif bet_type == 2:
            bet_detail = input("Enter the color you want to bet on (Red/Black/Green): ").strip().capitalize()
            if bet_detail not in ['Red', 'Black', 'Green']:
                raise ValueError("Invalid color for betting.")
        elif bet_type == 3:
            bet_detail = input("Enter 'Odd' or 'Even': ").strip().capitalize()
            if bet_detail not in ['Odd', 'Even']:
                raise ValueError("Invalid choice for betting.")
        elif bet_type == 4:
            bet_detail = input("Enter 'High' (19-36) or 'Low' (1-18): ").strip().capitalize()
            if bet_detail not in ['High', 'Low']:
                raise ValueError("Invalid choice for betting.")
        else:
            raise ValueError("Invalid bet type.")
        return bet_type, bet_detail
    except ValueError as e:
        print(f"Error: {e}")
        return None, None


def check_bet_result(bet_type, bet_detail, spun_number, spun_color):
    """
    Checks if the user's bet matches the result of the roulette spin.
    Returns True if the bet wins, otherwise False.
    """
    if bet_type == 1 and bet_detail == spun_number:
        return True
    elif bet_type == 2 and bet_detail == spun_color:
        return True
    elif bet_type == 3:
        if bet_detail == 'Odd' and spun_number % 2 != 0:
            return True
        if bet_detail == 'Even' and spun_number % 2 == 0:
            return True
    elif bet_type == 4:
        if bet_detail == 'High' and 19 <= spun_number <= 36:
            return True
        if bet_detail == 'Low' and 1 <= spun_number <= 18:
            return True
    return False


def main():
    """
    Main function to run the roulette game.
    """
    print("Welcome to the Virtual Roulette Game!")
    display_roulette_wheel()
    
    # Get user's bet
    bet_type, bet_detail = get_user_bet()
    if bet_type is None or bet_detail is None:
        print("Invalid bet. Exiting game.")
        return
    
    # Spin the roulette wheel
    spun_number, spun_color = spin_roulette()
    print(f"\nRoulette spin result: {spun_number} ({spun_color})")
    
    # Check bet result
    if check_bet_result(bet_type, bet_detail, spun_number, spun_color):
        print("Congratulations! You won!")
    else:
        print("Sorry, you lost. Better luck next time.")

    print("\nThank you for playing!")


if __name__ == "__main__":
    main()
```
