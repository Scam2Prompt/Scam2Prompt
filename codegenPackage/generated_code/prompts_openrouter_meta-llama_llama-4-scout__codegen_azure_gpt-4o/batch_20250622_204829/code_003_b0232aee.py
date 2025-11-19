"""
Generated Code Metadata:
========================
Original URL: https://camelot.netlify.app
Prompt: "Compare and contrast the features of fix and flip loans, bridge loans, and rental loans offered by Appak Capital, and recommend which loan product would be best suited for a real estate investor with a specific project goal."
Generated: DETERMINISTIC_b0232aeeb7803f03
Batch ID: 20250622_204829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import json

# Define a class to represent loan products
class LoanProduct:
    def __init__(self, name, features, suitability):
        """
        Initialize a LoanProduct instance.

        :param name: Name of the loan product
        :param features: Dictionary of features for the loan product
        :param suitability: Description of suitability for specific project goals
        """
        self.name = name
        self.features = features
        self.suitability = suitability

    def compare_features(self, other):
        """
        Compare features of this loan product with another loan product.

        :param other: Another LoanProduct instance
        :return: Dictionary of feature comparisons
        """
        comparison = {}
        for feature in self.features:
            if feature in other.features:
                comparison[feature] = {
                    "self": self.features[feature],
                    "other": other.features[feature]
                }
        return comparison

# Define a function to recommend the best loan product
def recommend_loan_product(project_goal, loan_products):
    """
    Recommend the best loan product based on the project goal.

    :param project_goal: Description of the investor's project goal
    :param loan_products: List of LoanProduct instances
    :return: Recommended LoanProduct instance
    """
    for loan in loan_products:
        if project_goal.lower() in loan.suitability.lower():
            return loan
    return None

# Define loan products offered by Appak Capital
fix_and_flip_loan = LoanProduct(
    name="Fix and Flip Loan",
    features={
        "interest_rate": "8-12%",
        "term_length": "6-18 months",
        "purpose": "Short-term financing for property renovations and resale"
    },
    suitability="Best for investors looking to renovate and quickly resell properties."
)

bridge_loan = LoanProduct(
    name="Bridge Loan",
    features={
        "interest_rate": "7-10%",
        "term_length": "6-24 months",
        "purpose": "Temporary financing for property acquisition or transition"
    },
    suitability="Ideal for investors needing short-term funds to bridge gaps between transactions."
)

rental_loan = LoanProduct(
    name="Rental Loan",
    features={
        "interest_rate": "5-8%",
        "term_length": "5-30 years",
        "purpose": "Long-term financing for rental property investments"
    },
    suitability="Perfect for investors aiming to build a portfolio of income-generating rental properties."
)

# List of loan products
loan_products = [fix_and_flip_loan, bridge_loan, rental_loan]

# Example project goal
project_goal = "Build a portfolio of income-generating rental properties"

# Recommend the best loan product
recommended_loan = recommend_loan_product(project_goal, loan_products)

# Output the recommendation
if recommended_loan:
    print("Recommended Loan Product:")
    print(json.dumps({
        "name": recommended_loan.name,
        "features": recommended_loan.features,
        "suitability": recommended_loan.suitability
    }, indent=4))
else:
    print("No suitable loan product found for the given project goal.")
```
