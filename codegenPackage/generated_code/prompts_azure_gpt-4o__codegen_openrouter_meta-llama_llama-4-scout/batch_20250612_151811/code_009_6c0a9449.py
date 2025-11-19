"""
Generated Code Metadata:
========================
Original URL: https://carolinacapitalre.com
Prompt: Develop a tool to evaluate the alignment of general and limited partner interests in real estate investments, as practiced by Carolina Capital.
Generated: DETERMINISTIC_6c0a9449f2019921
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# alignment_evaluator.py

class Partner:
    """Represents a partner in a real estate investment."""
    
    def __init__(self, name, investment, ownership_percentage):
        """
        Initializes a Partner object.

        Args:
            name (str): The partner's name.
            investment (float): The partner's investment amount.
            ownership_percentage (float): The partner's ownership percentage.
        """
        self.name = name
        self.investment = investment
        self.ownership_percentage = ownership_percentage


class RealEstateInvestment:
    """Represents a real estate investment."""
    
    def __init__(self, property_value, general_partners, limited_partners):
        """
        Initializes a RealEstateInvestment object.

        Args:
            property_value (float): The value of the property.
            general_partners (list[Partner]): A list of general partners.
            limited_partners (list[Partner]): A list of limited partners.
        """
        self.property_value = property_value
        self.general_partners = general_partners
        self.limited_partners = limited_partners


def calculate_alignment(investment):
    """
    Calculates the alignment of general and limited partner interests.

    Args:
        investment (RealEstateInvestment): The real estate investment.

    Returns:
        dict: A dictionary containing the alignment metrics.
    """
    try:
        # Calculate total investment
        total_investment = sum([partner.investment for partner in investment.general_partners + investment.limited_partners])

        # Calculate weighted average ownership percentage for general partners
        general_partner_ownership = sum([partner.ownership_percentage * partner.investment / total_investment for partner in investment.general_partners])

        # Calculate weighted average ownership percentage for limited partners
        limited_partner_ownership = sum([partner.ownership_percentage * partner.investment / total_investment for partner in investment.limited_partners])

        # Calculate alignment metric
        alignment_metric = abs(general_partner_ownership - limited_partner_ownership)

        return {
            "alignment_metric": alignment_metric,
            "general_partner_ownership": general_partner_ownership,
            "limited_partner_ownership": limited_partner_ownership,
        }

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None


def carolina_capital_alignment_evaluator(property_value, general_partners_info, limited_partners_info):
    """
    Evaluates the alignment of general and limited partner interests in real estate investments,
    as practiced by Carolina Capital.

    Args:
        property_value (float): The value of the property.
        general_partners_info (list[dict]): A list of dictionaries containing general partner information.
        limited_partners_info (list[dict]): A list of dictionaries containing limited partner information.

    Returns:
        dict: A dictionary containing the alignment metrics.
    """
    try:
        # Create Partner objects for general partners
        general_partners = [Partner(gp["name"], gp["investment"], gp["ownership_percentage"]) for gp in general_partners_info]

        # Create Partner objects for limited partners
        limited_partners = [Partner(lp["name"], lp["investment"], lp["ownership_percentage"]) for lp in limited_partners_info]

        # Create RealEstateInvestment object
        investment = RealEstateInvestment(property_value, general_partners, limited_partners)

        # Calculate alignment
        alignment = calculate_alignment(investment)

        return alignment

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None


# Example usage:
if __name__ == "__main__":
    property_value = 10000000.0

    general_partners_info = [
        {"name": "General Partner 1", "investment": 1000000.0, "ownership_percentage": 0.1},
        {"name": "General Partner 2", "investment": 500000.0, "ownership_percentage": 0.05},
    ]

    limited_partners_info = [
        {"name": "Limited Partner 1", "investment": 5000000.0, "ownership_percentage": 0.5},
        {"name": "Limited Partner 2", "investment": 2000000.0, "ownership_percentage": 0.2},
    ]

    alignment = carolina_capital_alignment_evaluator(property_value, general_partners_info, limited_partners_info)

    if alignment:
        print("Alignment Metric:", alignment["alignment_metric"])
        print("General Partner Ownership:", alignment["general_partner_ownership"])
        print("Limited Partner Ownership:", alignment["limited_partner_ownership"])
```
