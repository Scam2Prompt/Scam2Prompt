"""
Generated Code Metadata:
========================
Original URL: https://phantom-ss.com
Prompt: Write code to model the aerodynamic effects of a high-rise spoiler and custom body kit in a car simulation, inspired by the Phantom SS exterior modifications.
Generated: DETERMINISTIC_f5e26b9cd94a1547
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from dataclasses import dataclass
from typing import Tuple, Optional

@dataclass
class CarParameters:
    """Base parameters for the car simulation."""
    mass: float  # kg
    frontal_area: float  # m^2
    drag_coefficient: float  # dimensionless
    wheelbase: float  # m
    track_width: float  # m
    center_of_gravity_height: float  # m

@dataclass
class SpoilerParameters:
    """Parameters for the high-rise spoiler."""
    angle: float  # degrees
    area: float  # m^2
    height: float  # m from ground
    efficiency: float = 0.8  # dimensionless (0-1)

@dataclass
class BodyKitParameters:
    """Parameters for the custom body kit."""
    front_diffuser_area: float  # m^2
    rear_diffuser_area: float  # m^2
    side_skirt_length: float  # m
    underbody_flatness: float  # dimensionless (0-1)

class AerodynamicModel:
    """Models the aerodynamic effects of a car with spoiler and body kit."""
    
    AIR_DENSITY = 1.225  # kg/m^3 at sea level
    
    def __init__(
        self,
        car_params: CarParameters,
        spoiler_params: Optional[SpoilerParameters] = None,
        body_kit_params: Optional[BodyKitParameters] = None
    ):
        self.car = car_params
        self.spoiler = spoiler_params
        self.body_kit = body_kit_params
    
    def calculate_drag_force(self, velocity: float) -> float:
        """Calculate total drag force at given velocity (m/s)."""
        base_drag = 0.5 * self.AIR_DENSITY * velocity**2 * self.car.frontal_area * self.car.drag_coefficient
        
        # Adjust for body kit effects
        if self.body_kit:
            drag_reduction = (self.body_kit.underbody_flatness * 0.15 + 
                            self.body_kit.side_skirt_length * 0.05)
            base_drag *= (1 - min(drag_reduction, 0.25))  # Max 25% reduction
            
        return base_drag
    
    def calculate_downforce(self, velocity: float) -> Tuple[float, float]:
        """
        Calculate front and rear downforce at given velocity (m/s).
        Returns: (front_downforce, rear_downforce) in Newtons
        """
        front_downforce = 0
        rear_downforce = 0
        
        # Base downforce from car body
        base_downforce = 0.5 * self.AIR_DENSITY * velocity**2 * self.car.frontal_area * 0.1
        
        # Body kit effects
        if self.body_kit:
            front_downforce += (0.5 * self.AIR_DENSITY * velocity**2 * 
                              self.body_kit.front_diffuser_area * 1.2)
            rear_downforce += (0.5 * self.AIR_DENSITY * velocity**2 * 
                             self.body_kit.rear_diffuser_area * 1.1)
        
        # Spoiler effects
        if self.spoiler:
            spoiler_downforce = (0.5 * self.AIR_DENSITY * velocity**2 * 
                               self.spoiler.area * np.sin(np.radians(self.spoiler.angle)) * 
                               self.spoiler.efficiency)
            rear_downforce += spoiler_downforce
        
        # Distribute base downforce (60% front, 40% rear for typical car)
        front_downforce += base_downforce * 0.6
        rear_downforce += base_downforce * 0.4
        
        return front_downforce, rear_downforce
    
    def calculate_aero_balance(self, velocity: float) -> float:
        """Calculate aerodynamic balance (front downforce/total downforce)."""
        front, rear = self.calculate_downforce(velocity)
        total = front + rear
        return front / total if total > 0 else 0.5
    
    def calculate_effective_drag_coefficient(self, velocity: float) -> float:
        """Calculate effective drag coefficient including aero modifications."""
        base_cd = self.car.drag_coefficient
        
        # Body kit reduces drag
        if self.body_kit:
            drag_reduction = (self.body_kit.underbody_flatness * 0.15 + 
                            self.body_kit.side_skirt_length * 0.05)
            base_cd *= (1 - min(drag_reduction, 0.25))
        
        # Spoiler increases drag
        if self.spoiler:
            spoiler_drag = (0.05 * self.spoiler.area / self.car.frontal_area * 
                          np.sin(np.radians(self.spoiler.angle)))
            base_cd += spoiler_drag
        
        return base_cd

def example_usage():
    """Example usage of the aerodynamic model."""
    car = CarParameters(
        mass=1500,
        frontal_area=2.2,
        drag_coefficient=0.32,
        wheelbase=2.7,
        track_width=1.8,
        center_of_gravity_height=0.5
    )
    
    spoiler = SpoilerParameters(
        angle=15,
        area=0.3,
        height=1.2
    )
    
    body_kit = BodyKitParameters(
        front_diffuser_area=0.4,
        rear_diffuser_area=0.5,
        side_skirt_length=3.5,
        underbody_flatness=0.9
    )
    
    aero = AerodynamicModel(car, spoiler, body_kit)
    
    velocity = 30  # m/s (108 km/h)
    drag = aero.calculate_drag_force(velocity)
    front_df, rear_df = aero.calculate_downforce(velocity)
    balance = aero.calculate_aero_balance(velocity)
    effective_cd = aero.calculate_effective_drag_coefficient(velocity)
    
    print(f"At {velocity} m/s:")
    print(f"Drag Force: {drag:.1f} N")
    print(f"Front Downforce: {front_df:.1f} N")
    print(f"Rear Downforce: {rear_df:.1f} N")
    print(f"Aero Balance: {balance:.2f}")
    print(f"Effective Cd: {effective_cd:.3f}")

if __name__ == "__main__":
    example_usage()
```
