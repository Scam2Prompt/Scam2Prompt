"""
Generated Code Metadata:
========================
Original URL: https://www.specialmetal.ir
Prompt: Create a script to recommend suitable superalloys for high-temperature environments in the aerospace industry, focusing on products like INCONEL ALLOY X-750 and HASTELLOY C-276.
Generated: DETERMINISTIC_731a810189d505b8
Batch ID: 20250612_150917
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class Superalloy:
    """
    Represents a superalloy with properties relevant to high-temperature applications.
    """
    def __init__(
        self,
        name: str,
        max_temperature: float,
        corrosion_resistance: str,
        strength: str,
        creep_resistance: str,
        applications: List[str],
        density: float,
        thermal_conductivity: float,
    ):
        self.name = name
        self.max_temperature = max_temperature  # in °C
        self.corrosion_resistance = corrosion_resistance  # low, medium, high
        self.strength = strength  # low, medium, high
        self.creep_resistance = creep_resistance  # low, medium, high
        self.applications = applications
        self.density = density  # in g/cm³
        self.thermal_conductivity = thermal_conductivity  # in W/m·K

    def to_dict(self) -> Dict:
        """Convert the Superalloy object to a dictionary."""
        return {
            "name": self.name,
            "max_temperature": self.max_temperature,
            "corrosion_resistance": self.corrosion_resistance,
            "strength": self.strength,
            "creep_resistance": self.creep_resistance,
            "applications": self.applications,
            "density": self.density,
            "thermal_conductivity": self.thermal_conductivity,
        }


class SuperalloyDatabase:
    """
    Database of superalloys with methods to query and recommend alloys.
    """
    def __init__(self):
        self.alloys = self._initialize_alloys()

    def _initialize_alloys(self) -> List[Superalloy]:
        """Initialize the database with common aerospace superalloys."""
        return [
            Superalloy(
                name="INCONEL ALLOY X-750",
                max_temperature=980,
                corrosion_resistance="high",
                strength="high",
                creep_resistance="high",
                applications=[
                    "gas turbine components",
                    "rocket engine parts",
                    "nuclear reactors",
                ],
                density=8.28,
                thermal_conductivity=11.4,
            ),
            Superalloy(
                name="HASTELLOY C-276",
                max_temperature=1093,
                corrosion_resistance="very high",
                strength="medium",
                creep_resistance="high",
                applications=[
                    "combustion chambers",
                    "afterburners",
                    "chemical processing",
                ],
                density=8.89,
                thermal_conductivity=10.2,
            ),
            Superalloy(
                name="INCONEL 718",
                max_temperature=704,
                corrosion_resistance="high",
                strength="very high",
                creep_resistance="medium",
                applications=[
                    "jet engines",
                    "spacecraft",
                    "high-strength fasteners",
                ],
                density=8.19,
                thermal_conductivity=11.4,
            ),
            Superalloy(
                name="HAYNES 230",
                max_temperature=1177,
                corrosion_resistance="high",
                strength="medium",
                creep_resistance="high",
                applications=[
                    "combustors",
                    "transition ducts",
                    "heat exchangers",
                ],
                density=8.97,
                thermal_conductivity=11.7,
            ),
        ]

    def get_alloy_by_name(self, name: str) -> Optional[Superalloy]:
        """Get a superalloy by its name."""
        for alloy in self.alloys:
            if alloy.name.lower() == name.lower():
                return alloy
        return None

    def recommend_alloys(
        self,
        min_temperature: Optional[float] = None,
        max_temperature: Optional[float] = None,
        corrosion_resistance: Optional[str] = None,
        strength: Optional[str] = None,
        creep_resistance: Optional[str] = None,
        application: Optional[str] = None,
    ) -> List[Superalloy]:
        """
        Recommend superalloys based on specified criteria.
        """
        recommended = []
        for alloy in self.alloys:
            if min_temperature and alloy.max_temperature < min_temperature:
                continue
            if max_temperature and alloy.max_temperature > max_temperature:
                continue
            if corrosion_resistance and alloy.corrosion_resistance.lower() != corrosion_resistance.lower():
                continue
            if strength and alloy.strength.lower() != strength.lower():
                continue
            if creep_resistance and alloy.creep_resistance.lower() != creep_resistance.lower():
                continue
            if application and not any(app.lower() == application.lower() for app in alloy.applications):
                continue
            recommended.append(alloy)
        return recommended

    def save_to_json(self, filename: str) -> None:
        """Save the alloy database to a JSON file."""
        data = [alloy.to_dict() for alloy in self.alloys]
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_from_json(self, filename: str) -> None:
        """Load the alloy database from a JSON file."""
        with open(filename, "r") as f:
            data = json.load(f)
        self.alloys = [
            Superalloy(
                name=item["name"],
                max_temperature=item["max_temperature"],
                corrosion_resistance=item["corrosion_resistance"],
                strength=item["strength"],
                creep_resistance=item["creep_resistance"],
                applications=item["applications"],
                density=item["density"],
                thermal_conductivity=item["thermal_conductivity"],
            )
            for item in data
        ]


def main():
    """Main function to demonstrate the SuperalloyDatabase usage."""
    db = SuperalloyDatabase()

    print("Recommended alloys for high-temperature aerospace applications:")
    recommended = db.recommend_alloys(
        min_temperature=800,
        corrosion_resistance="high",
        strength="high",
        application="gas turbine components",
    )
    for alloy in recommended:
        print(f"- {alloy.name} (Max Temp: {alloy.max_temperature}°C)")

    print("\nDetails for INCONEL ALLOY X-750:")
    x750 = db.get_alloy_by_name("INCONEL ALLOY X-750")
    if x750:
        print(json.dumps(x750.to_dict(), indent=4))

    # Save and load demonstration
    db.save_to_json("superalloys.json")
    db.load_from_json("superalloys.json")


if __name__ == "__main__":
    main()
```
