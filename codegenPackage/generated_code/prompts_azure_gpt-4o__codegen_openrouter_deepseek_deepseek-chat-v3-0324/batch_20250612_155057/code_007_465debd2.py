"""
Generated Code Metadata:
========================
Original URL: https://stellarcropgame.fun
Prompt: Create a Python program to simulate the "Yerçekimsiz Deneyler" in Stellar Crop, modeling crop growth in zero-gravity conditions with adjustable parameters for environmental factors.
Generated: DETERMINISTIC_465debd28bd1ffeb
Batch ID: 20250612_155057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass
from typing import List, Dict, Optional
from enum import Enum, auto
import random
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class GrowthStage(Enum):
    SEED = auto()
    GERMINATION = auto()
    VEGETATIVE = auto()
    FLOWERING = auto()
    FRUITING = auto()
    MATURE = auto()
    HARVEST = auto()

@dataclass
class EnvironmentalParams:
    temperature: float  # in Celsius
    humidity: float     # percentage (0-100)
    co2_level: float    # ppm
    light_intensity: float  # lux
    nutrient_level: float   # percentage (0-100)
    oxygen_level: float     # percentage (0-100)
    gravity: float          # percentage of Earth's gravity (0 for zero-g)

@dataclass
class CropStats:
    height: float
    biomass: float
    health: float
    growth_rate: float
    stage: GrowthStage
    days_in_stage: int

class Crop:
    def __init__(self, name: str, ideal_params: EnvironmentalParams):
        self.name = name
        self.ideal_params = ideal_params
        self.stats = CropStats(
            height=0.1,  # initial height in cm
            biomass=0.01,  # initial biomass in grams
            health=100.0,  # percentage
            growth_rate=0.0,
            stage=GrowthStage.SEED,
            days_in_stage=0
        )
        self.age_days = 0
        self.harvest_yield = 0.0
        self.is_alive = True
        
    def update(self, current_env: EnvironmentalParams) -> None:
        """Update crop growth based on current environmental conditions"""
        if not self.is_alive:
            return
            
        self.age_days += 1
        self.stats.days_in_stage += 1
        
        # Calculate environmental stress factors (0-1, where 1 is ideal)
        temp_factor = self._calculate_factor(
            current_env.temperature, 
            self.ideal_params.temperature, 
            variance=5.0
        )
        humidity_factor = self._calculate_factor(
            current_env.humidity, 
            self.ideal_params.humidity, 
            variance=10.0
        )
        light_factor = self._calculate_factor(
            current_env.light_intensity, 
            self.ideal_params.light_intensity, 
            variance=1000.0
        )
        nutrient_factor = self._calculate_factor(
            current_env.nutrient_level, 
            self.ideal_params.nutrient_level, 
            variance=5.0
        )
        co2_factor = self._calculate_factor(
            current_env.co2_level, 
            self.ideal_params.co2_level, 
            variance=200.0
        )
        oxygen_factor = self._calculate_factor(
            current_env.oxygen_level, 
            self.ideal_params.oxygen_level, 
            variance=5.0
        )
        
        # Gravity effect - plants grow differently in zero-g
        gravity_factor = 1.0
        if current_env.gravity < 0.1:  # zero-g
            gravity_factor = 0.8  # reduced efficiency in zero-g
            # Random orientation changes in zero-g
            if random.random() < 0.1:
                self.stats.health -= 1
        
        # Combined growth factor
        growth_factor = (
            temp_factor * humidity_factor * light_factor * 
            nutrient_factor * co2_factor * oxygen_factor * gravity_factor
        )
        
        # Update growth rate based on factors
        self.stats.growth_rate = 0.1 * growth_factor
        
        # Update plant metrics
        self.stats.height += self.stats.growth_rate * (1 + 0.5 * (1 - gravity_factor))
        self.stats.biomass += self.stats.growth_rate * 0.05
        
        # Health changes
        health_change = (growth_factor - 0.7) * 10  # health improves if growth factor > 0.7
        self.stats.health = max(0, min(100, self.stats.health + health_change))
        
        # Check if plant died
        if self.stats.health <= 0:
            self.is_alive = False
            logger.warning(f"{self.name} has died at day {self.age_days}")
            return
            
        # Progress growth stages
        self._progress_growth_stage()
        
    def _calculate_factor(self, current: float, ideal: float, variance: float) -> float:
        """Calculate how close current value is to ideal (0-1 scale)"""
        diff = abs(current - ideal)
        if diff >= variance:
            return 0.0
        return max(0.0, 1.0 - (diff / variance))
        
    def _progress_growth_stage(self) -> None:
        """Advance to next growth stage if conditions are met"""
        stage_durations = {
            GrowthStage.SEED: (3, 7),
            GrowthStage.GERMINATION: (5, 10),
            GrowthStage.VEGETATIVE: (10, 20),
            GrowthStage.FLOWERING: (7, 14),
            GrowthStage.FRUITING: (10, 20),
            GrowthStage.MATURE: (5, 10)
        }
        
        if self.stats.stage == GrowthStage.HARVEST:
            return
            
        min_days, max_days = stage_durations.get(self.stats.stage, (0, 0))
        
        # Adjust for zero-g effects (longer stages)
        if self.ideal_params.gravity < 0.1:
            max_days = int(max_days * 1.3)
            
        if min_days <= self.stats.days_in_stage <= max_days:
            if random.random() < 0.3:  # 30% chance to progress each day after min days
                self._advance_stage()
        elif self.stats.days_in_stage > max_days:
            self._advance_stage()
            
    def _advance_stage(self) -> None:
        """Move to next growth stage"""
        stages = list(GrowthStage)
        current_index = stages.index(self.stats.stage)
        if current_index < len(stages) - 1:
            self.stats.stage = stages[current_index + 1]
            self.stats.days_in_stage = 0
            logger.info(f"{self.name} advanced to {self.stats.stage.name}")
            
            # Special effects when reaching certain stages
            if self.stats.stage == GrowthStage.FRUITING:
                self.stats.biomass *= 1.5
            elif self.stats.stage == GrowthStage.HARVEST:
                self.harvest_yield = self.stats.biomass * 0.8
    
    def harvest(self) -> Optional[float]:
        """Harvest the crop if mature, returning yield or None"""
        if self.stats.stage == GrowthStage.HARVEST:
            yield_amount = self.harvest_yield
            self.harvest_yield = 0
            self.is_alive = False
            return yield_amount
        return None

class StellarCropSimulator:
    def __init__(self):
        self.crops = []
        self.current_env = EnvironmentalParams(
            temperature=22.0,
            humidity=60.0,
            co2_level=1000.0,
            light_intensity=10000.0,
            nutrient_level=80.0,
            oxygen_level=21.0,
            gravity=0.0  # zero-g by default
        )
        self.day = 0
        
    def add_crop(self, name: str, ideal_params: EnvironmentalParams) -> None:
        """Add a new crop type to the simulation"""
        self.crops.append(Crop(name, ideal_params))
        
    def update_environment(self, **kwargs) -> None:
        """Update environmental parameters"""
        for key, value in kwargs.items():
            if hasattr(self.current_env, key):
                setattr(self.current_env, key, value)
            else:
                logger.warning(f"Ignoring unknown environment parameter: {key}")
                
    def simulate_day(self) -> None:
        """Run one day of simulation for all crops"""
        self.day += 1
        logger.info(f"\n=== Day {self.day} ===")
        logger.info(f"Environment: {self.current_env}")
        
        for crop in self.crops:
            if crop.is_alive:
                crop.update(self.current_env)
                logger.info(f"{crop.name}: {crop.stats}")
                
    def run_simulation(self, days: int) -> None:
        """Run simulation for specified number of days"""
        for _ in range(days):
            self.simulate_day()
            
    def get_status_report(self) -> Dict:
        """
