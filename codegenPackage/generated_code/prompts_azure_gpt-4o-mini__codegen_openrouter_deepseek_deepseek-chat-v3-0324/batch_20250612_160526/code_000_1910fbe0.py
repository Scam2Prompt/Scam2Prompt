"""
Generated Code Metadata:
========================
Original URL: https://tekrollindustrial.com.br
Prompt: Generate a code snippet for a system that optimizes the process of lifting and transporting heavy loads, focusing on ergonomic safety and efficiency as described by Tekroll Industrial.
Generated: DETERMINISTIC_1910fbe0a2d1b2f6
Batch ID: 20250612_160526
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
from typing import Optional, Tuple, List

@dataclass
class Load:
    """Represents a physical load to be lifted and transported."""
    weight: float  # in kilograms
    dimensions: Tuple[float, float, float]  # length, width, height in meters
    center_of_gravity: Tuple[float, float, float]  # x, y, z coordinates relative to load's base
    fragility: float  # 0.0 (not fragile) to 1.0 (extremely fragile)

@dataclass
class Worker:
    """Represents a worker who will handle the load."""
    strength_capacity: float  # max weight in kg the worker can safely lift
    reach: float  # maximum horizontal reach in meters
    lifting_height: Tuple[float, float]  # min and max comfortable lifting height in meters
    experience_level: int  # 1 (novice) to 5 (expert)

class LoadOptimizer:
    """Optimizes load lifting and transportation for ergonomic safety and efficiency."""
    
    MAX_RECOMMENDED_WEIGHT = 25.0  # kg per OSHA guidelines
    IDEAL_LIFT_HEIGHT = (0.75, 1.25)  # meters (waist height)
    
    def __init__(self):
        self.safety_margin = 0.8  # 80% of max capacity for safety
        
    def calculate_optimal_grip(self, load: Load, worker: Worker) -> Optional[Tuple[float, float]]:
        """
        Calculates optimal grip positions based on load and worker capabilities.
        Returns (distance_from_worker, height) in meters or None if unsafe.
        """
        if load.weight > worker.strength_capacity * self.safety_margin:
            return None
            
        # Calculate horizontal distance limit
        max_distance = min(worker.reach, load.dimensions[0]/2, load.dimensions[1]/2)
        
        # Calculate vertical range
        min_height = max(worker.lifting_height[0], self.IDEAL_LIFT_HEIGHT[0])
        max_height = min(worker.lifting_height[1], self.IDEAL_LIFT_HEIGHT[1])
        
        if min_height > max_height:
            return None
            
        # Optimal is midpoint of safe range
        optimal_distance = max_distance * 0.7  # 70% of max for comfort
        optimal_height = (min_height + max_height) / 2
        
        return (optimal_distance, optimal_height)
    
    def recommend_team_size(self, load: Load) -> int:
        """Recommends number of workers needed based on load weight."""
        if load.weight <= self.MAX_RECOMMENDED_WEIGHT:
            return 1
        return math.ceil(load.weight / self.MAX_RECOMMENDED_WEIGHT)
    
    def generate_lift_plan(self, load: Load, workers: List[Worker]) -> dict:
        """
        Generates a complete lift plan considering all safety factors.
        Returns a dictionary with recommendations or error messages.
        """
        plan = {
            'load': load,
            'workers': workers,
            'recommendations': [],
            'warnings': []
        }
        
        if load.weight <= 0:
            plan['warnings'].append("Invalid load weight")
            return plan
            
        required_workers = self.recommend_team_size(load)
        if len(workers) < required_workers:
            plan['warnings'].append(f"Insufficient workers. Required: {required_workers}")
            
        for i, worker in enumerate(workers[:required_workers]):
            grip = self.calculate_optimal_grip(load, worker)
            if grip:
                plan['recommendations'].append({
                    'worker': i+1,
                    'grip_distance': grip[0],
                    'grip_height': grip[1],
                    'notes': 'Maintain neutral spine during lift'
                })
            else:
                plan['warnings'].append(f"Worker {i+1} cannot safely handle this load")
                
        if load.fragility > 0.7:
            plan['recommendations'].append({
                'special_instructions': 'Use extreme caution - fragile load',
                'required_equipment': ['anti-slip padding', 'load stabilizers']
            })
            
        return plan

# Example usage
if __name__ == "__main__":
    optimizer = LoadOptimizer()
    
    sample_load = Load(
        weight=40.0,
        dimensions=(1.2, 0.8, 0.5),
        center_of_gravity=(0.6, 0.4, 0.25),
        fragility=0.3
    )
    
    sample_workers = [
        Worker(strength_capacity=30.0, reach=1.0, lifting_height=(0.5, 1.5), experience_level=3),
        Worker(strength_capacity=25.0, reach=0.9, lifting_height=(0.6, 1.4), experience_level=4)
    ]
    
    plan = optimizer.generate_lift_plan(sample_load, sample_workers)
    print(plan)
```
