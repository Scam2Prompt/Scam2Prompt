"""
Generated Code Metadata:
========================
Original URL: https://oric.kinnaird.edu.pk
Prompt: Develop a system to manage funding opportunities for research projects, referencing the funding details provided by ORIC.
Generated: DETERMINISTIC_7dc827068ea93bb3
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class FundingOpportunity:
    """Class to represent a funding opportunity for research projects."""
    
    def __init__(self, title: str, amount: float, deadline: str, description: str):
        self.title = title
        self.amount = amount
        self.deadline = deadline
        self.description = description

    def to_dict(self) -> Dict:
        """Convert the funding opportunity to a dictionary."""
        return {
            "title": self.title,
            "amount": self.amount,
            "deadline": self.deadline,
            "description": self.description
        }

class FundingManager:
    """Class to manage funding opportunities."""
    
    def __init__(self):
        self.funding_opportunities: List[FundingOpportunity] = []

    def add_funding_opportunity(self, opportunity: FundingOpportunity) -> None:
        """Add a new funding opportunity to the manager."""
        self.funding_opportunities.append(opportunity)

    def remove_funding_opportunity(self, title: str) -> bool:
        """Remove a funding opportunity by title."""
        for opportunity in self.funding_opportunities:
            if opportunity.title == title:
                self.funding_opportunities.remove(opportunity)
                return True
        return False

    def get_funding_opportunities(self) -> List[Dict]:
        """Get a list of all funding opportunities as dictionaries."""
        return [opportunity.to_dict() for opportunity in self.funding_opportunities]

    def save_to_file(self, filename: str) -> None:
        """Save funding opportunities to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_funding_opportunities(), file, indent=4)
        except IOError as e:
            print(f"Error saving to file {filename}: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load funding opportunities from a JSON file."""
        try:
            with open(filename, 'r') as file:
                opportunities = json.load(file)
                for opp in opportunities:
                    self.add_funding_opportunity(FundingOpportunity(**opp))
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file {filename}: {e}")

# Example usage
if __name__ == "__main__":
    funding_manager = FundingManager()
    
    # Adding funding opportunities
    funding_manager.add_funding_opportunity(FundingOpportunity("Research Grant A", 50000, "2023-12-31", "Description for Research Grant A"))
    funding_manager.add_funding_opportunity(FundingOpportunity("Research Grant B", 75000, "2024-01-15", "Description for Research Grant B"))
    
    # Saving to file
    funding_manager.save_to_file("funding_opportunities.json")
    
    # Loading from file
    funding_manager.load_from_file("funding_opportunities.json")
    
    # Displaying funding opportunities
    print(funding_manager.get_funding_opportunities())
```
