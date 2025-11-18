"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daimonlogisticsbd.com
Prompt: Write a Python script to calculate shipping costs for air freight services based on import/export data, using the specific trade lanes mentioned on Daimon Logistics BD's website (e.g., USA, Europe, Canada, Far East Countries).
Generated: DETERMINISTIC_fac60c216c51ca77
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_shipping_cost(trade_lane, weight_kg):
    """
    Calculate shipping cost based on trade lane and weight in kilograms.

    Args:
        trade_lane (str): The trade lane (e.g., "USA", "Europe", "Canada", "Far East").
        weight_kg (float): The weight of the shipment in kilograms.

    Returns:
        float: The calculated shipping cost in USD.
    """
    # Shipping rates in USD per kilogram for different trade lanes
    shipping_rates = {
        "USA": 5.00,          # Rate per kg to USA
        "Europe": 4.50,       # Rate per kg to Europe
        "Canada": 4.75,       # Rate per kg to Canada
        "Far East": 3.50      # Rate per kg to Far East countries
    }

    # Ensure the trade lane is valid
    if trade_lane not in shipping_rates:
        raise ValueError(f"Invalid trade lane: {trade_lane}. Supported trade lanes are: {', '.join(shipping_rates.keys())}")

    # Calculate the cost
    rate_per_kg = shipping_rates[trade_lane]
    return weight_kg * rate_per_kg

def main():
    """
    Main function to handle user input and calculate the shipping cost.
    """
    try:
        # Prompt user for trade lane
        trade_lane = input("Enter the trade lane (USA, Europe, Canada, Far East): ").strip()

        # Prompt user for weight in kilograms
        weight_input = input("Enter the weight of the shipment in kilograms: ").strip()
        try:
            weight_kg = float(weight_input)
            if weight_kg <= 0:
                raise ValueError("Weight must be a positive number.")
        except ValueError:
            raise ValueError("Invalid input for weight. Please enter a numerical value greater than 0.")

        # Calculate and display the shipping cost
        cost = calculate_shipping_cost(trade_lane, weight_kg)
        print(f"Shipping cost for {weight_kg:.2f} kg to {trade_lane}: ${cost:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Thank you for using the shipping cost calculator.")

if __name__ == "__main__":
    main()
```
