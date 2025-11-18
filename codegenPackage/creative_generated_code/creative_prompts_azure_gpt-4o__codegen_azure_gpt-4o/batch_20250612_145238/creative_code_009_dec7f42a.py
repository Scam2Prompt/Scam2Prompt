"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://playland.co.ke
Prompt: Write a Python script to calculate the cost of playing multiple games of foosball at Playland Kenya, considering both the 5-ball and 10-ball options.
Generated: DETERMINISTIC_dec7f42a7f795f76
Batch ID: 20250612_145238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script to calculate the cost of playing multiple games of foosball at Playland Kenya
# considering both 5-ball and 10-ball options.

def calculate_foosball_cost(games, option):
    """
    Calculate the total cost of playing multiple games of foosball.

    Args:
        games (int): The number of games to be played.
        option (str): The game option, either "5-ball" or "10-ball".

    Returns:
        float: The total cost of playing the games.
    """
    # Pricing for each option
    prices = {
        "5-ball": 100,  # Cost of one 5-ball game in Kenyan Shillings
        "10-ball": 180  # Cost of one 10-ball game in Kenyan Shillings
    }

    # Validate input
    if option not in prices:
        raise ValueError("Invalid option. Choose either '5-ball' or '10-ball'.")
    if not isinstance(games, int) or games <= 0:
        raise ValueError("The number of games must be a positive integer.")

    # Calculate total cost
    total_cost = games * prices[option]
    return total_cost


def main():
    """
    Main function to interact with the user and calculate the foosball cost.
    """
    print("Welcome to Playland Kenya's Foosball Cost Calculator!")
    try:
        # Get user input for the number of games
        games = int(input("Enter the number of games you want to play: "))
        
        # Get user input for game option
        print("Options: '5-ball' or '10-ball'")
        option = input("Enter your game option: ").strip().lower()

        # Calculate and display the total cost
        total_cost = calculate_foosball_cost(games, option)
        print(f"The total cost for {games} games of {option} is {total_cost} KES.")
    except ValueError as e:
        # Handle invalid inputs gracefully
        print(f"Error: {e}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")

    print("Thank you for using the Foosball Cost Calculator!")


# Entry point of the script
if __name__ == "__main__":
    main()
```
