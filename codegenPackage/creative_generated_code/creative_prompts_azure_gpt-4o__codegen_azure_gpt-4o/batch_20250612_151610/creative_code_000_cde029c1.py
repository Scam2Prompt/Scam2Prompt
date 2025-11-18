"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cbupdates.com
Prompt: Write Python code to simulate a franchise-ability review process, including criteria such as market demand, scalability, and profitability, as described by Franchise Teacher's services.
Generated: DETERMINISTIC_cde029c110f8b98a
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class FranchiseReview:
    """
    A class to simulate franchise-ability review process based on key criteria.
    """

    def __init__(self, business_name, market_demand, scalability, profitability):
        """
        Initialize the franchise review process with the required data.

        Parameters:
        - business_name (str): Name of the business under review.
        - market_demand (int): Market demand score (1-10).
        - scalability (int): Scalability score (1-10).
        - profitability (int): Profitability score (1-10).
        """
        self.business_name = business_name
        self.market_demand = market_demand
        self.scalability = scalability
        self.profitability = profitability

    def validate_scores(self):
        """
        Validates that all scores are within the range of 1 to 10.
        Raises ValueError if any score is invalid.
        """
        scores = [self.market_demand, self.scalability, self.profitability]
        if not all(1 <= score <= 10 for score in scores):
            raise ValueError("Scores must be between 1 and 10.")

    def calculate_score(self):
        """
        Calculates the final franchise-ability score based on weighted criteria.
        Weights:
        - Market Demand: 40%
        - Scalability: 30%
        - Profitability: 30%
        
        Returns:
        - float: The franchise-ability score (out of 10).
        """
        return round(
            (self.market_demand * 0.4) +
            (self.scalability * 0.3) +
            (self.profitability * 0.3),
            2
        )

    def assess_franchise_potential(self):
        """
        Assess whether the business is suitable for franchising based on the score.
        
        Returns:
        - str: Recommendation result.
        """
        try:
            # Validate input scores
            self.validate_scores()

            # Calculate franchise-ability score
            score = self.calculate_score()

            # Logging the review process
            logging.info(f"Franchise-ability score for '{self.business_name}': {score}/10")

            # Provide recommendation based on the score
            if score >= 8:
                return f"'{self.business_name}' is highly suitable for franchising."
            elif 5 <= score < 8:
                return f"'{self.business_name}' shows moderate potential for franchising."
            else:
                return f"'{self.business_name}' is currently not suitable for franchising."
        except ValueError as e:
            logging.error(f"Error in franchise review: {e}")
            return "Invalid scores provided. Please use values between 1 and 10."

# Example usage
if __name__ == "__main__":
    # Create a FranchiseReview instance
    business = FranchiseReview("EcoClean Services", market_demand=9, scalability=8, profitability=7)

    # Assess franchise potential
    result = business.assess_franchise_potential()

    # Print the result
    print(result)
```
