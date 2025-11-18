"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.trendsetterzs.com
Prompt: Develop a script that automates the calculation of competitive product pricing and service fees for apparel sourcing, referencing Trend Setterzs' dynamic business models.
Generated: DETERMINISTIC_c3b932bbcc08cdcd
Batch ID: 20250612_154327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_pricing(base_cost, markup_percentage, service_fee_percentage, dynamic_factor=1.0):
    """
    Calculates the competitive product pricing and service fees.

    Args:
        base_cost (float): The base cost of the apparel.
        markup_percentage (float): The percentage markup for profit.
        service_fee_percentage (float): The percentage service fee to be applied.
        dynamic_factor (float, optional): Factor to dynamically adjust pricing based on Trend Setterzs' business models. Default is 1.0.

    Returns:
        dict: A dictionary containing the final calculated price and service fee.
    """
    try:
        # Validate input
        if base_cost < 0 or markup_percentage < 0 or service_fee_percentage < 0 or dynamic_factor <= 0:
            raise ValueError("Inputs must be positive values.")

        # Calculate markup amount
        markup_amount = base_cost * (markup_percentage / 100)

        # Calculate the service fee
        service_fee = base_cost * (service_fee_percentage / 100)

        # Calculate dynamic price adjustment
        adjusted_price = (base_cost + markup_amount + service_fee) * dynamic_factor

        # Round values for presentation
        return {
            'final_price': round(adjusted_price, 2),
            'service_fee': round(service_fee, 2)
        }

    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

def main():
    """
    Main function to run the pricing script. This is the entry point of the program.
    """
    try:
        # Example inputs for testing purposes
        base_cost = float(input("Enter base cost of the apparel: "))  # e.g., $100
        markup_percentage = float(input("Enter markup percentage: "))  # e.g., 30%
        service_fee_percentage = float(input("Enter service fee percentage: "))  # e.g., 10%
        dynamic_factor = float(input("Enter dynamic factor (default is 1.0): "))  # e.g., 1.2

        # Calculate and display results
        results = calculate_pricing(base_cost, markup_percentage, service_fee_percentage, dynamic_factor)
        print("\nFinal Calculations:")
        print(f"Competitive Price: ${results['final_price']}")
        print(f"Service Fee: ${results['service_fee']}")

    except ValueError:
        print("Invalid input. Please provide numerical values only.")
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
        sys.exit(0)

if __name__ == "__main__":
    # Run the main function
    main()
```
