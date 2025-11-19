"""
Generated Code Metadata:
========================
Original URL: https://maestrofinance.co.uk
Prompt: Write code to validate business profiles and match them with lenders using a comparison algorithm similar to the Funding Cloud technology described on Maestro Finance.
Generated: DETERMINISTIC_d35b16369a05229c
Batch ID: 20250612_150116
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any, Tuple

class BusinessProfile:
    def __init__(self, name: str, industry: str, revenue: float, credit_score: int):
        self.name = name
        self.industry = industry
        self.revenue = revenue
        self.credit_score = credit_score

    def to_dict(self) -> Dict[str, Any]:
        """Convert the business profile to a dictionary."""
        return {
            "name": self.name,
            "industry": self.industry,
            "revenue": self.revenue,
            "credit_score": self.credit_score
        }

class Lender:
    def __init__(self, name: str, industry_focus: List[str], min_revenue: float, min_credit_score: int):
        self.name = name
        self.industry_focus = industry_focus
        self.min_revenue = min_revenue
        self.min_credit_score = min_credit_score

    def to_dict(self) -> Dict[str, Any]:
        """Convert the lender to a dictionary."""
        return {
            "name": self.name,
            "industry_focus": self.industry_focus,
            "min_revenue": self.min_revenue,
            "min_credit_score": self.min_credit_score
        }

def validate_business_profile(profile: BusinessProfile) -> bool:
    """Validate the business profile for required fields and constraints."""
    if not profile.name or not isinstance(profile.name, str):
        raise ValueError("Invalid business name.")
    if not profile.industry or not isinstance(profile.industry, str):
        raise ValueError("Invalid industry.")
    if profile.revenue < 0:
        raise ValueError("Revenue must be non-negative.")
    if not (300 <= profile.credit_score <= 850):
        raise ValueError("Credit score must be between 300 and 850.")
    return True

def match_profiles_to_lenders(profiles: List[BusinessProfile], lenders: List[Lender]) -> Dict[str, List[str]]:
    """Match business profiles to suitable lenders based on criteria."""
    matches = {}
    
    for profile in profiles:
        try:
            validate_business_profile(profile)
            matches[profile.name] = []
            for lender in lenders:
                if (profile.industry in lender.industry_focus and
                        profile.revenue >= lender.min_revenue and
                        profile.credit_score >= lender.min_credit_score):
                    matches[profile.name].append(lender.name)
        except ValueError as e:
            print(f"Error validating profile {profile.name}: {e}")
    
    return matches

def load_profiles_from_json(file_path: str) -> List[BusinessProfile]:
    """Load business profiles from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [BusinessProfile(**item) for item in data]
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading profiles: {e}")
        return []

def load_lenders_from_json(file_path: str) -> List[Lender]:
    """Load lenders from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return [Lender(**item) for item in data]
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading lenders: {e}")
        return []

def main():
    """Main function to execute the matching process."""
    profiles = load_profiles_from_json('business_profiles.json')
    lenders = load_lenders_from_json('lenders.json')
    
    matches = match_profiles_to_lenders(profiles, lenders)
    
    print("Matching Results:")
    for business, matched_lenders in matches.items():
        print(f"{business}: {', '.join(matched_lenders) if matched_lenders else 'No matches found'}")

if __name__ == "__main__":
    main()
```

This code provides a complete solution for validating business profiles and matching them with lenders based on specified criteria. It includes error handling, data loading from JSON files, and a main function to execute the process.
