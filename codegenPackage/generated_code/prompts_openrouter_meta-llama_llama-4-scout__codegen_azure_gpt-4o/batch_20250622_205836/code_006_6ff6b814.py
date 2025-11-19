"""
Generated Code Metadata:
========================
Original URL: https://solanche-token.blogspot.com
Prompt: Develop a script to calculate the potential returns on investment for $SAVAX holders based on the token's roadmap and price increase projections.
Generated: DETERMINISTIC_6ff6b814b38e8b07
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def calculate_roi(initial_investment, price_projections):
    """
    Calculate the potential returns on investment based on price projections.

    Parameters:
        initial_investment (float): The amount of money initially invested in $SAVAX.
        price_projections (list of float): A list of projected future prices for $SAVAX.

    Returns:
        list of dict: A list of dictionaries containing the projected price, 
                      potential value of the investment, and ROI percentage.
    """
    if initial_investment <= 0:
        raise ValueError("Initial investment must be greater than zero.")
    if not price_projections or not all(price > 0 for price in price_projections):
        raise ValueError("Price projections must be a non-empty list of positive values.")

    results = []
    for projected_price in price_projections:
        # Calculate the potential value of the investment
        potential_value = initial_investment * projected_price
        # Calculate the ROI percentage
        roi_percentage = ((potential_value - initial_investment) / initial_investment) * 100
        # Append the results
        results.append({
            "projected_price": projected_price,
            "potential_value": potential_value,
            "roi_percentage": roi_percentage
        })
    return results


def main():
    """
    Main function to execute the ROI calculation script.
    """
    try:
        # User input for initial investment
        initial_investment = float(input("Enter your initial investment in $SAVAX (USD): "))
        # User input for price projections
        price_projections_input = input("Enter projected prices for $SAVAX (comma-separated): ")
        price_projections = [float(price.strip()) for price in price_projections_input.split(",")]

        # Calculate ROI
        roi_results = calculate_roi(initial_investment, price_projections)

        # Display results
        print("\nPotential Returns on Investment:")
        print(f"{'Projected Price':<20}{'Potential Value (USD)':<25}{'ROI (%)':<10}")
        print("-" * 55)
        for result in roi_results:
            print(f"{result['projected_price']:<20}{result['potential_value']:<25.2f}{result['roi_percentage']:<10.2f}")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
