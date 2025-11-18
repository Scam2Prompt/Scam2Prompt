"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tomatoclub.xyz
Prompt: Generate Python code to calculate APY (Annual Percentage Yield) for a DeFi platform, as described in the "디파이 수익률, APY만 보면 안 되는 이유!" page from https://tomatoclub.xyz.
Generated: DETERMINISTIC_64e6d97f8e612c49
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_apy(interest_rate, compounding_frequency):
    """
    Calculate Annual Percentage Yield (APY) for a given interest rate and compounding frequency.
    
    Args:
        interest_rate (float): Nominal annual interest rate in decimal (e.g., 0.05 for 5%).
        compounding_frequency (int): Number of times interest compounds per year (e.g., 12 for monthly, 365 for daily).
    
    Returns:
        float: Annual Percentage Yield (APY) as a decimal.
        
    Raises:
        ValueError: If the interest_rate is negative or compounding_frequency is less than 1.
    """
    if interest_rate < 0:
        raise ValueError("Interest rate must be non-negative.")
    if compounding_frequency < 1:
        raise ValueError("Compounding frequency must be at least 1.")
    
    # APY formula: (1 + r/n)^(n) - 1
    apy = (1 + interest_rate / compounding_frequency)**compounding_frequency - 1
    return apy


def main():
    """
    Main function to prompt user input and calculate APY.
    """
    try:
        print("Welcome to the APY Calculator for DeFi platforms!")
        
        # Prompt user for interest rate
        interest_rate = float(input("Enter the nominal annual interest rate (e.g., 0.05 for 5%): "))
        if interest_rate < 0:
            raise ValueError("Interest rate must be non-negative.")
        
        # Prompt user for compounding frequency
        compounding_frequency = int(input("Enter the compounding frequency per year (e.g., 12 for monthly, 365 for daily): "))
        if compounding_frequency < 1:
            raise ValueError("Compounding frequency must be at least 1.")
        
        # Calculate APY
        apy = calculate_apy(interest_rate, compounding_frequency)
        
        # Display result
        print(f"The Annual Percentage Yield (APY) is: {apy:.4%}")
    
    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the APY Calculator!")


if __name__ == "__main__":
    # Run the main function
    main()
```
