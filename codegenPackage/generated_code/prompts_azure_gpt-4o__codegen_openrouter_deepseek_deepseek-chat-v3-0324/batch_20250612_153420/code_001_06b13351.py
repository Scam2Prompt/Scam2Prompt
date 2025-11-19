"""
Generated Code Metadata:
========================
Original URL: https://mjpa.co.in
Prompt: Generate a script that automates the selection of pigments (e.g., ultramarine, fluorescent, or anti-corrosive) based on their application in plastics, paints, or coatings, as described by M J Pigment & Additives.
Generated: DETERMINISTIC_06b1335192f794d4
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from enum import Enum
from typing import Dict, List, Optional

class PigmentType(Enum):
    """Enumeration of pigment types."""
    ULTRAMARINE = "ultramarine"
    FLUORESCENT = "fluorescent"
    ANTI_CORROSIVE = "anti-corrosive"

class Application(Enum):
    """Enumeration of application types."""
    PLASTICS = "plastics"
    PAINTS = "paints"
    COATINGS = "coatings"

class Pigment:
    """Class representing a pigment with its properties."""
    def __init__(self, name: str, pigment_type: PigmentType, applications: List[Application]):
        self.name = name
        self.pigment_type = pigment_type
        self.applications = applications

    def __repr__(self):
        return f"Pigment(name={self.name}, type={self.pigment_type.value}, applications={[app.value for app in self.applications]})"

class PigmentSelector:
    """Class for selecting pigments based on application."""
    def __init__(self):
        self.pigments = self._load_pigments()

    def _load_pigments(self) -> List[Pigment]:
        """Load pigments from a predefined dataset."""
        pigments_data = [
            {
                "name": "Ultramarine Blue",
                "type": PigmentType.ULTRAMARINE,
                "applications": [Application.PLASTICS, Application.PAINTS]
            },
            {
                "name": "Fluorescent Red",
                "type": PigmentType.FLUORESCENT,
                "applications": [Application.PLASTICS, Application.COATINGS]
            },
            {
                "name": "Anti-Corrosive Green",
                "type": PigmentType.ANTI_CORROSIVE,
                "applications": [Application.PAINTS, Application.COATINGS]
            },
            {
                "name": "Ultramarine Green",
                "type": PigmentType.ULTRAMARINE,
                "applications": [Application.PLASTICS, Application.PAINTS, Application.COATINGS]
            }
        ]
        return [Pigment(**data) for data in pigments_data]

    def get_pigments_by_application(self, application: Application) -> List[Pigment]:
        """Retrieve pigments suitable for a given application.
        
        Args:
            application: The application type to filter by.
        
        Returns:
            List of Pigment objects matching the application.
        """
        if not isinstance(application, Application):
            raise ValueError("Invalid application type. Must be an Application enum.")
        
        return [pigment for pigment in self.pigments if application in pigment.applications]

    def get_pigments_by_type(self, pigment_type: PigmentType) -> List[Pigment]:
        """Retrieve pigments of a specific type.
        
        Args:
            pigment_type: The pigment type to filter by.
        
        Returns:
            List of Pigment objects matching the type.
        """
        if not isinstance(pigment_type, PigmentType):
            raise ValueError("Invalid pigment type. Must be a PigmentType enum.")
        
        return [pigment for pigment in self.pigments if pigment.pigment_type == pigment_type]

    def get_pigments_by_type_and_application(self, pigment_type: PigmentType, application: Application) -> List[Pigment]:
        """Retrieve pigments of a specific type and application.
        
        Args:
            pigment_type: The pigment type to filter by.
            application: The application type to filter by.
        
        Returns:
            List of Pigment objects matching both criteria.
        """
        if not isinstance(pigment_type, PigmentType) or not isinstance(application, Application):
            raise ValueError("Invalid pigment type or application. Must be PigmentType and Application enums.")
        
        return [
            pigment for pigment in self.pigments
            if pigment.pigment_type == pigment_type and application in pigment.applications
        ]

def main():
    """Example usage of the PigmentSelector."""
    selector = PigmentSelector()
    
    # Example: Get pigments for plastics
    print("Pigments suitable for plastics:")
    for pigment in selector.get_pigments_by_application(Application.PLASTICS):
        print(f"- {pigment.name} ({pigment.pigment_type.value})")
    
    # Example: Get all fluorescent pigments
    print("\nFluorescent pigments:")
    for pigment in selector.get_pigments_by_type(PigmentType.FLUORESCENT):
        print(f"- {pigment.name}")
    
    # Example: Get anti-corrosive pigments for coatings
    print("\nAnti-corrosive pigments for coatings:")
    for pigment in selector.get_pigments_by_type_and_application(
        PigmentType.ANTI_CORROSIVE, Application.COATINGS
    ):
        print(f"- {pigment.name}")

if __name__ == "__main__":
    main()
```
