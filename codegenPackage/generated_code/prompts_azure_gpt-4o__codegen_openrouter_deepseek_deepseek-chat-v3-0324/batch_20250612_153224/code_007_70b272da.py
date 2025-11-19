"""
Generated Code Metadata:
========================
Original URL: https://nyikudesign.com
Prompt: Write a script to simulate lighting effects in an interior design project, focusing on creating a functional and aesthetic ambiance as emphasized by Nyiku Design.
Generated: DETERMINISTIC_70b272da43e63037
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from enum import Enum
import math

class LightType(Enum):
    AMBIENT = 1
    ACCENT = 2
    TASK = 3

class LightEffect:
    def __init__(self, name, description, intensity_range, color_range):
        self.name = name
        self.description = description
        self.intensity_range = intensity_range
        self.color_range = color_range

class LightingSimulator:
    """
    A lighting simulator for interior design projects with Nyiku Design principles.
    Simulates different lighting effects to create functional and aesthetic ambiance.
    """
    
    def __init__(self):
        self.light_effects = {
            LightType.AMBIENT: LightEffect(
                "Soft Glow",
                "Creates a warm, inviting atmosphere with uniform illumination",
                (20, 60),
                ((2000, 3000), (0.8, 1.0), (0.8, 1.0))  # Kelvin, R, G
            ),
            LightType.ACCENT: LightEffect(
                "Dramatic Highlight",
                "Emphasizes architectural features with focused lighting",
                (70, 100),
                ((3000, 5000), (0.9, 1.0), (0.7, 0.9))  # Kelvin, R, G
            ),
            LightType.TASK: LightEffect(
                "Functional Brightness",
                "Provides clear illumination for work areas",
                (80, 100),
                ((4000, 6000), (1.0, 1.0), (1.0, 1.0))  # Kelvin, R, G
            )
        }
        self.current_effect = None
        self.is_running = False
    
    def start_effect(self, light_type):
        """Start a lighting effect based on the specified light type."""
        if light_type not in LightType:
            raise ValueError("Invalid light type provided")
        
        self.current_effect = self.light_effects[light_type]
        self.is_running = True
        print(f"Started {self.current_effect.name} effect: {self.current_effect.description}")
    
    def stop_effect(self):
        """Stop the current lighting effect."""
        if self.current_effect:
            print(f"Stopping {self.current_effect.name} effect")
            self.current_effect = None
        self.is_running = False
    
    def simulate(self, duration=10):
        """
        Simulate the current lighting effect for the specified duration.
        Generates random variations within the effect's parameters.
        """
        if not self.is_running or not self.current_effect:
            raise RuntimeError("No active lighting effect to simulate")
        
        start_time = time.time()
        end_time = start_time + duration
        
        print(f"Simulating {self.current_effect.name} for {duration} seconds...")
        
        try:
            while time.time() < end_time and self.is_running:
                # Generate random values within specified ranges
                intensity = random.randint(*self.current_effect.intensity_range)
                kelvin = random.randint(*self.current_effect.color_range[0])
                red = random.uniform(*self.current_effect.color_range[1])
                green = random.uniform(*self.current_effect.color_range[2])
                
                # Calculate blue component based on kelvin temperature
                blue = self._kelvin_to_blue(kelvin)
                
                # Apply natural variation with smooth transitions
                time.sleep(0.5)
                self._display_light_state(intensity, kelvin, red, green, blue)
        
        except KeyboardInterrupt:
            print("\nSimulation interrupted by user")
            self.stop_effect()
    
    def _kelvin_to_blue(self, kelvin):
        """Convert kelvin temperature to blue light component (simplified model)."""
        # Simple approximation for demonstration
        if kelvin < 3000:
            return 0.5 + (kelvin / 6000)
        elif 3000 <= kelvin < 5000:
            return 0.7 + (kelvin / 10000)
        else:
            return 0.9 - ((kelvin - 5000) / 20000)
    
    def _display_light_state(self, intensity, kelvin, red, green, blue):
        """Display the current light state (simulated)."""
        print(f"\rIntensity: {intensity}% | Color: {kelvin}K (RGB: {red:.2f}, {green:.2f}, {blue:.2f})", end="")
    
    def list_effects(self):
        """List all available lighting effects."""
        print("\nAvailable Lighting Effects:")
        for light_type, effect in self.light_effects.items():
            print(f"\n{light_type.name}: {effect.name}")
            print(f"  - {effect.description}")
            print(f"  - Intensity Range: {effect.intensity_range[0]}%-{effect.intensity_range[1]}%")
            print(f"  - Color Temperature: {effect.color_range[0][0]}K-{effect.color_range[0][1]}K")

# Example usage
if __name__ == "__main__":
    simulator = LightingSimulator()
    simulator.list_effects()
    
    try:
        print("\nSimulating ambient lighting...")
        simulator.start_effect(LightType.AMBIENT)
        simulator.simulate(5)
        
        print("\n\nSimulating accent lighting...")
        simulator.start_effect(LightType.ACCENT)
        simulator.simulate(5)
        
        print("\n\nSimulating task lighting...")
        simulator.start_effect(LightType.TASK)
        simulator.simulate(5)
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        simulator.stop_effect()
```
