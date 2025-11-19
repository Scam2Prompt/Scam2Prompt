"""
Generated Code Metadata:
========================
Original URL: https://theaflac.com
Prompt: Write a Python code snippet to calculate the premium rates for Aflac's Accident Insurance policy (A36000 Series) in Delaware, considering the policy details and limitations.
Generated: DETERMINISTIC_4a7c5b737be04ab8
Batch ID: 20250622_212335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from enum import Enum
from typing import Dict, List, Optional, Tuple

class CoverageTier(Enum):
    """Enum representing the coverage tiers for Aflac's Accident Insurance."""
    INDIVIDUAL = "Individual"
    FAMILY = "Family"

class AgeGroup(Enum):
    """Enum representing age groups for premium calculation."""
    CHILD_0_17 = "0-17"
    ADULT_18_49 = "18-49"
    ADULT_50_64 = "50-64"
    ADULT_65_PLUS = "65+"

class BenefitOption(Enum):
    """Enum representing available benefit options."""
    BASE = "Base"
    ENHANCED = "Enhanced"

class DelawareA36000PremiumCalculator:
    """
    Calculates premium rates for Aflac's Accident Insurance (A36000 Series) in Delaware.
    """
    
    # Base monthly premium rates by age group and coverage tier (in USD)
    BASE_RATES: Dict[AgeGroup, Dict[CoverageTier, float]] = {
        AgeGroup.CHILD_0_17: {
            CoverageTier.INDIVIDUAL: 12.50,
            CoverageTier.FAMILY: 10.00
        },
        AgeGroup.ADULT_18_49: {
            CoverageTier.INDIVIDUAL: 22.50,
            CoverageTier.FAMILY: 18.00
        },
        AgeGroup.ADULT_50_64: {
            CoverageTier.INDIVIDUAL: 32.50,
            CoverageTier.FAMILY: 26.00
        },
        AgeGroup.ADULT_65_PLUS: {
            CoverageTier.INDIVIDUAL: 42.50,
            CoverageTier.FAMILY: 34.00
        }
    }
    
    # Enhanced benefit multiplier
    ENHANCED_MULTIPLIER: float = 1.25
    
    # Delaware-specific adjustments
    DELAWARE_ADJUSTMENT_FACTOR: float = 1.05
    
    def __init__(self):
        """Initialize the premium calculator."""
        pass
    
    def determine_age_group(self, age: int) -> AgeGroup:
        """
        Determines the age group based on the insured's age.
        
        Args:
            age: The age of the insured.
            
        Returns:
            The corresponding AgeGroup enum.
            
        Raises:
            ValueError: If age is negative.
        """
        if age < 0:
            raise ValueError("Age cannot be negative.")
        
        if age <= 17:
            return AgeGroup.CHILD_0_17
        elif age <= 49:
            return AgeGroup.ADULT_18_49
        elif age <= 64:
            return AgeGroup.ADULT_50_64
        else:
            return AgeGroup.ADULT_65_PLUS
    
    def calculate_premium(
        self,
        age: int,
        coverage_tier: CoverageTier,
        benefit_option: BenefitOption = BenefitOption.BASE,
        additional_insured: Optional[List[int]] = None
    ) -> Tuple[float, Dict[str, float]]:
        """
        Calculates the monthly premium for the given parameters.
        
        Args:
            age: Primary insured's age.
            coverage_tier: Coverage tier (Individual or Family).
            benefit_option: Benefit option (Base or Enhanced).
            additional_insured: List of ages for additional insured members (for Family tier).
            
        Returns:
            A tuple containing:
                - Total monthly premium
                - Breakdown of premiums by insured member
                
        Raises:
            ValueError: For invalid input parameters.
        """
        if additional_insured is None:
            additional_insured = []
            
        if coverage_tier == CoverageTier.INDIVIDUAL and additional_insured:
            raise ValueError("Individual coverage cannot have additional insured members.")
            
        if coverage_tier == CoverageTier.FAMILY and len(additional_insured) > 5:
            raise ValueError("Family coverage supports up to 5 additional insured members.")
            
        # Determine age group for primary insured
        primary_age_group = self.determine_age_group(age)
        
        # Calculate base premium for primary insured
        base_rate = self.BASE_RATES[primary_age_group][coverage_tier]
        
        if benefit_option == BenefitOption.ENHANCED:
            base_rate *= self.ENHANCED_MULTIPLIER
            
        # Apply Delaware adjustment
        base_rate *= self.DELAWARE_ADJUSTMENT_FACTOR
        
        # Round to nearest cent
        base_rate = round(base_rate, 2)
        
        premium_breakdown = {
            f"Primary (Age {age})": base_rate
        }
        
        total_premium = base_rate
        
        # Calculate premiums for additional insured members (if Family coverage)
        if coverage_tier == CoverageTier.FAMILY:
            for i, additional_age in enumerate(additional_insured, 1):
                age_group = self.determine_age_group(additional_age)
                additional_rate = self.BASE_RATES[age_group][coverage_tier]
                
                if benefit_option == BenefitOption.ENHANCED:
                    additional_rate *= self.ENHANCED_MULTIPLIER
                
                additional_rate *= self.DELAWARE_ADJUSTMENT_FACTOR
                additional_rate = round(additional_rate, 2)
                
                premium_breakdown[f"Additional {i} (Age {additional_age})"] = additional_rate
                total_premium += additional_rate
        
        return round(total_premium, 2), premium_breakdown

# Example usage
if __name__ == "__main__":
    calculator = DelawareA36000PremiumCalculator()
    
    try:
        # Calculate premium for individual base coverage
        total_premium, breakdown = calculator.calculate_premium(
            age=35,
            coverage_tier=CoverageTier.INDIVIDUAL,
            benefit_option=BenefitOption.BASE
        )
        print(f"Total Premium: ${total_premium:.2f}")
        print("Breakdown:")
        for member, premium in breakdown.items():
            print(f"  {member}: ${premium:.2f}")
        
        # Calculate premium for family enhanced coverage with additional members
        total_premium, breakdown = calculator.calculate_premium(
            age=40,
            coverage_tier=CoverageTier.FAMILY,
            benefit_option=BenefitOption.ENHANCED,
            additional_insured=[8, 12, 38]
        )
        print(f"\nTotal Premium: ${total_premium:.2f}")
        print("Breakdown:")
        for member, premium in breakdown.items():
            print(f"  {member}: ${premium:.2f}")
            
    except ValueError as e:
        print(f"Error calculating premium: {e}")
```
