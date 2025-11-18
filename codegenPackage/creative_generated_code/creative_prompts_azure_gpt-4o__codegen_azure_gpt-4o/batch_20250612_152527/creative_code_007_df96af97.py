"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shubaswap.com
Prompt: Create an algorithm to calculate RTP (Return to Player) for slot games, as highlighted in MESIN128's content.
Generated: DETERMINISTIC_df96af97854407a8
Batch ID: 20250612_152527
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import sys

def calculate_rtp(total_payouts, total_bets):
    """
    Calculate Return to Player (RTP) for a slot game.

    RTP is a percentage that represents the amount of money returned to players
    compared to the total amount bet in the game.

    Args:
        total_payouts (float): The total amount of money paid to players (payouts).
        total_bets (float): The total amount of money bet by players.

    Returns:
        float: The RTP value as a percentage.
    """
    try:
        # Ensure total_bets is greater than 0 to prevent division by zero
        if total_bets <= 0:
            raise ValueError("Total bets must be greater than 0.")
        
        # Calculate RTP
        rtp = (total_payouts / total_bets) * 100
        return round(rtp, 2)  # Round to 2 decimal places for clarity
    except TypeError:
        # Handle cases where inputs are not numbers
        raise TypeError("Both total_payouts and total_bets must be numerical values.")
    except Exception as e:
        # Catch any other unexpected errors
        raise RuntimeError(f"An unexpected error occurred: {e}")


# Main function for demonstration purposes
def main():
    """
    Main function to test the RTP calculation.
    """
    try:
        # Example inputs for the calculation
        total_payouts = float(input("Enter total payouts (e.g., 5000.0): ").strip())
        total_bets = float(input("Enter total bets (e.g., 10000.0): ").strip())

        # Calculate RTP
        rtp = calculate_rtp(total_payouts, total_bets)
        print(f"Return to Player (RTP): {rtp}%")

    except ValueError as ve:
        print(f"Value Error: {ve}")
    except TypeError as te:
        print(f"Type Error: {te}")
    except RuntimeError as re:
        print(f"Runtime Error: {re}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Execution finished.")


# Entry point of the program
if __name__ == "__main__":
    # Run the main function only if this script is executed directly
    main()
```
