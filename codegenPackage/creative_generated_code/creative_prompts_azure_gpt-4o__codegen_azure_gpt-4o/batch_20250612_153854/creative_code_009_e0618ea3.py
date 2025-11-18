"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alghanim-capital.com
Prompt: Create a program that models collaboration and mutual success metrics for investment partnerships, inspired by Alghanim Capital's emphasis on teamwork and stakeholder cooperation.
Generated: DETERMINISTIC_e0618ea3d59ff1cb
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program: Investment Partnership Collaboration Metrics
Description: This Python program models collaboration and mutual success metrics
             for investment partnerships, inspired by teamwork and stakeholder cooperation.
Author: Professional Software Developer
Date: YYYY-MM-DD
"""

# Import necessary modules
import logging
from typing import List, Dict

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class Partner:
    """
    Class to represent an individual investment partner.
    Attributes:
        name (str): Name of the partner.
        contribution (float): Monetary contribution of the partner.
        collaboration_score (float): Collaboration score, measured by mutual cooperation.
    """

    def __init__(self, name: str, contribution: float):
        self.name = name
        self.contribution = contribution
        self.collaboration_score = 0.0


class Partnership:
    """
    Class to represent the investment partnership.
    Attributes:
        partners (List[Partner]): List of Partner objects involved in the partnership.
        success_metric (float): Overall success metric based on contributions and collaboration.
    """

    def __init__(self):
        self.partners: List[Partner] = []
        self.success_metric: float = 0.0

    def add_partner(self, name: str, contribution: float):
        """
        Adds a new partner to the partnership.
        Args:
            name (str): Name of the partner.
            contribution (float): Monetary contribution of the partner.
        """
        try:
            if contribution <= 0:
                raise ValueError("Contribution must be a positive value.")
            new_partner = Partner(name, contribution)
            self.partners.append(new_partner)
            logging.info(f"Partner '{name}' added with contribution: {contribution}")
        except ValueError as e:
            logging.error(f"Error adding partner: {e}")

    def calculate_collaboration_score(self):
        """
        Calculates collaboration scores for all partners based on contributions.
        Collaboration is measured as a percentage of the total contribution.
        """
        try:
            total_contribution = sum(partner.contribution for partner in self.partners)
            if total_contribution == 0:
                raise ValueError("Total contribution cannot be zero.")
            for partner in self.partners:
                partner.collaboration_score = (partner.contribution / total_contribution) * 100
                logging.info(f"Partner '{partner.name}' collaboration score: {partner.collaboration_score:.2f}%")
        except ValueError as e:
            logging.error(f"Error calculating collaboration scores: {e}")

    def calculate_success_metric(self):
        """
        Calculates overall success metric based on partner collaboration scores.
        Success metric is the average collaboration score of all partners.
        """
        try:
            if not self.partners:
                raise ValueError("No partners exist to calculate success metric.")
            self.success_metric = sum(partner.collaboration_score for partner in self.partners) / len(self.partners)
            logging.info(f"Overall success metric: {self.success_metric:.2f}%")
        except ValueError as e:
            logging.error(f"Error calculating success metric: {e}")

    def get_partnership_details(self) -> Dict[str, Dict]:
        """
        Retrieves details of the partnership including partner metrics and overall success.
        Returns:
            Dict[str, Dict]: Partnership details.
        """
        partner_details = {
            partner.name: {
                "Contribution": partner.contribution,
                "Collaboration Score (%)": partner.collaboration_score
            }
            for partner in self.partners
        }
        return {
            "Partners": partner_details,
            "Overall Success Metric (%)": self.success_metric
        }


# Entry point for the program
if __name__ == "__main__":
    # Example usage of the Partnership class
    try:
        partnership = Partnership()
        partnership.add_partner("Alice", 10000)
        partnership.add_partner("Bob", 20000)
        partnership.add_partner("Charlie", 15000)

        partnership.calculate_collaboration_score()
        partnership.calculate_success_metric()

        partnership_details = partnership.get_partnership_details()
        logging.info("Final Partnership Details:")
        for partner, details in partnership_details["Partners"].items():
            logging.info(f"Partner: {partner}, Details: {details}")
        logging.info(f"Overall Success Metric: {partnership_details['Overall Success Metric (%)']}%")
    except Exception as e:
        logging.error(f"Unexpected error occurred: {e}")
```
