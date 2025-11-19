"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kangaroopunchclub.com
Prompt: Write a script that models the physics of a punch, inspired by the content on kangaroopunchclub.com.
Generated: DETERMINISTIC_65312cbe421babf4
Batch ID: 20250612_162127
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class Punch:
    """A class to model the physics of a punch."""

    def __init__(self, mass_kg, velocity_m_s, angle_deg):
        """
        Initializes the Punch object.

        Parameters:
        mass_kg (float): Mass of the fist (in kilograms).
        velocity_m_s (float): Velocity of the punch (in meters per second).
        angle_deg (float): Angle of the punch relative to the horizontal (in degrees).
        """
        self.mass_kg = mass_kg
        self.velocity_m_s = velocity_m_s
        self.angle_rad = math.radians(angle_deg)  # Convert angle to radians

    def kinetic_energy(self):
        """Calculates the kinetic energy of the punch."""
        try:
            ke = 0.5 * self.mass_kg * (self.velocity_m_s ** 2)
            return ke
        except Exception as e:
            print(f"Error calculating kinetic energy: {e}")
            return None

    def momentum(self):
        """Calculates the momentum of the punch."""
        try:
            p = self.mass_kg * self.velocity_m_s
            return p
        except Exception as e:
            print(f"Error calculating momentum: {e}")
            return None

    def force_of_impact(self, contact_time_s):
        """
        Calculates the average force of impact.

        Parameters:
        contact_time_s (float): Contact time during the punch (in seconds).
        """
        try:
            if contact_time_s <= 0:
                raise ValueError("Contact time must be greater than zero.")
            # Using impulse = change in momentum = force * time
            force = self.momentum() / contact_time_s
            return force
        except ValueError as ve:
            print(ve)
            return None
        except Exception as e:
            print(f"Error calculating force of impact: {e}")
            return None

    def punch_components(self):
        """Returns the horizontal and vertical components of the punch's velocity."""
        try:
            v_horizontal = self.velocity_m_s * math.cos(self.angle_rad)
            v_vertical = self.velocity_m_s * math.sin(self.angle_rad)
            return v_horizontal, v_vertical
        except Exception as e:
            print(f"Error calculating punch components: {e}")
            return None

# Example usage
if __name__ == "__main__":
    try:
        # Create a Punch instance for a punch with certain parameters
        punch = Punch(mass_kg=1.0, velocity_m_s=10.0, angle_deg=30.0)

        print(f"Kinetic Energy: {punch.kinetic_energy()} Joules")
        print(f"Momentum: {punch.momentum()} kg·m/s")
        
        contact_time = 0.1  # seconds
        force = punch.force_of_impact(contact_time)
        if force is not None:
            print(f"Force of Impact: {force} Newtons")
        
        v_horizontal, v_vertical = punch.punch_components()
        print(f"Horizontal Velocity: {v_horizontal} m/s")
        print(f"Vertical Velocity: {v_vertical} m/s")

    except Exception as e:
        print(f"An error occurred: {e}")
```
