"""
Generated Code Metadata:
========================
Original URL: https://meatmaster.pe
Prompt: Write code to simulate the grilling process on a Parrilla with tapa de dos niveles, incorporating the material properties and dimensions provided by Meat Master.
Generated: DETERMINISTIC_0da47bd2df5ed8c1
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from enum import Enum
from typing import Dict, Tuple, Optional

class MeatType(Enum):
    """Enum representing different types of meat."""
    BEEF = "beef"
    CHICKEN = "chicken"
    PORK = "pork"
    FISH = "fish"

class Doneness(Enum):
    """Enum representing meat doneness levels."""
    RARE = "rare"
    MEDIUM_RARE = "medium_rare"
    MEDIUM = "medium"
    MEDIUM_WELL = "medium_well"
    WELL_DONE = "well_done"

class Parrilla:
    """Class representing a two-level Parrilla grill."""
    
    def __init__(self, material: str, dimensions: Tuple[float, float, float], heat_capacity: float):
        """
        Initialize the Parrilla grill.
        
        Args:
            material: Material of the grill (e.g., "stainless_steel")
            dimensions: Tuple of (length, width, height) in meters
            heat_capacity: Heat capacity of the material in J/(kg·K)
        """
        self.material = material
        self.dimensions = dimensions
        self.heat_capacity = heat_capacity
        self.temperature = 0.0  # Current temperature in Celsius
        self.upper_level_temp = 0.0  # Upper level temperature
        self.lower_level_temp = 0.0  # Lower level temperature
        self.is_covered = False
        self.meat_on_grill: Dict[str, Dict] = {}  # Track meat items by ID
        
    def preheat(self, target_temp: float, level: str = "both") -> None:
        """
        Preheat the grill to the target temperature.
        
        Args:
            target_temp: Target temperature in Celsius
            level: Which level to preheat ("upper", "lower", or "both")
        """
        if target_temp <= 0:
            raise ValueError("Target temperature must be positive")
            
        print(f"Preheating {level} level(s) to {target_temp}°C...")
        
        # Simulate heating process
        heating_rate = 5.0  # degrees per second
        while (self.temperature < target_temp if level == "both" else 
               (self.upper_level_temp < target_temp if level == "upper" else 
                self.lower_level_temp < target_temp)):
            time.sleep(0.1)
            if level in ["upper", "both"]:
                self.upper_level_temp = min(self.upper_level_temp + heating_rate, target_temp)
            if level in ["lower", "both"]:
                self.lower_level_temp = min(self.lower_level_temp + heating_rate, target_temp)
            self.temperature = (self.upper_level_temp + self.lower_level_temp) / 2
            
        print(f"Grill preheated to {target_temp}°C")
        
    def cover(self) -> None:
        """Cover the grill with the lid."""
        self.is_covered = True
        print("Grill covered")
        
    def uncover(self) -> None:
        """Remove the grill cover."""
        self.is_covered = False
        print("Grill uncovered")
        
    def place_meat(self, meat_id: str, meat_type: MeatType, thickness: float, 
                   level: str = "upper", initial_temp: float = 20.0) -> None:
        """
        Place meat on the grill.
        
        Args:
            meat_id: Unique identifier for the meat
            meat_type: Type of meat
            thickness: Thickness of meat in centimeters
            level: Which level to place meat ("upper" or "lower")
            initial_temp: Initial temperature of meat in Celsius
        """
        if meat_id in self.meat_on_grill:
            raise ValueError(f"Meat with ID {meat_id} already on grill")
            
        if level not in ["upper", "lower"]:
            raise ValueError("Level must be 'upper' or 'lower'")
            
        self.meat_on_grill[meat_id] = {
            "type": meat_type,
            "thickness": thickness,
            "level": level,
            "temp": initial_temp,
            "start_time": time.time(),
            "doneness": None
        }
        print(f"Placed {meat_type.value} (ID: {meat_id}) on {level} level")
        
    def remove_meat(self, meat_id: str) -> Dict:
        """
        Remove meat from the grill.
        
        Args:
            meat_id: ID of meat to remove
            
        Returns:
            Dictionary containing meat information
        """
        if meat_id not in self.meat_on_grill:
            raise ValueError(f"No meat with ID {meat_id} on grill")
            
        meat = self.meat_on_grill.pop(meat_id)
        print(f"Removed {meat['type'].value} (ID: {meat_id}) from grill")
        return meat
        
    def grill_meat(self, meat_id: str, target_doneness: Doneness) -> None:
        """
        Grill meat to the desired doneness level.
        
        Args:
            meat_id: ID of meat to grill
            target_doneness: Desired doneness level
        """
        if meat_id not in self.meat_on_grill:
            raise ValueError(f"No meat with ID {meat_id} on grill")
            
        meat = self.meat_on_grill[meat_id]
        level_temp = self.upper_level_temp if meat["level"] == "upper" else self.lower_level_temp
        
        if level_temp < 150:
            raise ValueError("Grill temperature too low for cooking")
            
        print(f"Grilling {meat['type'].value} (ID: {meat_id}) to {target_doneness.value}...")
        
        # Cooking parameters based on meat type and thickness
        cooking_params = self._get_cooking_params(meat["type"], meat["thickness"], target_doneness)
        target_temp = cooking_params["target_temp"]
        estimated_time = cooking_params["time"]
        
        # Simulate cooking process
        start_time = time.time()
        while meat["temp"] < target_temp:
            time.sleep(0.1)
            elapsed = time.time() - start_time
            heat_transfer_rate = self._calculate_heat_transfer(meat, level_temp, self.is_covered)
            meat["temp"] += heat_transfer_rate * 0.1  # Update temperature
            
            # Update doneness based on current temperature
            meat["doneness"] = self._determine_doneness(meat["temp"], meat["type"])
            
            # Safety check to prevent overcooking
            if elapsed > estimated_time * 1.5:
                print("Warning: Meat is cooking longer than expected")
                break
                
        print(f"{meat['type'].value} (ID: {meat_id}) reached {target_doneness.value}")
        
    def _get_cooking_params(self, meat_type: MeatType, thickness: float, 
                           doneness: Doneness) -> Dict[str, float]:
        """
        Get cooking parameters based on meat type, thickness, and desired doneness.
        
        Args:
            meat_type: Type of meat
            thickness: Thickness in cm
            doneness: Desired doneness level
            
        Returns:
            Dictionary with target_temp and estimated_time
        """
        # Base temperatures for doneness (in Celsius)
        doneness_temp = {
            Doneness.RARE: 52,
            Doneness.MEDIUM_RARE: 57,
            Doneness.MEDIUM: 63,
            Doneness.MEDIUM_WELL: 68,
            Doneness.WELL_DONE: 74
        }
        
        # Cooking time multipliers based on meat type and thickness
        multipliers = {
            MeatType.BEEF: 1.0,
            MeatType.PORK: 1.2,
            MeatType.CHICKEN: 1.5,
            MeatType.FISH: 0.8
        }
        
        target_temp = doneness_temp[doneness]
        base_time = thickness * 60  # 1 minute per cm thickness
        estimated_time = base_time * multipliers[meat_type]
        
        return {
            "target_temp": target_temp,
            "time": estimated_time
        }
        
    def _calculate_heat_transfer(self, meat: Dict, level_temp: float, is_covered: bool) -> float:
        """
        Calculate heat transfer rate to meat based on various factors.
        
        Args:
            meat: Meat dictionary
            level_temp: Temperature of the cooking level
            is_covered: Whether grill is covered
            
        Returns:
            Heat transfer rate in °C/s
        """
        # Base heat transfer rate (depends on temperature difference)
        base_rate = (level_temp - meat["temp"]) * 0.01
        
        # Adjust for thickness (thicker meat cooks slower)
        thickness_factor = 1.0 / (meat["thickness"] * 0.1)
        
        # Adjust for covered state
        cover_factor = 1.5 if is_covered else 1.0
        
        # Adjust for meat type
        type_factor = {
            MeatType.BEE
