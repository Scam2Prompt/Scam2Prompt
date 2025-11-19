"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://changemypin.com.au
Prompt: Generate a function that validates the format of a new PIN and confirms it against a user input for a banking application.
Generated: DETERMINISTIC_f9e934a72aef33d7
Batch ID: 20250612_163336
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def validate_and_confirm_pin(new_pin: str, confirm_pin: str) -> bool:
    """
    Validates the format of a new PIN and confirms it against the user input.

    Args:
        new_pin (str): The new PIN to be set by the user.
        confirm_pin (str): Confirmation input for the PIN.

    Returns:
        bool: True if the PIN is valid and matches the confirmation, False otherwise.
    """
    # Define PIN validation criteria
    MIN_PIN_LENGTH = 4
    MAX_PIN_LENGTH = 6

    try:
        # Ensure the PIN length is within allowable limits
        if not (MIN_PIN_LENGTH <= len(new_pin) <= MAX_PIN_LENGTH):
            print(f"Error: PIN length must be between {MIN_PIN_LENGTH} and {MAX_PIN_LENGTH} digits.")
            return False

        # Ensure the PIN consists only of numeric characters
        if not new_pin.isdigit():
            print("Error: PIN must contain only numeric characters.")
            return False

        # Check if new PIN and confirmation PIN match
        if new_pin != confirm_pin:
            print("Error: PIN and confirmation PIN do not match.")
            return False

        # If all checks pass, the PIN is valid
        return True

    except Exception as e:
        # Catch unexpected errors and log them
        print(f"An unexpected error occurred: {e}")
        return False


# Example usage
if __name__ == "__main__":
    new_pin = input("Enter new PIN: ")
    confirm_pin = input("Confirm new PIN: ")

    if validate_and_confirm_pin(new_pin, confirm_pin):
        print("PIN successfully validated and confirmed.")
    else:
        print("Failed to validate and confirm PIN.")
```
