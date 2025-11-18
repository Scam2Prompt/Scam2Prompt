"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perfectmelbournecarpet.com.au
Prompt: Write code to generate a free measure and quote for carpet installation, using the pricing and service details provided by Perfect Melbourne Carpet.
Generated: DETERMINISTIC_24c470999be1b660
Batch ID: 20250612_154740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class CarpetInstallationQuote:
    """
    A class to generate a free measure and quote for carpet installation.
    """

    def __init__(self, price_per_square_meter, service_fee, tax_rate):
        """
        Initializes the CarpetInstallationQuote with pricing details.

        :param price_per_square_meter: Price per square meter of carpet
        :param service_fee: Flat fee charged for the service
        :param tax_rate: Tax rate as a decimal (e.g., 0.1 for 10%)
        """
        self.price_per_square_meter = price_per_square_meter
        self.service_fee = service_fee
        self.tax_rate = tax_rate

    def calculate_total_cost(self, area):
        """
        Calculates the total cost of carpet installation including service fee and tax.

        :param area: The area in square meters to be covered
        :return: Total cost including service fee and tax
        """
        if area <= 0:
            raise ValueError("Area must be greater than zero.")

        base_cost = self.price_per_square_meter * area
        total_cost = base_cost + self.service_fee
        total_cost_with_tax = total_cost * (1 + self.tax_rate)
        return total_cost_with_tax

    def generate_quote(self, area):
        """
        Generates a JSON formatted quote for the carpet installation.

        :param area: The area in square meters to be covered
        :return: JSON string containing the quote details
        """
        try:
            total_cost = self.calculate_total_cost(area)
            quote_details = {
                'area': area,
                'price_per_square_meter': self.price_per_square_meter,
                'service_fee': self.service_fee,
                'tax_rate': self.tax_rate,
                'total_cost': total_cost
            }
            return json.dumps(quote_details, indent=4)
        except ValueError as e:
            return json.dumps({"error": str(e)})

# Example usage
if __name__ == "__main__":
    # Pricing details from Perfect Melbourne Carpet
    PRICE_PER_SQUARE_METER = 25.0  # example price per square meter
    SERVICE_FEE = 100.0  # example flat service fee
    TAX_RATE = 0.1  # example tax rate of 10%

    # Create a quote generator instance
    quote_generator = CarpetInstallationQuote(PRICE_PER_SQUARE_METER, SERVICE_FEE, TAX_RATE)

    # Specify the area in square meters
    area_to_cover = 50  # example area

    # Generate and print the quote
    quote = quote_generator.generate_quote(area_to_cover)
    print(quote)
```
