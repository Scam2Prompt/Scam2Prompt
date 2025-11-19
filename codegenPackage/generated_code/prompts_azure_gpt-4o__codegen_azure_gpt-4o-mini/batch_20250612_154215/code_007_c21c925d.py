"""
Generated Code Metadata:
========================
Original URL: https://adelanto.cl
Prompt: Provide a Python example of an intermediary financial service that connects SMEs with lenders for short, medium, and long-term credit, as described on Adelanto.cl.
Generated: DETERMINISTIC_c21c925d3f0f5064
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any, Optional

class SME:
    """Class representing a Small and Medium-sized Enterprise (SME)."""
    
    def __init__(self, name: str, credit_score: int, requested_amount: float, term: str):
        self.name = name
        self.credit_score = credit_score
        self.requested_amount = requested_amount
        self.term = term  # 'short', 'medium', 'long'

    def to_dict(self) -> Dict[str, Any]:
        """Convert SME instance to dictionary."""
        return {
            "name": self.name,
            "credit_score": self.credit_score,
            "requested_amount": self.requested_amount,
            "term": self.term
        }

class Lender:
    """Class representing a lender."""
    
    def __init__(self, name: str, max_amount: float, min_credit_score: int, term_options: List[str]):
        self.name = name
        self.max_amount = max_amount
        self.min_credit_score = min_credit_score
        self.term_options = term_options

    def to_dict(self) -> Dict[str, Any]:
        """Convert Lender instance to dictionary."""
        return {
            "name": self.name,
            "max_amount": self.max_amount,
            "min_credit_score": self.min_credit_score,
            "term_options": self.term_options
        }

class FinancialService:
    """Class representing the intermediary financial service."""
    
    def __init__(self):
        self.smes: List[SME] = []
        self.lenders: List[Lender] = []

    def add_sme(self, sme: SME) -> None:
        """Add an SME to the service."""
        self.smes.append(sme)

    def add_lender(self, lender: Lender) -> None:
        """Add a lender to the service."""
        self.lenders.append(lender)

    def match_smes_to_lenders(self) -> Dict[str, List[str]]:
        """Match SMEs to suitable lenders based on their criteria."""
        matches = {}
        for sme in self.smes:
            suitable_lenders = []
            for lender in self.lenders:
                if (sme.requested_amount <= lender.max_amount and
                        sme.credit_score >= lender.min_credit_score and
                        sme.term in lender.term_options):
                    suitable_lenders.append(lender.name)
            matches[sme.name] = suitable_lenders
        return matches

    def save_matches_to_file(self, matches: Dict[str, List[str]], filename: str) -> None:
        """Save the matches to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(matches, file, indent=4)
        except IOError as e:
            print(f"Error saving matches to file: {e}")

# Example usage
if __name__ == "__main__":
    # Create financial service instance
    service = FinancialService()

    # Add SMEs
    service.add_sme(SME("SME A", 700, 50000, "short"))
    service.add_sme(SME("SME B", 650, 30000, "medium"))

    # Add Lenders
    service.add_lender(Lender("Lender 1", 60000, 680, ["short", "medium"]))
    service.add_lender(Lender("Lender 2", 40000, 640, ["medium", "long"]))

    # Match SMEs to lenders
    matches = service.match_smes_to_lenders()
    print("Matches found:", matches)

    # Save matches to a file
    service.save_matches_to_file(matches, "matches.json")
```
