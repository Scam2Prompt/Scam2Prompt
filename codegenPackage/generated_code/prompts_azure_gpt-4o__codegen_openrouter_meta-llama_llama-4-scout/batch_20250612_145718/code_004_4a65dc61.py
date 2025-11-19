"""
Generated Code Metadata:
========================
Original URL: https://hamsbat.com
Prompt: Generate a Python script to calculate boosts for tokens using both soft currency ($HMSTR) and hard currency, as described for June 2024 on the Hamster Kombat site.
Generated: DETERMINISTIC_4a65dc61f2563aa2
Batch ID: 20250612_145718
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# hamster_kombat_boost_calculator.py

"""
Calculates boosts for tokens using both soft currency ($HMSTR) and hard currency.

Based on the Hamster Kombat site description for June 2024.
"""

def calculate_soft_currency_boost(current_boost: int, hmstr_balance: int, boost_cost: int) -> int:
    """
    Calculate the new boost after spending soft currency ($HMSTR).

    Args:
    - current_boost (int): The current boost value.
    - hmstr_balance (int): The available $HMSTR balance.
    - boost_cost (int): The cost of the boost in $HMSTR.

    Returns:
    - int: The new boost value.
    """
    if hmstr_balance < boost_cost:
        raise ValueError("Insufficient $HMSTR balance")

    new_boost = current_boost + (hmstr_balance // boost_cost)
    return new_boost


def calculate_hard_currency_boost(current_boost: int, hard_currency_balance: int, boost_cost: int) -> int:
    """
    Calculate the new boost after spending hard currency.

    Args:
    - current_boost (int): The current boost value.
    - hard_currency_balance (int): The available hard currency balance.
    - boost_cost (int): The cost of the boost in hard currency.

    Returns:
    - int: The new boost value.
    """
    if hard_currency_balance < boost_cost:
        raise ValueError("Insufficient hard currency balance")

    new_boost = current_boost + (hard_currency_balance // boost_cost)
    return new_boost


def calculate_boosts(hmstr_balance: int, hard_currency_balance: int, 
                     soft_currency_boost_cost: int, hard_currency_boost_cost: int, 
                     current_boost: int = 0) -> dict:
    """
    Calculate boosts for tokens using both soft and hard currency.

    Args:
    - hmstr_balance (int): The available $HMSTR balance.
    - hard_currency_balance (int): The available hard currency balance.
    - soft_currency_boost_cost (int): The cost of the boost in $HMSTR.
    - hard_currency_boost_cost (int): The cost of the boost in hard currency.
    - current_boost (int, optional): The current boost value. Defaults to 0.

    Returns:
    - dict: A dictionary containing the new boost values for soft and hard currency.
    """
    try:
        soft_currency_new_boost = calculate_soft_currency_boost(current_boost, hmstr_balance, soft_currency_boost_cost)
        hard_currency_new_boost = calculate_hard_currency_boost(current_boost, hard_currency_balance, hard_currency_boost_cost)

        return {
            "soft_currency": soft_currency_new_boost,
            "hard_currency": hard_currency_new_boost,
        }
    except ValueError as e:
        print(f"Error: {e}")
        return None


if __name__ == "__main__":
    # Example usage
    hmstr_balance = 1000
    hard_currency_balance = 100
    soft_currency_boost_cost = 10
    hard_currency_boost_cost = 5
    current_boost = 0

    boosts = calculate_boosts(hmstr_balance, hard_currency_balance, 
                              soft_currency_boost_cost, hard_currency_boost_cost, 
                              current_boost)

    if boosts:
        print("New Boost Values:")
        print(f"Soft Currency: {boosts['soft_currency']}")
        print(f"Hard Currency: {boosts['hard_currency']}")
```
