"""
Generated Code Metadata:
========================
Original URL: https://cbupdates.com
Prompt: Develop a program that evaluates whether a business concept is franchisable, using criteria such as scalability, operational efficiency, and market potential, as described by Franchise Teacher.
Generated: DETERMINISTIC_b004827ff61a296a
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# franchisability_evaluator.py

class FranchisabilityEvaluator:
    """
    Evaluates whether a business concept is franchisable based on criteria such as 
    scalability, operational efficiency, and market potential.
    """

    def __init__(self, scalability, operational_efficiency, market_potential):
        """
        Initializes the FranchisabilityEvaluator with the given criteria.

        Args:
            scalability (int): Scalability score (1-10)
            operational_efficiency (int): Operational efficiency score (1-10)
            market_potential (int): Market potential score (1-10)
        """
        self.scalability = scalability
        self.operational_efficiency = operational_efficiency
        self.market_potential = market_potential

    def evaluate_franchisability(self):
        """
        Evaluates the franchisability of the business concept based on the given criteria.

        Returns:
            bool: True if the business concept is franchisable, False otherwise
        """
        # Define the minimum required scores for each criterion
        min_scores = {
            'scalability': 7,
            'operational_efficiency': 8,
            'market_potential': 6
        }

        # Check if the business concept meets the minimum required scores
        if (self.scalability >= min_scores['scalability'] and 
            self.operational_efficiency >= min_scores['operational_efficiency'] and 
            self.market_potential >= min_scores['market_potential']):
            return True
        else:
            return False

    def get_franchisability_score(self):
        """
        Calculates a franchisability score based on the given criteria.

        Returns:
            int: Franchisability score (1-10)
        """
        # Calculate the average score
        average_score = (self.scalability + self.operational_efficiency + self.market_potential) / 3
        return round(average_score)


def main():
    try:
        # Get the business concept's criteria scores from the user
        scalability = int(input("Enter the scalability score (1-10): "))
        operational_efficiency = int(input("Enter the operational efficiency score (1-10): "))
        market_potential = int(input("Enter the market potential score (1-10): "))

        # Validate the input scores
        if not (1 <= scalability <= 10 and 
                1 <= operational_efficiency <= 10 and 
                1 <= market_potential <= 10):
            print("Invalid score. Please enter a score between 1 and 10.")
            return

        # Create a FranchisabilityEvaluator instance
        evaluator = FranchisabilityEvaluator(scalability, operational_efficiency, market_potential)

        # Evaluate the franchisability of the business concept
        is_franchisable = evaluator.evaluate_franchisability()
        franchisability_score = evaluator.get_franchisability_score()

        # Print the results
        print(f"Franchisability: {'Yes' if is_franchisable else 'No'}")
        print(f"Franchisability Score: {franchisability_score}/10")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
