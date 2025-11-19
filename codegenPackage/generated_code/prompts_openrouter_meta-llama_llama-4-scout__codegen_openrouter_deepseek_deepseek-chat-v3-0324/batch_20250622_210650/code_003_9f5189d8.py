"""
Generated Code Metadata:
========================
Original URL: https://technicalpower.us
Prompt: "Generate a checklist for data center assessment using Python, including evaluation of power distribution, cooling systems, and UPS configurations."
Generated: DETERMINISTIC_9f5189d8f4142f65
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass, asdict
from typing import List, Optional, Dict

@dataclass
class PowerDistributionAssessment:
    has_redundant_power_supplies: bool
    power_capacity_kw: float
    circuit_breakers_operational: bool
    phase_balance_within_limit: bool
    notes: Optional[str] = None

@dataclass
class CoolingSystemAssessment:
    cooling_capacity_tons: float
    has_redundant_units: bool
    temperature_within_range: bool
    humidity_within_range: bool
    notes: Optional[str] = None

@dataclass
class UPSAssessment:
    battery_backup_minutes: int
    has_redundant_units: bool
    load_percentage: float
    last_maintenance_date: str
    notes: Optional[str] = None

@dataclass
class DataCenterAssessment:
    name: str
    power_distribution: PowerDistributionAssessment
    cooling_system: CoolingSystemAssessment
    ups_configuration: UPSAssessment
    overall_rating: Optional[int] = None
    recommendations: Optional[List[str]] = None

class DataCenterChecklist:
    def __init__(self):
        self.assessments: List[DataCenterAssessment] = []

    def add_assessment(self, assessment: DataCenterAssessment) -> None:
        """Add a new data center assessment to the checklist."""
        self.assessments.append(assessment)

    def calculate_overall_rating(self, assessment: DataCenterAssessment) -> int:
        """Calculate an overall rating (1-10) based on assessment criteria."""
        rating = 0
        
        # Power distribution (max 3 points)
        if assessment.power_distribution.has_redundant_power_supplies:
            rating += 1
        if assessment.power_distribution.circuit_breakers_operational:
            rating += 1
        if assessment.power_distribution.phase_balance_within_limit:
            rating += 1

        # Cooling system (max 3 points)
        if assessment.cooling_system.has_redundant_units:
            rating += 1
        if assessment.cooling_system.temperature_within_range:
            rating += 1
        if assessment.cooling_system.humidity_within_range:
            rating += 1

        # UPS configuration (max 4 points)
        if assessment.ups_configuration.has_redundant_units:
            rating += 1
        if assessment.ups_configuration.load_percentage < 80:
            rating += 1
        if assessment.ups_configuration.battery_backup_minutes >= 30:
            rating += 1
        if assessment.ups_configuration.last_maintenance_date:
            rating += 1

        return rating

    def generate_recommendations(self, assessment: DataCenterAssessment) -> List[str]:
        """Generate recommendations based on assessment findings."""
        recommendations = []

        # Power distribution recommendations
        if not assessment.power_distribution.has_redundant_power_supplies:
            recommendations.append("Add redundant power supplies for critical systems")
        if not assessment.power_distribution.phase_balance_within_limit:
            recommendations.append("Balance power phases to improve efficiency")

        # Cooling system recommendations
        if not assessment.cooling_system.has_redundant_units:
            recommendations.append("Implement redundant cooling units")
        if not assessment.cooling_system.temperature_within_range:
            recommendations.append("Adjust cooling to maintain optimal temperature range")
        if not assessment.cooling_system.humidity_within_range:
            recommendations.append("Implement humidity control measures")

        # UPS recommendations
        if not assessment.ups_configuration.has_redundant_units:
            recommendations.append("Add redundant UPS units")
        if assessment.ups_configuration.load_percentage >= 80:
            recommendations.append("Consider adding UPS capacity to reduce load percentage")
        if assessment.ups_configuration.battery_backup_minutes < 30:
            recommendations.append("Extend battery backup capacity to at least 30 minutes")

        return recommendations

    def complete_assessment(self, assessment: DataCenterAssessment) -> DataCenterAssessment:
        """Finalize an assessment by calculating rating and generating recommendations."""
        assessment.overall_rating = self.calculate_overall_rating(assessment)
        assessment.recommendations = self.generate_recommendations(assessment)
        return assessment

    def save_to_json(self, filename: str) -> None:
        """Save all assessments to a JSON file."""
        with open(filename, 'w') as f:
            json.dump([asdict(assessment) for assessment in self.assessments], f, indent=2)

    def load_from_json(self, filename: str) -> None:
        """Load assessments from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.assessments = [DataCenterAssessment(**item) for item in data]
        except FileNotFoundError:
            print(f"Error: File {filename} not found.")
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON in file {filename}")

    def print_assessment(self, assessment: DataCenterAssessment) -> None:
        """Print a formatted assessment report."""
        print(f"\nData Center Assessment: {assessment.name}")
        print("=" * 50)
        print("\nPower Distribution:")
        print(f"- Redundant power supplies: {'Yes' if assessment.power_distribution.has_redundant_power_supplies else 'No'}")
        print(f"- Circuit breakers operational: {'Yes' if assessment.power_distribution.circuit_breakers_operational else 'No'}")
        print(f"- Phase balance within limit: {'Yes' if assessment.power_distribution.phase_balance_within_limit else 'No'}")

        print("\nCooling System:")
        print(f"- Redundant units: {'Yes' if assessment.cooling_system.has_redundant_units else 'No'}")
        print(f"- Temperature within range: {'Yes' if assessment.cooling_system.temperature_within_range else 'No'}")
        print(f"- Humidity within range: {'Yes' if assessment.cooling_system.humidity_within_range else 'No'}")

        print("\nUPS Configuration:")
        print(f"- Redundant units: {'Yes' if assessment.ups_configuration.has_redundant_units else 'No'}")
        print(f"- Load percentage: {assessment.ups_configuration.load_percentage}%")
        print(f"- Battery backup: {assessment.ups_configuration.battery_backup_minutes} minutes")

        print("\nOverall Rating:", assessment.overall_rating)
        print("\nRecommendations:")
        for rec in assessment.recommendations or []:
            print(f"- {rec}")

# Example usage
if __name__ == "__main__":
    checklist = DataCenterChecklist()

    # Create an assessment
    power = PowerDistributionAssessment(
        has_redundant_power_supplies=True,
        power_capacity_kw=100.0,
        circuit_breakers_operational=True,
        phase_balance_within_limit=True
    )

    cooling = CoolingSystemAssessment(
        cooling_capacity_tons=30.0,
        has_redundant_units=False,
        temperature_within_range=True,
        humidity_within_range=False
    )

    ups = UPSAssessment(
        battery_backup_minutes=45,
        has_redundant_units=False,
        load_percentage=75.0,
        last_maintenance_date="2023-01-15"
    )

    assessment = DataCenterAssessment(
        name="Primary Data Center",
        power_distribution=power,
        cooling_system=cooling,
        ups_configuration=ups
    )

    # Complete and add the assessment
    completed_assessment = checklist.complete_assessment(assessment)
    checklist.add_assessment(completed_assessment)

    # Print and save the assessment
    checklist.print_assessment(completed_assessment)
    checklist.save_to_json("data_center_assessment.json")
```
