"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lossgroupcriteria.com
Prompt: Develop a program to optimize the management of insurance claims across multiple cities, referencing the nationwide presence and operational model of Loss Group Criteria.
Generated: DETERMINISTIC_e93eb6a82c91a2bb
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python program designed to optimize the management of insurance claims across multiple cities:

```python
import logging
from typing import List, Dict

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Claim:
    """
    Represents an individual insurance claim.
    """
    def __init__(self, claim_id: str, city: str, amount: float, status: str):
        """
        Initializes a Claim object.

        :param claim_id: Unique identifier for the claim.
        :param city: The city where the claim originated.
        :param amount: The monetary value of the claim.
        :param status: Status of the claim (e.g., 'Pending', 'Approved', 'Denied').
        """
        self.claim_id = claim_id
        self.city = city
        self.amount = amount
        self.status = status


class InsuranceClaimManager:
    """
    Manages insurance claims across multiple cities.
    """
    def __init__(self):
        """
        Initializes an InsuranceClaimManager object.
        """
        self.claims = []  # List to store all claims

    def add_claim(self, claim: Claim) -> None:
        """
        Adds a new claim to the manager.

        :param claim: A Claim object to add.
        """
        if not isinstance(claim, Claim):
            logging.error("Invalid claim type provided.")
            raise ValueError("Expected a Claim object.")
        self.claims.append(claim)
        logging.info(f"Added claim {claim.claim_id} from {claim.city}, amount: {claim.amount}, status: {claim.status}")

    def get_claims_by_city(self, city: str) -> List[Claim]:
        """
        Retrieves all claims for a specific city.

        :param city: The city to filter claims by.
        :return: List of claims from the specified city.
        """
        return [claim for claim in self.claims if claim.city.lower() == city.lower()]

    def update_claim_status(self, claim_id: str, new_status: str) -> None:
        """
        Updates the status of a claim.

        :param claim_id: Unique identifier of the claim to update.
        :param new_status: New status to set for the claim.
        """
        for claim in self.claims:
            if claim.claim_id == claim_id:
                logging.info(f"Updating status for claim {claim_id} to {new_status}")
                claim.status = new_status
                return
        logging.error(f"Claim with ID {claim_id} not found.")
        raise ValueError(f"Claim with ID {claim_id} does not exist.")

    def get_summary_by_city(self) -> Dict[str, Dict[str, float]]:
        """
        Generates a summary of claims by city.

        :return: Dictionary containing summary data by city.
        """
        summary = {}
        for claim in self.claims:
            if claim.city not in summary:
                summary[claim.city] = {"total_amount": 0, "total_claims": 0}
            summary[claim.city]["total_amount"] += claim.amount
            summary[claim.city]["total_claims"] += 1
        return summary

    def display_summary(self) -> None:
        """
        Displays the summary of claims by city.
        """
        summary = self.get_summary_by_city()
        logging.info("Claims Summary by City:")
        for city, data in summary.items():
            logging.info(f"City: {city}, Total Claims: {data['total_claims']}, Total Amount: ${data['total_amount']:.2f}")


# Example usage of the InsuranceClaimManager
if __name__ == "__main__":
    try:
        # Initialize the claim manager
        manager = InsuranceClaimManager()

        # Add some claims
        manager.add_claim(Claim(claim_id="C001", city="New York", amount=1200.50, status="Pending"))
        manager.add_claim(Claim(claim_id="C002", city="Chicago", amount=800.00, status="Approved"))
        manager.add_claim(Claim(claim_id="C003", city="New York", amount=450.75, status="Denied"))
        manager.add_claim(Claim(claim_id="C004", city="Los Angeles", amount=950.00, status="Pending"))

        # Display summary by city
        manager.display_summary()

        # Update claim status
        manager.update_claim_status(claim_id="C001", new_status="Approved")

        # Get claims for a specific city
        ny_claims = manager.get_claims_by_city("New York")
        logging.info(f"Claims in New York: {[claim.__dict__ for claim in ny_claims]}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```

This program meets all the requested requirements, adheres to programming best practices, and includes comprehensive error handling and documentation through comments.
