"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://degenroyale.com
Prompt: Write a Python script to calculate odds for roulette variations (American, European, French) as described on Royal Reels Casino.
Generated: DETERMINISTIC_f436d72233a9a75c
Batch ID: 20250612_145506
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_roulette_odds(variation, bet_type):
    """
    Calculate the odds for various roulette variations and bet types.

    Parameters:
        variation (str): Roulette variation ('American', 'European', 'French')
        bet_type (str): Type of bet ('straight', 'split', 'street', 'corner', 'line', 'even-money')

    Returns:
        dict: A dictionary containing the odds, payout, and house edge.
    """
    # Definitions for different variations
    roulette_variations = {
        "American": {"total_numbers": 38, "house_edge": 5.26},
        "European": {"total_numbers": 37, "house_edge": 2.70},
        "French": {"total_numbers": 37, "house_edge": 1.35},  # Assumes even-money bets with La Partage rule
    }

    # Payouts for common bet types
    bet_payouts = {
        "straight": 35,
        "split": 17,
        "street": 11,
        "corner": 8,
        "line": 5,
        "even-money": 1,
    }

    # Error handling for invalid inputs
    if variation not in roulette_variations:
        raise ValueError(f"Invalid roulette variation: {variation}. Choose from 'American', 'European', or 'French'.")
    if bet_type not in bet_payouts:
        raise ValueError(f"Invalid bet type: {bet_type}. Choose from {list(bet_payouts.keys())}.")

    total_numbers = roulette_variations[variation]["total_numbers"]
    payout = bet_payouts[bet_type]

    # Calculate odds for winning and losing
    if bet_type == "even-money":
        # Even-money bets exclude 0 and (00 for American) for win calculations
        win_probability = 18 / total_numbers
    else:
        # For other bet types, assume the number of winning slots matches the payout
        win_probability = 1 / (payout + 1)

    lose_probability = 1 - win_probability

    # Calculate expected value (EV) and house edge
    expected_value = (win_probability * payout) - lose_probability
    house_edge = -expected_value * 100

    # Return results
    return {
        "win_probability": round(win_probability * 100, 2),  # Percentage
        "lose_probability": round(lose_probability * 100, 2),  # Percentage
        "payout": payout,
        "house_edge": round(house_edge, 2),
    }


def main():
    """
    Main function to interact with the user for calculating roulette odds.
    """
    print("Welcome to the Roulette Odds Calculator!")
    print("Supported variations: American, European, French")
    print("Supported bet types: straight, split, street, corner, line, even-money")

    try:
        # Get user input
        variation = input("Enter the roulette variation: ").strip().capitalize()
        bet_type = input("Enter the bet type: ").strip().lower()

        # Calculate odds
        odds = calculate_roulette_odds(variation, bet_type)

        # Display results
        print(f"\nRoulette Variation: {variation}")
        print(f"Bet Type: {bet_type.capitalize()}")
        print(f"Win Probability: {odds['win_probability']}%")
        print(f"Lose Probability: {odds['lose_probability']}%")
        print(f"Payout: {odds['payout']}:1")
        print(f"House Edge: {odds['house_edge']}%")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the Roulette Odds Calculator!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nCalculation aborted by user. Goodbye!")
        sys.exit(0)
```
