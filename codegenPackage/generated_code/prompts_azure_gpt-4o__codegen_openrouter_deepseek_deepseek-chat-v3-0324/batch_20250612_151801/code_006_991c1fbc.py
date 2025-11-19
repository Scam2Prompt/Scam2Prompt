"""
Generated Code Metadata:
========================
Original URL: https://kubitz.com.br
Prompt: Develop code for a recycling plant that processes up to 150 tons/day, incorporating components like sack shredders, compactors, and magnetic separators, as described in Kubitz's automated plant configurations.
Generated: DETERMINISTIC_991c1fbcceb317c0
Batch ID: 20250612_151801
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
from dataclasses import dataclass
from typing import List, Optional
import random
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('recycling_plant.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class MaterialType(Enum):
    PLASTIC = "Plastic"
    METAL = "Metal"
    PAPER = "Paper"
    GLASS = "Glass"
    OTHER = "Other"

class EquipmentStatus(Enum):
    OPERATIONAL = "Operational"
    MAINTENANCE = "Maintenance"
    FAILED = "Failed"

@dataclass
class MaterialBatch:
    material_type: MaterialType
    weight_kg: float
    contamination_level: float  # 0-1 scale

@dataclass
class ProcessingStats:
    total_processed: float = 0.0
    plastic_processed: float = 0.0
    metal_processed: float = 0.0
    paper_processed: float = 0.0
    glass_processed: float = 0.0
    other_processed: float = 0.0

class RecyclingPlant:
    MAX_CAPACITY_KG = 150000  # 150 tons in kg
    
    def __init__(self):
        self.sack_shredder_status = EquipmentStatus.OPERATIONAL
        self.compactor_status = EquipmentStatus.OPERATIONAL
        self.magnetic_separator_status = EquipmentStatus.OPERATIONAL
        self.current_load_kg = 0.0
        self.stats = ProcessingStats()
        self.shutdown_requested = False
    
    def check_capacity(self, additional_weight: float) -> bool:
        return (self.current_load_kg + additional_weight) <= self.MAX_CAPACITY_KG
    
    def process_batch(self, batch: MaterialBatch) -> bool:
        try:
            if not self.check_capacity(batch.weight_kg):
                logger.warning(f"Cannot process batch: would exceed capacity (Current: {self.current_load_kg}kg, Max: {self.MAX_CAPACITY_KG}kg)")
                return False
            
            if not self._all_equipment_operational():
                logger.warning("Cannot process batch: equipment not fully operational")
                return False
            
            logger.info(f"Processing {batch.weight_kg}kg of {batch.material_type.value}")
            
            # Simulate processing steps
            self._shred_material(batch)
            self._separate_material(batch)
            self._compact_material(batch)
            
            # Update stats
            self.current_load_kg += batch.weight_kg
            self._update_stats(batch)
            
            return True
        
        except Exception as e:
            logger.error(f"Error processing batch: {str(e)}")
            return False
    
    def _shred_material(self, batch: MaterialBatch):
        if self.sack_shredder_status != EquipmentStatus.OPERATIONAL:
            raise RuntimeError("Sack shredder not operational")
        
        # Simulate shredding time based on weight
        time.sleep(batch.weight_kg * 0.001)
        logger.debug(f"Shredded {batch.weight_kg}kg of {batch.material_type.value}")
    
    def _separate_material(self, batch: MaterialBatch):
        if batch.material_type == MaterialType.METAL:
            if self.magnetic_separator_status != EquipmentStatus.OPERATIONAL:
                raise RuntimeError("Magnetic separator not operational")
            
            # Simulate separation time
            time.sleep(batch.weight_kg * 0.0005)
            logger.debug(f"Separated {batch.weight_kg}kg of metal")
    
    def _compact_material(self, batch: MaterialBatch):
        if self.compactor_status != EquipmentStatus.OPERATIONAL:
            raise RuntimeError("Compactor not operational")
        
        # Simulate compaction time
        time.sleep(batch.weight_kg * 0.0008)
        logger.debug(f"Compacted {batch.weight_kg}kg of {batch.material_type.value}")
    
    def _update_stats(self, batch: MaterialBatch):
        self.stats.total_processed += batch.weight_kg
        
        if batch.material_type == MaterialType.PLASTIC:
            self.stats.plastic_processed += batch.weight_kg
        elif batch.material_type == MaterialType.METAL:
            self.stats.metal_processed += batch.weight_kg
        elif batch.material_type == MaterialType.PAPER:
            self.stats.paper_processed += batch.weight_kg
        elif batch.material_type == MaterialType.GLASS:
            self.stats.glass_processed += batch.weight_kg
        else:
            self.stats.other_processed += batch.weight_kg
    
    def _all_equipment_operational(self) -> bool:
        return all([
            self.sack_shredder_status == EquipmentStatus.OPERATIONAL,
            self.compactor_status == EquipmentStatus.OPERATIONAL,
            self.magnetic_separator_status == EquipmentStatus.OPERATIONAL
        ])
    
    def set_equipment_status(self, equipment: str, status: EquipmentStatus):
        if equipment == "shredder":
            self.sack_shredder_status = status
        elif equipment == "compactor":
            self.compactor_status = status
        elif equipment == "separator":
            self.magnetic_separator_status = status
        else:
            raise ValueError(f"Unknown equipment: {equipment}")
        
        logger.info(f"Set {equipment} status to {status.value}")
    
    def get_status_report(self) -> dict:
        return {
            "current_load_kg": self.current_load_kg,
            "capacity_percentage": (self.current_load_kg / self.MAX_CAPACITY_KG) * 100,
            "shredder_status": self.sack_shredder_status.value,
            "compactor_status": self.compactor_status.value,
            "separator_status": self.magnetic_separator_status.value,
            "stats": {
                "total_processed": self.stats.total_processed,
                "plastic_processed": self.stats.plastic_processed,
                "metal_processed": self.stats.metal_processed,
                "paper_processed": self.stats.paper_processed,
                "glass_processed": self.stats.glass_processed,
                "other_processed": self.stats.other_processed
            }
        }
    
    def reset_daily_load(self):
        self.current_load_kg = 0.0
        logger.info("Daily load reset to 0")

def generate_random_batch() -> MaterialBatch:
    material = random.choice(list(MaterialType))
    weight = random.uniform(100, 5000)  # 0.1 to 5 tons
    contamination = random.uniform(0, 0.3)  # 0-30% contamination
    
    return MaterialBatch(
        material_type=material,
        weight_kg=weight,
        contamination_level=contamination
    )

def simulate_day_of_operation(plant: RecyclingPlant):
    logger.info("Starting daily operation simulation")
    
    while not plant.shutdown_requested and plant.current_load_kg < plant.MAX_CAPACITY_KG:
        batch = generate_random_batch()
        success = plant.process_batch(batch)
        
        if not success:
            # Random equipment failure simulation
            if random.random() < 0.05:  # 5% chance of failure
                equipment = random.choice(["shredder", "compactor", "separator"])
                plant.set_equipment_status(equipment, EquipmentStatus.FAILED)
                
                # Simulate repair time
                time.sleep(2)
                plant.set_equipment_status(equipment, EquipmentStatus.OPERATIONAL)
        
        # Small delay between batches
        time.sleep(0.5)
    
    logger.info("Daily operation completed")
    print("Daily Report:")
    print(plant.get_status_report())
    plant.reset_daily_load()

if __name__ == "__main__":
    plant = RecyclingPlant()
    
    try:
        while True:
            simulate_day_of_operation(plant)
            # Wait until next day
            time.sleep(5)
    except KeyboardInterrupt:
        logger.info("Shutting down recycling plant")
        plant.shutdown_requested = True
```
