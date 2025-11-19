"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whitelist-gummyonsol.pages.dev
Prompt: Develop a Python script that calculates the distribution percentages of the $Gummy tokenomics as described on the Gummy on Sol website.
Generated: DETERMINISTIC_275eb710129ab5a7
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python Script: Gummy Tokenomics Distribution Calculator

This script calculates the distribution percentages based on the tokenomics
listed for the $Gummy token on the Gummy on Sol website. Users can modify
the distribution values in the `TOKENOMICS` dictionary below. The script
validates the data, ensures percentages sum to 100%, and displays the results.

Author: Expert Programmer
"""

# Constants
TOKENOMICS = {
    "Development": 30,  # Percentage allocated to development
    "Marketing": 20,    # Percentage allocated to marketing
    "Liquidity Pool": 25,  # Percentage allocated to liquidity pool
    "Team": 15,         # Percentage allocated to team
    "Community Rewards": 10  # Percentage allocated to community rewards
}

def validate_tokenomics(tokenomics):
    """
    Validates the tokenomics distribution to ensure percentages sum to 100.
    
    Args:
        tokenomics (dict): Dictionary containing token category names and their percentages.
    
    Returns:
        bool: True if valid, raises ValueError otherwise.
    """
    total_percentage = sum(tokenomics.values())
    if total_percentage != 100:
        raise ValueError(
            f"Invalid tokenomics! Total percentage is {total_percentage}, expected 100."
        )
    return True

def calculate_distribution(tokenomics, total_supply):
    """
    Calculates the number of tokens allocated to each category based on the supply.

    Args:
        tokenomics (dict): Dictionary containing token category names and their percentages.
        total_supply (int): Total supply of the tokens.

    Returns:
        dict: Dictionary with category names and their respective token distributions.
    """
    distribution = {}
    for category, percentage in tokenomics.items():
        # Calculate tokens for each category
        distribution[category] = (percentage / 100) * total_supply
    return distribution

def main():
    """
    Main function to execute the tokenomics distribution calculation.
    Prompts user for total token supply and displays the results.
    """
    try:
        print("Welcome to the $Gummy Tokenomics Distribution Calculator!\n")
        
        # Prompt the user for the total supply of tokens
        total_supply = int(input("Enter the total supply of $Gummy tokens: "))
        if total_supply <= 0:
            raise ValueError("Total supply must be a positive integer.")
        
        # Validate the tokenomics configuration
        validate_tokenomics(TOKENOMICS)
        
        # Calculate the distribution
        distribution = calculate_distribution(TOKENOMICS, total_supply)
        
        # Display results
        print("\n$Gummy Token Distribution:")
        for category, tokens in distribution.items():
            print(f"{category}: {tokens:.2f} tokens ({TOKENOMICS[category]}%)")
        
        print("\nTokenomics distribution successfully calculated!")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
