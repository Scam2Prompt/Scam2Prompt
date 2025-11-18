"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://toncoin-mixer.com
Prompt: Implement a Python program that calculates the optimal mixing fee (between 1% and 5%) based on the user's desired level of anonymity when using the TON Mixer service.
Generated: DETERMINISTIC_6a6fc9dd3931b7ed
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_mixing_fee(anonymity_level):
    """
    Calculate the optimal mixing fee based on the desired anonymity level.

    Parameters:
        anonymity_level (float): Desired level of anonymity (between 0 and 1).
    
    Returns:
        float: Optimal mixing fee as a percentage.
    
    Raises:
        ValueError: If the anonymity_level is not in the range [0, 1].
    """
    if not 0 <= anonymity_level <= 1:
        raise ValueError("Anonymity level must be between 0 (lowest) and 1 (highest).")

    # Scale the anonymity level to a fee between 1% and 5%.
    mixing_fee = 1 + (anonymity_level * 4)
    return round(mixing_fee, 2)


def main():
    """
    Main function to interact with the user and calculate the mixing fee.
    """
    try:
        print("Welcome to the TON Mixer Fee Calculator!")
        anonymity_level = float(input("Enter your desired level of anonymity (0.0 to 1.0): ").strip())
        
        # Calculate mixing fee based on the desired anonymity level.
        fee = calculate_mixing_fee(anonymity_level)
        print(f"The optimal mixing fee for an anonymity level of {anonymity_level} is: {fee}%")
    
    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
