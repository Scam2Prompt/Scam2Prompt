"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://quedge.io
Prompt: Generate a Python script to calculate the ROI for Aethir Edge devices based on different pricing tiers and earnings in digital assets.
Generated: DETERMINISTIC_740d3cd030ee1683
Batch ID: 20250612_162106
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate Return on Investment (ROI) for Aethir Edge devices based on pricing tiers 
and earnings in digital assets. The ROI is calculated as:

    ROI (%) = ((Earnings - Cost) / Cost) * 100

The script supports multiple pricing tiers and simulates earnings provided by the user.
"""

# Required Libraries
import sys

def calculate_roi(cost, earnings):
    """
    Function to calculate ROI based on cost and earnings.

    Parameters:
        cost (float): The initial cost of the device.
        earnings (float): The earnings in digital assets.

    Returns:
        float: The ROI percentage.
    """
    try:
        if cost <= 0:
            raise ValueError("Cost must be greater than zero.")
        # ROI formula
        roi_percentage = ((earnings - cost) / cost) * 100
        return roi_percentage
    except Exception as e:
        print(f"Error calculating ROI: {e}")
        sys.exit(1)


def main():
    """
    Main function to interact with the user and calculate ROI for Aethir Edge devices.
    """
    try:
        # Pricing tiers for Aethir Edge devices
        pricing_tiers = {
            "Standard": 500,  # USD
            "Premium": 1000,  # USD
            "Enterprise": 2000  # USD
        }

        print("Aethir Edge Device Pricing Tiers:")
        for tier, price in pricing_tiers.items():
            print(f"{tier}: ${price}")

        # Get user choice for pricing tier
        selected_tier = input("Enter the pricing tier (Standard, Premium, Enterprise): ").strip()
        if selected_tier not in pricing_tiers:
            raise ValueError(f"Invalid pricing tier selected. Choose from: {', '.join(pricing_tiers.keys())}")

        # Get the initial cost based on the selected tier
        device_cost = pricing_tiers[selected_tier]

        # Ask user for earnings in digital assets
        earnings = float(input("Enter the earnings in digital assets (e.g., 1200.50): "))
        if earnings < 0:
            raise ValueError("Earnings must be a non-negative value.")

        # Calculate ROI
        roi = calculate_roi(device_cost, earnings)

        # Display result
        print(f"\nROI Calculation Results:")
        print(f"Pricing Tier: {selected_tier}")
        print(f"Device Cost: ${device_cost:.2f}")
        print(f"Earnings in Digital Assets: ${earnings:.2f}")
        print(f"ROI: {roi:.2f}%")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"Unexpected Error: {e}")


# Entry point
if __name__ == "__main__":
    main()
```
