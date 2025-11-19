"""
Generated Code Metadata:
========================
Original URL: https://tonmixers.com
Prompt: Generate code to check the minimum and maximum Toncoin amounts (15 TON to 5000 TON) allowed for mixing and validate user input accordingly.
Generated: DETERMINISTIC_7bd6eeae6a1d8ff5
Batch ID: 20250612_151626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def validate_toncoin_amount(amount: float) -> bool:
    """
    Validates if the provided Toncoin amount is within the allowed mixing range.
    
    Args:
        amount (float): The Toncoin amount to validate.
        
    Returns:
        bool: True if the amount is valid, False otherwise.
    """
    MIN_AMOUNT = 15.0
    MAX_AMOUNT = 5000.0
    
    if not isinstance(amount, (int, float)):
        return False
    
    if amount < MIN_AMOUNT or amount > MAX_AMOUNT:
        return False
    
    return True


def get_valid_toncoin_amount() -> float:
    """
    Prompts the user to input a Toncoin amount and validates it.
    Continues prompting until a valid amount is provided.
    
    Returns:
        float: The validated Toncoin amount.
    """
    MIN_AMOUNT = 15.0
    MAX_AMOUNT = 5000.0
    
    while True:
        try:
            user_input = input(f"Enter Toncoin amount to mix ({MIN_AMOUNT} - {MAX_AMOUNT} TON): ")
            amount = float(user_input)
            
            if validate_toncoin_amount(amount):
                return amount
            else:
                print(f"Amount must be between {MIN_AMOUNT} and {MAX_AMOUNT} TON.")
                
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


# Example usage
if __name__ == "__main__":
    try:
        amount = get_valid_toncoin_amount()
        print(f"Valid amount entered: {amount} TON")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
