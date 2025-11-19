"""
Generated Code Metadata:
========================
Original URL: https://mail.gtempus.com
Prompt: Create a sample insurance policy quoting tool that incorporates features highlighted by Tempus, such as life, auto, and health insurance options.
Generated: DETERMINISTIC_446ec07260fd3234
Batch ID: 20250612_163156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, List, Optional


class InsuranceType(Enum):
    """Enum representing different types of insurance policies."""
    LIFE = auto()
    AUTO = auto()
    HEALTH = auto()


@dataclass
class Applicant:
    """Class representing an insurance applicant."""
    name: str
    age: int
    gender: str
    health_conditions: List[str] = None
    driving_record: Dict[str, int] = None

    def __post_init__(self):
        """Initialize optional fields."""
        if self.health_conditions is None:
            self.health_conditions = []
        if self.driving_record is None:
            self.driving_record = {"accidents": 0, "violations": 0}


@dataclass
class PolicyQuote:
    """Class representing an insurance policy quote."""
    insurance_type: InsuranceType
    applicant: Applicant
    monthly_premium: float
    coverage_details: Dict[str, str]
    deductible: float


class InsuranceQuotingTool:
    """Main class for generating insurance policy quotes."""

    BASE_RATES = {
        InsuranceType.LIFE: 30.0,
        InsuranceType.AUTO: 50.0,
        InsuranceType.HEALTH: 200.0
    }

    def __init__(self):
        """Initialize with default underwriting rules."""
        self.underwriting_rules = {
            InsuranceType.LIFE: self._calculate_life_insurance,
            InsuranceType.AUTO: self._calculate_auto_insurance,
            InsuranceType.HEALTH: self._calculate_health_insurance
        }

    def get_quote(self, insurance_type: InsuranceType, applicant: Applicant) -> PolicyQuote:
        """
        Generate a policy quote for the given insurance type and applicant.
        
        Args:
            insurance_type: Type of insurance policy
            applicant: Applicant information
            
        Returns:
            PolicyQuote object with calculated premium and details
            
        Raises:
            ValueError: If invalid insurance type or applicant data
        """
        if not isinstance(insurance_type, InsuranceType):
            raise ValueError("Invalid insurance type")
        
        if not isinstance(applicant, Applicant) or applicant.age <= 0:
            raise ValueError("Invalid applicant data")

        calculator = self.underwriting_rules.get(insurance_type)
        if not calculator:
            raise ValueError("Unsupported insurance type")

        return calculator(applicant)

    def _calculate_life_insurance(self, applicant: Applicant) -> PolicyQuote:
        """Calculate life insurance premium based on applicant details."""
        base_rate = self.BASE_RATES[InsuranceType.LIFE]
        age_factor = max(1.0, applicant.age / 40)  # Premium increases with age
        health_factor = 1.0 + (0.1 * len(applicant.health_conditions))
        
        premium = base_rate * age_factor * health_factor
        coverage = f"${500000 - (10000 * len(applicant.health_conditions))} term life coverage"
        
        return PolicyQuote(
            insurance_type=InsuranceType.LIFE,
            applicant=applicant,
            monthly_premium=round(premium, 2),
            coverage_details={"coverage_amount": coverage},
            deductible=0.0
        )

    def _calculate_auto_insurance(self, applicant: Applicant) -> PolicyQuote:
        """Calculate auto insurance premium based on applicant details."""
        base_rate = self.BASE_RATES[InsuranceType.AUTO]
        age_factor = 1.5 if applicant.age < 25 else 1.0  # Higher for young drivers
        record_factor = 1.0 + (0.2 * applicant.driving_record["accidents"]) + \
                       (0.1 * applicant.driving_record["violations"])
        
        premium = base_rate * age_factor * record_factor
        coverage = "Full coverage" if record_factor < 1.5 else "Basic liability"
        
        return PolicyQuote(
            insurance_type=InsuranceType.AUTO,
            applicant=applicant,
            monthly_premium=round(premium, 2),
            coverage_details={"coverage_type": coverage},
            deductible=500.0
        )

    def _calculate_health_insurance(self, applicant: Applicant) -> PolicyQuote:
        """Calculate health insurance premium based on applicant details."""
        base_rate = self.BASE_RATES[InsuranceType.HEALTH]
        age_factor = 1.0 + (applicant.age / 100)  # Premium increases with age
        health_factor = 1.0 + (0.15 * len(applicant.health_conditions))
        
        premium = base_rate * age_factor * health_factor
        coverage = "Comprehensive" if health_factor < 1.3 else "Standard"
        
        return PolicyQuote(
            insurance_type=InsuranceType.HEALTH,
            applicant=applicant,
            monthly_premium=round(premium, 2),
            coverage_details={"plan_type": coverage},
            deductible=1000.0 if health_factor < 1.5 else 2000.0
        )


def main():
    """Example usage of the insurance quoting tool."""
    quoting_tool = InsuranceQuotingTool()

    # Create sample applicants
    applicant1 = Applicant(
        name="John Doe",
        age=35,
        gender="Male",
        health_conditions=["Asthma"],
        driving_record={"accidents": 1, "violations": 0}
    )

    applicant2 = Applicant(
        name="Jane Smith",
        age=28,
        gender="Female",
        health_conditions=[],
        driving_record={"accidents": 0, "violations": 2}
    )

    # Get quotes for different insurance types
    try:
        life_quote = quoting_tool.get_quote(InsuranceType.LIFE, applicant1)
        auto_quote = quoting_tool.get_quote(InsuranceType.AUTO, applicant2)
        health_quote = quoting_tool.get_quote(InsuranceType.HEALTH, applicant1)

        # Print quotes
        print("Insurance Quotes Generated:")
        print(json.dumps({
            "life_quote": life_quote.__dict__,
            "auto_quote": auto_quote.__dict__,
            "health_quote": health_quote.__dict__
        }, indent=2, default=str))

    except ValueError as e:
        print(f"Error generating quote: {e}")


if __name__ == "__main__":
    main()
```
