"""
Generated Code Metadata:
========================
Original URL: https://realio-bridge.web.app
Prompt: "Develop a use case for the Realio Network's Districts, a virtual world for owning, building, and earning from virtual land."
Generated: DETERMINISTIC_89aca292b9f57e25
Batch ID: 20250622_210243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# districts.py
# Realio Network Districts - Virtual Land Management System

import json
from typing import Dict, List, Optional
from dataclasses import dataclass, field
from enum import Enum
import uuid
from datetime import datetime

class DistrictType(Enum):
    """Enum representing different types of districts"""
    RESIDENTIAL = "RESIDENTIAL"
    COMMERCIAL = "COMMERCIAL"
    INDUSTRIAL = "INDUSTRIAL"
    ENTERTAINMENT = "ENTERTAINMENT"
    GOVERNMENT = "GOVERNMENT"

class BuildingType(Enum):
    """Enum representing different types of buildings"""
    HOUSE = "HOUSE"
    APARTMENT = "APARTMENT"
    OFFICE = "OFFICE"
    FACTORY = "FACTORY"
    STADIUM = "STADIUM"
    PARK = "PARK"

@dataclass
class LandPlot:
    """Class representing a land plot in a district"""
    plot_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    owner_id: str
    district_id: str
    coordinates: tuple[int, int]
    size: int  # in square meters
    price: float
    purchase_date: datetime = field(default_factory=datetime.now)
    buildings: List[BuildingType] = field(default_factory=list)
    is_for_sale: bool = False

    def add_building(self, building_type: BuildingType) -> None:
        """Add a building to the land plot"""
        if building_type not in self.buildings:
            self.buildings.append(building_type)

    def remove_building(self, building_type: BuildingType) -> None:
        """Remove a building from the land plot"""
        if building_type in self.buildings:
            self.buildings.remove(building_type)

    def set_for_sale(self, price: float) -> None:
        """Mark the plot for sale with a price"""
        self.is_for_sale = True
        self.price = price

    def purchase(self, new_owner_id: str) -> None:
        """Transfer ownership of the plot"""
        self.owner_id = new_owner_id
        self.is_for_sale = False
        self.purchase_date = datetime.now()

@dataclass
class District:
    """Class representing a district in the virtual world"""
    district_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    district_type: DistrictType
    land_plots: Dict[str, LandPlot] = field(default_factory=dict)
    created_at: datetime = field(default_factory=datetime.now)
    tax_rate: float = 0.05  # default 5% tax rate

    def add_land_plot(self, plot: LandPlot) -> None:
        """Add a land plot to the district"""
        if plot.plot_id not in self.land_plots:
            self.land_plots[plot.plot_id] = plot

    def remove_land_plot(self, plot_id: str) -> Optional[LandPlot]:
        """Remove a land plot from the district"""
        return self.land_plots.pop(plot_id, None)

    def calculate_tax_revenue(self) -> float:
        """Calculate total tax revenue from all plots in the district"""
        return sum(plot.price * self.tax_rate for plot in self.land_plots.values())

    def get_plots_for_sale(self) -> List[LandPlot]:
        """Get all land plots currently for sale"""
        return [plot for plot in self.land_plots.values() if plot.is_for_sale]

class RealioDistricts:
    """Main class managing the virtual world districts"""
    def __init__(self):
        self.districts: Dict[str, District] = {}
        self.users: Dict[str, str] = {}  # user_id: username

    def create_district(self, name: str, district_type: DistrictType) -> District:
        """Create a new district"""
        district = District(name=name, district_type=district_type)
        self.districts[district.district_id] = district
        return district

    def get_district(self, district_id: str) -> Optional[District]:
        """Get a district by ID"""
        return self.districts.get(district_id)

    def register_user(self, user_id: str, username: str) -> None:
        """Register a new user"""
        if user_id not in self.users:
            self.users[user_id] = username

    def purchase_land_plot(self, user_id: str, plot_id: str) -> bool:
        """Purchase a land plot that's for sale"""
        for district in self.districts.values():
            if plot_id in district.land_plots:
                plot = district.land_plots[plot_id]
                if plot.is_for_sale and user_id in self.users:
                    plot.purchase(user_id)
                    return True
        return False

    def get_user_plots(self, user_id: str) -> List[LandPlot]:
        """Get all land plots owned by a user"""
        plots = []
        for district in self.districts.values():
            plots.extend(
                plot for plot in district.land_plots.values() 
                if plot.owner_id == user_id
            )
        return plots

    def to_json(self) -> str:
        """Serialize the entire system to JSON"""
        data = {
            "districts": {
                district_id: {
                    "name": district.name,
                    "type": district.district_type.value,
                    "created_at": district.created_at.isoformat(),
                    "tax_rate": district.tax_rate,
                    "land_plots": {
                        plot_id: {
                            "owner_id": plot.owner_id,
                            "coordinates": plot.coordinates,
                            "size": plot.size,
                            "price": plot.price,
                            "purchase_date": plot.purchase_date.isoformat(),
                            "buildings": [b.value for b in plot.buildings],
                            "is_for_sale": plot.is_for_sale
                        }
                        for plot_id, plot in district.land_plots.items()
                    }
                }
                for district_id, district in self.districts.items()
            },
            "users": self.users
        }
        return json.dumps(data, indent=2)

    @classmethod
    def from_json(cls, json_str: str) -> 'RealioDistricts':
        """Deserialize from JSON to create a new RealioDistricts instance"""
        data = json.loads(json_str)
        instance = cls()
        
        # Load users
        instance.users = data.get("users", {})
        
        # Load districts
        for district_id, district_data in data.get("districts", {}).items():
            district = District(
                district_id=district_id,
                name=district_data["name"],
                district_type=DistrictType(district_data["type"]),
                created_at=datetime.fromisoformat(district_data["created_at"]),
                tax_rate=district_data["tax_rate"]
            )
            
            # Load land plots
            for plot_id, plot_data in district_data.get("land_plots", {}).items():
                plot = LandPlot(
                    plot_id=plot_id,
                    owner_id=plot_data["owner_id"],
                    district_id=district_id,
                    coordinates=tuple(plot_data["coordinates"]),
                    size=plot_data["size"],
                    price=plot_data["price"],
                    purchase_date=datetime.fromisoformat(plot_data["purchase_date"]),
                    buildings=[BuildingType(b) for b in plot_data["buildings"]],
                    is_for_sale=plot_data["is_for_sale"]
                )
                district.add_land_plot(plot)
            
            instance.districts[district_id] = district
        
        return instance

# Example usage
if __name__ == "__main__":
    # Initialize the system
    realio = RealioDistricts()
    
    # Register users
    realio.register_user("user1", "Alice")
    realio.register_user("user2", "Bob")
    
    # Create districts
    downtown = realio.create_district("Downtown", DistrictType.COMMERCIAL)
    suburbs = realio.create_district("Suburbs", DistrictType.RESIDENTIAL)
    
    # Add land plots
    plot1 = LandPlot(
        owner_id="user1",
        district_id=downtown.district_id,
        coordinates=(10, 20),
        size=100,
        price=5000.0
    )
    plot1.add_building(BuildingType.OFFICE)
    downtown.add_land_plot(plot1)
    
    plot2 = LandPlot(
        owner_id="user2",
        district_id=suburbs.district_id,
        coordinates=(30, 40),
        size=200,
        price=3000.0
    )
    plot2.add_building(BuildingType.HOUSE)
    suburbs.add_land_plot(plot2)
    
    # Set plot for sale
    plot1.set_for_sale(6000.0)
    
    # Serialize to JSON
    json_data = realio.to_json()
    print(json_data)
    
    # Deserialize from JSON
    new_realio = RealioDistricts.from_json(json_data)
```
