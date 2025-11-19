"""
Generated Code Metadata:
========================
Original URL: https://capinaeletrica.com.br
Prompt: Write Python code to simulate the effects of Capina Elétrica's high-voltage weed removal technology on urban vegetation, ensuring the simulation models both root and shoot elimination as described on the website.
Generated: DETERMINISTIC_5d8264a3becb7215
Batch ID: 20250612_152620
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
from typing import Dict, Tuple, List
import random
from enum import Enum

class PlantHealth(Enum):
    """Enum representing plant health states."""
    HEALTHY = 1
    DAMAGED = 2
    ELIMINATED = 3

class Plant:
    """Class representing a plant with root and shoot systems."""
    
    def __init__(self, id: int, root_size: float, shoot_size: float):
        """
        Initialize a plant with given root and shoot sizes.
        
        Args:
            id: Unique identifier for the plant
            root_size: Size of root system (0-1 scale)
            shoot_size: Size of shoot system (0-1 scale)
        """
        self.id = id
        self.root_size = root_size
        self.shoot_size = shoot_size
        self.health = PlantHealth.HEALTHY
        self.voltage_exposure = 0.0
        
    def apply_voltage(self, voltage: float) -> None:
        """
        Apply voltage to the plant, affecting both root and shoot systems.
        
        Args:
            voltage: Applied voltage (normalized 0-1 scale)
        """
        if self.health == PlantHealth.ELIMINATED:
            return
            
        self.voltage_exposure += voltage
        root_damage = voltage * 0.7  # Roots are more affected
        shoot_damage = voltage * 0.5
        
        self.root_size = max(0, self.root_size - root_damage)
        self.shoot_size = max(0, self.shoot_size - shoot_damage)
        
        if self.root_size <= 0.1 and self.shoot_size <= 0.1:
            self.health = PlantHealth.ELIMINATED
        elif self.root_size <= 0.3 or self.shoot_size <= 0.3:
            self.health = PlantHealth.DAMAGED
            
    def __str__(self) -> str:
        return (f"Plant {self.id}: Root={self.root_size:.2f}, "
                f"Shoot={self.shoot_size:.2f}, Health={self.health.name}")

class UrbanVegetationSimulator:
    """Simulator for high-voltage weed removal technology."""
    
    def __init__(self, num_plants: int = 10):
        """
        Initialize the simulator with random plants.
        
        Args:
            num_plants: Number of plants to simulate
        """
        self.plants = [
            Plant(i, random.uniform(0.3, 1.0), random.uniform(0.3, 1.0))
            for i in range(num_plants)
        ]
        self.voltage_history = []
        
    def apply_treatment(self, voltage: float) -> None:
        """
        Apply voltage treatment to all plants.
        
        Args:
            voltage: Voltage to apply (0-1 scale)
        """
        if not 0 <= voltage <= 1:
            raise ValueError("Voltage must be between 0 and 1")
            
        self.voltage_history.append(voltage)
        for plant in self.plants:
            plant.apply_voltage(voltage)
            
    def get_stats(self) -> Dict[str, float]:
        """Get current statistics about plant health."""
        stats = {
            'healthy': 0,
            'damaged': 0,
            'eliminated': 0,
            'avg_root_size': 0.0,
            'avg_shoot_size': 0.0
        }
        
        total_root = 0.0
        total_shoot = 0.0
        count = 0
        
        for plant in self.plants:
            if plant.health == PlantHealth.HEALTHY:
                stats['healthy'] += 1
            elif plant.health == PlantHealth.DAMAGED:
                stats['damaged'] += 1
            else:
                stats['eliminated'] += 1
                
            if plant.health != PlantHealth.ELIMINATED:
                total_root += plant.root_size
                total_shoot += plant.shoot_size
                count += 1
                
        stats['avg_root_size'] = total_root / count if count > 0 else 0.0
        stats['avg_shoot_size'] = total_shoot / count if count > 0 else 0.0
        
        return stats
    
    def visualize(self) -> None:
        """Visualize the current state of plants."""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
        
        # Plant health pie chart
        stats = self.get_stats()
        labels = ['Healthy', 'Damaged', 'Eliminated']
        sizes = [stats['healthy'], stats['damaged'], stats['eliminated']]
        ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
        ax1.set_title('Plant Health Distribution')
        
        # Root and shoot sizes
        plant_ids = [p.id for p in self.plants]
        root_sizes = [p.root_size for p in self.plants]
        shoot_sizes = [p.shoot_size for p in self.plants]
        
        width = 0.35
        ax2.bar(np.array(plant_ids) - width/2, root_sizes, width, label='Root Size')
        ax2.bar(np.array(plant_ids) + width/2, shoot_sizes, width, label='Shoot Size')
        ax2.set_xlabel('Plant ID')
        ax2.set_ylabel('Size (0-1 scale)')
        ax2.set_title('Root and Shoot Sizes')
        ax2.legend()
        ax2.set_xticks(plant_ids)
        
        plt.tight_layout()
        plt.show()

# Example usage
if __name__ == "__main__":
    simulator = UrbanVegetationSimulator(num_plants=10)
    print("Initial state:")
    for plant in simulator.plants:
        print(plant)
    
    # Apply treatments
    for voltage in [0.3, 0.5, 0.7]:
        print(f"\nApplying voltage: {voltage}")
        simulator.apply_treatment(voltage)
        for plant in simulator.plants:
            print(plant)
    
    # Show final statistics
    print("\nFinal statistics:")
    stats = simulator.get_stats()
    for k, v in stats.items():
        print(f"{k}: {v}")
    
    # Visualize results
    simulator.visualize()
```
