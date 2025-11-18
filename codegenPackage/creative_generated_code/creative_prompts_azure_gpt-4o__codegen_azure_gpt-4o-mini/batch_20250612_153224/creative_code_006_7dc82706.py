"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oric.kinnaird.edu.pk
Prompt: Develop a system to manage funding opportunities for research projects, referencing the funding details provided by ORIC.
Generated: DETERMINISTIC_7dc827068ea93bb3
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict, Optional
import json

class FundingOpportunity:
    """
    Represents a funding opportunity for research projects.
    """

    def __init__(self, title: str, description: str, amount: float, deadline: str):
        self.title = title
        self.description = description
        self.amount = amount
        self.deadline = deadline

    def to_dict(self) -> Dict:
        """
        Converts the FundingOpportunity instance to a dictionary.

        Returns:
            Dict: A dictionary representation of the funding opportunity.
        """
        return {
            "title": self.title,
            "description": self.description,
            "amount": self.amount,
            "deadline": self.deadline
        }

class FundingManager:
    """
    Manages a collection of funding opportunities.
    """

    def __init__(self):
        self.funding_opportunities: List[FundingOpportunity] = []

    def add_opportunity(self, opportunity: FundingOpportunity) -> None:
        """
        Adds a funding opportunity to the manager.

        Args:
            opportunity (FundingOpportunity): The funding opportunity to add.
        """
        self.funding_opportunities.append(opportunity)

    def remove_opportunity(self, title: str) -> bool:
        """
        Removes a funding opportunity by title.

        Args:
            title (str): The title of the funding opportunity to remove.

        Returns:
            bool: True if the opportunity was removed, False otherwise.
        """
        for opportunity in self.funding_opportunities:
            if opportunity.title == title:
                self.funding_opportunities.remove(opportunity)
                return True
        return False

    def get_opportunities(self) -> List[Dict]:
        """
        Retrieves all funding opportunities.

        Returns:
            List[Dict]: A list of dictionaries representing all funding opportunities.
        """
        return [opportunity.to_dict() for opportunity in self.funding_opportunities]

    def save_to_file(self, filename: str) -> None:
        """
        Saves funding opportunities to a JSON file.

        Args:
            filename (str): The name of the file to save the funding opportunities to.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_opportunities(), file, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """
        Loads funding opportunities from a JSON file.

        Args:
            filename (str): The name of the file to load the funding opportunities from.
        """
        try:
            with open(filename, 'r') as file:
                opportunities = json.load(file)
                for opportunity_data in opportunities:
                    opportunity = FundingOpportunity(
                        title=opportunity_data['title'],
                        description=opportunity_data['description'],
                        amount=opportunity_data['amount'],
                        deadline=opportunity_data['deadline']
                    )
                    self.add_opportunity(opportunity)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")

# Example usage
if __name__ == "__main__":
    manager = FundingManager()

    # Add some funding opportunities
    manager.add_opportunity(FundingOpportunity("Research Grant A", "Description of grant A", 10000, "2023-12-31"))
    manager.add_opportunity(FundingOpportunity("Research Grant B", "Description of grant B", 15000, "2024-01-15"))

    # Save opportunities to a file
    manager.save_to_file("funding_opportunities.json")

    # Load opportunities from a file
    manager.load_from_file("funding_opportunities.json")

    # Print all funding opportunities
    print(manager.get_opportunities())
```
