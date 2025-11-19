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

class PromotionalCampaign:
    """
    A class to design a promotional souvenir campaign for a company launch.
    Includes budget planning and product recommendations based on branding guidelines.
    """

    def __init__(self, company_name, branding_guidelines, budget):
        """
        Initialize the campaign with company details, branding guidelines, and budget.

        :param company_name: Name of the company launching the campaign.
        :param branding_guidelines: Dictionary containing branding guidelines (e.g., colors, logo, etc.).
        :param budget: Total budget allocated for the campaign.
        """
        self.company_name = company_name
        self.branding_guidelines = branding_guidelines
        self.budget = budget
        self.products = []

    def recommend_products(self):
        """
        Recommend promotional products based on branding guidelines and budget.
        """
        # Example product recommendations based on branding guidelines
        self.products = [
            {
                "name": "Custom T-Shirts",
                "unit_price": 10.0,
                "quantity": int(self.budget * 0.4 / 10.0),  # Allocate 40% of budget
                "branding": self.branding_guidelines.get("logo", "Default Logo"),
            },
            {
                "name": "Branded Mugs",
                "unit_price": 5.0,
                "quantity": int(self.budget * 0.3 / 5.0),  # Allocate 30% of budget
                "branding": self.branding_guidelines.get("colors", "Default Colors"),
            },
            {
                "name": "Keychains",
                "unit_price": 2.0,
                "quantity": int(self.budget * 0.2 / 2.0),  # Allocate 20% of budget
                "branding": self.branding_guidelines.get("tagline", "Default Tagline"),
            },
            {
                "name": "Stickers",
                "unit_price": 0.5,
                "quantity": int(self.budget * 0.1 / 0.5),  # Allocate 10% of budget
                "branding": self.branding_guidelines.get("colors", "Default Colors"),
            },
        ]

    def generate_budget_plan(self):
        """
        Generate a detailed budget plan for the campaign.

        :return: Dictionary containing the budget plan.
        """
        budget_plan = {
            "total_budget": self.budget,
            "products": [],
        }

        for product in self.products:
            total_cost = product["unit_price"] * product["quantity"]
            budget_plan["products"].append({
                "name": product["name"],
                "unit_price": product["unit_price"],
                "quantity": product["quantity"],
                "total_cost": total_cost,
                "branding": product["branding"],
            })

        return budget_plan

    def save_campaign_to_file(self, filename="campaign.json"):
        """
        Save the campaign details to a JSON file.

        :param filename: Name of the file to save the campaign details.
        """
        try:
            campaign_data = {
                "company_name": self.company_name,
                "branding_guidelines": self.branding_guidelines,
                "budget": self.budget,
                "products": self.products,
            }
            with open(filename, "w") as file:
                json.dump(campaign_data, file, indent=4)
            print(f"Campaign details saved to {filename}")
        except Exception as e:
            print(f"Error saving campaign to file: {e}")

# Example usage
if __name__ == "__main__":
    # Define company details and branding guidelines
    company_name = "Tech Innovators Inc."
    branding_guidelines = {
        "logo": "Tech Innovators Logo",
        "colors": "Blue and White",
        "tagline": "Innovating the Future",
    }
    budget = 5000  # Total budget for the campaign

    # Create a promotional campaign
    campaign = PromotionalCampaign(company_name, branding_guidelines, budget)

    # Recommend products and generate budget plan
    campaign.recommend_products()
    budget_plan = campaign.generate_budget_plan()

    # Print the budget plan
    print("Budget Plan:")
    print(json.dumps(budget_plan, indent=4))

    # Save campaign details to a file
    campaign.save_campaign_to_file()
```
