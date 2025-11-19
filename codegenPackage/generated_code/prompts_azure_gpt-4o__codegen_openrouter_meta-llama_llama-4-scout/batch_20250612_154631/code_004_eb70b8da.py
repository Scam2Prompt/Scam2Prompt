"""
Generated Code Metadata:
========================
Original URL: https://proposal-ownthedoge.com
Prompt: Create a script to calculate the donation impact of merchandise sales from the Wow by Doge brand, specifically tracking contributions to Save the Children.
Generated: DETERMINISTIC_eb70b8dad5af5352
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# donation_impact_tracker.py

"""
Tracks the donation impact of merchandise sales from Wow by Doge brand,
specifically contributions to Save the Children.
"""

import logging
from dataclasses import dataclass
from typing import List

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@dataclass
class MerchandiseSale:
    """Represents a single merchandise sale."""
    sale_id: int
    product_name: str
    sale_price: float
    donation_percentage: float  # percentage of sale price donated

class DonationImpactTracker:
    """Tracks donation impact of merchandise sales."""

    def __init__(self):
        self.total_donations = 0.0
        self.sales_data = []

    def add_sale(self, sale: MerchandiseSale):
        """Adds a merchandise sale to the tracker."""
        self.sales_data.append(sale)
        donation_amount = sale.sale_price * (sale.donation_percentage / 100)
        self.total_donations += donation_amount
        logging.info(f"Added sale: {sale.product_name} - Donation: ${donation_amount:.2f}")

    def get_total_donations(self) -> float:
        """Returns the total donations tracked."""
        return self.total_donations

    def get_sales_data(self) -> List[MerchandiseSale]:
        """Returns a list of all sales data."""
        return self.sales_data

def load_sales_data(file_path: str) -> List[MerchandiseSale]:
    """
    Loads sales data from a CSV file.

    Args:
    file_path (str): Path to the CSV file.

    Returns:
    List[MerchandiseSale]: A list of MerchandiseSale objects.

    Raises:
    FileNotFoundError: If the file does not exist.
    Exception: If there's an error parsing the file.
    """
    try:
        sales_data = []
        with open(file_path, 'r') as file:
            # Assuming CSV format: sale_id,product_name,sale_price,donation_percentage
            for line in file.readlines()[1:]:  # Skip header
                sale_id, product_name, sale_price, donation_percentage = line.strip().split(',')
                sales_data.append(MerchandiseSale(
                    int(sale_id),
                    product_name,
                    float(sale_price),
                    float(donation_percentage)
                ))
        return sales_data
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        raise
    except Exception as e:
        logging.error(f"Error loading sales data: {e}")
        raise

def main():
    tracker = DonationImpactTracker()
    try:
        sales_data = load_sales_data('sales_data.csv')
        for sale in sales_data:
            tracker.add_sale(sale)
        logging.info(f"Total donations: ${tracker.get_total_donations():.2f}")
        # Optionally, save the sales data and total donations to a database or file
    except Exception as e:
        logging.error(f"Error tracking donations: {e}")

if __name__ == "__main__":
    main()
```
