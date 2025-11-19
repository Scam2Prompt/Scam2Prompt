"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://figurefourchampionship.com
Prompt: What are the implications of Figure Four Championship ceasing orders for leather straps and accessories by October 31st, 2024?
Generated: DETERMINISTIC_303d5e95314d6969
Batch ID: 20250612_164040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly! Below is a Python script that analyzes the financial and operational implications of a hypothetical company, "Figure Four Championship," ceasing orders for leather straps and accessories by October 31st, 2024:

```python
import datetime


class BusinessImpactAnalyzer:
    """
    A class to analyze the business implications of ceasing orders for specific products.
    """

    def __init__(self, company_name: str, product_category: str, cutoff_date: datetime.date):
        """
        Initialize the impact analyzer with company details.

        :param company_name: Name of the company ceasing orders.
        :param product_category: Category of products being discontinued.
        :param cutoff_date: Date by which orders will be ceased.
        """
        self.company_name = company_name
        self.product_category = product_category
        self.cutoff_date = cutoff_date

    def calculate_financial_impact(self, annual_revenue: float, revenue_percentage: float) -> float:
        """
        Calculate the financial impact of discontinuing the product category.

        :param annual_revenue: Total annual revenue of the company.
        :param revenue_percentage: Percentage of annual revenue attributed to the discontinued product category.
        :return: Financial loss due to discontinued product category.
        """
        if revenue_percentage < 0 or revenue_percentage > 100:
            raise ValueError("Revenue percentage must be between 0 and 100.")
        return annual_revenue * (revenue_percentage / 100)

    def operational_impact(self, total_employees: int, affected_employees_percentage: float) -> int:
        """
        Calculate the number of employees affected by ceasing orders.

        :param total_employees: Total number of employees in the company.
        :param affected_employees_percentage: Percentage of employees working on the discontinued product category.
        :return: Number of employees impacted.
        """
        if affected_employees_percentage < 0 or affected_employees_percentage > 100:
            raise ValueError("Affected employees percentage must be between 0 and 100.")
        return int(total_employees * (affected_employees_percentage / 100))

    def generate_report(self, annual_revenue: float, revenue_percentage: float, total_employees: int, affected_employees_percentage: float) -> dict:
        """
        Generate a report detailing the financial and operational impacts.

        :param annual_revenue: Total annual revenue of the company.
        :param revenue_percentage: Percentage of annual revenue attributed to the discontinued product category.
        :param total_employees: Total number of employees in the company.
        :param affected_employees_percentage: Percentage of employees working on the discontinued product category.
        :return: A dictionary containing impact details.
        """
        try:
            financial_loss = self.calculate_financial_impact(annual_revenue, revenue_percentage)
            impacted_employees = self.operational_impact(total_employees, affected_employees_percentage)
            return {
                "company_name": self.company_name,
                "product_category": self.product_category,
                "cutoff_date": self.cutoff_date.isoformat(),
                "financial_loss": f"${financial_loss:,.2f}",
                "impacted_employees": impacted_employees
            }
        except ValueError as e:
            return {"error": str(e)}


# Example usage
if __name__ == "__main__":
    # Company information
    company_name = "Figure Four Championship"
    product_category = "Leather Straps and Accessories"
    cutoff_date = datetime.date(2024, 10, 31)

    # Initialize the analyzer
    analyzer = BusinessImpactAnalyzer(company_name, product_category, cutoff_date)

    # Example data
    annual_revenue = 5000000  # $5,000,000
    revenue_percentage = 25.0  # 25% of revenue comes from leather straps/accessories
    total_employees = 200  # Total employees in the company
    affected_employees_percentage = 20.0  # 20% of employees work on leather straps/accessories

    # Generate the impact report
    report = analyzer.generate_report(annual_revenue, revenue_percentage, total_employees, affected_employees_percentage)

    # Print the report
    print("Impact Analysis Report:")
    for key, value in report.items():
        print(f"{key}: {value}")
```

### Code Summary
- **BusinessImpactAnalyzer** class encapsulates the logic for calculating financial and operational impacts.
- Error handling ensures that percentage values are within valid ranges.
- Sample usage generates a report based on hypothetical data and prints the results in a human-readable format.
