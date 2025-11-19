"""
Generated Code Metadata:
========================
Original URL: https://www.flyvirtualfrontier.net
Prompt: Provide a step-by-step guide to implement automated operations for virtual airlines, including route planning and PIREP filing, inspired by vFrontier's approach.
Generated: DETERMINISTIC_2e5cb4aed197b225
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Automated Operations for Virtual Airlines
Inspired by vFrontier's approach

This script provides functionality for:
1. Route planning
2. PIREP (Pilot Report) filing
3. Automated operations management
"""

import json
import requests
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import logging
from enum import Enum

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class FlightPhase(Enum):
    """Enum for flight phases"""
    PREFLIGHT = "Preflight"
    TAXI = "Taxi"
    TAKEOFF = "Takeoff"
    CLIMB = "Climb"
    CRUISE = "Cruise"
    DESCENT = "Descent"
    LANDING = "Landing"
    PARKED = "Parked"

class Aircraft:
    """Class representing an aircraft"""
    
    def __init__(self, registration: str, model: str, max_range: float, fuel_capacity: float):
        """
        Initialize aircraft
        
        Args:
            registration: Aircraft registration number
            model: Aircraft model
            max_range: Maximum range in nautical miles
            fuel_capacity: Fuel capacity in gallons
        """
        self.registration = registration
        self.model = model
        self.max_range = max_range
        self.fuel_capacity = fuel_capacity

class Airport:
    """Class representing an airport"""
    
    def __init__(self, icao: str, name: str, latitude: float, longitude: float):
        """
        Initialize airport
        
        Args:
            icao: ICAO code
            name: Airport name
            latitude: Latitude coordinate
            longitude: Longitude coordinate
        """
        self.icao = icao
        self.name = name
        self.latitude = latitude
        self.longitude = longitude

class RoutePlanner:
    """Handles route planning operations"""
    
    def __init__(self, airports_db: Dict[str, Airport]):
        """
        Initialize route planner
        
        Args:
            airports_db: Dictionary of Airport objects keyed by ICAO code
        """
        self.airports_db = airports_db
    
    def calculate_distance(self, icao1: str, icao2: str) -> float:
        """
        Calculate distance between two airports in nautical miles
        
        Args:
            icao1: Departure airport ICAO
            icao2: Arrival airport ICAO
            
        Returns:
            Distance in nautical miles
            
        Raises:
            ValueError: If either airport is not found
        """
        if icao1 not in self.airports_db or icao2 not in self.airports_db:
            raise ValueError("One or both airports not found in database")
            
        airport1 = self.airports_db[icao1]
        airport2 = self.airports_db[icao2]
        
        # Haversine formula implementation
        lat1, lon1 = airport1.latitude, airport1.longitude
        lat2, lon2 = airport2.latitude, airport2.longitude
        
        # Convert to radians
        lat1, lon1, lat2, lon2 = map(
            lambda x: x * 0.0174533, [lat1, lon1, lat2, lon2]
        )
        
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        
        a = (pow(math.sin(dlat / 2), 2) + 
             math.cos(lat1) * math.cos(lat2) * 
             pow(math.sin(dlon / 2), 2))
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        
        # Earth radius in nautical miles
        distance = 3440 * c
        return distance
    
    def plan_route(
        self, 
        origin: str, 
        destination: str, 
        aircraft: Aircraft,
        max_leg_distance: float = 800.0
    ) -> List[str]:
        """
        Plan a route between two airports with possible stops
        
        Args:
            origin: Starting airport ICAO
            destination: Destination airport ICAO
            aircraft: Aircraft being used
            max_leg_distance: Maximum distance per leg
            
        Returns:
            List of ICAO codes representing the route
            
        Raises:
            ValueError: If route cannot be planned
        """
        if origin not in self.airports_db or destination not in self.airports_db:
            raise ValueError("Origin or destination airport not found")
            
        total_distance = self.calculate_distance(origin, destination)
        
        # Direct flight possible
        if total_distance <= aircraft.max_range and total_distance <= max_leg_distance:
            return [origin, destination]
            
        # Need intermediate stops
        route = [origin]
        current_pos = origin
        
        while current_pos != destination:
            # Find suitable next airport
            next_airport = self._find_next_airport(
                current_pos, 
                destination, 
                aircraft, 
                max_leg_distance
            )
            
            if not next_airport:
                raise ValueError("Cannot plan route with given constraints")
                
            route.append(next_airport)
            current_pos = next_airport
            
        return route
    
    def _find_next_airport(
        self, 
        current: str, 
        destination: str, 
        aircraft: Aircraft, 
        max_leg_distance: float
    ) -> Optional[str]:
        """
        Find next suitable airport along route
        
        Args:
            current: Current airport ICAO
            destination: Final destination ICAO
            aircraft: Aircraft being used
            max_leg_distance: Maximum leg distance
            
        Returns:
            ICAO code of next airport or None if none found
        """
        current_airport = self.airports_db[current]
        dest_airport = self.airports_db[destination]
        
        # Get airports within max_leg_distance sorted by proximity to destination
        candidates = []
        
        for icao, airport in self.airports_db.items():
            if icao == current:
                continue
                
            distance = self.calculate_distance(current, icao)
            if distance <= max_leg_distance and distance <= aircraft.max_range:
                progress = self.calculate_distance(icao, destination)
                candidates.append((icao, progress))
        
        if not candidates:
            return None
            
        # Select airport that makes most progress toward destination
        candidates.sort(key=lambda x: x[1])
        return candidates[0][0]

class PIREP:
    """Class representing a Pilot Report"""
    
    def __init__(
        self, 
        flight_number: str, 
        departure: str, 
        arrival: str, 
        aircraft: str,
        pilot_id: str
    ):
        """
        Initialize PIREP
        
        Args:
            flight_number: Flight number
            departure: Departure airport ICAO
            arrival: Arrival airport ICAO
            aircraft: Aircraft registration
            pilot_id: Pilot identifier
        """
        self.flight_number = flight_number
        self.departure = departure
        self.arrival = arrival
        self.aircraft = aircraft
        self.pilot_id = pilot_id
        self.departure_time = None
        self.arrival_time = None
        self.fuel_used = 0.0
        self.distance = 0.0
        self.flight_phase = FlightPhase.PREFLIGHT
        self.notes = ""
    
    def update_flight_phase(self, phase: FlightPhase):
        """Update current flight phase"""
        self.flight_phase = phase
        logger.info(f"Flight {self.flight_number} phase changed to {phase.value}")
        
        if phase == FlightPhase.TAKEOFF and not self.departure_time:
            self.departure_time = datetime.utcnow()
        elif phase == FlightPhase.PARKED and not self.arrival_time:
            self.arrival_time = datetime.utcnow()
    
    def add_note(self, note: str):
        """Add note to PIREP"""
        self.notes += f"{datetime.utcnow().isoformat()}: {note}\n"
    
    def calculate_distance(self, route_planner: RoutePlanner) -> float:
        """Calculate flight distance"""
        try:
            self.distance = route_planner.calculate_distance(
                self.departure, 
                self.arrival
            )
            return self.distance
        except ValueError as e:
            logger.error(f"Error calculating distance: {e}")
            return 0.0
    
    def to_dict(self) -> Dict:
        """Convert PIREP to dictionary for serialization"""
        return {
            "flight_number": self.flight_number,
            "departure": self.departure,
            "arrival": self.arrival,
            "aircraft": self.aircraft,
            "pilot_id": self.pilot_id,
            "departure_time": self.departure_time.isoformat() if self.departure
