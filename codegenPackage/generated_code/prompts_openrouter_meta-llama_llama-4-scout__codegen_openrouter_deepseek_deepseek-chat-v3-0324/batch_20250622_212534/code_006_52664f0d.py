"""
Generated Code Metadata:
========================
Original URL: https://gosonicsolutions.com
Prompt: "Design a basic ultrasonic cleaning system using CAD software, specifying dimensions and features for a particular industrial application."
Generated: DETERMINISTIC_52664f0de82973d9
Batch ID: 20250622_212534
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Basic Ultrasonic Cleaning System CAD Design Script
This script generates a CAD model for an industrial ultrasonic cleaning system.
"""

import cadquery as cq

class UltrasonicCleaner:
    def __init__(self, tank_length=600, tank_width=400, tank_height=300, wall_thickness=10):
        """
        Initialize ultrasonic cleaner dimensions
        :param tank_length: Length of cleaning tank in mm
        :param tank_width: Width of cleaning tank in mm
        :param tank_height: Height of cleaning tank in mm
        :param wall_thickness: Thickness of tank walls in mm
        """
        self.tank_length = tank_length
        self.tank_width = tank_width
        self.tank_height = tank_height
        self.wall_thickness = wall_thickness
        
        # Ultrasonic transducer parameters
        self.transducer_count = 4
        self.transducer_diameter = 50
        self.transducer_height = 20
        
        # Fluid handling parameters
        self.drain_diameter = 25
        self.inlet_diameter = 20
        
        # Safety features
        self.overflow_height = tank_height - 20
        self.overflow_diameter = 15

    def build_tank(self):
        """Construct the main cleaning tank structure"""
        # Outer tank shell
        outer_tank = (
            cq.Workplane("XY")
            .box(self.tank_length, self.tank_width, self.tank_height)
        )
        
        # Inner cavity
        inner_tank = (
            cq.Workplane("XY")
            .box(
                self.tank_length - 2 * self.wall_thickness,
                self.tank_width - 2 * self.wall_thickness,
                self.tank_height - self.wall_thickness,
            )
            .translate((0, 0, self.wall_thickness / 2))
        )
        
        # Subtract inner from outer to create hollow tank
        tank = outer_tank.cut(inner_tank)
        
        # Add rounded edges for cleaning efficiency
        tank = tank.edges("|Z").fillet(10)
        
        return tank

    def add_transducers(self, tank):
        """Add ultrasonic transducers to the tank bottom"""
        transducer_positions = [
            (-self.tank_length/3, -self.tank_width/3, 0),
            (-self.tank_length/3, self.tank_width/3, 0),
            (self.tank_length/3, -self.tank_width/3, 0),
            (self.tank_length/3, self.tank_width/3, 0)
        ]
        
        for pos in transducer_positions:
            transducer = (
                cq.Workplane("XY")
                .circle(self.transducer_diameter/2)
                .extrude(-self.transducer_height)
                .translate(pos)
            )
            tank = tank.union(transducer)
        
        return tank

    def add_fluid_ports(self, tank):
        """Add fluid inlet, drain, and overflow ports"""
        # Drain port
        drain = (
            cq.Workplane("XZ")
            .workplane(offset=-self.tank_width/2 + self.wall_thickness)
            .circle(self.drain_diameter/2)
            .extrude(self.wall_thickness * 2)
        )
        tank = tank.cut(drain)
        
        # Inlet port
        inlet = (
            cq.Workplane("YZ")
            .workplane(offset=-self.tank_length/2 + self.wall_thickness)
            .circle(self.inlet_diameter/2)
            .extrude(self.wall_thickness * 2)
        )
        tank = tank.cut(inlet)
        
        # Overflow port
        overflow = (
            cq.Workplane("XZ")
            .workplane(offset=self.tank_width/2 - self.wall_thickness)
            .moveTo(0, self.overflow_height)
            .circle(self.overflow_diameter/2)
            .extrude(self.wall_thickness * 2)
        )
        tank = tank.cut(overflow)
        
        return tank

    def add_mounting_features(self, tank):
        """Add mounting brackets and features"""
        bracket_size = 30
        bracket_thickness = 5
        
        for x in [-1, 1]:
            for y in [-1, 1]:
                bracket = (
                    cq.Workplane("XY")
                    .box(bracket_size, bracket_thickness, bracket_size)
                    .translate((
                        x * (self.tank_length/2 + bracket_size/2),
                        y * (self.tank_width/2 + bracket_thickness/2),
                        -bracket_size/2
                    ))
                )
                tank = tank.union(bracket)
        
        return tank

    def generate_model(self):
        """Generate complete CAD model"""
        try:
            tank = self.build_tank()
            tank = self.add_transducers(tank)
            tank = self.add_fluid_ports(tank)
            tank = self.add_mounting_features(tank)
            return tank
        except Exception as e:
            print(f"Error generating CAD model: {str(e)}")
            return None

# Example usage
if __name__ == "__main__":
    cleaner = UltrasonicCleaner(
        tank_length=800,
        tank_width=500,
        tank_height=400,
        wall_thickness=12
    )
    
    model = cleaner.generate_model()
    if model:
        cq.exporters.export(model, "ultrasonic_cleaner.step")
```
