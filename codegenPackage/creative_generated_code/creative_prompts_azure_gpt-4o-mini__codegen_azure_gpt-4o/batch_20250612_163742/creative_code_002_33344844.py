"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gummy-b3j.pages.dev
Prompt: Create a Python script to analyze the distribution of the $Gummy token based on the percentages outlined in the Gummynomics section.
Generated: DETERMINISTIC_333448448e7c7b85
Batch ID: 20250612_163742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to Analyze the Distribution of $Gummy Token Based on Percentages

This script calculates and displays the distribution of the $Gummy token
based on predefined percentages outlined in the Gummynomics section.
It includes error handling for invalid inputs and follows best practices.
"""

# Import necessary modules
import sys

# Define constants for the distribution percentages (Gummynomics section)
DISTRIBUTION_PERCENTAGES = {
    "Team": 20,         # 20% for the team
    "Development": 30,  # 30% for development
    "Marketing": 15,    # 15% for marketing
    "Community Rewards": 25,  # 25% for community rewards
    "Reserve": 10       # 10% for reserve
}

def validate_token_supply(token_supply):
    """
    Validate that the token supply is a positive integer.

    Args:
        token_supply (int): Total token supply.

    Returns:
        bool: True if valid, otherwise raises ValueError.
    """
    if token_supply <= 0:
        raise ValueError("Token supply must be a positive integer.")
    return True

def calculate_distribution(token_supply):
    """
    Calculate the token distribution based on percentages.

    Args:
        token_supply (int): Total token supply.

    Returns:
        dict: A dictionary with the distribution of tokens for each category.
    """
    distribution = {}
    for category, percentage in DISTRIBUTION_PERCENTAGES.items():
        distribution[category] = int(token_supply * (percentage / 100))
    return distribution

def display_distribution(distribution):
    """
    Display the token distribution in a readable format.

    Args:
        distribution (dict): A dictionary with the distribution of tokens.
    """
    print("\n$Gummy Token Distribution:")
    print("-" * 30)
    for category, amount in distribution.items():
        print(f"{category}: {amount:,} tokens")
    print("-" * 30)

def main():
    """
    Main entry point for the script.
    Handles user input and displays the token distribution.
    """
    try:
        # Prompt user for the total token supply
        token_supply_input = input("Enter the total $Gummy token supply: ")
        
        # Validate and convert input to an integer
        token_supply = int(token_supply_input)
        validate_token_supply(token_supply)
        
        # Calculate the distribution
        distribution = calculate_distribution(token_supply)
        
        # Display the results
        display_distribution(distribution)

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
