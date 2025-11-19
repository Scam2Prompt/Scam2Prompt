"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earno-trade.net
Prompt: Develop a script that evaluates the impact of inflation on rental income and property value over a 10-year period, using the investment strategies from earno-trade.net.
Generated: DETERMINISTIC_b58c6fac82c4a2a6
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def evaluate_inflation_impact(start_rent, start_property_value, annual_inflation_rate, annual_rent_increase_rate):
    """
    Evaluate the impact of inflation on rental income and property value over a 10-year period.
    
    Parameters:
    - start_rent (float): Initial annual rental income.
    - start_property_value (float): Initial property value.
    - annual_inflation_rate (float): Annual inflation rate (as a percentage, e.g., 2.5 for 2.5%).
    - annual_rent_increase_rate (float): Annual rental increase rate (as a percentage, e.g., 3 for 3%).

    Returns:
    - dict: A dictionary containing the yearly rental income and property value.
    """
    # Validate inputs
    if any(x < 0 for x in [start_rent, start_property_value, annual_inflation_rate, annual_rent_increase_rate]):
        raise ValueError("Input values cannot be negative.")

    # Constants
    years = 10

    # Initialize results
    results = {
        "Year": [],
        "Rental Income ($)": [],
        "Property Value ($)": []
    }

    # Simulation loop for 10 years
    current_rent = start_rent
    current_property_value = start_property_value

    for year in range(1, years + 1):
        # Append year
        results["Year"].append(year)
        
        # Append current rental income and property value
        results["Rental Income ($)"].append(round(current_rent, 2))
        results["Property Value ($)"].append(round(current_property_value, 2))
        
        # Calculate next year's rental income and property value
        current_rent += current_rent * (annual_rent_increase_rate / 100)
        current_property_value += current_property_value * (annual_inflation_rate / 100)

    return results


def main():
    """
    Main entry point for the script. Prompts the user for input, evaluates inflation impact,
    and displays the results.
    """
    try:
        print("Evaluate the impact of inflation on rental income and property value over 10 years.")
        
        # Collect user input
        start_rent = float(input("Enter initial annual rental income ($): "))
        start_property_value = float(input("Enter initial property value ($): "))
        annual_inflation_rate = float(input("Enter annual inflation rate (%): "))
        annual_rent_increase_rate = float(input("Enter annual rental increase rate (%): "))
        
        # Evaluate impact
        results = evaluate_inflation_impact(
            start_rent,
            start_property_value,
            annual_inflation_rate,
            annual_rent_increase_rate
        )
        
        # Print results
        print("\nImpact of Inflation on Rental Income and Property Value Over 10 Years:")
        print(f"{'Year':<5} {'Rental Income ($)':<20} {'Property Value ($)':<20}")
        print("-" * 50)
        for year, rent, value in zip(results["Year"], results["Rental Income ($)"], results["Property Value ($)"]):
            print(f"{year:<5} {rent:<20} {value:<20}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Run the script
    main()
```
