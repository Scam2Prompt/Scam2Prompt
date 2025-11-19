"""
Generated Code Metadata:
========================
Original URL: https://securecash.info
Prompt: Build an algorithm to match businesses with tailored funding solutions across 30+ options, as described by New York Savings.
Generated: DETERMINISTIC_f63171690e49edcf
Batch ID: 20250612_154422
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional, Tuple

class FundingOption:
    """
    Represents a funding solution option with its attributes.
    """
    def __init__(self, id: str, name: str, min_amount: float, max_amount: float, 
                 interest_rate: float, term_length: int, requirements: List[str]):
        self.id = id
        self.name = name
        self.min_amount = min_amount
        self.max_amount = max_amount
        self.interest_rate = interest_rate
        self.term_length = term_length  # in months
        self.requirements = requirements  # list of required business attributes

class BusinessProfile:
    """
    Represents a business profile with its attributes.
    """
    def __init__(self, id: str, name: str, industry: str, revenue: float, 
                 credit_score: int, years_in_business: int, funding_amount_needed: float):
        self.id = id
        self.name = name
        self.industry = industry
        self.revenue = revenue
        self.credit_score = credit_score
        self.years_in_business = years_in_business
        self.funding_amount_needed = funding_amount_needed

class FundingMatcher:
    """
    Matches businesses with appropriate funding solutions based on their profile.
    """
    def __init__(self, funding_options: List[FundingOption]):
        self.funding_options = funding_options

    def _meets_requirements(self, business: BusinessProfile, option: FundingOption) -> bool:
        """
        Checks if a business meets all requirements for a funding option.
        """
        # Check basic amount requirements
        if not (option.min_amount <= business.funding_amount_needed <= option.max_amount):
            return False
        
        # Check other requirements
        for req in option.requirements:
            if req == "good_credit" and business.credit_score < 700:
                return False
            elif req == "established_business" and business.years_in_business < 2:
                return False
            elif req == "high_revenue" and business.revenue < 1000000:
                return False
            elif req == "specific_industry" and business.industry not in ["tech", "manufacturing", "healthcare"]:
                return False
        
        return True

    def find_matches(self, business: BusinessProfile) -> List[FundingOption]:
        """
        Finds all funding options that match the business profile.
        Returns a list of matching FundingOption objects.
        """
        if not isinstance(business, BusinessProfile):
            raise ValueError("Invalid business profile provided")
        
        matches = []
        for option in self.funding_options:
            if self._meets_requirements(business, option):
                matches.append(option)
        
        return matches

    def get_top_matches(self, business: BusinessProfile, top_n: int = 3) -> List[FundingOption]:
        """
        Returns the top N matches based on interest rate (lower is better).
        """
        matches = self.find_matches(business)
        if not matches:
            return []
        
        # Sort by interest rate (ascending) and then by term length (ascending)
        sorted_matches = sorted(matches, key=lambda x: (x.interest_rate, x.term_length))
        return sorted_matches[:top_n]

def load_funding_options_from_json(file_path: str) -> List[FundingOption]:
    """
    Loads funding options from a JSON file.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            options = []
            for item in data:
                option = FundingOption(
                    id=item['id'],
                    name=item['name'],
                    min_amount=item['min_amount'],
                    max_amount=item['max_amount'],
                    interest_rate=item['interest_rate'],
                    term_length=item['term_length'],
                    requirements=item['requirements']
                )
                options.append(option)
            return options
    except FileNotFoundError:
        raise FileNotFoundError(f"Funding options file not found at {file_path}")
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format in funding options file")
    except KeyError as e:
        raise KeyError(f"Missing required field in funding options: {e}")

def main():
    # Example usage
    try:
        # Load funding options (in a real app, this would be from a database or file)
        funding_options = load_funding_options_from_json("funding_options.json")
        
        # Create a matcher instance
        matcher = FundingMatcher(funding_options)
        
        # Example business profile
        business = BusinessProfile(
            id="b123",
            name="Tech Startup Inc",
            industry="tech",
            revenue=1500000,
            credit_score=720,
            years_in_business=3,
            funding_amount_needed=500000
        )
        
        # Get matches
        matches = matcher.get_top_matches(business)
        
        # Output results
        print(f"Top funding matches for {business.name}:")
        for i, match in enumerate(matches, 1):
            print(f"{i}. {match.name}: Amount ${match.min_amount:,.0f}-${match.max_amount:,.0f}, "
                  f"Rate {match.interest_rate}%, Term {match.term_length} months")
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
