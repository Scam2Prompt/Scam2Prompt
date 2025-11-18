"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamsbat.com
Prompt: Generate a Python script to calculate boosts for tokens using both soft currency ($HMSTR) and hard currency, as described for June 2024 on the Hamster Kombat site.
Generated: DETERMINISTIC_4a65dc61f2563aa2
Batch ID: 20250612_145718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def calculate_boosts(token_count, soft_currency_amount, hard_currency_amount):
    """
    Calculate boosts for tokens using both soft currency ($HMSTR) and hard currency.
    
    Args:
        token_count (int): The number of tokens.
        soft_currency_amount (float): Amount of soft currency ($HMSTR).
        hard_currency_amount (float): Amount of hard currency.
    
    Returns:
        dict: A dictionary containing calculated boosts.
    """
    try:
        # Validate input types
        if not isinstance(token_count, int) or token_count <= 0:
            raise ValueError("Token count must be a positive integer.")
        if not isinstance(soft_currency_amount, (int, float)) or soft_currency_amount < 0:
            raise ValueError("Soft currency amount must be a non-negative number.")
        if not isinstance(hard_currency_amount, (int, float)) or hard_currency_amount < 0:
            raise ValueError("Hard currency amount must be a non-negative number.")

        # Constants (example rates for calculation; adjust as per Hamster Kombat site details)
        SOFT_CURRENCY_RATE = 0.1  # Boost per $HMSTR
        HARD_CURRENCY_RATE = 0.5  # Boost per hard currency unit

        # Calculate boosts
        soft_currency_boost = soft_currency_amount * SOFT_CURRENCY_RATE
        hard_currency_boost = hard_currency_amount * HARD_CURRENCY_RATE
        total_boost = soft_currency_boost + hard_currency_boost

        # Boost per token
        if token_count > 0:
            boost_per_token = total_boost / token_count
        else:
            boost_per_token = 0

        # Return results as a dictionary
        return {
            "token_count": token_count,
            "soft_currency_boost": soft_currency_boost,
            "hard_currency_boost": hard_currency_boost,
            "total_boost": total_boost,
            "boost_per_token": boost_per_token
        }

    except ValueError as e:
        logging.error(f"Input validation error: {e}")
        raise
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise


def main():
    """
    Main function to demonstrate the calculation of boosts.
    """
    try:
        # Example inputs
        token_count = 10
        soft_currency_amount = 150.0  # Example amount in $HMSTR
        hard_currency_amount = 50.0  # Example amount in hard currency

        # Calculate boosts
        boosts = calculate_boosts(token_count, soft_currency_amount, hard_currency_amount)

        # Display results
        logging.info("Boost Calculation Results:")
        for key, value in boosts.items():
            logging.info(f"{key}: {value}")

    except Exception as e:
        logging.error(f"Failed to calculate boosts: {e}")


if __name__ == "__main__":
    main()
```
