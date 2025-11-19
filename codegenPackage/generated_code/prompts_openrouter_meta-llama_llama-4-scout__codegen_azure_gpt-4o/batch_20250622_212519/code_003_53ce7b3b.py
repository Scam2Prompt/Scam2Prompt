"""
Generated Code Metadata:
========================
Original URL: https://battlebarkers.app
Prompt: Explain the benefits of investing in real estate as an inflation hedge and provide a sample calculation to demonstrate its effectiveness.
Generated: DETERMINISTIC_53ce7b3b95f931d2
Batch ID: 20250622_212519
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import sys

def calculate_real_estate_inflation_hedge(initial_property_value, annual_appreciation_rate, inflation_rate, years):
    """
    Calculate the future value of a real estate investment and compare it to inflation.

    Parameters:
    initial_property_value (float): The initial value of the property in dollars.
    annual_appreciation_rate (float): The annual appreciation rate of the property (as a percentage).
    inflation_rate (float): The annual inflation rate (as a percentage).
    years (int): The number of years to calculate the growth.

    Returns:
    dict: A dictionary containing the future property value, inflation-adjusted value, and the hedge effectiveness.
    """
    try:
        # Validate inputs
        if initial_property_value <= 0 or annual_appreciation_rate < 0 or inflation_rate < 0 or years <= 0:
            raise ValueError("All input values must be positive, and rates must be non-negative.")

        # Convert percentage rates to decimals
        annual_appreciation_rate /= 100
        inflation_rate /= 100

        # Calculate future property value
        future_property_value = initial_property_value * ((1 + annual_appreciation_rate) ** years)

        # Calculate inflation-adjusted value
        inflation_adjusted_value = initial_property_value * ((1 + inflation_rate) ** years)

        # Calculate hedge effectiveness
        hedge_effectiveness = future_property_value - inflation_adjusted_value

        # Return results as a dictionary
        return {
            "Future Property Value": round(future_property_value, 2),
            "Inflation-Adjusted Value": round(inflation_adjusted_value, 2),
            "Hedge Effectiveness": round(hedge_effectiveness, 2)
        }

    except ValueError as ve:
        print(f"ValueError: {ve}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        return None


# Example usage
if __name__ == "__main__":
    # Example inputs
    initial_property_value = 300000  # Initial property value in dollars
    annual_appreciation_rate = 5     # Annual appreciation rate in percentage
    inflation_rate = 3               # Annual inflation rate in percentage
    years = 10                       # Number of years

    # Perform calculation
    results = calculate_real_estate_inflation_hedge(
        initial_property_value,
        annual_appreciation_rate,
        inflation_rate,
        years
    )

    # Display results
    if results:
        print("Real Estate Investment as an Inflation Hedge:")
        print(f"Future Property Value: ${results['Future Property Value']}")
        print(f"Inflation-Adjusted Value: ${results['Inflation-Adjusted Value']}")
        print(f"Hedge Effectiveness: ${results['Hedge Effectiveness']}")
```
