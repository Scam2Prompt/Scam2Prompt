"""
Generated Code Metadata:
========================
Original URL: https://playland.co.ke
Prompt: Write a Python script to calculate the cost of playing multiple games of foosball at Playland Kenya, considering both the 5-ball and 10-ball options.
Generated: DETERMINISTIC_dec7f42a7f795f76
Batch ID: 20250612_145238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_foosball_cost():
    """
    Calculate the total cost of playing foosball games at Playland Kenya.
    Supports both 5-ball and 10-ball game options with different pricing.
    """
    
    # Pricing information (in Kenyan Shillings)
    PRICES = {
        '5-ball': 50,
        '10-ball': 80
    }
    
    print("Welcome to Playland Kenya Foosball Calculator!")
    print(f"Current prices: 5-ball game - KSh {PRICES['5-ball']}, 10-ball game - KSh {PRICES['10-ball']}\n")
    
    try:
        # Get user input
        five_ball_games = int(input("Enter number of 5-ball games: "))
        ten_ball_games = int(input("Enter number of 10-ball games: "))
        
        if five_ball_games < 0 or ten_ball_games < 0:
            raise ValueError("Number of games cannot be negative")
        
        # Calculate costs
        five_ball_cost = five_ball_games * PRICES['5-ball']
        ten_ball_cost = ten_ball_games * PRICES['10-ball']
        total_cost = five_ball_cost + ten_ball_cost
        
        # Display results
        print("\n--- Cost Breakdown ---")
        print(f"5-ball games: {five_ball_games} x KSh {PRICES['5-ball']} = KSh {five_ball_cost}")
        print(f"10-ball games: {ten_ball_games} x KSh {PRICES['10-ball']} = KSh {ten_ball_cost}")
        print(f"\nTOTAL COST: KSh {total_cost}")
        
    except ValueError as e:
        print(f"\nError: {e}. Please enter valid positive numbers.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")


if __name__ == "__main__":
    calculate_foosball_cost()
```
