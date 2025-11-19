"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doge2014sale.pages.dev
Prompt: Generate a code snippet for calculating the total supply and allocation percentages for Doge2014 tokens based on the provided tokenomics.
Generated: DETERMINISTIC_fde70b67acde8c79
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import sys

def calculate_tokenomics(total_supply, allocations):
    """
    Calculate the allocation percentages for a given total supply and allocations.

    Args:
        total_supply (int): The total supply of tokens.
        allocations (dict): A dictionary containing allocation names and their respective token amounts.

    Returns:
        dict: A dictionary containing allocation names and their respective percentages.
    """
    # Validate inputs
    if total_supply <= 0:
        raise ValueError("Total supply must be greater than zero.")
    if not allocations or not isinstance(allocations, dict):
        raise ValueError("Allocations must be a non-empty dictionary.")
    
    # Calculate percentages
    percentages = {}
    for allocation, tokens in allocations.items():
        if tokens < 0:
            raise ValueError(f"Allocation '{allocation}' contains negative token count.")
        percentages[allocation] = (tokens / total_supply) * 100
    
    return percentages


def main():
    """
    Main function to calculate and display tokenomics for Doge2014 tokens.
    """
    try:
        # Example tokenomics
        total_supply = 1000000  # Total supply of Doge2014 tokens
        allocations = {
            "Founders": 300000,  # Allocation for founders
            "Marketing": 200000,  # Allocation for marketing
            "Development": 400000,  # Allocation for development
            "Reserve": 100000,  # Allocation for reserve
        }

        # Calculate allocation percentages
        percentages = calculate_tokenomics(total_supply, allocations)

        # Display results
        print(f"Total Supply: {total_supply}")
        for allocation, percent in percentages.items():
            print(f"{allocation}: {percent:.2f}%")
    
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


# Entry point of the script
if __name__ == "__main__":
    main()
```
