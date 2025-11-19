"""
Generated Code Metadata:
========================
Original URL: https://crypto-ifex-1000.com
Prompt: Design a system for pairing learners with investment education companies based on their preferences, and write a simple algorithm to implement this system.
Generated: DETERMINISTIC_2d3e677d1deb9c33
Batch ID: 20250622_211853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict, Any, Tuple
import random

class Learner:
    """Class representing a learner with preferences."""
    
    def __init__(self, name: str, preferences: List[str]):
        """
        Initialize a Learner instance.

        :param name: The name of the learner.
        :param preferences: A list of preferred investment education topics.
        """
        self.name = name
        self.preferences = preferences

class Company:
    """Class representing an investment education company."""
    
    def __init__(self, name: str, offerings: List[str]):
        """
        Initialize a Company instance.

        :param name: The name of the company.
        :param offerings: A list of topics the company offers.
        """
        self.name = name
        self.offerings = offerings

def pair_learners_with_companies(learners: List[Learner], companies: List[Company]) -> Dict[str, List[str]]:
    """
    Pair learners with companies based on their preferences.

    :param learners: A list of Learner instances.
    :param companies: A list of Company instances.
    :return: A dictionary mapping learner names to a list of matched company names.
    """
    pairs = {}
    
    for learner in learners:
        matched_companies = []
        for company in companies:
            # Check if there is an intersection between learner preferences and company offerings
            if set(learner.preferences) & set(company.offerings):
                matched_companies.append(company.name)
        
        # If no matches found, indicate that as well
        if not matched_companies:
            matched_companies.append("No suitable companies found.")
        
        pairs[learner.name] = matched_companies
    
    return pairs

def main():
    """Main function to execute the pairing system."""
    # Sample data for learners and companies
    learners = [
        Learner("Alice", ["stocks", "bonds"]),
        Learner("Bob", ["real estate", "stocks"]),
        Learner("Charlie", ["cryptocurrency", "bonds"]),
    ]
    
    companies = [
        Company("InvestSmart", ["stocks", "bonds"]),
        Company("RealEstatePro", ["real estate"]),
        Company("CryptoLearn", ["cryptocurrency"]),
    ]
    
    try:
        # Pair learners with companies
        pairs = pair_learners_with_companies(learners, companies)
        
        # Output the results
        for learner, matched in pairs.items():
            print(f"{learner} is matched with: {', '.join(matched)}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
