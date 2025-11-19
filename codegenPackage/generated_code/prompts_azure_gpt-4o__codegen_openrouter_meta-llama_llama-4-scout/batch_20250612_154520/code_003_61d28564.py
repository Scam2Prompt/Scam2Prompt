"""
Generated Code Metadata:
========================
Original URL: https://orlandoplasmacenters.com
Prompt: Write code to validate donor eligibility based on the criteria provided by Orlando Plasma Centers (e.g., age, weight, health status, and medical screening results).
Generated: DETERMINISTIC_61d28564a14acf5d
Batch ID: 20250612_154520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from dataclasses import dataclass
from enum import Enum
from typing import Optional

class HealthStatus(str, Enum):
    """Enum for donor's health status"""
    HEALTHY = "healthy"
    UNHEALTHY = "unhealthy"

@dataclass
class Donor:
    """Class to represent a donor"""
    age: int
    weight: float  # in kg
    health_status: HealthStatus
    medical_screening_results: dict  # dictionary of test results

class DonorEligibilityValidator:
    """Class to validate donor eligibility"""

    def __init__(self, min_age: int = 18, max_age: int = 70, min_weight: float = 45.0):
        """
        Initialize validator with eligibility criteria

        Args:
        - min_age (int): minimum age for donation (default: 18)
        - max_age (int): maximum age for donation (default: 70)
        - min_weight (float): minimum weight for donation in kg (default: 45.0)
        """
        self.min_age = min_age
        self.max_age = max_age
        self.min_weight = min_weight

    def validate_age(self, donor: Donor) -> bool:
        """Check if donor's age is within eligible range"""
        return self.min_age <= donor.age <= self.max_age

    def validate_weight(self, donor: Donor) -> bool:
        """Check if donor's weight is within eligible range"""
        return donor.weight >= self.min_weight

    def validate_health_status(self, donor: Donor) -> bool:
        """Check if donor's health status is eligible"""
        return donor.health_status == HealthStatus.HEALTHY

    def validate_medical_screening_results(self, donor: Donor) -> bool:
        """Check if donor's medical screening results are eligible"""
        # Assume all test results must be negative
        return all(result.lower() == "negative" for result in donor.medical_screening_results.values())

    def is_eligible(self, donor: Donor) -> bool:
        """Check if donor is eligible based on all criteria"""
        return (self.validate_age(donor) and 
                self.validate_weight(donor) and 
                self.validate_health_status(donor) and 
                self.validate_medical_screening_results(donor))

def main():
    try:
        validator = DonorEligibilityValidator()

        # Example donor data
        donor1 = Donor(
            age=25,
            weight=55.0,
            health_status=HealthStatus.HEALTHY,
            medical_screening_results={
                "HIV": "Negative",
                "Hepatitis B": "Negative",
                "Hepatitis C": "Negative"
            }
        )

        donor2 = Donor(
            age=15,
            weight=40.0,
            health_status=HealthStatus.HEALTHY,
            medical_screening_results={
                "HIV": "Negative",
                "Hepatitis B": "Negative",
                "Hepatitis C": "Negative"
            }
        )

        donor3 = Donor(
            age=30,
            weight=50.0,
            health_status=HealthStatus.UNHEALTHY,
            medical_screening_results={
                "HIV": "Negative",
                "Hepatitis B": "Negative",
                "Hepatitis C": "Negative"
            }
        )

        donors = [donor1, donor2, donor3]

        for donor in donors:
            eligibility = validator.is_eligible(donor)
            print(f"Donor (age={donor.age}, weight={donor.weight}, health_status={donor.health_status}): Eligible = {eligibility}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
