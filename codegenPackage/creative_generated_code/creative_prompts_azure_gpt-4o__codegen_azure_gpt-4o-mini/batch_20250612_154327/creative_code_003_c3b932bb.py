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
import pandas as pd

class ProductPricingCalculator:
    """
    A class to automate the calculation of competitive product pricing and service fees for apparel sourcing.
    """

    def __init__(self, product_data_file):
        """
        Initializes the ProductPricingCalculator with product data from a CSV file.

        :param product_data_file: str - Path to the CSV file containing product data.
        """
        self.product_data_file = product_data_file
        self.product_data = self.load_product_data()
        
    def load_product_data(self):
        """
        Loads product data from a CSV file.

        :return: DataFrame - A pandas DataFrame containing product data.
        """
        try:
            data = pd.read_csv(self.product_data_file)
            return data
        except FileNotFoundError as e:
            raise RuntimeError(f"Error: The file '{self.product_data_file}' was not found.") from e
        except pd.errors.EmptyDataError as e:
            raise RuntimeError("Error: The file is empty.") from e
        except pd.errors.ParserError as e:
            raise RuntimeError("Error: The file could not be parsed.") from e

    def calculate_price(self, base_price, markup_percentage):
        """
        Calculates the final product price based on the base price and markup percentage.

        :param base_price: float - The base price of the product.
        :param markup_percentage: float - The markup percentage to be applied.
        :return: float - The final product price after applying markup.
        """
        if base_price < 0 or markup_percentage < 0:
            raise ValueError("Base price and markup percentage must be non-negative.")
        
        final_price = base_price * (1 + markup_percentage / 100)
        return round(final_price, 2)

    def calculate_service_fee(self, service_cost, fee_percentage):
        """
        Calculates the service fee based on the service cost and fee percentage.

        :param service_cost: float - The cost of the service.
        :param fee_percentage: float - The fee percentage to be applied.
        :return: float - The total service fee.
        """
        if service_cost < 0 or fee_percentage < 0:
            raise ValueError("Service cost and fee percentage must be non-negative.")
        
        service_fee = service_cost * (fee_percentage / 100)
        return round(service_fee, 2)

    def process_products(self):
        """
        Processes the loaded product data to calculate final prices and service fees for each product.
        """
        try:
            self.product_data['Final Price'] = self.product_data.apply(
                lambda row: self.calculate_price(row['Base Price'], row['Markup Percentage']), axis=1
            )
            self.product_data['Service Fee'] = self.product_data.apply(
                lambda row: self.calculate_service_fee(row['Service Cost'], row['Fee Percentage']), axis=1
            )
        except KeyError as e:
            raise RuntimeError(f"Error: Missing expected column in product data: {str(e)}") from e
        
    def save_results(self, output_file):
        """
        Saves the processed product data with calculated prices and fees to a new CSV file.

        :param output_file: str - Path to the output CSV file.
        """
        try:
            self.product_data.to_csv(output_file, index=False)
            print(f"Results successfully saved to '{output_file}'.")
        except Exception as e:
            raise RuntimeError(f"Error saving results to file: {str(e)}") from e

if __name__ == "__main__":
    # Example Usage
    try:
        calculator = ProductPricingCalculator('product_data.csv')
        calculator.process_products()
        calculator.save_results('processed_product_data.csv')
    except Exception as e:
        print(f"An error occurred: {e}")
```
