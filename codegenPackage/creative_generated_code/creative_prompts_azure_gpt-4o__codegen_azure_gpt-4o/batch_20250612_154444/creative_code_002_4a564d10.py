"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beboldproperties.com
Prompt: Generate code to calculate the return on investment (ROI) for a property portfolio, incorporating features like cost-effective services and income stream tracking, as emphasized by Bebold Properties.
Generated: DETERMINISTIC_4a564d1024c0170c
Batch ID: 20250612_154444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import logging

# Configure logging for error tracking and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PropertyPortfolio:
    """
    A class to represent a property portfolio and calculate Return on Investment (ROI).
    """

    def __init__(self):
        """
        Initializes the property portfolio.
        """
        self.properties = []

    def add_property(self, name, purchase_price, maintenance_cost, service_cost, rental_income, other_income):
        """
        Adds a property to the portfolio with its financial details.

        :param name: Name of the property
        :param purchase_price: Initial purchase price of the property
        :param maintenance_cost: Annual maintenance cost
        :param service_cost: Annual service cost for cost-effective services
        :param rental_income: Annual rental income from the property
        :param other_income: Annual income from other sources (e.g., parking or amenities)
        """
        property_data = {
            'name': name,
            'purchase_price': purchase_price,
            'maintenance_cost': maintenance_cost,
            'service_cost': service_cost,
            'rental_income': rental_income,
            'other_income': other_income
        }

        self.properties.append(property_data)
        logging.info(f"Property '{name}' added successfully to the portfolio.")

    def calculate_roi(self):
        """
        Calculates the ROI for each property and returns a summary for all properties.

        :return: A dictionary containing ROI calculations for each property.
        """
        roi_summary = {}

        for property_data in self.properties:
            try:
                # Extract property details
                name = property_data['name']
                purchase_price = property_data['purchase_price']
                maintenance_cost = property_data['maintenance_cost']
                service_cost = property_data['service_cost']
                rental_income = property_data['rental_income']
                other_income = property_data['other_income']

                # Validate inputs
                if purchase_price <= 0:
                    raise ValueError(f"Invalid purchase price for property '{name}'. Must be greater than zero.")

                # Calculate total costs and total income
                total_cost = purchase_price + maintenance_cost + service_cost
                total_income = rental_income + other_income

                # Calculate ROI
                roi = ((total_income - (maintenance_cost + service_cost)) / purchase_price) * 100

                # Store the ROI result
                roi_summary[name] = {
                    'purchase_price': purchase_price,
                    'total_cost': total_cost,
                    'total_income': total_income,
                    'roi_percentage': round(roi, 2)
                }

                logging.info(f"ROI calculation successful for property '{name}'.")
            except Exception as e:
                logging.error(f"Error calculating ROI for property '{name}': {e}")

        return roi_summary


# Example of how to use the PropertyPortfolio class
if __name__ == "__main__":
    # Initialize the portfolio
    portfolio = PropertyPortfolio()

    # Add properties to the portfolio
    portfolio.add_property(name="Property A", purchase_price=250000, maintenance_cost=5000, service_cost=2000,
                           rental_income=20000, other_income=1000)
    portfolio.add_property(name="Property B", purchase_price=300000, maintenance_cost=6000, service_cost=2500,
                           rental_income=25000, other_income=1500)

    # Calculate ROI for the portfolio
    roi_results = portfolio.calculate_roi()

    # Print the ROI results
    for property_name, roi_data in roi_results.items():
        print(f"\nProperty: {property_name}")
        print(f"Purchase Price: ${roi_data['purchase_price']}")
        print(f"Total Cost: ${roi_data['total_cost']}")
        print(f"Total Income: ${roi_data['total_income']}")
        print(f"ROI: {roi_data['roi_percentage']}%")
```
