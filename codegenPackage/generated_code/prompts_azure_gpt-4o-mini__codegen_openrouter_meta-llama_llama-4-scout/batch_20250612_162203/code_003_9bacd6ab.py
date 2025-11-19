"""
Generated Code Metadata:
========================
Original URL: https://solana-value-average-frontend.vercel.app
Prompt: Generate a function that calculates the total amount and total value increment for tokens deposited in a Solana Value Average app.
Generated: DETERMINISTIC_9bacd6abed423df6
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict

class Token:
    def __init__(self, name: str, amount: float, value: float):
        """
        Initialize a Token object.

        Args:
        - name (str): The name of the token.
        - amount (float): The amount of the token deposited.
        - value (float): The value of the token.
        """
        self.name = name
        self.amount = amount
        self.value = value

def calculate_total_amount_and_value(tokens: List[Token]) -> Dict[str, float]:
    """
    Calculate the total amount and total value of tokens deposited.

    Args:
    - tokens (List[Token]): A list of Token objects.

    Returns:
    - Dict[str, float]: A dictionary containing the total amount and total value.

    Raises:
    - ValueError: If the input list is empty.
    """
    if not tokens:
        raise ValueError("Input list cannot be empty")

    total_amount = sum(token.amount for token in tokens)
    total_value = sum(token.amount * token.value for token in tokens)

    return {"total_amount": total_amount, "total_value": total_value}

def calculate_value_increment(previous_value: float, current_value: float) -> float:
    """
    Calculate the value increment.

    Args:
    - previous_value (float): The previous total value.
    - current_value (float): The current total value.

    Returns:
    - float: The value increment.

    Raises:
    - ValueError: If the previous value or current value is negative.
    """
    if previous_value < 0 or current_value < 0:
        raise ValueError("Previous value and current value must be non-negative")

    return current_value - previous_value

def main():
    # Example usage:
    tokens = [
        Token("Token A", 10.0, 100.0),
        Token("Token B", 20.0, 200.0),
        Token("Token C", 30.0, 300.0),
    ]

    result = calculate_total_amount_and_value(tokens)
    print(f"Total Amount: {result['total_amount']}")
    print(f"Total Value: {result['total_value']}")

    previous_value = 5000.0
    value_increment = calculate_value_increment(previous_value, result["total_value"])
    print(f"Value Increment: {value_increment}")

if __name__ == "__main__":
    main()
```
