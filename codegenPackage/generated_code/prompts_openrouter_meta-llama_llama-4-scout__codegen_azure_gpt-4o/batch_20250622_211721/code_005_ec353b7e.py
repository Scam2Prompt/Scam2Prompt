"""
Generated Code Metadata:
========================
Original URL: https://singularity-finance.pages.dev
Prompt: "Develop a data ownership model for contributors to the AI economy on Singularity Finance, enabling them to benefit from yield generated through data usage."
Generated: DETERMINISTIC_ec353b7e0803b249
Batch ID: 20250622_211721
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import datetime
from typing import Dict, List

class Contributor:
    """
    Represents a contributor in the AI economy.
    Each contributor has a unique ID, name, and a share of ownership in the data pool.
    """
    def __init__(self, contributor_id: str, name: str, ownership_share: float):
        """
        Initialize a Contributor object.

        :param contributor_id: Unique identifier for the contributor
        :param name: Name of the contributor
        :param ownership_share: Percentage share of ownership in the data pool (0-100)
        """
        if ownership_share < 0 or ownership_share > 100:
            raise ValueError("Ownership share must be between 0 and 100.")
        
        self.contributor_id = contributor_id
        self.name = name
        self.ownership_share = ownership_share

class DataOwnershipModel:
    """
    Represents the data ownership model for contributors.
    Tracks contributors and calculates yield distribution based on ownership shares.
    """
    def __init__(self):
        """
        Initialize the DataOwnershipModel with an empty list of contributors.
        """
        self.contributors: List[Contributor] = []
        self.total_yield_generated: float = 0.0

    def add_contributor(self, contributor: Contributor):
        """
        Add a new contributor to the model.

        :param contributor: Contributor object to be added
        """
        self.contributors.append(contributor)

    def calculate_yield_distribution(self, total_yield: float) -> Dict[str, float]:
        """
        Calculate the yield distribution for each contributor based on their ownership share.

        :param total_yield: Total yield generated through data usage
        :return: Dictionary mapping contributor IDs to their yield amounts
        """
        if total_yield < 0:
            raise ValueError("Total yield must be non-negative.")
        
        self.total_yield_generated += total_yield
        yield_distribution = {}
        
        for contributor in self.contributors:
            yield_amount = (contributor.ownership_share / 100) * total_yield
            yield_distribution[contributor.contributor_id] = yield_amount
        
        return yield_distribution

    def get_contributor_summary(self) -> List[Dict[str, str]]:
        """
        Get a summary of all contributors and their ownership shares.

        :return: List of dictionaries containing contributor details
        """
        summary = []
        for contributor in self.contributors:
            summary.append({
                "Contributor ID": contributor.contributor_id,
                "Name": contributor.name,
                "Ownership Share (%)": f"{contributor.ownership_share:.2f}"
            })
        return summary

    def get_total_yield_generated(self) -> float:
        """
        Get the total yield generated so far.

        :return: Total yield generated
        """
        return self.total_yield_generated

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the data ownership model
        model = DataOwnershipModel()

        # Add contributors
        model.add_contributor(Contributor("C001", "Alice", 40.0))
        model.add_contributor(Contributor("C002", "Bob", 30.0))
        model.add_contributor(Contributor("C003", "Charlie", 30.0))

        # Generate yield and calculate distribution
        total_yield = 1000.0  # Example yield generated
        distribution = model.calculate_yield_distribution(total_yield)

        # Print yield distribution
        print("Yield Distribution:")
        for contributor_id, yield_amount in distribution.items():
            print(f"Contributor ID: {contributor_id}, Yield Amount: ${yield_amount:.2f}")

        # Print contributor summary
        print("\nContributor Summary:")
        for summary in model.get_contributor_summary():
            print(summary)

        # Print total yield generated
        print(f"\nTotal Yield Generated: ${model.get_total_yield_generated():.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
