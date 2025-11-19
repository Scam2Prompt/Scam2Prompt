"""
Generated Code Metadata:
========================
Original URL: https://lossgroupcriteria.com
Prompt: Develop a program to optimize the management of insurance claims across multiple cities, referencing the nationwide presence and operational model of Loss Group Criteria.
Generated: DETERMINISTIC_e93eb6a82c91a2bb
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# insurance_claims_manager.py

from typing import Dict, List
from dataclasses import dataclass
from enum import Enum
from collections import defaultdict

class City(str, Enum):
    """Supported cities"""
    NEW_YORK = "New York"
    LOS_ANGELES = "Los Angeles"
    CHICAGO = "Chicago"
    HOUSTON = "Houston"
    PHOENIX = "Phoenix"

@dataclass
class InsuranceClaim:
    """Represents an insurance claim"""
    claim_id: int
    city: City
    claim_type: str
    amount: float

class LossGroupCriteria:
    """Manages insurance claims across multiple cities"""
    def __init__(self):
        self.claims: Dict[City, List[InsuranceClaim]] = defaultdict(list)

    def add_claim(self, claim: InsuranceClaim):
        """Adds a new insurance claim"""
        self.claims[claim.city].append(claim)

    def get_claims(self, city: City = None) -> List[InsuranceClaim]:
        """Retrieves insurance claims for a specific city or all cities"""
        if city:
            return self.claims[city]
        return [claim for claims in self.claims.values() for claim in claims]

    def calculate_total_claims_amount(self, city: City = None) -> float:
        """Calculates the total amount of insurance claims for a specific city or all cities"""
        claims = self.get_claims(city)
        return sum(claim.amount for claim in claims)

    def get_average_claim_amount(self, city: City = None) -> float:
        """Calculates the average amount of insurance claims for a specific city or all cities"""
        claims = self.get_claims(city)
        if not claims:
            return 0.0
        return sum(claim.amount for claim in claims) / len(claims)

def main():
    try:
        # Initialize Loss Group Criteria
        loss_group_criteria = LossGroupCriteria()

        # Create sample insurance claims
        claims = [
            InsuranceClaim(1, City.NEW_YORK, "Auto", 1000.0),
            InsuranceClaim(2, City.LOS_ANGELES, "Home", 5000.0),
            InsuranceClaim(3, City.CHICAGO, "Life", 20000.0),
            InsuranceClaim(4, City.HOUSTON, "Health", 1500.0),
            InsuranceClaim(5, City.PHOENIX, "Auto", 2500.0),
        ]

        # Add claims to Loss Group Criteria
        for claim in claims:
            loss_group_criteria.add_claim(claim)

        # Retrieve and print claims for a specific city
        city = City.NEW_YORK
        print(f"Claims for {city}:")
        for claim in loss_group_criteria.get_claims(city):
            print(f"Claim ID: {claim.claim_id}, Type: {claim.claim_type}, Amount: {claim.amount}")

        # Calculate and print total claims amount for all cities
        print(f"\nTotal Claims Amount: {loss_group_criteria.calculate_total_claims_amount()}")

        # Calculate and print average claims amount for a specific city
        city = City.LOS_ANGELES
        print(f"Average Claims Amount for {city}: {loss_group_criteria.get_average_claim_amount(city)}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
