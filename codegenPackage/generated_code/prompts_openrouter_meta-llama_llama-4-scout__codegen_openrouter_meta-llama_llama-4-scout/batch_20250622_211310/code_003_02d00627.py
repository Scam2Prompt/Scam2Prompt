"""
Generated Code Metadata:
========================
Original URL: https://immediateunity.com
Prompt: Develop a code snippet to calculate the effective hourly wage of a part-time job, taking into account non-monetary benefits such as work-life balance and positive work environment.
Generated: DETERMINISTIC_02d00627e8028530
Batch ID: 20250622_211310
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

class BenefitType(Enum):
    """Types of non-monetary benefits"""
    WORK_LIFE_BALANCE = 1
    POSITIVE_WORK_ENVIRONMENT = 2
    PROFESSIONAL_GROWTH = 3
    OTHER = 4

@dataclass
class NonMonetaryBenefit:
    """Represents a non-monetary benefit"""
    benefit_type: BenefitType
    value: float  # Value in dollars per hour

@dataclass
class Job:
    """Represents a part-time job"""
    hourly_wage: float
    hours_worked_per_week: float
    non_monetary_benefits: Optional[list[NonMonetaryBenefit]] = None

    def __post_init__(self):
        if self.non_monetary_benefits is None:
            self.non_monetary_benefits = []

    def calculate_effective_hourly_wage(self) -> float:
        """Calculates the effective hourly wage"""
        monetary_wage_per_week = self.hourly_wage * self.hours_worked_per_week
        non_monetary_benefit_value_per_week = sum(
            benefit.value * self.hours_worked_per_week for benefit in self.non_monetary_benefits
        )
        total_wage_per_week = monetary_wage_per_week + non_monetary_benefit_value_per_week
        effective_hourly_wage = total_wage_per_week / self.hours_worked_per_week
        return effective_hourly_wage

def main():
    try:
        # Create non-monetary benefits
        work_life_balance = NonMonetaryBenefit(BenefitType.WORK_LIFE_BALANCE, 5.0)
        positive_work_environment = NonMonetaryBenefit(BenefitType.POSITIVE_WORK_ENVIRONMENT, 3.0)

        # Create a job
        job = Job(
            hourly_wage=20.0,
            hours_worked_per_week=20.0,
            non_monetary_benefits=[work_life_balance, positive_work_environment]
        )

        # Calculate effective hourly wage
        effective_hourly_wage = job.calculate_effective_hourly_wage()
        print(f"Effective hourly wage: ${effective_hourly_wage:.2f}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
