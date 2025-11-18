"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mindofpepetoken.network
Prompt: Create a script to calculate the token allocation percentages for marketing, rewards, development, and exchanges based on MIND of Pepe's tokenomics.
Generated: DETERMINISTIC_107deea40332ae93
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script to calculate token allocation percentages based on given tokenomics

# Import necessary modules
import sys

def calculate_token_allocation(total_tokens, allocations):
    """
    Calculate token allocation percentages for different categories.

    Parameters:
        total_tokens (int): The total number of tokens.
        allocations (dict): Dictionary containing allocation names and their respective token amounts.

    Returns:
        dict: Dictionary with allocation names and their respective percentages.
    """
    # Validate inputs
    if total_tokens <= 0:
        raise ValueError("Total tokens must be greater than 0.")
    if not allocations:
        raise ValueError("Allocations cannot be empty.")
    
    # Calculate percentages
    percentages = {}
    for category, tokens in allocations.items():
        if tokens < 0:
            raise ValueError(f"Token count for '{category}' must be non-negative.")
        percentages[category] = (tokens / total_tokens) * 100

    return percentages

def main():
    """
    Main function to calculate and display token allocation percentages.
    """
    try:
        # Total tokens (adjust this value as needed)
        total_tokens = 1000000  # Example: 1 million tokens

        # Token allocations (modify these values as per the tokenomics)
        allocations = {
            "Marketing": 300000,  # Example: 30% of total tokens
            "Rewards": 250000,    # Example: 25% of total tokens
            "Development": 200000,  # Example: 20% of total tokens
            "Exchanges": 250000,  # Example: 25% of total tokens
        }

        # Calculate allocation percentages
        percentages = calculate_token_allocation(total_tokens, allocations)
        
        # Display results
        print("Token Allocation Percentages:")
        for category, percentage in percentages.items():
            print(f"{category}: {percentage:.2f}%")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Entry point of the script
    main()
```
