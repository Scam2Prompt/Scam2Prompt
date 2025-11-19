"""
Generated Code Metadata:
========================
Original URL: https://sarl-verdier-irrigation.fr
Prompt: Write Python code to simulate an irrigation scheduling system for agricultural fields, incorporating parameters like soil moisture and rainfall, as described by SARL VERDIER IRRIGATION's focus on agricultural irrigation solutions.
Generated: DETERMINISTIC_4acefe78cc4d5ffa
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import time
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import random
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class IrrigationSystem:
    """Simulates an irrigation scheduling system for agricultural fields."""

    def __init__(self, config_file: str = 'config.json'):
        """
        Initialize the irrigation system with configuration.
        
        Args:
            config_file: Path to JSON configuration file.
        """
        self.config = self._load_config(config_file)
        self.fields = self._initialize_fields()
        self.weather_data = self._initialize_weather_data()
        self.irrigation_log = []

    def _load_config(self, config_file: str) -> Dict:
        """Load configuration from JSON file."""
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(f"Config file {config_file} not found.")
            raise
        except json.JSONDecodeError:
            logger.error(f"Invalid JSON in config file {config_file}.")
            raise

    def _initialize_fields(self) -> Dict[str, Dict]:
        """Initialize field data from configuration."""
        fields = {}
        for field in self.config['fields']:
            fields[field['id']] = {
                'name': field['name'],
                'crop_type': field['crop_type'],
                'area_hectares': field['area_hectares'],
                'soil_type': field['soil_type'],
                'current_moisture': field.get('initial_moisture', 50.0),
                'optimal_moisture_range': field['optimal_moisture_range'],
                'irrigation_system': field['irrigation_system'],
                'last_irrigation': None,
                'irrigation_history': []
            }
        return fields

    def _initialize_weather_data(self) -> Dict[str, List]:
        """Initialize weather data for simulation."""
        weather = {
            'forecast': [],
            'historical': []
        }
        
        # Generate 7 days of forecast
        for i in range(7):
            weather['forecast'].append({
                'date': (datetime.now() + timedelta(days=i)).strftime('%Y-%m-%d'),
                'temperature': random.uniform(15, 35),
                'rainfall': max(0, random.gauss(5, 3)),  # No negative rainfall
                'humidity': random.uniform(30, 90)
            })
        
        # Generate 30 days of historical data
        for i in range(30):
            weather['historical'].append({
                'date': (datetime.now() - timedelta(days=30-i)).strftime('%Y-%m-%d'),
                'temperature': random.uniform(10, 40),
                'rainfall': max(0, random.gauss(4, 3)),
                'humidity': random.uniform(25, 95)
            })
        
        return weather

    def get_soil_moisture(self, field_id: str) -> float:
        """Get current soil moisture for a field."""
        return self.fields[field_id]['current_moisture']

    def update_soil_moisture(self, field_id: str, rainfall: float, irrigation: float = 0.0) -> None:
        """
        Update soil moisture based on rainfall and irrigation.
        
        Args:
            field_id: ID of the field to update
            rainfall: Amount of rainfall in mm
            irrigation: Amount of irrigation water applied in mm
        """
        field = self.fields[field_id]
        
        # Calculate moisture change based on soil type
        soil_factors = {
            'sand': 0.6,
            'loam': 0.8,
            'clay': 1.0
        }
        factor = soil_factors.get(field['soil_type'], 0.7)
        
        # Update moisture (simplified model)
        moisture_increase = (rainfall + irrigation) * factor
        field['current_moisture'] = min(
            100.0,
            field['current_moisture'] + moisture_increase
        )
        
        # Natural moisture decrease (evaporation, plant uptake)
        field['current_moisture'] = max(
            0.0,
            field['current_moisture'] - random.uniform(1.0, 3.0)
        )
        
        logger.info(f"Updated moisture for field {field_id}: {field['current_moisture']:.1f}%")

    def needs_irrigation(self, field_id: str) -> bool:
        """Check if a field needs irrigation based on moisture levels."""
        field = self.fields[field_id]
        optimal_min, optimal_max = field['optimal_moisture_range']
        current = field['current_moisture']
        
        # Check if moisture is below optimal range
        if current < optimal_min:
            return True
        
        # Check if it's been too long since last irrigation (if applicable)
        if field['last_irrigation']:
            days_since = (datetime.now() - field['last_irrigation']).days
            if days_since > self.config.get('max_days_between_irrigation', 7):
                return True
        
        return False

    def calculate_irrigation_amount(self, field_id: str) -> float:
        """Calculate required irrigation amount in mm."""
        field = self.fields[field_id]
        optimal_min, _ = field['optimal_moisture_range']
        deficit = optimal_min - field['current_moisture']
        
        if deficit <= 0:
            return 0.0
        
        # Adjust based on soil type and crop
        soil_factors = {
            'sand': 1.2,
            'loam': 1.0,
            'clay': 0.8
        }
        crop_factors = {
            'wheat': 1.0,
            'corn': 1.2,
            'soybean': 0.9,
            'vegetables': 1.3
        }
        
        soil_factor = soil_factors.get(field['soil_type'], 1.0)
        crop_factor = crop_factors.get(field['crop_type'], 1.0)
        
        return max(0.0, deficit * soil_factor * crop_factor)

    def irrigate_field(self, field_id: str, amount: float) -> None:
        """
        Simulate irrigating a field with specified amount of water.
        
        Args:
            field_id: ID of the field to irrigate
            amount: Amount of water to apply in mm
        """
        if amount <= 0:
            logger.info(f"No irrigation needed for field {field_id}")
            return
            
        field = self.fields[field_id]
        logger.info(f"Irrigating field {field_id} ({field['name']}) with {amount:.1f}mm")
        
        # Update field data
        field['last_irrigation'] = datetime.now()
        field['irrigation_history'].append({
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'amount': amount,
            'system': field['irrigation_system']
        })
        
        # Update soil moisture
        self.update_soil_moisture(field_id, 0, amount)
        
        # Log irrigation
        self.irrigation_log.append({
            'timestamp': datetime.now().isoformat(),
            'field_id': field_id,
            'field_name': field['name'],
            'amount': amount,
            'system': field['irrigation_system']
        })

    def run_daily_schedule(self) -> None:
        """Run daily irrigation scheduling for all fields."""
        logger.info("Running daily irrigation schedule")
        
        # Get today's weather
        today_weather = next(
            (day for day in self.weather_data['forecast'] 
             if day['date'] == datetime.now().strftime('%Y-%m-%d')),
            {'rainfall': 0}
        )
        
        for field_id in self.fields:
            # Update moisture with today's rainfall
            self.update_soil_moisture(field_id, today_weather['rainfall'])
            
            # Check if irrigation is needed
            if self.needs_irrigation(field_id):
                amount = self.calculate_irrigation_amount(field_id)
                self.irrigate_field(field_id, amount)
            else:
                logger.info(f"No irrigation needed for field {field_id}")

    def save_irrigation_log(self, filename: str = 'irrigation_log.json') -> None:
        """Save irrigation log to JSON file."""
        try:
            with open(filename, 'w') as f:
                json.dump(self.irrigation_log, f, indent=2)
            logger.info(f"Irrigation log saved to {filename}")
        except IOError as e:
            logger.error(f"Failed to save irrigation log: {e}")
