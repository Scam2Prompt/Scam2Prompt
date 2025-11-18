"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pansos4dmax.site
Prompt: Create a program that calculates the RTP (Return to Player) for slot games, referencing the RTP accuracy mentioned on the PANSOS4D website.
Generated: DETERMINISTIC_98ffeff524f30f51
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# RTP Calculator for Slot Games
# This program calculates the RTP (Return to Player) percentage for slot games
# based on the total payouts and total bets. It includes validation and error handling.

def calculate_rtp(total_payouts: float, total_bets: float) -> float:
    """
    Calculate the Return to Player (RTP) percentage.
    
    Args:
        total_payouts (float): The total amount of money paid out to players.
        total_bets (float): The total amount of money wagered by players.
    
    Returns:
        float: RTP as a percentage.
    
    Raises:
        ValueError: If total_bets is zero or negative values are passed.
    """
    if total_bets <= 0:
        raise ValueError("Total bets must be greater than zero.")
    if total_payouts < 0:
        raise ValueError("Total payouts cannot be negative.")
    
    # RTP formula: (Total Payouts / Total Bets) * 100
    return (total_payouts / total_bets) * 100

def main():
    """
    Main function to get user input and calculate RTP.
    """
    print("RTP Calculator for Slot Games")
    print("----------------------------")
    
    try:
        # Get input from the user
        total_payouts = float(input("Enter the total payouts (in currency units): "))
        total_bets = float(input("Enter the total bets (in currency units): "))
        
        # Calculate RTP
        rtp = calculate_rtp(total_payouts, total_bets)
        
        # Display the result
        print(f"The RTP (Return to Player) is: {rtp:.2f}%")
    
    except ValueError as ve:
        # Handle invalid numerical inputs
        print(f"Input Error: {ve}")
    except Exception as e:
        # Handle unexpected exceptions
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the RTP Calculator!")

# Entry point of the script
if __name__ == "__main__":
    main()
```
