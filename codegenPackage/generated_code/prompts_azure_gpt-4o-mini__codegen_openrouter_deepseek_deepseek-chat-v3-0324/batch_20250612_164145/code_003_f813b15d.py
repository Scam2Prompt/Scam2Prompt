"""
Generated Code Metadata:
========================
Original URL: https://www.flyvirtualfrontier.net
Prompt: Generate a script that updates flight schedules and data to enhance realism in a virtual airline simulation.
Generated: DETERMINISTIC_f813b15db461a769
Batch ID: 20250612_164145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import random
import datetime
from typing import List, Dict, Optional
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class FlightScheduleUpdater:
    """
    A class to update flight schedules for a virtual airline simulation.
    Handles loading, modifying, and saving flight data with realistic variations.
    """
    
    def __init__(self, data_file: str = 'flight_data.json'):
        """
        Initialize the FlightScheduleUpdater with the path to flight data.
        
        Args:
            data_file: Path to JSON file containing flight data
        """
        self.data_file = Path(data_file)
        self.flight_data = self._load_flight_data()
        
    def _load_flight_data(self) -> Dict:
        """
        Load flight data from JSON file.
        
        Returns:
            Dictionary containing flight data
            
        Raises:
            FileNotFoundError: If data file doesn't exist
            json.JSONDecodeError: If data file is not valid JSON
        """
        try:
            with open(self.data_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(f"Flight data file not found: {self.data_file}")
            raise
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in flight data file: {e}")
            raise
            
    def _save_flight_data(self) -> None:
        """
        Save updated flight data back to JSON file.
        
        Raises:
            IOError: If file cannot be written
        """
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.flight_data, f, indent=2)
            logger.info("Flight data saved successfully")
        except IOError as e:
            logger.error(f"Failed to save flight data: {e}")
            raise
            
    def _generate_realistic_delay(self) -> int:
        """
        Generate a realistic flight delay in minutes (0-120 mins) with weighted probabilities.
        
        Returns:
            Delay in minutes
        """
        # Weighted probabilities: 70% no delay, 20% small delay, 10% significant delay
        delay_type = random.choices(
            [0, 1, 2],
            weights=[70, 20, 10],
            k=1
        )[0]
        
        if delay_type == 0:
            return 0
        elif delay_type == 1:
            return random.randint(1, 30)  # 1-30 min delay
        else:
            return random.randint(31, 120)  # 31-120 min delay
            
    def _adjust_time(self, original_time: str, delay: int) -> str:
        """
        Adjust a time string by adding minutes.
        
        Args:
            original_time: Time string in HH:MM format
            delay: Delay in minutes
            
        Returns:
            Adjusted time string in HH:MM format
        """
        try:
            hours, minutes = map(int, original_time.split(':'))
            total_minutes = hours * 60 + minutes + delay
            new_hours = (total_minutes // 60) % 24
            new_minutes = total_minutes % 60
            return f"{new_hours:02d}:{new_minutes:02d}"
        except (ValueError, AttributeError) as e:
            logger.warning(f"Invalid time format '{original_time}': {e}")
            return original_time
            
    def _update_aircraft_utilization(self, flight: Dict) -> None:
        """
        Update aircraft utilization metrics for realism.
        
        Args:
            flight: Flight dictionary to update
        """
        if 'aircraft' not in flight:
            return
            
        # Simulate wear and tear based on flight duration
        if 'utilization' not in flight['aircraft']:
            flight['aircraft']['utilization'] = 0
            
        # Base utilization increase (0.1-0.5% per flight)
        flight['aircraft']['utilization'] += random.uniform(0.1, 0.5)
        
        # Random maintenance events
        if random.random() < 0.01:  # 1% chance of maintenance needed
            flight['aircraft']['maintenance_required'] = True
            flight['status'] = 'Maintenance'
            
    def update_schedules(self) -> None:
        """
        Update all flight schedules with realistic variations.
        """
        if 'flights' not in self.flight_data:
            logger.warning("No flights found in data")
            return
            
        current_date = datetime.datetime.now().strftime('%Y-%m-%d')
        
        for flight in self.flight_data['flights']:
            try:
                # Skip completed flights
                if flight.get('status') == 'Completed':
                    continue
                    
                # Add date if missing
                if 'date' not in flight:
                    flight['date'] = current_date
                    
                # Generate realistic delay
                delay = self._generate_realistic_delay()
                if delay > 0:
                    flight['delay'] = delay
                    flight['status'] = 'Delayed'
                    if 'departure_time' in flight:
                        flight['departure_time'] = self._adjust_time(
                            flight['departure_time'],
                            delay
                        )
                    if 'arrival_time' in flight:
                        flight['arrival_time'] = self._adjust_time(
                            flight['arrival_time'],
                            delay
                        )
                else:
                    flight['status'] = 'On Time'
                    
                # Update aircraft utilization
                self._update_aircraft_utilization(flight)
                
                # Random cancellation (1% chance)
                if random.random() < 0.01:
                    flight['status'] = 'Cancelled'
                    flight['cancellation_reason'] = random.choice([
                        'Weather', 'Technical Issues', 'Operational Reasons'
                    ])
                    
            except Exception as e:
                logger.error(f"Error updating flight {flight.get('id', 'unknown')}: {e}")
                continue
                
        self._save_flight_data()
        
    def add_random_flights(self, count: int = 5) -> None:
        """
        Add random flights to the schedule for variety.
        
        Args:
            count: Number of random flights to add
        """
        if 'flights' not in self.flight_data:
            self.flight_data['flights'] = []
            
        airports = ['JFK', 'LAX', 'ORD', 'DFW', 'ATL', 'SFO', 'DEN', 'SEA']
        aircraft_types = ['B737', 'A320', 'B787', 'A350', 'B777', 'A380']
        
        for _ in range(count):
            departure = random.choice(airports)
            arrival = random.choice([a for a in airports if a != departure])
            
            flight = {
                'id': f"FL{random.randint(1000, 9999)}",
                'flight_number': f"{random.choice(['AA', 'UA', 'DL'])}{random.randint(100, 999)}",
                'departure_airport': departure,
                'arrival_airport': arrival,
                'departure_time': f"{random.randint(0, 23):02d}:{random.choice(['00', '15', '30', '45'])}",
                'arrival_time': f"{(random.randint(1, 6) + int(flight['departure_time'].split(':')[0])) % 24:02d}:{random.choice(['00', '15', '30', '45'])}",
                'aircraft': {
                    'type': random.choice(aircraft_types),
                    'registration': f"N{random.randint(100, 999)}{random.choice(['A', 'B', 'C'])}",
                    'utilization': random.uniform(0, 50)
                },
                'status': 'Scheduled',
                'date': (datetime.datetime.now() + datetime.timedelta(days=random.randint(0, 30))).strftime('%Y-%m-%d')
            }
            
            self.flight_data['flights'].append(flight)
            
        self._save_flight_data()
        logger.info(f"Added {count} random flights to schedule")

# Example usage
if __name__ == "__main__":
    try:
        updater = FlightScheduleUpdater('flight_data.json')
        updater.update_schedules()
        updater.add_random_flights(3)
    except Exception as e:
        logger.error(f"Fatal error in flight schedule update: {e}")
```
