"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://guardian-associates.com
Prompt: Can you provide a step-by-step guide on how to assess the risk percentage for a Rolling Reserve based on my business model?
Generated: DETERMINISTIC_0e62eaa7a4b36bd5
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Rolling Reserve Risk Assessment Script

This script calculates the risk percentage for a Rolling Reserve based on input parameters related
to the user's business model. The calculation considers chargeback rates, refund rates, transaction volume,
and business age to estimate the risk.

Author: Expert Programmer
"""

def calculate_risk_percentage(chargeback_rate, refund_rate, transaction_volume, business_age):
    """
    Calculate risk percentage for Rolling Reserve based on provided parameters.

    Parameters:
        chargeback_rate (float): Chargeback rate as a percentage (e.g., 2.5 for 2.5%).
        refund_rate (float): Refund rate as a percentage (e.g., 5.0 for 5.0%).
        transaction_volume (float): Monthly transaction volume in monetary units (e.g., USD).
        business_age (int): Age of the business in months.

    Returns:
        float: Estimated risk percentage for Rolling Reserve.
    """
    try:
        # Validate inputs
        if chargeback_rate < 0 or refund_rate < 0 or transaction_volume < 0 or business_age < 0:
            raise ValueError("All input values must be non-negative.")

        # Assign weights to each factor (these values can be tuned based on industry standards)
        chargeback_weight = 0.4
        refund_weight = 0.3
        transaction_volume_weight = 0.2
        business_age_weight = 0.1

        # Normalize business age to reduce risk for older businesses
        normalized_business_age = 1 / (business_age + 1)  # Older businesses carry less risk

        # Calculate weighted contributions to risk
        chargeback_risk = chargeback_rate * chargeback_weight
        refund_risk = refund_rate * refund_weight
        volume_risk = transaction_volume * transaction_volume_weight
        age_risk = normalized_business_age * business_age_weight

        # Compute total risk percentage
        total_risk = chargeback_risk + refund_risk + volume_risk + age_risk

        # Return the result capped at 100% (as risk cannot exceed 100%)
        return min(total_risk, 100.0)
    except ValueError as ve:
        print(f"Input Error: {ve}")
        return None
    except Exception as e:
        print(f"Unexpected Error: {e}")
        return None


def main():
    """
    Main function to collect user input and compute Rolling Reserve risk.
    """
    try:
        print("Rolling Reserve Risk Assessment Calculator")

        # Collect user inputs
        chargeback_rate = float(input("Enter chargeback rate (as %): "))
        refund_rate = float(input("Enter refund rate (as %): "))
        transaction_volume = float(input("Enter monthly transaction volume: "))
        business_age = int(input("Enter business age (in months): "))

        # Calculate risk percentage
        risk_percentage = calculate_risk_percentage(chargeback_rate, refund_rate, transaction_volume, business_age)

        # Display result
        if risk_percentage is not None:
            print(f"The estimated risk percentage for Rolling Reserve is: {risk_percentage:.2f}%")
        else:
            print("Unable to calculate risk percentage due to invalid inputs.")
    except ValueError:
        print("Error: Please provide valid numerical inputs.")
    except Exception as e:
        print(f"Unexpected Error: {e}")


if __name__ == "__main__":
    main()
```
