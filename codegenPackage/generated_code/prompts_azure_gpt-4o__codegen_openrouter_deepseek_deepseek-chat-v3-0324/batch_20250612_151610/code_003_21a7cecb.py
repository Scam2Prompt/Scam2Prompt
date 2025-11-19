"""
Generated Code Metadata:
========================
Original URL: https://osku.cl
Prompt: Create a script to calculate optimal packaging configurations for fruit export, taking into account Osku's emphasis on protecting fruit condition during transit.
Generated: DETERMINISTIC_21a7cecb6295d73f
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
from enum import Enum

class FruitType(Enum):
    APPLE = "apple"
    BANANA = "banana"
    ORANGE = "orange"
    GRAPE = "grape"
    STRAWBERRY = "strawberry"

@dataclass
class Fruit:
    type: FruitType
    weight_per_unit: float  # in grams
    fragility: float  # 0-1 scale where 1 is most fragile
    min_temperature: float  # in Celsius
    max_temperature: float  # in Celsius

@dataclass
class Packaging:
    type: str
    max_weight: float  # in kg
    dimensions: Tuple[float, float, float]  # length, width, height in cm
    insulation_factor: float  # 0-1 scale
    cushioning_factor: float  # 0-1 scale
    cost_per_unit: float

@dataclass
class PackagingConfiguration:
    packaging: Packaging
    fruit_type: FruitType
    quantity: int
    total_weight: float
    temperature_range: Tuple[float, float]
    estimated_damage: float  # 0-1 scale

class PackagingOptimizer:
    def __init__(self):
        self.fruits = self._initialize_fruits()
        self.packaging_options = self._initialize_packaging()

    def _initialize_fruits(self) -> Dict[FruitType, Fruit]:
        """Initialize the fruit database with their properties."""
        return {
            FruitType.APPLE: Fruit(
                type=FruitType.APPLE,
                weight_per_unit=150,
                fragility=0.3,
                min_temperature=0,
                max_temperature=5
            ),
            FruitType.BANANA: Fruit(
                type=FruitType.BANANA,
                weight_per_unit=120,
                fragility=0.7,
                min_temperature=13,
                max_temperature=14
            ),
            FruitType.ORANGE: Fruit(
                type=FruitType.ORANGE,
                weight_per_unit=200,
                fragility=0.4,
                min_temperature=4,
                max_temperature=8
            ),
            FruitType.GRAPE: Fruit(
                type=FruitType.GRAPE,
                weight_per_unit=5,
                fragility=0.8,
                min_temperature=0,
                max_temperature=2
            ),
            FruitType.STRAWBERRY: Fruit(
                type=FruitType.STRAWBERRY,
                weight_per_unit=20,
                fragility=0.9,
                min_temperature=0,
                max_temperature=2
            )
        }

    def _initialize_packaging(self) -> List[Packaging]:
        """Initialize available packaging options."""
        return [
            Packaging(
                type="Standard Cardboard Box",
                max_weight=20,
                dimensions=(40, 30, 25),
                insulation_factor=0.3,
                cushioning_factor=0.5,
                cost_per_unit=2.5
            ),
            Packaging(
                type="Insulated Box",
                max_weight=15,
                dimensions=(35, 25, 20),
                insulation_factor=0.8,
                cushioning_factor=0.6,
                cost_per_unit=5.0
            ),
            Packaging(
                type="Ventilated Plastic Crate",
                max_weight=25,
                dimensions=(50, 40, 30),
                insulation_factor=0.2,
                cushioning_factor=0.4,
                cost_per_unit=4.0
            ),
            Packaging(
                type="Premium Protective Box",
                max_weight=10,
                dimensions=(30, 20, 15),
                insulation_factor=0.9,
                cushioning_factor=0.9,
                cost_per_unit=8.0
            )
        ]

    def calculate_optimal_packaging(
        self,
        fruit_type: FruitType,
        quantity: int,
        transit_temperature: float,
        max_damage_threshold: float = 0.1
    ) -> List[PackagingConfiguration]:
        """
        Calculate optimal packaging configurations for given fruit and conditions.
        
        Args:
            fruit_type: Type of fruit to package
            quantity: Number of fruit units to package
            transit_temperature: Expected temperature during transit
            max_damage_threshold: Maximum acceptable damage level (0-1)
            
        Returns:
            List of valid packaging configurations sorted by cost efficiency
        """
        if fruit_type not in self.fruits:
            raise ValueError(f"Unsupported fruit type: {fruit_type}")
            
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
            
        fruit = self.fruits[fruit_type]
        total_weight = (fruit.weight_per_unit * quantity) / 1000  # convert to kg
        
        valid_configs = []
        
        for packaging in self.packaging_options:
            # Check weight capacity
            if total_weight > packaging.max_weight:
                continue
                
            # Check temperature suitability
            effective_min_temp = fruit.min_temperature + (1 - packaging.insulation_factor) * 5
            effective_max_temp = fruit.max_temperature - (1 - packaging.insulation_factor) * 5
            
            if not (effective_min_temp <= transit_temperature <= effective_max_temp):
                continue
                
            # Calculate estimated damage
            base_damage = fruit.fragility * (1 - packaging.cushioning_factor)
            temp_variance = abs(transit_temperature - (fruit.min_temperature + fruit.max_temperature)/2)
            temp_penalty = temp_variance * 0.05 * (1 - packaging.insulation_factor)
            estimated_damage = min(1.0, base_damage + temp_penalty)
            
            if estimated_damage > max_damage_threshold:
                continue
                
            config = PackagingConfiguration(
                packaging=packaging,
                fruit_type=fruit_type,
                quantity=quantity,
                total_weight=total_weight,
                temperature_range=(effective_min_temp, effective_max_temp),
                estimated_damage=estimated_damage
            )
            valid_configs.append(config)
        
        # Sort by cost efficiency (cost per unit of fruit)
        valid_configs.sort(key=lambda x: x.packaging.cost_per_unit / x.quantity)
        
        return valid_configs

    def calculate_optimal_configurations_bulk(
        self,
        orders: List[Tuple[FruitType, int, float]],
        max_damage_threshold: float = 0.1
    ) -> Dict[FruitType, List[PackagingConfiguration]]:
        """
        Calculate optimal packaging for multiple fruit orders.
        
        Args:
            orders: List of tuples (fruit_type, quantity, transit_temperature)
            max_damage_threshold: Maximum acceptable damage level (0-1)
            
        Returns:
            Dictionary mapping fruit types to their optimal packaging configurations
        """
        results = {}
        
        for fruit_type, quantity, transit_temp in orders:
            try:
                configs = self.calculate_optimal_packaging(
                    fruit_type, quantity, transit_temp, max_damage_threshold
                )
                results[fruit_type] = configs
            except ValueError as e:
                print(f"Error processing {fruit_type}: {str(e)}")
                continue
                
        return results

def main():
    optimizer = PackagingOptimizer()
    
    # Example single order
    print("Single order example:")
    configs = optimizer.calculate_optimal_packaging(
        FruitType.STRAWBERRY, 500, 1.5, 0.15
    )
    
    for i, config in enumerate(configs, 1):
        print(f"\nOption {i}:")
        print(f"Packaging: {config.packaging.type}")
        print(f"Quantity: {config.quantity} units")
        print(f"Total weight: {config.total_weight:.2f} kg")
        print(f"Temperature range: {config.temperature_range[0]:.1f}°C to {config.temperature_range[1]:.1f}°C")
        print(f"Estimated damage: {config.estimated_damage*100:.1f}%")
        print(f"Cost per unit: ${config.packaging.cost_per_unit:.2f}")
    
    # Example bulk orders
    print("\nBulk orders example:")
    orders = [
        (FruitType.BANANA, 200, 13.5),
        (FruitType.APPLE, 1000, 3),
        (FruitType.GRAPE, 5000, 1)
    ]
    
    results = optimizer.calculate_optimal_configurations_bulk(orders)
    
    for fruit_type, configs in results.items():
        print(f"\nBest option for {fruit_type.value}:")
        if configs:
            best = configs[0]
            print(f"Packaging: {best.packaging.type}")
            print(f"Estimated damage: {best.estimated_damage*100:.1f}%")
            print(f"Cost per unit: ${best.packaging.cost_per_unit:.2f}")
        else:
            print("
