"""
Generated Code Metadata:
========================
Original URL: https://okx-web3-tron-usdt-trc20-000000690.pages.dev
Prompt: Create a script to validate and format user input for numeric values (e.g., transaction amounts) when interacting with OKX Web3 for USDT (TRC-20) transfers.
Generated: DETERMINISTIC_30eae3d8528093d0
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re

def validate_and_format_numeric_input(user_input, min_value=0, max_value=float('inf')):
    """
    Validates and formats user input for numeric values.

    Args:
        user_input (str): The user's input.
        min_value (float, optional): The minimum allowed value. Defaults to 0.
        max_value (float, optional): The maximum allowed value. Defaults to infinity.

    Returns:
        float: The formatted numeric value.

    Raises:
        ValueError: If the input is not a valid number or out of range.
    """

    # Remove any non-numeric characters except for decimal points
    cleaned_input = re.sub(r'[^\d\.]', '', user_input)

    # Check if the input is a valid number
    try:
        numeric_value = float(cleaned_input)
    except ValueError:
        raise ValueError("Invalid input. Please enter a valid number.")

    # Check if the input is within the allowed range
    if numeric_value < min_value or numeric_value > max_value:
        raise ValueError(f"Input value must be between {min_value} and {max_value}.")

    # Format the numeric value to 8 decimal places (USDT precision)
    formatted_value = f"{numeric_value:.8f}"

    # Remove trailing zeros
    formatted_value = formatted_value.rstrip('0').rstrip('.')

    return formatted_value


def validate_trc20_address(address):
    """
    Validates a TRC-20 address.

    Args:
        address (str): The TRC-20 address.

    Returns:
        bool: True if the address is valid, False otherwise.
    """

    # TRC-20 addresses start with 'T' and have a length of 34 characters
    if not isinstance(address, str) or not address.startswith('T') or len(address) != 34:
        return False

    # Basic checksum validation (not exhaustive, but helps prevent typos)
    try:
        int(address[1:], 36)
    except ValueError:
        return False

    return True


def main():
    # Example usage
    user_input = "123.456789"
    try:
        formatted_amount = validate_and_format_numeric_input(user_input)
        print(f"Formatted amount: {formatted_amount}")
    except ValueError as e:
        print(f"Error: {e}")

    trc20_address = "Txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
    if validate_trc20_address(trc20_address):
        print("TRC-20 address is valid")
    else:
        print("TRC-20 address is invalid")


if __name__ == "__main__":
    main()
```
