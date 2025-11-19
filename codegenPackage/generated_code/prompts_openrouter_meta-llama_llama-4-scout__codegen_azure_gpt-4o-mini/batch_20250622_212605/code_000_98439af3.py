"""
Generated Code Metadata:
========================
Original URL: https://getsophon.network
Prompt: Write a Python script to calculate the bonus for a Stage 2 purchase of Sophon Tokens, given the presale live price and bonus percentage.
Generated: DETERMINISTIC_98439af3313127dd
Batch ID: 20250622_212605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_bonus(presale_price: float, bonus_percentage: float) -> float:
    """
    Calculate the bonus amount for a Stage 2 purchase of Sophon Tokens.

    Parameters:
    presale_price (float): The live price of the Sophon Tokens during the presale.
    bonus_percentage (float): The percentage of the bonus to be applied.

    Returns:
    float: The calculated bonus amount.
    
    Raises:
    ValueError: If presale_price or bonus_percentage is negative.
    """
    # Validate input parameters
    if presale_price < 0:
        raise ValueError("Presale price must be a non-negative value.")
    if bonus_percentage < 0:
        raise ValueError("Bonus percentage must be a non-negative value.")

    # Calculate the bonus amount
    bonus_amount = presale_price * (bonus_percentage / 100)
    
    return bonus_amount


def main():
    """
    Main function to execute the bonus calculation.
    """
    try:
        # Input: Presale price and bonus percentage
        presale_price = float(input("Enter the presale live price of Sophon Tokens: "))
        bonus_percentage = float(input("Enter the bonus percentage: "))

        # Calculate the bonus
        bonus = calculate_bonus(presale_price, bonus_percentage)

        # Output the result
        print(f"The calculated bonus for a Stage 2 purchase is: {bonus:.2f} tokens")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
