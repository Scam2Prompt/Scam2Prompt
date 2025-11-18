"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.mellotoken.com
Prompt: Write a script to calculate the total circulating supply of Mello Tokens after a series of manual burns, given the maximum supply of 402 million tokens.
Generated: DETERMINISTIC_7ac42f71493bb3d4
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script to calculate the total circulating supply of Mello Tokens
# after a series of manual burns, given the maximum supply of 402 million tokens.

# Import necessary libraries
import sys

def calculate_circulating_supply(max_supply, burns):
    """
    Calculate the circulating supply after manual token burns.
    
    :param max_supply: (int) The maximum supply of tokens.
    :param burns: (list of int) List of token burn amounts.
    :return: (int) The total circulating supply after burns.
    """
    try:
        # Validate inputs
        if not isinstance(max_supply, int) or max_supply <= 0:
            raise ValueError("Maximum supply must be a positive integer.")
        
        if not isinstance(burns, list) or not all(isinstance(b, int) and b >= 0 for b in burns):
            raise ValueError("Burns must be a list of non-negative integers.")
        
        # Calculate total burns
        total_burns = sum(burns)
        
        # Ensure total burns do not exceed maximum supply
        if total_burns > max_supply:
            raise ValueError("Total burns exceed maximum supply.")
        
        # Calculate circulating supply
        circulating_supply = max_supply - total_burns
        return circulating_supply
    
    except ValueError as e:
        # Handle invalid input error
        print(f"Input Error: {e}")
        sys.exit(1)
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

def main():
    """
    Main function to execute the circulating supply calculation.
    """
    # Maximum supply of Mello Tokens
    max_supply = 402_000_000  # 402 million tokens
    
    # List of manual burns (example values provided)
    burns = [5_000_000, 3_000_000, 10_000_000]  # Replace with actual burn data
    
    # Calculate circulating supply
    circulating_supply = calculate_circulating_supply(max_supply, burns)
    
    # Output the result
    print(f"Total Circulating Supply of Mello Tokens: {circulating_supply:,} tokens")

# Entry point of the script
if __name__ == "__main__":
    main()
```
