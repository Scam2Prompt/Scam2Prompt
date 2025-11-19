"""
Generated Code Metadata:
========================
Original URL: https://kraken-energy.com
Prompt: Write a Python script to evaluate and appraise oil and gas lease offers in Oklahoma, considering factors like location and market value.
Generated: DETERMINISTIC_50743e099fa70d1f
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class LeaseOffer:
    """
    A class to represent an oil and gas lease offer.
    """

    def __init__(self, location, market_value, offer_price):
        """
        Initializes a LeaseOffer instance.

        :param location: str, the location of the lease
        :param market_value: float, the market value of the lease
        :param offer_price: float, the price offered for the lease
        """
        self.location = location
        self.market_value = market_value
        self.offer_price = offer_price

    def evaluate_offer(self):
        """
        Evaluates the lease offer based on market value.

        :return: str, evaluation result
        """
        if self.offer_price < self.market_value:
            return "Offer is below market value."
        elif self.offer_price == self.market_value:
            return "Offer is at market value."
        else:
            return "Offer is above market value."


class LeaseEvaluator:
    """
    A class to evaluate multiple lease offers.
    """

    def __init__(self, offers):
        """
        Initializes a LeaseEvaluator instance.

        :param offers: list of LeaseOffer instances
        """
        self.offers = offers

    def evaluate_all_offers(self):
        """
        Evaluates all lease offers and returns a summary.

        :return: DataFrame, summary of evaluations
        """
        evaluations = []
        for offer in self.offers:
            evaluation = {
                'Location': offer.location,
                'Market Value': offer.market_value,
                'Offer Price': offer.offer_price,
                'Evaluation': offer.evaluate_offer()
            }
            evaluations.append(evaluation)

        return pd.DataFrame(evaluations)


def main():
    """
    Main function to run the lease evaluation.
    """
    try:
        # Sample lease offers
        offers = [
            LeaseOffer("Oklahoma City", 100000, 95000),
            LeaseOffer("Tulsa", 150000, 150000),
            LeaseOffer("Norman", 120000, 130000),
            LeaseOffer("Broken Arrow", 110000, 105000)
        ]

        # Create a LeaseEvaluator instance
        evaluator = LeaseEvaluator(offers)

        # Evaluate all offers
        evaluation_summary = evaluator.evaluate_all_offers()

        # Print the evaluation summary
        print(evaluation_summary)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
