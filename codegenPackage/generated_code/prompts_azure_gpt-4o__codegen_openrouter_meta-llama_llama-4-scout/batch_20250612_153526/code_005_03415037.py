"""
Generated Code Metadata:
========================
Original URL: https://myrolandclaim.org
Prompt: Create a Python function to validate user input against eligibility criteria for a legal claim, using the Roland Consumer Claim's conditions as an example.
Generated: DETERMINISTIC_03415037aa4848f5
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

def validate_roland_consumer_claim(
    purchase_date: str, 
    purchase_amount: float, 
    claimant_name: str, 
    claimant_email: str, 
    claimant_phone: str
) -> dict:
    """
    Validates user input against eligibility criteria for Roland Consumer Claim.

    Args:
    - purchase_date (str): Date of purchase in 'YYYY-MM-DD' format.
    - purchase_amount (float): Amount of purchase.
    - claimant_name (str): Name of claimant.
    - claimant_email (str): Email of claimant.
    - claimant_phone (str): Phone number of claimant.

    Returns:
    - dict: Dictionary containing validation result and error messages.
    """

    # Initialize validation result
    validation_result = {
        "is_eligible": False,
        "error_messages": []
    }

    # Check if claimant name is provided
    if not claimant_name:
        validation_result["error_messages"].append("Claimant name is required.")
    
    # Check if claimant email is provided and valid
    if not claimant_email:
        validation_result["error_messages"].append("Claimant email is required.")
    elif "@" not in claimant_email:
        validation_result["error_messages"].append("Invalid claimant email.")

    # Check if claimant phone is provided
    if not claimant_phone:
        validation_result["error_messages"].append("Claimant phone number is required.")

    # Check if purchase date is provided and within the last 30 days
    try:
        purchase_date_obj = datetime.strptime(purchase_date, "%Y-%m-%d")
        if (datetime.now() - purchase_date_obj).days > 30:
            validation_result["error_messages"].append("Purchase date must be within the last 30 days.")
    except ValueError:
        validation_result["error_messages"].append("Invalid purchase date format. Use 'YYYY-MM-DD'.")

    # Check if purchase amount is provided and greater than 0
    if purchase_amount is None or purchase_amount <= 0:
        validation_result["error_messages"].append("Purchase amount must be greater than 0.")

    # If no error messages, claimant is eligible
    if not validation_result["error_messages"]:
        validation_result["is_eligible"] = True

    return validation_result


def main():
    # Example usage
    purchase_date = "2024-09-01"
    purchase_amount = 1000.0
    claimant_name = "John Doe"
    claimant_email = "john@example.com"
    claimant_phone = "1234567890"

    result = validate_roland_consumer_claim(
        purchase_date, 
        purchase_amount, 
        claimant_name, 
        claimant_email, 
        claimant_phone
    )

    print("Validation Result:")
    print(f"Is Eligible: {result['is_eligible']}")
    if result["error_messages"]:
        print("Error Messages:")
        for error in result["error_messages"]:
            print(error)


if __name__ == "__main__":
    main()
```
