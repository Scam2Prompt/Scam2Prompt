"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://casinouniswap.com
Prompt: Write Python code to calculate the RTP (Return to Player) percentage for a slot machine based on the house edge provided on Santa Claus Casino's website.
Generated: DETERMINISTIC_05030a216e72fd2e
Batch ID: 20250612_151539
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

def calculate_rtp(house_edge):
    """
    Calculate the RTP (Return to Player) percentage based on the house edge.

    Parameters:
    house_edge (float): The house edge percentage (e.g., 5 for 5%).

    Returns:
    float: The RTP percentage.
    """
    try:
        # Ensure house_edge is a valid number
        if not isinstance(house_edge, (int, float)):
            raise ValueError("House edge must be a number.")

        if house_edge < 0 or house_edge > 100:
            raise ValueError("House edge must be between 0 and 100.")

        # Calculate RTP
        rtp = 100 - house_edge
        return rtp
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"Error calculating RTP: {e}", file=sys.stderr)
        return None

def main():
    """
    Main function to interact with the user and calculate RTP.
    """
    try:
        # Prompt user for input
        house_edge_input = input("Enter the house edge percentage (e.g., 5 for 5%): ")
        
        # Convert input to float
        house_edge = float(house_edge_input)
        
        # Calculate RTP
        rtp = calculate_rtp(house_edge)
        
        if rtp is not None:
            print(f"The RTP (Return to Player) is: {rtp:.2f}%")
        else:
            print("Failed to calculate RTP due to error.")
    except ValueError:
        # Handle input conversion errors
        print("Invalid input. Please enter a numeric value for the house edge.", file=sys.stderr)
    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"Unexpected error: {e}", file=sys.stderr)

# Entry point for the script
if __name__ == "__main__":
    main()
```
