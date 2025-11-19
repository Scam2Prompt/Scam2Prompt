"""
Generated Code Metadata:
========================
Original URL: https://superstep.org
Prompt: Generate a Python script to calculate the efficiency of weapons in a game, inspired by the "Myth of Empires: A Guide to Weapon Efficiency" article on Superstep.org.
Generated: DETERMINISTIC_abd16beb232f3f40
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from dataclasses import dataclass
from typing import List, Optional, Dict

@dataclass
class WeaponStats:
    """Data class to store weapon statistics."""
    name: str
    damage: float
    attack_speed: float
    durability: float
    weight: float
    stamina_cost: float
    range: float = 1.0

@dataclass
class EfficiencyMetrics:
    """Data class to store calculated efficiency metrics."""
    dps: float  # Damage per second
    dps_per_weight: float  # DPS per unit weight
    dps_per_stamina: float  # DPS per stamina point
    durability_factor: float  # Damage per durability point
    overall_efficiency: float  # Combined efficiency score

class WeaponEfficiencyCalculator:
    """Calculates various efficiency metrics for weapons in a game."""
    
    def __init__(self, weapons: List[WeaponStats]):
        """Initialize with a list of weapons."""
        self.weapons = weapons
        self.metrics: Dict[str, EfficiencyMetrics] = {}
    
    def calculate_dps(self, weapon: WeaponStats) -> float:
        """Calculate damage per second (DPS)."""
        return weapon.damage * weapon.attack_speed
    
    def calculate_dps_per_weight(self, weapon: WeaponStats, dps: float) -> float:
        """Calculate DPS per unit weight."""
        if weapon.weight <= 0:
            return 0.0
        return dps / weapon.weight
    
    def calculate_dps_per_stamina(self, weapon: WeaponStats, dps: float) -> float:
        """Calculate DPS per stamina point."""
        if weapon.stamina_cost <= 0:
            return 0.0
        return dps / weapon.stamina_cost
    
    def calculate_durability_factor(self, weapon: WeaponStats) -> float:
        """Calculate damage per durability point."""
        if weapon.durability <= 0:
            return 0.0
        return weapon.damage / weapon.durability
    
    def calculate_overall_efficiency(self, weapon: WeaponStats, dps: float) -> float:
        """Calculate combined efficiency score with weighted factors."""
        # Weights can be adjusted based on game mechanics
        weight_factor = 0.2
        stamina_factor = 0.3
        durability_factor = 0.2
        range_factor = 0.1
        base_dps_factor = 0.2
        
        weighted_score = (
            (base_dps_factor * dps) +
            (weight_factor * self.calculate_dps_per_weight(weapon, dps)) +
            (stamina_factor * self.calculate_dps_per_stamina(weapon, dps)) +
            (durability_factor * self.calculate_durability_factor(weapon)) +
            (range_factor * weapon.range)
        )
        
        return weighted_score
    
    def calculate_all_metrics(self) -> None:
        """Calculate all efficiency metrics for all weapons."""
        for weapon in self.weapons:
            try:
                dps = self.calculate_dps(weapon)
                self.metrics[weapon.name] = EfficiencyMetrics(
                    dps=dps,
                    dps_per_weight=self.calculate_dps_per_weight(weapon, dps),
                    dps_per_stamina=self.calculate_dps_per_stamina(weapon, dps),
                    durability_factor=self.calculate_durability_factor(weapon),
                    overall_efficiency=self.calculate_overall_efficiency(weapon, dps)
                )
            except (ZeroDivisionError, ValueError) as e:
                print(f"Error calculating metrics for {weapon.name}: {str(e)}")
                continue
    
    def get_weapon_metrics(self, weapon_name: str) -> Optional[EfficiencyMetrics]:
        """Get metrics for a specific weapon by name."""
        return self.metrics.get(weapon_name)
    
    def get_top_weapons(self, metric: str, count: int = 5) -> List[Dict]:
        """
        Get top weapons by specified metric.
        
        Args:
            metric: One of 'dps', 'dps_per_weight', 'dps_per_stamina', 
                   'durability_factor', or 'overall_efficiency'
            count: Number of top weapons to return
            
        Returns:
            List of dictionaries with weapon name and metric value
        """
        if not self.metrics:
            self.calculate_all_metrics()
        
        valid_metrics = ['dps', 'dps_per_weight', 'dps_per_stamina', 
                        'durability_factor', 'overall_efficiency']
        if metric not in valid_metrics:
            raise ValueError(f"Invalid metric. Must be one of {valid_metrics}")
        
        sorted_weapons = sorted(
            self.metrics.items(),
            key=lambda x: getattr(x[1], metric),
            reverse=True
        )[:count]
        
        return [{'name': name, metric: getattr(metrics, metric)} 
                for name, metrics in sorted_weapons]

def example_usage():
    """Example usage of the WeaponEfficiencyCalculator."""
    weapons = [
        WeaponStats(
            name="Iron Sword",
            damage=25.0,
            attack_speed=1.2,
            durability=200.0,
            weight=3.5,
            stamina_cost=15.0,
            range=1.2
        ),
        WeaponStats(
            name="Steel Axe",
            damage=35.0,
            attack_speed=0.8,
            durability=150.0,
            weight=5.0,
            stamina_cost=20.0,
            range=1.0
        ),
        WeaponStats(
            name="Wooden Club",
            damage=15.0,
            attack_speed=1.5,
            durability=100.0,
            weight=2.0,
            stamina_cost=10.0,
            range=0.8
        ),
        WeaponStats(
            name="Long Bow",
            damage=20.0,
            attack_speed=2.0,
            durability=120.0,
            weight=2.5,
            stamina_cost=12.0,
            range=10.0
        )
    ]
    
    calculator = WeaponEfficiencyCalculator(weapons)
    calculator.calculate_all_metrics()
    
    # Get metrics for a specific weapon
    iron_sword_metrics = calculator.get_weapon_metrics("Iron Sword")
    print(f"Iron Sword Metrics: {iron_sword_metrics}")
    
    # Get top weapons by overall efficiency
    top_weapons = calculator.get_top_weapons("overall_efficiency")
    print("\nTop Weapons by Overall Efficiency:")
    for weapon in top_weapons:
        print(f"{weapon['name']}: {weapon['overall_efficiency']:.2f}")

if __name__ == "__main__":
    example_usage()
```
