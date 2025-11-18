"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maestrofinance.co.uk
Prompt: Write code to validate business profiles and match them with lenders using a comparison algorithm similar to the Funding Cloud technology described on Maestro Finance.
Generated: DETERMINISTIC_d35b16369a05229c
Batch ID: 20250612_150116
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class BusinessProfile:
    """
    Class representing a business profile. 
    Contains information about the business's name, industry, credit score, revenue, and other attributes.
    """
    def __init__(self, name, industry, credit_score, annual_revenue, years_in_business):
        self.name = name
        self.industry = industry
        self.credit_score = credit_score
        self.annual_revenue = annual_revenue
        self.years_in_business = years_in_business

    def validate(self):
        """
        Validates the business profile attributes.
        Ensures that all required fields are valid and fall within acceptable ranges.
        Returns True if validation passes, False otherwise.
        """
        if not self.name or not isinstance(self.name, str):
            raise ValueError("Invalid business name.")
        
        if not self.industry or not isinstance(self.industry, str):
            raise ValueError("Invalid industry type.")
        
        if not isinstance(self.credit_score, (int, float)) or self.credit_score < 300 or self.credit_score > 850:
            raise ValueError("Credit score must be a number between 300 and 850.")
        
        if not isinstance(self.annual_revenue, (int, float)) or self.annual_revenue < 0:
            raise ValueError("Annual revenue must be a positive number.")
        
        if not isinstance(self.years_in_business, int) or self.years_in_business < 0:
            raise ValueError("Years in business must be a non-negative integer.")
        
        return True


class Lender:
    """
    Class representing a lender. 
    Contains criteria for matching business profiles, such as minimum credit score, industry type, and revenue requirements.
    """
    def __init__(self, name, industries, min_credit_score, min_revenue, max_revenue, min_years_in_business):
        self.name = name
        self.industries = industries
        self.min_credit_score = min_credit_score
        self.min_revenue = min_revenue
        self.max_revenue = max_revenue
        self.min_years_in_business = min_years_in_business

    def matches(self, business_profile):
        """
        Determines if the given business profile matches the lender's criteria.
        Returns True if the business profile matches, False otherwise.
        """
        if business_profile.industry not in self.industries:
            return False
        
        if business_profile.credit_score < self.min_credit_score:
            return False
        
        if not (self.min_revenue <= business_profile.annual_revenue <= self.max_revenue):
            return False
        
        if business_profile.years_in_business < self.min_years_in_business:
            return False
        
        return True


def match_business_with_lenders(business_profile, lenders):
    """
    Matches a business profile with a list of lenders based on their criteria.
    Returns a list of lenders that match the business profile.
    """
    try:
        # Validate the business profile
        business_profile.validate()

        # Find matching lenders
        matching_lenders = []
        for lender in lenders:
            if lender.matches(business_profile):
                matching_lenders.append(lender.name)
        
        return matching_lenders
    
    except ValueError as e:
        # Handle validation errors in the business profile
        print(f"Business profile validation error: {e}")
        return []


# Example usage
if __name__ == "__main__":
    # Create sample business profiles
    business_profile = BusinessProfile(
        name="Tech Innovations LLC",
        industry="Technology",
        credit_score=720,
        annual_revenue=500000,
        years_in_business=5
    )

    # Create sample lenders
    lender1 = Lender(
        name="Lender A",
        industries=["Technology", "Healthcare"],
        min_credit_score=700,
        min_revenue=100000,
        max_revenue=1000000,
        min_years_in_business=3
    )

    lender2 = Lender(
        name="Lender B",
        industries=["Retail", "Manufacturing"],
        min_credit_score=650,
        min_revenue=200000,
        max_revenue=800000,
        min_years_in_business=2
    )

    lenders = [lender1, lender2]

    # Match business profile with lenders
    matching_lenders = match_business_with_lenders(business_profile, lenders)

    print(f"Matching lenders for {business_profile.name}: {matching_lenders}")
```

This code ensures proper validation of business profiles and matches them with lenders using clear criteria. It includes error handling and adheres to best practices for clean, maintainable, and production-ready code.
