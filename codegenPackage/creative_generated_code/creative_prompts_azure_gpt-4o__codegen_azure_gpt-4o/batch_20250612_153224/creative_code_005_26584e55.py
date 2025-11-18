"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://propsfundedtrader.com
Prompt: Write a script to calculate the service fee for passing prop firm challenges based on account sizes (e.g., $100 for a $10K account, $500 for a $200K account) and simulate refund conditions if the challenge is not passed.
Generated: DETERMINISTIC_26584e557f64787d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# prop_firm_fee_calculator.py

# Import necessary modules for error handling and input validation.
import sys

def calculate_service_fee(account_size):
    """
    Calculate the service fee based on the prop firm account size.
    
    Parameters:
        account_size (int): The size of the account in USD.
    
    Returns:
        float: The corresponding service fee in USD.
    
    Raises:
        ValueError: If the account size is invalid or unsupported.
    """
    # Fee schedule based on account size.
    fee_schedule = {
        10000: 100.00,
        25000: 250.00,
        50000: 350.00,
        100000: 500.00,
        200000: 1000.00,
    }
    
    if account_size in fee_schedule:
        return fee_schedule[account_size]
    else:
        raise ValueError(
            f"Unsupported account size: {account_size}. "
            f"Supported sizes are {list(fee_schedule.keys())}."
        )


def simulate_refund(is_challenge_passed, service_fee):
    """
    Simulate whether a refund is issued based on the challenge outcome.
    
    Parameters:
        is_challenge_passed (bool): Outcome of the challenge (True if passed, False otherwise).
        service_fee (float): The service fee paid for the account.
    
    Returns:
        float: The amount refunded (0 if the challenge is passed, full fee if failed).
    """
    if not isinstance(is_challenge_passed, bool):
        raise ValueError("Challenge outcome must be a boolean value (True/False).")
    
    # If the challenge is not passed, refund the service fee.
    return service_fee if not is_challenge_passed else 0.0


def main():
    """
    Main function to handle user input and execute the service fee calculation and refund simulation.
    """
    try:
        # Prompt user for account size.
        account_size = int(input("Enter the account size (e.g., 10000, 25000, 50000, 100000, 200000): "))
        
        # Calculate the service fee for the selected account size.
        service_fee = calculate_service_fee(account_size)
        print(f"Service fee for ${account_size} account: ${service_fee:.2f}")
        
        # Prompt user for challenge outcome.
        challenge_outcome_input = input("Did you pass the challenge? (yes/no): ").strip().lower()
        if challenge_outcome_input not in ['yes', 'no']:
            raise ValueError("Invalid input for challenge outcome. Please enter 'yes' or 'no'.")
        
        is_challenge_passed = challenge_outcome_input == 'yes'
        
        # Simulate refund conditions based on challenge outcome.
        refund_amount = simulate_refund(is_challenge_passed, service_fee)
        if refund_amount > 0:
            print(f"Challenge not passed. Refund issued: ${refund_amount:.2f}")
        else:
            print("Challenge passed. No refund issued.")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


# Entry point for the script.
if __name__ == "__main__":
    main()
```
