"""
Generated Code Metadata:
========================
Original URL: https://healthinsuranceshop.ie
Prompt: Develop a Python script that compares health insurance plans based on pricing and benefits, using data from multiple providers like those mentioned on the Health Insurance Shop website (e.g., VHI, Laya Healthcare, Irish Life Health).
Generated: DETERMINISTIC_372c70e66d914967
Batch ID: 20250612_154820
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# health_insurance_comparator.py

import pandas as pd
from dataclasses import dataclass
from enum import Enum
from typing import List, Dict

class InsuranceProvider(Enum):
    """Enum for insurance providers"""
    VHI = "VHI"
    LAYA_HEALTHCARE = "Laya Healthcare"
    IRISH_LIFE_HEALTH = "Irish Life Health"

@dataclass
class HealthInsurancePlan:
    """Dataclass for health insurance plans"""
    provider: InsuranceProvider
    name: str
    premium: float
    benefits: List[str]

class HealthInsuranceComparator:
    """Class for comparing health insurance plans"""

    def __init__(self):
        self.plans = []

    def add_plan(self, plan: HealthInsurancePlan):
        """Add a health insurance plan to the comparator"""
        self.plans.append(plan)

    def compare_plans(self) -> Dict[str, Dict[str, str]]:
        """Compare health insurance plans based on pricing and benefits"""
        # Sort plans by premium
        sorted_plans = sorted(self.plans, key=lambda x: x.premium)

        # Create a dictionary to store the comparison results
        comparison_results = {}

        for plan in sorted_plans:
            comparison_results[plan.name] = {
                "Provider": plan.provider.value,
                "Premium": f"€{plan.premium:.2f}",
                "Benefits": ", ".join(plan.benefits)
            }

        return comparison_results

def load_plans_from_data(providers: List[InsuranceProvider]) -> List[HealthInsurancePlan]:
    """Load health insurance plans from data"""
    # Sample data for demonstration purposes
    data = {
        InsuranceProvider.VHI.value: [
            {"name": "VHI Gold", "premium": 100.0, "benefits": ["Hospital Stay", "Doctor Visits"]},
            {"name": "VHI Silver", "premium": 80.0, "benefits": ["Hospital Stay", "Some Doctor Visits"]}
        ],
        InsuranceProvider.LAYA_HEALTHCARE.value: [
            {"name": "Laya Gold", "premium": 120.0, "benefits": ["Hospital Stay", "All Doctor Visits", "Dental Care"]},
            {"name": "Laya Basic", "premium": 60.0, "benefits": ["Hospital Stay"]}
        ],
        InsuranceProvider.IRISH_LIFE_HEALTH.value: [
            {"name": "Irish Life Health Gold", "premium": 110.0, "benefits": ["Hospital Stay", "All Doctor Visits", "Optical Care"]},
            {"name": "Irish Life Health Basic", "premium": 70.0, "benefits": ["Hospital Stay", "Some Doctor Visits"]}
        ]
    }

    plans = []
    for provider in providers:
        for plan_data in data[provider.value]:
            try:
                plan = HealthInsurancePlan(
                    provider=provider,
                    name=plan_data["name"],
                    premium=plan_data["premium"],
                    benefits=plan_data["benefits"]
                )
                plans.append(plan)
            except KeyError as e:
                print(f"Error loading plan data: {e}")

    return plans

def main():
    comparator = HealthInsuranceComparator()

    providers = [InsuranceProvider.VHI, InsuranceProvider.LAYA_HEALTHCARE, InsuranceProvider.IRISH_LIFE_HEALTH]
    plans = load_plans_from_data(providers)

    for plan in plans:
        comparator.add_plan(plan)

    comparison_results = comparator.compare_plans()

    print("Health Insurance Plan Comparison:")
    for plan_name, plan_info in comparison_results.items():
        print(f"Plan: {plan_name}")
        for key, value in plan_info.items():
            print(f"  {key}: {value}")
        print()

if __name__ == "__main__":
    main()
```
