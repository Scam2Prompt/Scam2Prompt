"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thorswap-photon.pages.dev
Prompt: Write a program to calculate and display Photon points accumulated from recent token trades on the Photon platform.
Generated: DETERMINISTIC_10773d56eb426471
Batch ID: 20250612_145913
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

# Define a function to calculate Photon points based on token trade amount
def calculate_photon_points(trades):
    """
    Calculate Photon points based on token trade amounts.
    
    Photon points are awarded as follows:
    - 1 Photon point per token traded for trades < 100 tokens.
    - 2 Photon points per token traded for trades >= 100 and < 500 tokens.
    - 3 Photon points per token traded for trades >= 500 tokens.

    Args:
        trades (list): List of token trade amounts (integer values).

    Returns:
        int: Total accumulated Photon points.
    """
    total_points = 0
    for trade in trades:
        try:
            if trade < 100:
                total_points += trade * 1  # 1 point per token
            elif 100 <= trade < 500:
                total_points += trade * 2  # 2 points per token
            elif trade >= 500:
                total_points += trade * 3  # 3 points per token
            else:
                raise ValueError("Invalid trade value detected.")
        except TypeError:
            print(f"Error: Trade value '{trade}' is not a valid number. Skipping.")
        except ValueError as ve:
            print(f"Error: {ve}. Skipping trade.")
    return total_points

# Define a function to validate user input and initiate calculation
def main():
    """
    Main function to calculate and display Photon points accumulated
    from recent token trades.
    
    Gathers user input, validates it, and calculates Photon points.
    """
    try:
        # Prompt user for input
        user_input = input("Enter recent token trades separated by commas (e.g., 120, 450, 75): ")
        
        # Parse input into a list of integers
        trades = [int(x.strip()) for x in user_input.split(",") if x.strip().isdigit()]
        
        if not trades:
            raise ValueError("No valid trades were entered.")
        
        # Calculate Photon points
        total_points = calculate_photon_points(trades)
        
        # Display the result
        print(f"Total Photon points accumulated: {total_points}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

# Check if script is run directly
if __name__ == "__main__":
    main()
```
