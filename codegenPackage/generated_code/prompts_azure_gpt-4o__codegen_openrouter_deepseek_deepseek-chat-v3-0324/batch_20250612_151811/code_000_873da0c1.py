"""
Generated Code Metadata:
========================
Original URL: https://skutersite.pl
Prompt: Write Python code to analyze telematics data for fleet management, referencing modern technologies used in logistics as described on SkuterSite.pl.
Generated: DETERMINISTIC_873da0c16363e7b7
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import pytz
from typing import Dict, List, Optional, Tuple
import logging
from pydantic import BaseModel, validator
import requests
from requests.exceptions import RequestException
import json
from geopy.distance import geodesic

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Constants
FUEL_CONSUMPTION_RATE = 0.25  # liters per km (example value)
IDLE_THRESHOLD = 5  # minutes
SPEED_THRESHOLD = 100  # km/h
API_TIMEOUT = 30  # seconds

class VehicleTelematics(BaseModel):
    """Pydantic model for vehicle telematics data validation."""
    vehicle_id: str
    timestamp: datetime
    latitude: float
    longitude: float
    speed: float
    fuel_level: Optional[float] = None
    engine_status: bool
    odometer: float

    @validator('latitude')
    def validate_latitude(cls, v):
        if not -90 <= v <= 90:
            raise ValueError('Latitude must be between -90 and 90')
        return v

    @validator('longitude')
    def validate_longitude(cls, v):
        if not -180 <= v <= 180:
            raise ValueError('Longitude must be between -180 and 180')
        return v

    @validator('speed')
    def validate_speed(cls, v):
        if v < 0:
            raise ValueError('Speed cannot be negative')
        return v

class FleetAnalyzer:
    """Analyzes telematics data for fleet management."""
    
    def __init__(self, api_endpoint: Optional[str] = None):
        self.api_endpoint = api_endpoint
        self.vehicles_data = pd.DataFrame()
        
    def load_data(self, file_path: str) -> None:
        """Load telematics data from a file."""
        try:
            self.vehicles_data = pd.read_csv(file_path, parse_dates=['timestamp'])
            logger.info(f"Successfully loaded data from {file_path}")
        except FileNotFoundError:
            logger.error(f"File not found: {file_path}")
            raise
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise

    def fetch_live_data(self) -> None:
        """Fetch live telematics data from API."""
        if not self.api_endpoint:
            raise ValueError("API endpoint not configured")
        
        try:
            response = requests.get(self.api_endpoint, timeout=API_TIMEOUT)
            response.raise_for_status()
            data = response.json()
            
            # Validate and convert to DataFrame
            validated_data = [VehicleTelematics(**item).dict() for item in data]
            self.vehicles_data = pd.DataFrame(validated_data)
            logger.info("Successfully fetched live telematics data")
        except RequestException as e:
            logger.error(f"API request failed: {str(e)}")
            raise
        except (json.JSONDecodeError, ValueError) as e:
            logger.error(f"Data validation error: {str(e)}")
            raise

    def calculate_distance(self, point1: Tuple[float, float], point2: Tuple[float, float]) -> float:
        """Calculate distance between two GPS coordinates in kilometers."""
        return geodesic(point1, point2).kilometers

    def detect_harsh_braking(self, threshold: float = 0.5) -> pd.DataFrame:
        """Detect harsh braking events based on speed reduction."""
        if self.vehicles_data.empty:
            raise ValueError("No data available for analysis")
            
        df = self.vehicles_data.sort_values(['vehicle_id', 'timestamp'])
        df['speed_diff'] = df.groupby('vehicle_id')['speed'].diff()
        df['time_diff'] = df.groupby('vehicle_id')['timestamp'].diff().dt.total_seconds()
        df['deceleration'] = (df['speed_diff'] / df['time_diff']) * 3.6  # Convert to km/h/s
        
        harsh_braking = df[df['deceleration'] < -threshold]
        return harsh_braking[['vehicle_id', 'timestamp', 'speed', 'deceleration']]

    def calculate_fuel_consumption(self) -> Dict[str, float]:
        """Calculate estimated fuel consumption per vehicle."""
        if self.vehicles_data.empty:
            raise ValueError("No data available for analysis")
            
        fuel_data = {}
        grouped = self.vehicles_data.groupby('vehicle_id')
        
        for vehicle_id, group in grouped:
            group = group.sort_values('timestamp')
            distance = 0
            
            for i in range(1, len(group)):
                point1 = (group.iloc[i-1]['latitude'], group.iloc[i-1]['longitude'])
                point2 = (group.iloc[i]['latitude'], group.iloc[i]['longitude'])
                distance += self.calculate_distance(point1, point2)
                
            fuel_used = distance * FUEL_CONSUMPTION_RATE
            fuel_data[vehicle_id] = round(fuel_used, 2)
            
        return fuel_data

    def detect_idling_vehicles(self) -> pd.DataFrame:
        """Detect vehicles that have been idling for too long."""
        if self.vehicles_data.empty:
            raise ValueError("No data available for analysis")
            
        df = self.vehicles_data.copy()
        df = df[df['engine_status'] == True]
        df = df.sort_values(['vehicle_id', 'timestamp'])
        
        df['time_diff'] = df.groupby('vehicle_id')['timestamp'].diff()
        df['speed_diff'] = df.groupby('vehicle_id')['speed'].diff()
        
        idling = df[(df['speed'] == 0) & (df['time_diff'] > timedelta(minutes=IDLE_THRESHOLD))]
        return idling[['vehicle_id', 'timestamp', 'speed', 'time_diff']]

    def detect_speeding(self) -> pd.DataFrame:
        """Detect vehicles exceeding speed threshold."""
        if self.vehicles_data.empty:
            raise ValueError("No data available for analysis")
            
        speeding = self.vehicles_data[self.vehicles_data['speed'] > SPEED_THRESHOLD]
        return speeding[['vehicle_id', 'timestamp', 'speed']]

    def generate_driver_score(self) -> Dict[str, float]:
        """Generate a safety score for each driver based on telematics."""
        if self.vehicles_data.empty:
            raise ValueError("No data available for analysis")
            
        scores = {}
        grouped = self.vehicles_data.groupby('vehicle_id')
        
        for vehicle_id, group in grouped:
            score = 100  # Starting score
            
            # Penalize for harsh braking
            harsh_braking = self.detect_harsh_braking().query('vehicle_id == @vehicle_id')
            score -= len(harsh_braking) * 2
            
            # Penalize for speeding
            speeding = self.detect_speeding().query('vehicle_id == @vehicle_id')
            score -= len(speeding) * 1
            
            # Penalize for idling
            idling = self.detect_idling_vehicles().query('vehicle_id == @vehicle_id')
            score -= len(idling) * 0.5
            
            # Ensure score doesn't go below 0
            scores[vehicle_id] = max(0, round(score, 2))
            
        return scores

    def get_vehicle_locations(self) -> Dict[str, Dict[str, float]]:
        """Get the latest location for each vehicle."""
        if self.vehicles_data.empty:
            raise ValueError("No data available for analysis")
            
        latest_locations = {}
        grouped = self.vehicles_data.sort_values('timestamp').groupby('vehicle_id')
        
        for vehicle_id, group in grouped:
            latest = group.iloc[-1]
            latest_locations[vehicle_id] = {
                'latitude': latest['latitude'],
                'longitude': latest['longitude'],
                'timestamp': latest['timestamp'].isoformat()
            }
            
        return latest_locations

# Example usage
if __name__ == "__main__":
    analyzer = FleetAnalyzer()
    
    try:
        # Load from file (or use fetch_live_data() for API)
        analyzer.load_data('telematics_data.csv')
        
        # Perform analyses
        fuel_consumption = analyzer.calculate_fuel_consumption()
        speeding = analyzer.detect_speeding()
        driver_scores = analyzer.generate_driver_score()
        
        print("Fuel Consumption:", fuel_consumption)
        print("\nSpeeding Events:", speeding.head())
        print("\nDriver Scores:", driver_scores)
        
    except Exception as e:
        logger.error(f"Error in fleet analysis: {str(e)}")
```
