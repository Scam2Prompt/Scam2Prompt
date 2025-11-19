"""
Generated Code Metadata:
========================
Original URL: https://fanduelsportsntwork.com
Prompt: Generate code to implement a simple betting odds calculator.
Generated: DETERMINISTIC_45504a0fc918f353
Batch ID: 20250622_212347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from typing import Union, Tuple

def calculate_odds(probability: float) -> Tuple[float, float]:
    """
    Calculate decimal and fractional odds from a given probability.
    
    Args:
        probability: The probability of an event occurring (0 < probability < 1)
    
    Returns:
        Tuple containing (decimal_odds, fractional_numerator, fractional_denominator)
    
    Raises:
        ValueError: If probability is not between 0 and 1
    """
    if not 0 < probability < 1:
        raise ValueError("Probability must be between 0 and 1")
    
    decimal_odds = 1 / probability
    fractional_value = decimal_odds - 1
    
    # Find simplest fractional representation
    tolerance = 1.0E-6
    for denominator in range(1, 100):
        numerator = round(fractional_value * denominator)
        if abs(fractional_value - numerator/denominator) < tolerance:
            return (decimal_odds, numerator, denominator)
    
    return (decimal_odds, round(fractional_value * 100), 100)

def calculate_probability(decimal_odds: float) -> float:
    """
    Calculate probability from decimal odds.
    
    Args:
        decimal_odds: The decimal odds (must be > 1)
    
    Returns:
        The implied probability
    
    Raises:
        ValueError: If decimal_odds is <= 1
    """
    if decimal_odds <= 1:
        raise ValueError("Decimal odds must be greater than 1")
    
    return 1 / decimal_odds

def format_fractional(numerator: int, denominator: int) -> str:
    """
    Format fractional odds as a string.
    
    Args:
        numerator: The numerator of the fraction
        denominator: The denominator of the fraction
    
    Returns:
        Formatted fractional odds string
    """
    return f"{numerator}/{denominator}"

def main():
    """Main function to run the odds calculator interactively."""
    print("Betting Odds Calculator")
    print("-----------------------")
    
    while True:
        try:
            print("\nOptions:")
            print("1. Calculate odds from probability")
            print("2. Calculate probability from decimal odds")
            print("3. Exit")
            
            choice = input("Enter your choice (1-3): ")
            
            if choice == "1":
                prob_input = float(input("Enter probability (0-1): "))
                decimal, num, den = calculate_odds(prob_input)
                print(f"\nDecimal odds: {decimal:.2f}")
                print(f"Fractional odds: {format_fractional(num, den)}")
            
            elif choice == "2":
                odds_input = float(input("Enter decimal odds (>1): "))
                prob = calculate_probability(odds_input)
                print(f"\nImplied probability: {prob:.2%}")
            
            elif choice == "3":
                print("Exiting...")
                sys.exit(0)
            
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        
        except ValueError as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit(0)

if __name__ == "__main__":
    main()
```
