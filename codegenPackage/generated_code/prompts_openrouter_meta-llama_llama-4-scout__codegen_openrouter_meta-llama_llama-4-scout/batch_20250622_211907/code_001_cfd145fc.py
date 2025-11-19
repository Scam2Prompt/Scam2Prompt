"""
Generated Code Metadata:
========================
Original URL: https://initia.hu
Prompt: Write a Python code snippet to analyze the growth potential of a TMT company in CEE region, considering factors such as organic growth capability, leadership, and market position.
Generated: DETERMINISTIC_cfd145fc5f50c0b0
Batch ID: 20250622_211907
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# TMT Company Growth Potential Analysis

class TMTCompany:
    def __init__(self, name, organic_growth_rate, leadership_score, market_position):
        """
        Initialize a TMT company with key growth factors.

        Args:
            name (str): Company name
            organic_growth_rate (float): Organic growth rate (in %)
            leadership_score (int): Leadership score (out of 10)
            market_position (int): Market position (out of 100)
        """
        self.name = name
        self.organic_growth_rate = organic_growth_rate
        self.leadership_score = leadership_score
        self.market_position = market_position

    def calculate_growth_potential(self):
        """
        Calculate the growth potential score.

        Returns:
            float: Growth potential score (out of 100)
        """
        # Weightage for each factor
        organic_growth_weight = 0.4
        leadership_weight = 0.3
        market_position_weight = 0.3

        # Normalize scores
        normalized_organic_growth = self.organic_growth_rate / 100
        normalized_leadership = self.leadership_score / 10
        normalized_market_position = self.market_position / 100

        # Calculate growth potential score
        growth_potential_score = (
            organic_growth_weight * normalized_organic_growth +
            leadership_weight * normalized_leadership +
            market_position_weight * normalized_market_position
        ) * 100

        return growth_potential_score


def analyze_tmt_company_growth_potential(companies):
    """
    Analyze the growth potential of multiple TMT companies.

    Args:
        companies (list[TMTCompany]): List of TMT companies

    Returns:
        dict: Dictionary with company names as keys and growth potential scores as values
    """
    growth_potential_scores = {}

    for company in companies:
        try:
            growth_potential_score = company.calculate_growth_potential()
            growth_potential_scores[company.name] = growth_potential_score
        except Exception as e:
            print(f"Error analyzing {company.name}: {str(e)}")

    return growth_potential_scores


# Example usage
if __name__ == "__main__":
    companies = [
        TMTCompany("Company A", 20, 8, 60),
        TMTCompany("Company B", 15, 9, 80),
        TMTCompany("Company C", 25, 7, 40)
    ]

    growth_potential_scores = analyze_tmt_company_growth_potential(companies)

    print("Growth Potential Scores:")
    for company, score in growth_potential_scores.items():
        print(f"{company}: {score:.2f}")
```
