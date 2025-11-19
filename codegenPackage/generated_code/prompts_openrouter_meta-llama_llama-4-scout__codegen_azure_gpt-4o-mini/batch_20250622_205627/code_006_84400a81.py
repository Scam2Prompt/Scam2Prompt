"""
Generated Code Metadata:
========================
Original URL: https://www.merchandiso.com
Prompt: Design a promotional souvenir campaign for a new company launch, including a budget plan and product recommendations, using a company's branding guidelines.
Generated: DETERMINISTIC_84400a81a1f30676
Batch ID: 20250622_205627
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

class SouvenirCampaign:
    def __init__(self, company_name: str, budget: float, branding_guidelines: Dict[str, str]):
        """
        Initialize the SouvenirCampaign with company details and branding guidelines.

        :param company_name: Name of the company launching the campaign
        :param budget: Total budget allocated for the campaign
        :param branding_guidelines: A dictionary containing branding guidelines
        """
        self.company_name = company_name
        self.budget = budget
        self.branding_guidelines = branding_guidelines
        self.products = []

    def add_product(self, product_name: str, cost: float, quantity: int):
        """
        Add a product to the campaign.

        :param product_name: Name of the product
        :param cost: Cost of a single product
        :param quantity: Quantity of the product to be ordered
        """
        total_cost = cost * quantity
        if total_cost > self.budget:
            raise ValueError(f"Cannot add {product_name}: total cost {total_cost} exceeds budget {self.budget}.")
        
        self.products.append({
            'product_name': product_name,
            'cost': cost,
            'quantity': quantity,
            'total_cost': total_cost
        })
        self.budget -= total_cost

    def generate_campaign_report(self) -> Dict[str, List[Dict[str, str]]]:
        """
        Generate a report of the campaign including products and remaining budget.

        :return: A dictionary containing campaign details
        """
        return {
            'company_name': self.company_name,
            'remaining_budget': self.budget,
            'products': self.products
        }

    def save_report_to_json(self, file_path: str):
        """
        Save the campaign report to a JSON file.

        :param file_path: Path to the file where the report will be saved
        """
        report = self.generate_campaign_report()
        try:
            with open(file_path, 'w') as json_file:
                json.dump(report, json_file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to write report to {file_path}: {e}")

# Example usage
if __name__ == "__main__":
    # Define branding guidelines
    branding_guidelines = {
        'color_scheme': 'blue and white',
        'logo': 'company_logo.png',
        'font': 'Arial'
    }

    # Initialize the campaign
    campaign = SouvenirCampaign(company_name="NewCo", budget=1000.0, branding_guidelines=branding_guidelines)

    # Add products to the campaign
    try:
        campaign.add_product(product_name="Branded Mug", cost=5.0, quantity=100)
        campaign.add_product(product_name="T-Shirt", cost=10.0, quantity=50)
        campaign.add_product(product_name="Notebook", cost=3.0, quantity=200)

        # Save the campaign report to a JSON file
        campaign.save_report_to_json("campaign_report.json")
    except ValueError as ve:
        print(f"Error: {ve}")
    except IOError as ioe:
        print(f"Error: {ioe}")
```
