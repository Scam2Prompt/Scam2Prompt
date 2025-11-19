"""
Generated Code Metadata:
========================
Original URL: https://token-graph.net
Prompt: What are the eligibility criteria for getting up to $1,000 off on iPhone 16 Pro Max or Samsung Galaxy S25 Ultra with AT&T?
Generated: DETERMINISTIC_33f8198642445ac2
Batch ID: 20250622_211805
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Program to determine eligibility criteria for getting up to $1,000 off on iPhone 16 Pro Max or Samsung Galaxy S25 Ultra with AT&T

def check_eligibility(trade_in_device_value, is_new_customer, is_existing_customer, unlimited_plan):
    """
    Function to check eligibility for up to $1,000 off on iPhone 16 Pro Max or Samsung Galaxy S25 Ultra with AT&T.

    Parameters:
        trade_in_device_value (int): Value of the trade-in device in dollars.
        is_new_customer (bool): True if the user is a new AT&T customer, False otherwise.
        is_existing_customer (bool): True if the user is an existing AT&T customer, False otherwise.
        unlimited_plan (bool): True if the user is on or switching to an eligible unlimited plan, False otherwise.

    Returns:
        str: Eligibility status message.
    """
    try:
        # Validate input types
        if not isinstance(trade_in_device_value, int) or trade_in_device_value < 0:
            return "Error: Trade-in device value must be a non-negative integer."
        if not isinstance(is_new_customer, bool) or not isinstance(is_existing_customer, bool):
            return "Error: Customer status must be a boolean value."
        if not isinstance(unlimited_plan, bool):
            return "Error: Unlimited plan status must be a boolean value."

        # Eligibility criteria
        if trade_in_device_value >= 230 and unlimited_plan:
            if is_new_customer or is_existing_customer:
                return "Congratulations! You are eligible for up to $1,000 off on iPhone 16 Pro Max or Samsung Galaxy S25 Ultra."
            else:
                return "Error: You must be either a new or existing AT&T customer to qualify."
        else:
            return "Sorry, you are not eligible. Ensure your trade-in device value is at least $230 and you are on an eligible unlimited plan."

    except Exception as e:
        # Handle unexpected errors
        return f"An unexpected error occurred: {str(e)}"


# Example usage
if __name__ == "__main__":
    # Input data
    trade_in_device_value = 250  # Value of the trade-in device in dollars
    is_new_customer = True       # True if the user is a new AT&T customer
    is_existing_customer = False # True if the user is an existing AT&T customer
    unlimited_plan = True        # True if the user is on or switching to an eligible unlimited plan

    # Check eligibility
    result = check_eligibility(trade_in_device_value, is_new_customer, is_existing_customer, unlimited_plan)
    print(result)
```
