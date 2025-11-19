"""
Generated Code Metadata:
========================
Original URL: https://luxeratravel.com
Prompt: "Design a system to curate exquisite travel itineraries based on client-centric planning experiences, using Luxera Travel's approach as a model."
Generated: DETERMINISTIC_2f997a6848e70872
Batch ID: 20250622_205955
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import List, Dict, Optional
import uuid
from enum import Enum

class TravelPreference(Enum):
    ADVENTURE = "Adventure"
    LUXURY = "Luxury"
    CULTURAL = "Cultural"
    RELAXATION = "Relaxation"
    FAMILY = "Family"
    ROMANTIC = "Romantic"

class BudgetLevel(Enum):
    ECONOMY = "Economy"
    STANDARD = "Standard"
    PREMIUM = "Premium"
    LUXURY = "Luxury"

class Activity:
    def __init__(self, name: str, description: str, duration_hours: float, cost: float):
        self.id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.duration_hours = duration_hours
        self.cost = cost

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "duration_hours": self.duration_hours,
            "cost": self.cost
        }

class Accommodation:
    def __init__(self, name: str, description: str, cost_per_night: float, rating: float):
        self.id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.cost_per_night = cost_per_night
        self.rating = rating

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "cost_per_night": self.cost_per_night,
            "rating": self.rating
        }

class Transportation:
    def __init__(self, mode: str, description: str, cost: float, duration_hours: float):
        self.id = str(uuid.uuid4())
        self.mode = mode
        self.description = description
        self.cost = cost
        self.duration_hours = duration_hours

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "mode": self.mode,
            "description": self.description,
            "cost": self.cost,
            "duration_hours": self.duration_hours
        }

class DayItinerary:
    def __init__(self, date: datetime):
        self.id = str(uuid.uuid4())
        self.date = date
        self.activities: List[Activity] = []
        self.accommodation: Optional[Accommodation] = None
        self.transportation: List[Transportation] = []

    def add_activity(self, activity: Activity) -> None:
        self.activities.append(activity)

    def set_accommodation(self, accommodation: Accommodation) -> None:
        self.accommodation = accommodation

    def add_transportation(self, transportation: Transportation) -> None:
        self.transportation.append(transportation)

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "date": self.date.strftime("%Y-%m-%d"),
            "activities": [activity.to_dict() for activity in self.activities],
            "accommodation": self.accommodation.to_dict() if self.accommodation else None,
            "transportation": [transport.to_dict() for transport in self.transportation]
        }

class TravelItinerary:
    def __init__(self, client_name: str, destination: str, start_date: datetime, end_date: datetime):
        self.id = str(uuid.uuid4())
        self.client_name = client_name
        self.destination = destination
        self.start_date = start_date
        self.end_date = end_date
        self.preferences: List[TravelPreference] = []
        self.budget_level: Optional[BudgetLevel] = None
        self.day_itineraries: List[DayItinerary] = []

    def add_preference(self, preference: TravelPreference) -> None:
        self.preferences.append(preference)

    def set_budget_level(self, budget_level: BudgetLevel) -> None:
        self.budget_level = budget_level

    def add_day_itinerary(self, day_itinerary: DayItinerary) -> None:
        if day_itinerary.date < self.start_date or day_itinerary.date > self.end_date:
            raise ValueError("Day itinerary date must be within the travel period")
        self.day_itineraries.append(day_itinerary)

    def calculate_total_cost(self) -> float:
        total_cost = 0.0
        for day in self.day_itineraries:
            if day.accommodation:
                total_cost += day.accommodation.cost_per_night
            for activity in day.activities:
                total_cost += activity.cost
            for transport in day.transportation:
                total_cost += transport.cost
        return total_cost

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "client_name": self.client_name,
            "destination": self.destination,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d"),
            "preferences": [pref.value for pref in self.preferences],
            "budget_level": self.budget_level.value if self.budget_level else None,
            "day_itineraries": [day.to_dict() for day in self.day_itineraries],
            "total_cost": self.calculate_total_cost()
        }

    def save_to_file(self, filename: str) -> None:
        with open(filename, 'w') as f:
            json.dump(self.to_dict(), f, indent=2)

    @classmethod
    def load_from_file(cls, filename: str) -> 'TravelItinerary':
        with open(filename, 'r') as f:
            data = json.load(f)
        
        start_date = datetime.strptime(data['start_date'], "%Y-%m-%d")
        end_date = datetime.strptime(data['end_date'], "%Y-%m-%d")
        itinerary = cls(data['client_name'], data['destination'], start_date, end_date)
        
        for pref in data['preferences']:
            itinerary.add_preference(TravelPreference(pref))
        
        if data['budget_level']:
            itinerary.set_budget_level(BudgetLevel(data['budget_level']))
        
        for day_data in data['day_itineraries']:
            day_date = datetime.strptime(day_data['date'], "%Y-%m-%d")
            day_itinerary = DayItinerary(day_date)
            
            if day_data['accommodation']:
                acc_data = day_data['accommodation']
                accommodation = Accommodation(
                    acc_data['name'],
                    acc_data['description'],
                    acc_data['cost_per_night'],
                    acc_data['rating']
                )
                day_itinerary.set_accommodation(accommodation)
            
            for act_data in day_data['activities']:
                activity = Activity(
                    act_data['name'],
                    act_data['description'],
                    act_data['duration_hours'],
                    act_data['cost']
                )
                day_itinerary.add_activity(activity)
            
            for trans_data in day_data['transportation']:
                transport = Transportation(
                    trans_data['mode'],
                    trans_data['description'],
                    trans_data['cost'],
                    trans_data['duration_hours']
                )
                day_itinerary.add_transportation(transport)
            
            itinerary.add_day_itinerary(day_itinerary)
        
        return itinerary

class ItineraryBuilder:
    def __init__(self):
        self.itinerary = None

    def create_new_itinerary(self, client_name: str, destination: str, start_date: datetime, end_date: datetime) -> None:
        self.itinerary = TravelItinerary(client_name, destination, start_date, end_date)

    def add_preference(self, preference: TravelPreference) -> None:
        if not self.itinerary:
            raise ValueError("No itinerary created yet")
        self.itinerary.add_preference(preference)

    def set_budget_level(self, budget_level: BudgetLevel) -> None:
        if not self.itinerary:
            raise ValueError("No itinerary created yet")
        self.itinerary.set_budget_level(budget_level)

    def add_day_itinerary(self, day_itinerary: DayItinerary) -> None:
        if not self.itinerary:
            raise ValueError("No itinerary created yet")
        self.itinerary.add_day_itinerary(day_itinerary)

    def get_itinerary(self) -> TravelItinerary:
        if not self.itinerary:
            raise ValueError("No itinerary created yet")
        return self.itinerary

class ItineraryRecommendationEngine:
    def __init__(self):
        self.activity_database = []
        self.accommodation_database = []
        self.transportation_database = []

    def load_databases(self, activities_file: str, accommodations_file: str, transport_file: str) -> None:
        try:
            with open(activities_file, 'r') as f:
                activities_data = json.load(f)
                self.activity_d
