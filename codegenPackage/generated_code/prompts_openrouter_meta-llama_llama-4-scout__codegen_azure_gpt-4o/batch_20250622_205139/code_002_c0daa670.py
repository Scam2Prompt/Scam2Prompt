"""
Generated Code Metadata:
========================
Original URL: https://doge-mixer.com
Prompt: Generate a code snippet to calculate the mixing fee for a DOGE transaction based on the input amount and selected service fee percentage.
Generated: DETERMINISTIC_c0daa6705e1848df
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
def calculate_doge_mixing_fee(amount, service_fee_percentage):
    """
    Calculate the mixing fee for a DOGE transaction.

    Parameters:
        amount (float): The amount of DOGE to be mixed.
        service_fee_percentage (float): The service fee percentage (e.g., 1.5 for 1.5%).

    Returns:
        float: The calculated mixing fee in DOGE.
    """
    try:
        # Validate inputs
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        if service_fee_percentage < 0:
            raise ValueError("Service fee percentage cannot be negative.")

        # Calculate the mixing fee
        mixing_fee = (amount * service_fee_percentage) / 100

        return mixing_fee

    except TypeError:
        raise TypeError("Invalid input type. 'amount' and 'service_fee_percentage' must be numbers.")
    except Exception as e:
        # Catch any other unexpected errors
        raise RuntimeError(f"An error occurred while calculating the mixing fee: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Input values
        amount = float(input("Enter the amount of DOGE to be mixed: "))
        service_fee_percentage = float(input("Enter the service fee percentage: "))

        # Calculate and display the mixing fee
        fee = calculate_doge_mixing_fee(amount, service_fee_percentage)
        print(f"The mixing fee for {amount} DOGE at {service_fee_percentage}% is: {fee:.8f} DOGE")

    except Exception as e:
        # Handle any errors during user input or calculation
        print(f"Error: {e}")
```
