"""
Generated Code Metadata:
========================
Original URL: https://k.kakenvyf.com
Prompt: Write a code snippet in R or Python to calculate the potential return on investment (ROI) for a portfolio of properties, considering factors like rental income, property appreciation, and operating expenses.
Generated: DETERMINISTIC_edf137cab89de4a7
Batch ID: 20250622_210300
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here is the Python code for calculating the potential ROI for a portfolio of properties:

```python
# Import necessary libraries
import pandas as pd

def calculate_roi(properties):
    """
    Calculate the Return on Investment (ROI) for a portfolio of properties.

    Parameters:
        properties (list of dict): A list of dictionaries where each dictionary contains
                                   details about a property:
                                   - purchase_price (float): The initial purchase price of the property.
                                   - rental_income (float): Monthly rental income from the property.
                                   - appreciation_rate (float): Annual appreciation rate (as a percentage).
                                   - operating_expenses (float): Monthly operating expenses for the property.
                                   - holding_period (int): Number of years the property is held.

    Returns:
        pd.DataFrame: A DataFrame containing the ROI for each property and the overall portfolio ROI.
    """
    # Validate input
    if not isinstance(properties, list) or not all(isinstance(p, dict) for p in properties):
        raise ValueError("Input must be a list of dictionaries representing properties.")

    # Initialize results list
    results = []

    for property in properties:
        try:
            # Extract property details
            purchase_price = property['purchase_price']
            rental_income = property['rental_income']
            appreciation_rate = property['appreciation_rate'] / 100  # Convert percentage to decimal
            operating_expenses = property['operating_expenses']
            holding_period = property['holding_period']

            # Validate property details
            if purchase_price <= 0 or rental_income < 0 or appreciation_rate < 0 or operating_expenses < 0 or holding_period <= 0:
                raise ValueError("Invalid property details. Ensure all values are positive and non-zero where applicable.")

            # Calculate total rental income over the holding period
            total_rental_income = rental_income * 12 * holding_period

            # Calculate total operating expenses over the holding period
            total_operating_expenses = operating_expenses * 12 * holding_period

            # Calculate property appreciation over the holding period
            appreciated_value = purchase_price * (1 + appreciation_rate) ** holding_period

            # Calculate net profit
            net_profit = (appreciated_value - purchase_price) + (total_rental_income - total_operating_expenses)

            # Calculate ROI
            roi = (net_profit / purchase_price) * 100  # ROI as a percentage

            # Append results
            results.append({
                'purchase_price': purchase_price,
                'rental_income': rental_income,
                'appreciation_rate': appreciation_rate * 100,  # Convert back to percentage
                'operating_expenses': operating_expenses,
                'holding_period': holding_period,
                'net_profit': net_profit,
                'roi': roi
            })
        except KeyError as e:
            raise KeyError(f"Missing required property detail: {e}")
        except Exception as e:
            raise RuntimeError(f"Error calculating ROI for property: {e}")

    # Convert results to a DataFrame
    results_df = pd.DataFrame(results)

    # Calculate overall portfolio ROI
    total_purchase_price = results_df['purchase_price'].sum()
    total_net_profit = results_df['net_profit'].sum()
    portfolio_roi = (total_net_profit / total_purchase_price) * 100

    # Add portfolio ROI to the DataFrame
    results_df.loc['Portfolio'] = {
        'purchase_price': total_purchase_price,
        'rental_income': None,
        'appreciation_rate': None,
        'operating_expenses': None,
        'holding_period': None,
        'net_profit': total_net_profit,
        'roi': portfolio_roi
    }

    return results_df


# Example usage
if __name__ == "__main__":
    # Define a portfolio of properties
    portfolio = [
        {
            'purchase_price': 300000,
            'rental_income': 2000,
            'appreciation_rate': 5,
            'operating_expenses': 500,
            'holding_period': 10
        },
        {
            'purchase_price': 500000,
            'rental_income': 3000,
            'appreciation_rate': 4,
            'operating_expenses': 800,
            'holding_period': 8
        }
    ]

    # Calculate ROI
    roi_df = calculate_roi(portfolio)

    # Display results
    print(roi_df)
```

This code is production-ready, well-documented, and includes error handling.
