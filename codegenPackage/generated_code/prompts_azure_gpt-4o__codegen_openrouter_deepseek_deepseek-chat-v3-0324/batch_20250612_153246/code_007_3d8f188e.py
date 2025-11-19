"""
Generated Code Metadata:
========================
Original URL: https://pahubel.com
Prompt: Write a Python program to simulate the spatial planning of healthcare facilities, ensuring compliance with industry standards and legal requirements, as emphasized by Pahubel Ibérica S.L.
Generated: DETERMINISTIC_3d8f188e33da8cba
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import math
from typing import List, Dict, Tuple, Optional
from enum import Enum
from dataclasses import dataclass
import random

class FacilityType(Enum):
    HOSPITAL = "Hospital"
    CLINIC = "Clinic"
    PHARMACY = "Pharmacy"
    LABORATORY = "Laboratory"
    REHAB_CENTER = "Rehabilitation Center"

class LegalRequirement(Enum):
    MIN_DISTANCE = "Minimum Distance Between Facilities"
    MAX_CAPACITY = "Maximum Capacity"
    ACCESSIBILITY = "Accessibility Standards"
    ZONING = "Zoning Regulations"
    SAFETY = "Safety Standards"

@dataclass
class Facility:
    id: str
    facility_type: FacilityType
    capacity: int
    location: Tuple[float, float]  # (latitude, longitude)
    compliance_checks: Dict[LegalRequirement, bool]

class HealthcareFacilityPlanner:
    def __init__(self, facilities: List[Facility] = None):
        self.facilities = facilities if facilities else []
        self.legal_requirements = {
            FacilityType.HOSPITAL: {
                LegalRequirement.MIN_DISTANCE: 5000,  # meters
                LegalRequirement.MAX_CAPACITY: 1000,
                LegalRequirement.ACCESSIBILITY: True,
                LegalRequirement.ZONING: True,
                LegalRequirement.SAFETY: True
            },
            FacilityType.CLINIC: {
                LegalRequirement.MIN_DISTANCE: 2000,
                LegalRequirement.MAX_CAPACITY: 200,
                LegalRequirement.ACCESSIBILITY: True,
                LegalRequirement.ZONING: True,
                LegalRequirement.SAFETY: True
            },
            FacilityType.PHARMACY: {
                LegalRequirement.MIN_DISTANCE: 500,
                LegalRequirement.MAX_CAPACITY: 50,
                LegalRequirement.ACCESSIBILITY: True,
                LegalRequirement.ZONING: True,
                LegalRequirement.SAFETY: True
            },
            FacilityType.LABORATORY: {
                LegalRequirement.MIN_DISTANCE: 1000,
                LegalRequirement.MAX_CAPACITY: 100,
                LegalRequirement.ACCESSIBILITY: True,
                LegalRequirement.ZONING: True,
                LegalRequirement.SAFETY: True
            },
            FacilityType.REHAB_CENTER: {
                LegalRequirement.MIN_DISTANCE: 3000,
                LegalRequirement.MAX_CAPACITY: 150,
                LegalRequirement.ACCESSIBILITY: True,
                LegalRequirement.ZONING: True,
                LegalRequirement.SAFETY: True
            }
        }

    def add_facility(self, facility: Facility) -> bool:
        """Add a facility after validating compliance with legal requirements."""
        if not self._validate_facility(facility):
            return False
        self.facilities.append(facility)
        return True

    def _validate_facility(self, facility: Facility) -> bool:
        """Validate if a facility complies with all legal requirements."""
        # Check capacity
        max_capacity = self.legal_requirements[facility.facility_type][LegalRequirement.MAX_CAPACITY]
        if facility.capacity > max_capacity:
            facility.compliance_checks[LegalRequirement.MAX_CAPACITY] = False
            return False
        facility.compliance_checks[LegalRequirement.MAX_CAPACITY] = True

        # Check distance to other facilities of the same type
        min_distance = self.legal_requirements[facility.facility_type][LegalRequirement.MIN_DISTANCE]
        for existing_facility in self.facilities:
            if existing_facility.facility_type == facility.facility_type:
                distance = self._calculate_distance(facility.location, existing_facility.location)
                if distance < min_distance:
                    facility.compliance_checks[LegalRequirement.MIN_DISTANCE] = False
                    return False
        facility.compliance_checks[LegalRequirement.MIN_DISTANCE] = True

        # Other checks (simplified for example)
        facility.compliance_checks[LegalRequirement.ACCESSIBILITY] = True
        facility.compliance_checks[LegalRequirement.ZONING] = True
        facility.compliance_checks[LegalRequirement.SAFETY] = True

        return True

    def _calculate_distance(self, loc1: Tuple[float, float], loc2: Tuple[float, float]) -> float:
        """Calculate distance between two points in meters using Haversine formula."""
        lat1, lon1 = loc1
        lat2, lon2 = loc2
        R = 6371000  # Earth radius in meters
        phi1 = math.radians(lat1)
        phi2 = math.radians(lat2)
        delta_phi = math.radians(lat2 - lat1)
        delta_lambda = math.radians(lon2 - lon1)

        a = (math.sin(delta_phi / 2) ** 2 +
             math.cos(phi1) * math.cos(phi2) *
             math.sin(delta_lambda / 2) ** 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

        return R * c

    def generate_report(self) -> Dict:
        """Generate a compliance report for all facilities."""
        report = {
            "total_facilities": len(self.facilities),
            "facilities": [],
            "compliance_summary": {
                req.value: sum(1 for f in self.facilities if f.compliance_checks.get(req, False))
                for req in LegalRequirement
            }
        }

        for facility in self.facilities:
            report["facilities"].append({
                "id": facility.id,
                "type": facility.facility_type.value,
                "capacity": facility.capacity,
                "location": facility.location,
                "compliance": {k.value: v for k, v in facility.compliance_checks.items()}
            })

        return report

    def save_to_json(self, filename: str) -> bool:
        """Save the current state to a JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump({
                    "facilities": [
                        {
                            "id": f.id,
                            "type": f.facility_type.value,
                            "capacity": f.capacity,
                            "location": f.location,
                            "compliance_checks": {k.value: v for k, v in f.compliance_checks.items()}
                        }
                        for f in self.facilities
                    ]
                }, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving to file: {e}")
            return False

    def load_from_json(self, filename: str) -> bool:
        """Load facilities from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.facilities = []
                for facility_data in data["facilities"]:
                    facility = Facility(
                        id=facility_data["id"],
                        facility_type=FacilityType(facility_data["type"]),
                        capacity=facility_data["capacity"],
                        location=tuple(facility_data["location"]),
                        compliance_checks={
                            LegalRequirement(k): v 
                            for k, v in facility_data["compliance_checks"].items()
                        }
                    )
                    self.facilities.append(facility)
            return True
        except Exception as e:
            print(f"Error loading from file: {e}")
            return False

def generate_sample_facilities() -> List[Facility]:
    """Generate sample facilities for testing."""
    facilities = []
    types = list(FacilityType)
    for i in range(10):
        facility_type = random.choice(types)
        facilities.append(Facility(
            id=f"facility_{i}",
            facility_type=facility_type,
            capacity=random.randint(10, 200),
            location=(random.uniform(40.0, 42.0), random.uniform(-3.0, -1.0)),
            compliance_checks={req: False for req in LegalRequirement}
        ))
    return facilities

def main():
    """Main execution function."""
    planner = HealthcareFacilityPlanner()
    
    # Add sample facilities
    for facility in generate_sample_facilities():
        if planner.add_facility(facility):
            print(f"Added facility {facility.id} ({facility.facility_type.value})")
        else:
            print(f"Failed to add facility {facility.id} - compliance issues")

    # Generate and print report
    report = planner.generate_report()
    print("\nCompliance Report:")
    print(json.dumps(report, indent=2))

    # Save to file
    if planner.save_to_json("healthcare_facilities.json"):
        print("\nData saved to healthcare_facilities.json")

if __name__ == "__main__":
    main()
```
