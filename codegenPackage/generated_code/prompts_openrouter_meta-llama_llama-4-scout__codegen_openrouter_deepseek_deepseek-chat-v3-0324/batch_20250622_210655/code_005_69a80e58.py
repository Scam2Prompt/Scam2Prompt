"""
Generated Code Metadata:
========================
Original URL: https://avasconcelos.adv.br
Prompt: "Write a Python script to help a company assess its eligibility for tax benefits under the MP 2.199-14/2001 law, considering factors such as location, industry, and revenue."
Generated: DETERMINISTIC_69a80e58051a064b
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from enum import Enum
from typing import Optional, Dict, List

class Industry(Enum):
    MANUFACTURING = "Manufacturing"
    TECHNOLOGY = "Technology"
    AGRICULTURE = "Agriculture"
    CONSTRUCTION = "Construction"
    SERVICES = "Services"
    OTHER = "Other"

class Location(Enum):
    NORTH = "North Region"
    NORTHEAST = "Northeast Region"
    CENTER_WEST = "Center-West Region"
    SOUTHEAST = "Southeast Region"
    SOUTH = "South Region"

class TaxBenefitEligibility:
    """
    Assesses eligibility for tax benefits under MP 2.199-14/2001 law.
    """
    
    def __init__(self):
        # Thresholds and rules based on MP 2.199-14/2001 law
        self.revenue_threshold = 10000000  # 10 million in local currency
        self.eligible_industries = [
            Industry.MANUFACTURING,
            Industry.TECHNOLOGY,
            Industry.AGRICULTURE
        ]
        self.eligible_locations = [
            Location.NORTHEAST,
            Location.NORTH,
            Location.CENTER_WEST
        ]
    
    def check_eligibility(
        self,
        industry: Industry,
        location: Location,
        annual_revenue: float
    ) -> Dict[str, bool]:
        """
        Checks eligibility based on provided parameters.
        
        Args:
            industry: Company's industry sector
            location: Company's geographic location
            annual_revenue: Company's annual revenue
            
        Returns:
            Dictionary with eligibility results and reasons
        """
        results = {
            "is_eligible": False,
            "reasons": []
        }
        
        # Check industry eligibility
        if industry not in self.eligible_industries:
            results["reasons"].append("Industry not eligible for benefits")
        else:
            results["reasons"].append("Industry is eligible")
        
        # Check location eligibility
        if location not in self.eligible_locations:
            results["reasons"].append("Location not eligible for benefits")
        else:
            results["reasons"].append("Location is eligible")
        
        # Check revenue threshold
        if annual_revenue > self.revenue_threshold:
            results["reasons"].append(f"Revenue exceeds threshold of {self.revenue_threshold}")
        else:
            results["reasons"].append("Revenue within eligible range")
        
        # Determine overall eligibility
        if (industry in self.eligible_industries and 
            location in self.eligible_locations and 
            annual_revenue <= self.revenue_threshold):
            results["is_eligible"] = True
        
        return results

def get_user_input() -> Dict[str, Optional[str]]:
    """
    Collects user input for eligibility assessment.
    
    Returns:
        Dictionary with user-provided values
    """
    inputs = {
        "industry": None,
        "location": None,
        "revenue": None
    }
    
    print("\nTax Benefit Eligibility Assessment (MP 2.199-14/2001)\n")
    print("Available Industries:")
    for i, industry in enumerate(Industry, 1):
        print(f"{i}. {industry.value}")
    
    try:
        industry_choice = int(input("\nSelect your industry (1-6): "))
        inputs["industry"] = list(Industry)[industry_choice - 1]
    except (ValueError, IndexError):
        print("Invalid industry selection")
        return inputs
    
    print("\nAvailable Locations:")
    for i, location in enumerate(Location, 1):
        print(f"{i}. {location.value}")
    
    try:
        location_choice = int(input("\nSelect your location (1-5): "))
        inputs["location"] = list(Location)[location_choice - 1]
    except (ValueError, IndexError):
        print("Invalid location selection")
        return inputs
    
    try:
        revenue_input = input("\nEnter your annual revenue (local currency): ")
        inputs["revenue"] = float(revenue_input)
    except ValueError:
        print("Invalid revenue value")
        return inputs
    
    return inputs

def main():
    """
    Main function to execute the tax benefit eligibility assessment.
    """
    assessor = TaxBenefitEligibility()
    user_input = get_user_input()
    
    if None in user_input.values():
        print("\nInvalid input. Please try again.")
        sys.exit(1)
    
    results = assessor.check_eligibility(
        industry=user_input["industry"],
        location=user_input["location"],
        annual_revenue=user_input["revenue"]
    )
    
    print("\n=== Assessment Results ===")
    print(f"Eligible: {'Yes' if results['is_eligible'] else 'No'}")
    print("\nDetails:")
    for reason in results["reasons"]:
        print(f"- {reason}")

if __name__ == "__main__":
    main()
```
