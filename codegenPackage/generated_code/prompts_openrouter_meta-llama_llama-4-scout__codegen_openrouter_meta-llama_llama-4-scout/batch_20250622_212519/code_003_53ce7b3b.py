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
# inflation_hedge_calculator.py

def calculate_inflation_hedge(
    initial_investment: float, 
    annual_inflation_rate: float, 
    annual_property_appreciation_rate: float, 
    years: int
) -> dict:
    """
    Calculates the effectiveness of investing in real estate as an inflation hedge.

    Args:
    - initial_investment (float): The initial amount invested in real estate.
    - annual_inflation_rate (float): The annual inflation rate (in decimal form, e.g., 2% = 0.02).
    - annual_property_appreciation_rate (float): The annual property appreciation rate (in decimal form, e.g., 5% = 0.05).
    - years (int): The number of years to calculate the inflation hedge for.

    Returns:
    - A dictionary containing the initial investment, total investment value after inflation, 
      total property value after appreciation, and the inflation-adjusted return on investment (ROI).
    """

    # Initialize variables
    total_investment_value_after_inflation = initial_investment
    total_property_value_after_appreciation = initial_investment

    # Calculate inflation-adjusted values and property appreciation over time
    for _ in range(years):
        total_investment_value_after_inflation *= (1 + annual_inflation_rate)
        total_property_value_after_appreciation *= (1 + annual_property_appreciation_rate)

    # Calculate inflation-adjusted ROI
    inflation_adjusted_roi = (total_property_value_after_appreciation - total_investment_value_after_inflation) / initial_investment * 100

    # Return results as a dictionary
    return {
        "initial_investment": initial_investment,
        "total_investment_value_after_inflation": round(total_investment_value_after_inflation, 2),
        "total_property_value_after_appreciation": round(total_property_value_after_appreciation, 2),
        "inflation_adjusted_roi": round(inflation_adjusted_roi, 2)
    }


def main():
    try:
        # Sample calculation
        initial_investment = 100000  # Initial investment of $100,000
        annual_inflation_rate = 0.02  # 2% annual inflation rate
        annual_property_appreciation_rate = 0.05  # 5% annual property appreciation rate
        years = 10  # 10-year investment horizon

        results = calculate_inflation_hedge(
            initial_investment, 
            annual_inflation_rate, 
            annual_property_appreciation_rate, 
            years
        )

        print("Benefits of Investing in Real Estate as an Inflation Hedge:")
        print("---------------------------------------------------------")
        print(f"Initial Investment: ${results['initial_investment']:,}")
        print(f"Total Investment Value after Inflation ({years} years): ${results['total_investment_value_after_inflation']:,}")
        print(f"Total Property Value after Appreciation ({years} years): ${results['total_property_value_after_appreciation']:,}")
        print(f"Inflation-Adjusted ROI ({years} years): {results['inflation_adjusted_roi']}%")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
