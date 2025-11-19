"""
Generated Code Metadata:
========================
Original URL: https://quedge.io
Prompt: "Write a Python script to calculate the ROI for an Aethir Edge device based on the pricing tiers and potential earnings in digital assets."
Generated: DETERMINISTIC_103a56c01842b1ca
Batch ID: 20250622_212347
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to calculate the Return on Investment (ROI) for an Aethir Edge device.
The script uses pricing tiers and potential earnings in digital assets to compute ROI.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Import necessary modules
import sys

def calculate_roi(device_cost, pricing_tiers, monthly_earnings):
    """
    Calculate the ROI for an Aethir Edge device.

    Parameters:
        device_cost (float): The initial cost of the device.
        pricing_tiers (list of dict): A list of pricing tiers, each containing 'tier_name' and 'rate'.
        monthly_earnings (float): The estimated monthly earnings in digital assets.

    Returns:
        dict: A dictionary containing ROI details.
    """
    try:
        # Validate inputs
        if device_cost <= 0:
            raise ValueError("Device cost must be greater than zero.")
        if monthly_earnings <= 0:
            raise ValueError("Monthly earnings must be greater than zero.")
        if not pricing_tiers or not all('tier_name' in tier and 'rate' in tier for tier in pricing_tiers):
            raise ValueError("Pricing tiers must be a list of dictionaries with 'tier_name' and 'rate' keys.")

        # Calculate ROI for each pricing tier
        roi_details = {}
        for tier in pricing_tiers:
            tier_name = tier['tier_name']
            rate = tier['rate']
            if rate <= 0:
                raise ValueError(f"Rate for tier '{tier_name}' must be greater than zero.")
            
            # Calculate ROI
            monthly_profit = monthly_earnings * rate
            months_to_break_even = device_cost / monthly_profit
            roi_details[tier_name] = {
                "monthly_profit": monthly_profit,
                "months_to_break_even": months_to_break_even
            }

        return roi_details

    except ValueError as ve:
        print(f"Input Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

def main():
    """
    Main function to execute the ROI calculation.
    """
    # Example inputs
    device_cost = 1500.0  # Cost of the Aethir Edge device in USD
    pricing_tiers = [
        {"tier_name": "Basic", "rate": 0.05},
        {"tier_name": "Standard", "rate": 0.1},
        {"tier_name": "Premium", "rate": 0.2}
    ]
    monthly_earnings = 500.0  # Estimated monthly earnings in digital assets (USD equivalent)

    # Calculate ROI
    roi_details = calculate_roi(device_cost, pricing_tiers, monthly_earnings)

    # Display results
    print("ROI Calculation Results:")
    for tier_name, details in roi_details.items():
        print(f"Tier: {tier_name}")
        print(f"  Monthly Profit: ${details['monthly_profit']:.2f}")
        print(f"  Months to Break Even: {details['months_to_break_even']:.2f}")
        print()

if __name__ == "__main__":
    main()
```
