"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oraclememe-com.pages.dev
Prompt: Develop a Python script to calculate token allocation percentages for presale, staking rewards, liquidity, marketing, development, and community funds based on the Oracle Meme tokenomics data.
Generated: DETERMINISTIC_21dcc2617e2da17a
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Token Allocation Percentage Calculator

This script calculates the allocation percentages for various categories of
tokenomics based on the Oracle Meme token data provided by the user.

Categories:
- Presale
- Staking Rewards
- Liquidity
- Marketing
- Development
- Community Funds

Usage:
Run the script and input the total token supply and allocation amounts for
each category when prompted.

Author: Professional Software Developer
"""

def calculate_percentages(total_supply, allocations):
    """
    Calculate the percentage allocation for each category.

    :param total_supply: Total token supply (int or float).
    :param allocations: Dictionary containing allocation amounts for each category (dict).
    :return: Dictionary containing allocation percentages for each category (dict).
    """
    try:
        # Validate inputs
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")
        if not allocations or not all(amount >= 0 for amount in allocations.values()):
            raise ValueError("All allocation amounts must be non-negative.")

        # Calculate percentages
        percentages = {
            category: (amount / total_supply) * 100
            for category, amount in allocations.items()
        }

        return percentages
    except TypeError:
        raise TypeError("Invalid input types. Ensure total_supply is a number and allocations is a dictionary.")
    except Exception as e:
        raise Exception(f"An error occurred while calculating percentages: {e}")

def main():
    """
    Main function to handle user input and calculate token allocation percentages.
    """
    try:
        # Input: Total token supply
        total_supply = float(input("Enter the total token supply: "))
        
        # Input: Allocation amounts for each category
        allocations = {}
        allocations['Presale'] = float(input("Enter the token amount allocated for Presale: "))
        allocations['Staking Rewards'] = float(input("Enter the token amount allocated for Staking Rewards: "))
        allocations['Liquidity'] = float(input("Enter the token amount allocated for Liquidity: "))
        allocations['Marketing'] = float(input("Enter the token amount allocated for Marketing: "))
        allocations['Development'] = float(input("Enter the token amount allocated for Development: "))
        allocations['Community Funds'] = float(input("Enter the token amount allocated for Community Funds: "))
        
        # Calculate allocation percentages
        percentages = calculate_percentages(total_supply, allocations)

        # Display results
        print("\nToken Allocation Percentages:")
        for category, percentage in percentages.items():
            print(f"{category}: {percentage:.2f}%")
    
    except ValueError as ve:
        print(f"Value Error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
