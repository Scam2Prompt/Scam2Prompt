"""
Generated Code Metadata:
========================
Original URL: https://ohclift.com
Prompt: Develop a technical specification for an hydraulic disabled platform with a lifting capacity of 500 kg, incorporating the design and safety considerations highlighted in the OHC Lift product catalog.
Generated: DETERMINISTIC_5fde67988cb144bf
Batch ID: 20250622_205553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Technical Specification for Hydraulic Disabled Platform with 500kg Capacity

This module defines the technical specifications for a hydraulic disabled platform
based on OHC Lift product catalog requirements. It includes design parameters,
safety features, and operational constraints.
"""

class HydraulicDisabledPlatform:
    """
    A hydraulic platform designed for disabled access with 500kg lifting capacity.
    Incorporates design and safety features from OHC Lift product catalog.
    """
    
    def __init__(self):
        # Platform Specifications
        self.max_capacity = 500  # kg
        self.platform_dimensions = {'width': 900, 'depth': 1400}  # mm
        self.platform_height_range = (150, 900)  # mm (min to max)
        self.operating_voltage = 230  # V AC
        self.hydraulic_pressure = 16  # MPa
        
        # Safety Features
        self.safety_features = {
            'emergency_stop': True,
            'safety_edges': True,
            'anti_crush_sensors': True,
            'manual_lowering_valve': True,
            'non_slip_surface': True,
            'safety_handrails': True,
            'overload_protection': True
        }
        
        # Operational Parameters
        self.lifting_speed = 0.08  # m/s
        self.lower_speed = 0.1  # m/s
        self.max_operating_temperature = 40  # °C
        self.min_operating_temperature = -10  # °C
        self.ip_rating = 'IP54'  # Ingress protection rating
        
        # Structural Components
        self.materials = {
            'platform': 'aluminum',
            'frame': 'galvanized_steel',
            'hydraulic_cylinders': 'chromed_steel',
            'handrails': 'stainless_steel'
        }
        
        # Certifications
        self.certifications = [
            'EN 81-41',
            'CE Marking',
            'Machinery Directive 2006/42/EC'
        ]
    
    def check_load_capacity(self, current_load):
        """
        Verify if current load is within safe operating limits.
        
        Args:
            current_load (float): Current weight on platform in kg
            
        Returns:
            bool: True if load is within capacity, False otherwise
        """
        if current_load <= 0:
            raise ValueError("Load must be positive")
        return current_load <= self.max_capacity
    
    def emergency_procedure(self):
        """
        Execute emergency stop procedure.
        Activates all safety systems and lowers platform safely.
        """
        print("Emergency stop activated")
        print("Engaging safety brakes")
        print("Lowering platform to ground level")
        print("Disabling power to hydraulic system")
    
    def get_specification_summary(self):
        """
        Return a formatted summary of platform specifications.
        
        Returns:
            str: Formatted specification summary
        """
        summary = f"""
        Hydraulic Disabled Platform Specifications:
        - Max Capacity: {self.max_capacity} kg
        - Platform Dimensions: {self.platform_dimensions['width']}mm x {self.platform_dimensions['depth']}mm
        - Height Range: {self.platform_height_range[0]}mm to {self.platform_height_range[1]}mm
        - Lifting Speed: {self.lifting_speed} m/s
        - Safety Features: {', '.join([f for f, v in self.safety_features.items() if v])}
        - Certifications: {', '.join(self.certifications)}
        """
        return summary

# Example usage
if __name__ == "__main__":
    platform = HydraulicDisabledPlatform()
    print(platform.get_specification_summary())
    
    try:
        print(f"Can carry 450kg: {platform.check_load_capacity(450)}")
        print(f"Can carry 600kg: {platform.check_load_capacity(600)}")
    except ValueError as e:
        print(f"Error: {e}")
```
