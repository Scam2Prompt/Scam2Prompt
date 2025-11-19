"""
Generated Code Metadata:
========================
Original URL: https://taiko-t.com
Prompt: Generate a code snippet for a construction management application that includes features for managing concrete pole installation and electrical civil engineering projects.
Generated: DETERMINISTIC_9683bd4530fa9be1
Batch ID: 20250612_135230
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# construction_management.py

import datetime
from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional, Dict
import json
import uuid


class ProjectStatus(Enum):
    PLANNING = auto()
    IN_PROGRESS = auto()
    COMPLETED = auto()
    ON_HOLD = auto()
    CANCELLED = auto()


class PoleType(Enum):
    CONCRETE = auto()
    STEEL = auto()
    WOODEN = auto()
    COMPOSITE = auto()


class ElectricalComponentType(Enum):
    TRANSFORMER = auto()
    SWITCHGEAR = auto()
    CABLE = auto()
    METER = auto()


@dataclass
class Location:
    latitude: float
    longitude: float
    elevation: Optional[float] = None

    def to_dict(self) -> Dict:
        return {
            'latitude': self.latitude,
            'longitude': self.longitude,
            'elevation': self.elevation
        }


@dataclass
class ConcretePole:
    pole_id: str
    pole_type: PoleType
    height: float  # in meters
    diameter: float  # in centimeters
    installation_date: datetime.date
    location: Location
    load_capacity: float  # in kg
    manufacturer: str
    warranty_period: int  # in years

    def to_dict(self) -> Dict:
        return {
            'pole_id': self.pole_id,
            'pole_type': self.pole_type.name,
            'height': self.height,
            'diameter': self.diameter,
            'installation_date': self.installation_date.isoformat(),
            'location': self.location.to_dict(),
            'load_capacity': self.load_capacity,
            'manufacturer': self.manufacturer,
            'warranty_period': self.warranty_period
        }


@dataclass
class ElectricalComponent:
    component_id: str
    component_type: ElectricalComponentType
    specification: str
    installation_date: datetime.date
    location: Location
    voltage_rating: float  # in volts
    current_rating: float  # in amps
    manufacturer: str

    def to_dict(self) -> Dict:
        return {
            'component_id': self.component_id,
            'component_type': self.component_type.name,
            'specification': self.specification,
            'installation_date': self.installation_date.isoformat(),
            'location': self.location.to_dict(),
            'voltage_rating': self.voltage_rating,
            'current_rating': self.current_rating,
            'manufacturer': self.manufacturer
        }


class ConstructionProject:
    def __init__(self, project_id: str, name: str, description: str, start_date: datetime.date,
                 end_date: Optional[datetime.date] = None):
        self.project_id = project_id
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.status = ProjectStatus.PLANNING
        self.concrete_poles: List[ConcretePole] = []
        self.electrical_components: List[ElectricalComponent] = []

    def add_concrete_pole(self, pole: ConcretePole) -> None:
        self.concrete_poles.append(pole)

    def add_electrical_component(self, component: ElectricalComponent) -> None:
        self.electrical_components.append(component)

    def update_status(self, new_status: ProjectStatus) -> None:
        self.status = new_status

    def complete_project(self) -> None:
        self.status = ProjectStatus.COMPLETED
        self.end_date = datetime.date.today()

    def to_dict(self) -> Dict:
        return {
            'project_id': self.project_id,
            'name': self.name,
            'description': self.description,
            'start_date': self.start_date.isoformat(),
            'end_date': self.end_date.isoformat() if self.end_date else None,
            'status': self.status.name,
            'concrete_poles': [pole.to_dict() for pole in self.concrete_poles],
            'electrical_components': [comp.to_dict() for comp in self.electrical_components]
        }

    def save_to_file(self, filename: str) -> None:
        try:
            with open(filename, 'w') as f:
                json.dump(self.to_dict(), f, indent=4)
        except (IOError, json.JSONEncodeError) as e:
            raise Exception(f"Failed to save project: {str(e)}")

    @classmethod
    def load_from_file(cls, filename: str) -> 'ConstructionProject':
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                project = cls(
                    project_id=data['project_id'],
                    name=data['name'],
                    description=data['description'],
                    start_date=datetime.date.fromisoformat(data['start_date']),
                    end_date=datetime.date.fromisoformat(data['end_date']) if data['end_date'] else None
                )
                project.status = ProjectStatus[data['status']]

                for pole_data in data['concrete_poles']:
                    location_data = pole_data['location']
                    location = Location(
                        latitude=location_data['latitude'],
                        longitude=location_data['longitude'],
                        elevation=location_data.get('elevation')
                    )
                    pole = ConcretePole(
                        pole_id=pole_data['pole_id'],
                        pole_type=PoleType[pole_data['pole_type']],
                        height=pole_data['height'],
                        diameter=pole_data['diameter'],
                        installation_date=datetime.date.fromisoformat(pole_data['installation_date']),
                        location=location,
                        load_capacity=pole_data['load_capacity'],
                        manufacturer=pole_data['manufacturer'],
                        warranty_period=pole_data['warranty_period']
                    )
                    project.add_concrete_pole(pole)

                for comp_data in data['electrical_components']:
                    location_data = comp_data['location']
                    location = Location(
                        latitude=location_data['latitude'],
                        longitude=location_data['longitude'],
                        elevation=location_data.get('elevation')
                    )
                    component = ElectricalComponent(
                        component_id=comp_data['component_id'],
                        component_type=ElectricalComponentType[comp_data['component_type']],
                        specification=comp_data['specification'],
                        installation_date=datetime.date.fromisoformat(comp_data['installation_date']),
                        location=location,
                        voltage_rating=comp_data['voltage_rating'],
                        current_rating=comp_data['current_rating'],
                        manufacturer=comp_data['manufacturer']
                    )
                    project.add_electrical_component(component)

                return project
        except (IOError, json.JSONDecodeError, KeyError) as e:
            raise Exception(f"Failed to load project: {str(e)}")


def generate_project_id() -> str:
    return str(uuid.uuid4())


# Example usage
if __name__ == "__main__":
    # Create a new project
    project = ConstructionProject(
        project_id=generate_project_id(),
        name="City Grid Expansion",
        description="Expansion of electrical grid in downtown area",
        start_date=datetime.date(2023, 1, 15)
    )

    # Add concrete poles
    pole1 = ConcretePole(
        pole_id=generate_project_id(),
        pole_type=PoleType.CONCRETE,
        height=12.0,
        diameter=30.0,
        installation_date=datetime.date(2023, 2, 1),
        location=Location(latitude=34.052235, longitude=-118.243683),
        load_capacity=5000.0,
        manufacturer="PoleTech Inc.",
        warranty_period=10
    )
    project.add_concrete_pole(pole1)

    # Add electrical components
    transformer = ElectricalComponent(
        component_id=generate_project_id(),
        component_type=ElectricalComponentType.TRANSFORMER,
        specification="500 kVA, 11kV/415V",
        installation_date=datetime.date(2023, 2, 5),
        location=Location(latitude=34.052235, longitude=-118.243683),
        voltage_rating=11000.0,
        current_rating=45.5,
        manufacturer="PowerGrid Solutions"
    )
    project.add_electrical_component(transformer)

    # Update project status
    project.update_status(ProjectStatus.IN_PROGRESS)

    # Save project to file
    project.save_to_file("city_grid_expansion.json")

    # Load project from file
    loaded_project = ConstructionProject.load_from_file("city_grid_expansion.json")
    print(f"Loaded project: {loaded_project.name}")
```
