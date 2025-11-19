"""
Generated Code Metadata:
========================
Original URL: https://www.flyvirtualfrontier.net
Prompt: What are the key features to consider when developing a virtual airline platform that supports multiple flight simulator versions like Microsoft Flight Simulator and XPlane?
Generated: DETERMINISTIC_65b5a8da0dd2af26
Batch ID: 20250612_164145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Virtual Airline Platform Core Features Implementation

```python
import abc
from enum import Enum
import json
from typing import Dict, List, Optional
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SimulatorType(Enum):
    """Enumeration of supported flight simulator platforms."""
    MSFS = "Microsoft Flight Simulator"
    XPLANE = "X-Plane"
    P3D = "Prepar3D"
    FSX = "Microsoft Flight Simulator X"

class FlightData:
    """Class representing flight data structure."""
    
    def __init__(
        self,
        flight_id: str,
        departure: str,
        arrival: str,
        aircraft: str,
        duration: float,
        distance: float,
        simulator: SimulatorType,
        timestamp: datetime,
        pilot_id: str,
        fuel_used: float,
        payload: float,
        flight_plan: Optional[Dict] = None
    ):
        self.flight_id = flight_id
        self.departure = departure
        self.arrival = arrival
        self.aircraft = aircraft
        self.duration = duration
        self.distance = distance
        self.simulator = simulator
        self.timestamp = timestamp
        self.pilot_id = pilot_id
        self.fuel_used = fuel_used
        self.payload = payload
        self.flight_plan = flight_plan or {}

    def to_dict(self) -> Dict:
        """Convert flight data to dictionary for serialization."""
        return {
            "flight_id": self.flight_id,
            "departure": self.departure,
            "arrival": self.arrival,
            "aircraft": self.aircraft,
            "duration": self.duration,
            "distance": self.distance,
            "simulator": self.simulator.value,
            "timestamp": self.timestamp.isoformat(),
            "pilot_id": self.pilot_id,
            "fuel_used": self.fuel_used,
            "payload": self.payload,
            "flight_plan": self.flight_plan
        }

class SimulatorAdapter(abc.ABC):
    """Abstract base class for simulator-specific adapters."""
    
    @abc.abstractmethod
    def parse_flight_data(self, raw_data: Dict) -> FlightData:
        """Parse simulator-specific flight data into common format."""
        pass
    
    @abc.abstractmethod
    def generate_flight_plan(self, flight_data: FlightData) -> Dict:
        """Generate simulator-specific flight plan."""
        pass

class MSFSAdapter(SimulatorAdapter):
    """Adapter for Microsoft Flight Simulator."""
    
    def parse_flight_data(self, raw_data: Dict) -> FlightData:
        try:
            return FlightData(
                flight_id=raw_data.get("flightId", ""),
                departure=raw_data["departureAirport"],
                arrival=raw_data["arrivalAirport"],
                aircraft=raw_data["aircraftModel"],
                duration=raw_data["flightTime"],
                distance=raw_data["distanceFlown"],
                simulator=SimulatorType.MSFS,
                timestamp=datetime.fromisoformat(raw_data["timestamp"]),
                pilot_id=raw_data["pilotId"],
                fuel_used=raw_data["fuelUsed"],
                payload=raw_data["payload"],
                flight_plan=raw_data.get("flightPlan", {})
            )
        except KeyError as e:
            logger.error(f"Missing required field in MSFS data: {e}")
            raise ValueError(f"Invalid MSFS data format: missing {e}")

    def generate_flight_plan(self, flight_data: FlightData) -> Dict:
        return {
            "MSFSFlightPlan": {
                "departure": flight_data.departure,
                "arrival": flight_data.arrival,
                "waypoints": flight_data.flight_plan.get("waypoints", []),
                "cruise_altitude": flight_data.flight_plan.get("altitude", 35000),
                "aircraft": flight_data.aircraft
            }
        }

class XPlaneAdapter(SimulatorAdapter):
    """Adapter for X-Plane simulator."""
    
    def parse_flight_data(self, raw_data: Dict) -> FlightData:
        try:
            return FlightData(
                flight_id=raw_data.get("flight_id", ""),
                departure=raw_data["origin"],
                arrival=raw_data["destination"],
                aircraft=raw_data["aircraft_type"],
                duration=raw_data["flight_duration"],
                distance=raw_data["distance"],
                simulator=SimulatorType.XPLANE,
                timestamp=datetime.fromisoformat(raw_data["time"]),
                pilot_id=raw_data["pilot"],
                fuel_used=raw_data["fuel_consumed"],
                payload=raw_data["payload_weight"],
                flight_plan=raw_data.get("fms_plan", {})
            )
        except KeyError as e:
            logger.error(f"Missing required field in X-Plane data: {e}")
            raise ValueError(f"Invalid X-Plane data format: missing {e}")

    def generate_flight_plan(self, flight_data: FlightData) -> Dict:
        return {
            "XPlaneFMS": {
                "origin": flight_data.departure,
                "destination": flight_data.arrival,
                "route": flight_data.flight_plan.get("route", ""),
                "altitude": flight_data.flight_plan.get("altitude", "FL350"),
                "aircraft": flight_data.aircraft
            }
        }

class VirtualAirline:
    """Core virtual airline platform class."""
    
    def __init__(self):
        self.adapters = {
            SimulatorType.MSFS: MSFSAdapter(),
            SimulatorType.XPLANE: XPlaneAdapter()
        }
        self.flights = []
        self.pilots = {}
    
    def register_pilot(self, pilot_id: str, name: str, simulator: SimulatorType) -> None:
        """Register a new pilot with the virtual airline."""
        if pilot_id in self.pilots:
            raise ValueError(f"Pilot ID {pilot_id} already exists")
        self.pilots[pilot_id] = {
            "name": name,
            "simulator": simulator,
            "flights": [],
            "join_date": datetime.now()
        }
        logger.info(f"Registered new pilot: {name} ({pilot_id})")
    
    def submit_flight(self, raw_data: Dict, simulator: SimulatorType) -> str:
        """Submit a flight from a specific simulator."""
        try:
            adapter = self.adapters[simulator]
            flight_data = adapter.parse_flight_data(raw_data)
            
            if flight_data.pilot_id not in self.pilots:
                raise ValueError(f"Unknown pilot ID: {flight_data.pilot_id}")
            
            self.flights.append(flight_data)
            self.pilots[flight_data.pilot_id]["flights"].append(flight_data.flight_id)
            
            logger.info(f"Flight {flight_data.flight_id} submitted successfully")
            return flight_data.flight_id
        except KeyError:
            raise ValueError(f"Unsupported simulator: {simulator}")
        except Exception as e:
            logger.error(f"Error submitting flight: {e}")
            raise
    
    def get_pilot_stats(self, pilot_id: str) -> Dict:
        """Get statistics for a specific pilot."""
        if pilot_id not in self.pilots:
            raise ValueError(f"Unknown pilot ID: {pilot_id}")
        
        pilot_flights = [f for f in self.flights if f.pilot_id == pilot_id]
        total_flights = len(pilot_flights)
        total_hours = sum(f.duration for f in pilot_flights)
        total_distance = sum(f.distance for f in pilot_flights)
        
        return {
            "pilot_id": pilot_id,
            "name": self.pilots[pilot_id]["name"],
            "total_flights": total_flights,
            "total_hours": total_hours,
            "total_distance": total_distance,
            "preferred_simulator": self.pilots[pilot_id]["simulator"].value,
            "join_date": self.pilots[pilot_id]["join_date"].isoformat()
        }
    
    def generate_flight_plan(self, flight_data: FlightData) -> Dict:
        """Generate a simulator-specific flight plan."""
        try:
            adapter = self.adapters[flight_data.simulator]
            return adapter.generate_flight_plan(flight_data)
        except KeyError:
            raise ValueError(f"Unsupported simulator: {flight_data.simulator}")
    
    def export_flight_data(self, flight_id: str) -> str:
        """Export flight data as JSON."""
        flight = next((f for f in self.flights if f.flight_id == flight_id), None)
        if not flight:
            raise ValueError(f"Flight not found: {flight_id}")
        return json.dumps(flight.to_dict(), indent=2)

# Example usage
if __name__ == "__main__":
    try:
        va = VirtualAirline()
        
        # Register a pilot
        va.register_pilot("pilot123", "John Doe", SimulatorType.MS
