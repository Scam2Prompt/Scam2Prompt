"""
Generated Code Metadata:
========================
Original URL: https://www.trendsetterzs.com
Prompt: Develop a script that automates the calculation of competitive product pricing and service fees for apparel sourcing, referencing Trend Setterzs' dynamic business models.
Generated: DETERMINISTIC_c3b932bbcc08cdcd
Batch ID: 20250612_154327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class ApparelPricingCalculator:
    """
    A class to calculate competitive product pricing and service fees for apparel sourcing.
    """

    def __init__(self, cost_data: pd.DataFrame, markup_percentage: float):
        """
        Initializes the pricing calculator with cost data and markup percentage.

        :param cost_data: DataFrame containing product cost data with columns ['product_id', 'base_cost']
        :param markup_percentage: Percentage to apply as markup on base costs
        """
        self.cost_data = cost_data
        self.markup_percentage = markup_percentage

    def validate_data(self):
        """
        Validates the input data to ensure it contains the required columns and data types.
        Raises ValueError if validation fails.
        """
        required_columns = ['product_id', 'base_cost']
        for column in required_columns:
            if column not in self.cost_data.columns:
                raise ValueError(f"Missing required column: {column}")

        if not pd.api.types.is_numeric_dtype(self.cost_data['base_cost']):
            raise ValueError("base_cost must be numeric.")

    def calculate_pricing(self):
        """
        Calculates the final pricing based on base cost and markup percentage.

        :return: DataFrame with product_id, base_cost, and final_price
        """
        self.validate_data()
        
        # Calculate final price
        self.cost_data['final_price'] = self.cost_data['base_cost'] * (1 + self.markup_percentage / 100)
        return self.cost_data[['product_id', 'base_cost', 'final_price']]

    def calculate_service_fees(self, service_fee_percentage: float):
        """
        Calculates service fees based on the final price.

        :param service_fee_percentage: Percentage to apply as service fee on final prices
        :return: DataFrame with product_id and service_fee
        """
        if 'final_price' not in self.cost_data.columns:
            raise ValueError("Final prices must be calculated before calculating service fees.")

        self.cost_data['service_fee'] = self.cost_data['final_price'] * (service_fee_percentage / 100)
        return self.cost_data[['product_id', 'service_fee']]

def main():
    # Sample cost data
    data = {
        'product_id': [1, 2, 3],
        'base_cost': [10.0, 15.0, 20.0]
    }
    
    # Create a DataFrame
    cost_data = pd.DataFrame(data)

    # Initialize the pricing calculator with a 30% markup
    calculator = ApparelPricingCalculator(cost_data, markup_percentage=30)

    try:
        # Calculate pricing
        pricing = calculator.calculate_pricing()
        print("Pricing Data:")
        print(pricing)

        # Calculate service fees with a 10% service fee
        service_fees = calculator.calculate_service_fees(service_fee_percentage=10)
        print("\nService Fees Data:")
        print(service_fees)

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
