"""
Generated Code Metadata:
========================
Original URL: https://hispanicservices.com
Prompt: Generate a sample tax planning checklist for a small business in Georgia, including considerations for state taxes, sales taxes, and property taxes.
Generated: DETERMINISTIC_3f9ee25484161f3a
Batch ID: 20250622_205045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tax_planning_checklist.py

class TaxPlanningChecklist:
    def __init__(self, business_name, business_type, annual_revenue):
        """
        Initialize a TaxPlanningChecklist object.

        Args:
            business_name (str): Name of the business.
            business_type (str): Type of business (e.g., sole proprietorship, partnership, corporation).
            annual_revenue (float): Annual revenue of the business.
        """
        self.business_name = business_name
        self.business_type = business_type
        self.annual_revenue = annual_revenue

    def state_taxes(self):
        """
        Considerations for state taxes in Georgia.

        Returns:
            list: List of state tax considerations.
        """
        state_taxes = [
            "Georgia corporate income tax rate: 5.25%",
            "Georgia individual income tax rate: 1% - 5.25%",
            "Annual state tax filing requirement: Form 1120 (corporations) or Form 1040 (individuals)",
            "Quarterly estimated tax payments: Form 1040-ES (individuals) or Form 1120-W (corporations)"
        ]
        return state_taxes

    def sales_taxes(self):
        """
        Considerations for sales taxes in Georgia.

        Returns:
            list: List of sales tax considerations.
        """
        sales_taxes = [
            "Georgia sales tax rate: 4%",
            "Local sales tax rates vary (0% - 5.9%); average local rate: 3.5%",
            "Combined state and local sales tax rate: 7.4% (avg.)",
            "Monthly sales tax filing requirement: Form ST-3"
        ]
        return sales_taxes

    def property_taxes(self):
        """
        Considerations for property taxes in Georgia.

        Returns:
            list: List of property tax considerations.
        """
        property_taxes = [
            "Property tax rates vary by county; average effective rate: 0.94%",
            "Annual property tax filing requirement: Form 323 (real property) or Form 329 (personal property)",
            "Payment deadlines: typically December 31st or January 1st"
        ]
        return property_taxes

    def generate_checklist(self):
        """
        Generate a sample tax planning checklist.

        Returns:
            dict: Dictionary containing tax planning checklist items.
        """
        checklist = {
            "Business Information": [
                f"Business Name: {self.business_name}",
                f"Business Type: {self.business_type}",
                f"Annual Revenue: ${self.annual_revenue:,.2f}"
            ],
            "State Taxes": self.state_taxes(),
            "Sales Taxes": self.sales_taxes(),
            "Property Taxes": self.property_taxes()
        }
        return checklist


def main():
    try:
        business_name = input("Enter business name: ")
        business_type = input("Enter business type: ")
        annual_revenue = float(input("Enter annual revenue: $"))

        checklist = TaxPlanningChecklist(business_name, business_type, annual_revenue)
        tax_planning_checklist = checklist.generate_checklist()

        print("\nSample Tax Planning Checklist:")
        for category, items in tax_planning_checklist.items():
            print(f"\n{category}:")
            for item in items:
                print(f"- {item}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
