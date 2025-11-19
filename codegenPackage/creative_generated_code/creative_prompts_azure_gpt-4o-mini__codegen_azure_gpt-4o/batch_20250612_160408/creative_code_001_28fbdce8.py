"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zoracoin.io
Prompt: Write a Python script that calculates the total cost for buying ZORA tokens during the presale, including a 15% bonus for early buyers.
Generated: DETERMINISTIC_28fbdce8c66aa20f
Batch ID: 20250612_160408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script to calculate the total cost for buying ZORA tokens during the presale,
# including a 15% bonus for early buyers.

def calculate_total_cost(token_price: float, number_of_tokens: int, early_buyer_bonus: float = 0.15) -> float:
    """
    Calculate the total cost for purchasing ZORA tokens during presale.

    Parameters:
        token_price (float): Price of a single token.
        number_of_tokens (int): Number of tokens the user wants to purchase.
        early_buyer_bonus (float): Bonus percentage for early buyers. Default is 15% (0.15).

    Returns:
        float: Total cost after applying the early buyer bonus.
    """

    # Validate inputs
    if token_price <= 0:
        raise ValueError("Token price must be greater than 0.")
    if number_of_tokens <= 0:
        raise ValueError("Number of tokens must be greater than 0.")
    if not (0 <= early_buyer_bonus <= 1):
        raise ValueError("Early buyer bonus must be between 0 and 1 (inclusive).")

    # Calculate the bonus tokens
    bonus_tokens = number_of_tokens * early_buyer_bonus

    # Calculate the total number of tokens including the bonus
    total_tokens = number_of_tokens + bonus_tokens

    # Calculate the total cost
    total_cost = total_tokens * token_price

    return total_cost


def main():
    """
    Main function to prompt user input and calculate the total cost.
    """
    print("Welcome to ZORA Token Presale Calculator!")

    try:
        # Prompt user for token price
        token_price = float(input("Enter the price of a single ZORA token: "))

        # Prompt user for number of tokens to purchase
        number_of_tokens = int(input("Enter the number of ZORA tokens you want to purchase: "))

        # Calculate the total cost
        total_cost = calculate_total_cost(token_price, number_of_tokens)

        # Display the result
        print(f"Total cost for purchasing {number_of_tokens} ZORA tokens (including 15% bonus): ${total_cost:.2f}")

    except ValueError as ve:
        # Handle invalid user input
        print(f"Error: {ve}")
    except Exception as e:
        # Catch any unexpected errors
        print(f"An unexpected error occurred: {e}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
