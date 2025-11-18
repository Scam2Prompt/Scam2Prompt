"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kinikangg.pages.dev
Prompt: Write code to calculate and display the "win rate" based on full inventory resources, as mentioned in the AI Waifu Spy Result feature.
Generated: DETERMINISTIC_2b9a1e703b82dd05
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary module
import sys

def calculate_win_rate(total_resources, winning_resources):
    """
    Calculate the win rate based on total inventory resources and winning resources.

    Parameters:
        total_resources (int): Total amount of resources in inventory.
        winning_resources (int): Resources contributing to a win.

    Returns:
        float: Win rate as a percentage.
    """
    try:
        # Validate input
        if total_resources <= 0:
            raise ValueError("Total resources must be greater than zero.")
        if winning_resources < 0 or winning_resources > total_resources:
            raise ValueError("Winning resources must be between 0 and total resources.")

        # Calculate win rate
        win_rate = (winning_resources / total_resources) * 100
        return win_rate

    except ValueError as ve:
        # Handle invalid input values
        print(f"Error: {ve}", file=sys.stderr)
        return None
    except Exception as e:
        # Handle unexpected errors
        print(f"Unexpected error: {e}", file=sys.stderr)
        return None


def display_win_rate(win_rate):
    """
    Display the calculated win rate in a readable format.

    Parameters:
        win_rate (float): The win rate percentage.
    """
    if win_rate is not None:
        print(f"Win Rate: {win_rate:.2f}%")
    else:
        print("Unable to calculate win rate.")


def main():
    """
    Main function to interact with the user and calculate/display win rate.
    """
    try:
        print("AI Waifu Spy Result - Win Rate Calculator")
        
        # Input: Total resources
        total_resources = int(input("Enter total inventory resources: "))
        
        # Input: Winning resources
        winning_resources = int(input("Enter winning resources: "))
        
        # Calculate win rate
        win_rate = calculate_win_rate(total_resources, winning_resources)
        
        # Display win rate
        display_win_rate(win_rate)

    except ValueError:
        print("Invalid input. Please enter valid integers for resources.", file=sys.stderr)
    except Exception as e:
        print(f"Unexpected error encountered: {e}", file=sys.stderr)


# Entry point of the program
if __name__ == "__main__":
    main()
```
