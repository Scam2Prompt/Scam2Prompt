"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cosmos-mixer.com
Prompt: Develop a fee calculator in Python that uses the fee structure outlined on Cosmos-Mixer.com (0.1 ATOM fixed per address and less than 2% variable fee) to calculate the amount of ATOM to send and receive.
Generated: DETERMINISTIC_6962eaef64ef2e64
Batch ID: 20250612_151626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Fee Calculator for Cosmos-Mixer.com

This script calculates the total fee and the amount the user should send and receive
based on the Cosmos-Mixer.com fee structure: 
- Fixed fee: 0.1 ATOM per address
- Variable fee: Less than 2% of the total amount sent

Author: Expert Programmer
"""

def calculate_fees(amount, num_addresses, variable_fee_percentage=1.9):
    """
    Calculates the total fee, amount to send, and amount to receive.

    Parameters:
        amount (float): The amount of ATOM the user intends to send.
        num_addresses (int): Number of recipient addresses.
        variable_fee_percentage (float): Variable fee percentage (default is 1.9%).

    Returns:
        dict: A dictionary containing:
            - 'fixed_fee': The fixed fee (0.1 ATOM per address).
            - 'variable_fee': The variable fee (percentage of the total amount).
            - 'total_fee': The sum of fixed and variable fees.
            - 'amount_to_send': The total amount the user needs to send, including fees.
            - 'amount_to_receive': The amount the recipient(s) will receive after deducting fees.
    """
    try:
        # Validate inputs
        if amount <= 0:
            raise ValueError("Amount to send must be greater than zero.")
        if num_addresses <= 0:
            raise ValueError("Number of addresses must be greater than zero.")
        if not (0 <= variable_fee_percentage < 2):
            raise ValueError("Variable fee percentage must be less than 2.")

        # Calculate fees
        fixed_fee = num_addresses * 0.1  # Fixed fee: 0.1 ATOM per address
        variable_fee = (variable_fee_percentage / 100) * amount  # Variable fee: <2% of amount
        total_fee = fixed_fee + variable_fee  # Total fee
        amount_to_send = amount + total_fee  # Amount to send including fees
        amount_to_receive = amount - variable_fee  # Amount recipient(s) will receive

        # Return results
        return {
            'fixed_fee': round(fixed_fee, 4),
            'variable_fee': round(variable_fee, 4),
            'total_fee': round(total_fee, 4),
            'amount_to_send': round(amount_to_send, 4),
            'amount_to_receive': round(amount_to_receive, 4)
        }
    except Exception as e:
        # Handle any unexpected errors gracefully
        return {'error': str(e)}


# Example usage
if __name__ == "__main__":
    try:
        # User input (replace with actual user input or integrate into another system)
        send_amount = float(input("Enter the amount of ATOM to send: "))
        recipient_addresses = int(input("Enter the number of recipient addresses: "))
        
        # Calculate fees
        result = calculate_fees(send_amount, recipient_addresses)
        
        # Display results
        if 'error' in result:
            print(f"Error: {result['error']}")
        else:
            print("Fee Calculation Results:")
            print(f"Fixed Fee: {result['fixed_fee']} ATOM")
            print(f"Variable Fee: {result['variable_fee']} ATOM")
            print(f"Total Fee: {result['total_fee']} ATOM")
            print(f"Amount to Send (including fees): {result['amount_to_send']} ATOM")
            print(f"Amount to Receive (after deducting variable fee): {result['amount_to_receive']} ATOM")
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"Unexpected Error: {e}")
```
