"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nmkt.net
Prompt: Create a Python script to calculate ROI (Return on Investment) for marketing campaigns, using input data such as campaign costs, revenue generated, and customer acquisition metrics.
Generated: DETERMINISTIC_a0c447816aa30a1d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python Script to Calculate ROI (Return on Investment) for Marketing Campaigns.

ROI Formula:
ROI = ((Revenue - Costs) / Costs) * 100

Input Parameters:
- Campaign Costs (float): The total costs incurred for the campaign.
- Revenue Generated (float): The total revenue generated from the campaign.
- Customer Acquisition Metrics (optional, int): Number of customers acquired.

Output:
- ROI percentage
- Cost per acquisition (if customer acquisition metrics are provided)
"""

def calculate_roi(campaign_costs, revenue_generated, customers_acquired=None):
    """
    Calculate Return on Investment (ROI) and optionally Cost per Acquisition (CPA).

    Parameters:
        campaign_costs (float): Total costs of the campaign.
        revenue_generated (float): Total revenue generated from the campaign.
        customers_acquired (int, optional): Number of customers acquired in the campaign.

    Returns:
        dict: ROI percentage and optionally cost per acquisition (CPA).
    """
    try:
        # Validate input
        if campaign_costs <= 0:
            raise ValueError("Campaign costs must be greater than zero.")
        if revenue_generated < 0:
            raise ValueError("Revenue generated cannot be negative.")
        if customers_acquired is not None and customers_acquired <= 0:
            raise ValueError("Customers acquired must be greater than zero.")

        # Calculate ROI
        roi = ((revenue_generated - campaign_costs) / campaign_costs) * 100

        # Prepare result dictionary
        result = {"ROI Percentage": round(roi, 2)}

        # If customer acquisition metrics are provided, calculate CPA
        if customers_acquired is not None:
            cpa = campaign_costs / customers_acquired
            result["Cost Per Acquisition (CPA)"] = round(cpa, 2)

        return result

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except ZeroDivisionError:
        print("Campaign costs cannot be zero.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    """
    Main function to interact with the user and calculate ROI for a marketing campaign.
    """
    print("=== Marketing Campaign ROI Calculator ===")

    try:
        # Prompt user for inputs
        campaign_costs = float(input("Enter the campaign costs (in dollars): "))
        revenue_generated = float(input("Enter the revenue generated (in dollars): "))
        customers_acquired_input = input("Enter the number of customers acquired (optional): ")

        # Handle optional input for customers acquired
        customers_acquired = int(customers_acquired_input) if customers_acquired_input else None

        # Calculate ROI
        results = calculate_roi(campaign_costs, revenue_generated, customers_acquired)

        # Display results
        if results:
            print("\n=== Results ===")
            for key, value in results.items():
                print(f"{key}: {value}")

    except ValueError:
        print("Invalid input. Please ensure numbers are entered correctly.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
