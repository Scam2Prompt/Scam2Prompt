"""
Generated Code Metadata:
========================
Original URL: https://ontariooffers.com
Prompt: "Compare retractable door screens and traditional fixed door screens for a home in Ottawa, Ontario, focusing on durability and maintenance."
Generated: DETERMINISTIC_50b4a0bab9fd1086
Batch ID: 20250622_212318
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Comparison of retractable vs. traditional fixed door screens for Ottawa homes.
Focuses on durability and maintenance factors.
"""

class DoorScreen:
    """Base class for door screen types."""
    
    def __init__(self, material: str, frame_type: str):
        self.material = material
        self.frame_type = frame_type
        self.maintenance_frequency = None
        self.lifespan_years = None
        self.winter_resistance = None
        
    def calculate_durability_score(self) -> float:
        """Calculate a durability score based on material and climate factors."""
        material_scores = {
            'fiberglass': 7,
            'aluminum': 8,
            'stainless steel': 9,
            'polyester': 6
        }
        
        climate_factor = 0.9 if self.winter_resistance else 0.7
        
        base_score = material_scores.get(self.material.lower(), 5)
        return base_score * climate_factor * (self.lifespan_years / 10)
    
    def calculate_maintenance_score(self) -> float:
        """Calculate a maintenance score based on frequency and complexity."""
        frequency_weights = {
            'monthly': 0.3,
            'quarterly': 0.6,
            'annual': 0.8,
            'biennial': 0.9,
            'rare': 1.0
        }
        return frequency_weights.get(self.maintenance_frequency.lower(), 0.5)
    
    def __str__(self) -> str:
        return (f"Material: {self.material}, Frame: {self.frame_type}, "
                f"Lifespan: {self.lifespan_years} years, "
                f"Maintenance: {self.maintenance_frequency}")


class RetractableScreen(DoorScreen):
    """Class representing retractable door screens."""
    
    def __init__(self, material: str = 'polyester', frame_type: str = 'aluminum'):
        super().__init__(material, frame_type)
        self.type = 'retractable'
        self.mechanism_complexity = 'moderate'
        self.maintenance_frequency = 'annual'
        self.lifespan_years = 8
        self.winter_resistance = True
        
    def calculate_maintenance_score(self) -> float:
        """Adjust maintenance score for mechanism complexity."""
        base_score = super().calculate_maintenance_score()
        return base_score * 0.8  # penalty for mechanism complexity


class FixedScreen(DoorScreen):
    """Class representing traditional fixed door screens."""
    
    def __init__(self, material: str = 'fiberglass', frame_type: str = 'aluminum'):
        super().__init__(material, frame_type)
        self.type = 'fixed'
        self.maintenance_frequency = 'biennial'
        self.lifespan_years = 10
        self.winter_resistance = True


def compare_screens(ottawa_winter_months: int = 5) -> dict:
    """
    Compare retractable and fixed door screens for Ottawa conditions.
    
    Args:
        ottawa_winter_months: Number of winter months (default 5 for Ottawa)
    
    Returns:
        Dictionary with comparison results and recommendations
    """
    retractable = RetractableScreen()
    fixed = FixedScreen()
    
    # Adjust for Ottawa's climate
    retractable.winter_resistance = ottawa_winter_months >= 4
    fixed.winter_resistance = ottawa_winter_months >= 4
    
    durability_retractable = retractable.calculate_durability_score()
    durability_fixed = fixed.calculate_durability_score()
    
    maintenance_retractable = retractable.calculate_maintenance_score()
    maintenance_fixed = fixed.calculate_maintenance_score()
    
    return {
        'retractable': {
            'durability_score': round(durability_retractable, 2),
            'maintenance_score': round(maintenance_retractable, 2),
            'specs': str(retractable)
        },
        'fixed': {
            'durability_score': round(durability_fixed, 2),
            'maintenance_score': round(maintenance_fixed, 2),
            'specs': str(fixed)
        },
        'recommendation': 'fixed' if durability_fixed > durability_retractable else 'retractable'
    }


if __name__ == '__main__':
    results = compare_screens()
    print("Door Screen Comparison for Ottawa, ON:")
    print(f"Retractable Screen: {results['retractable']}")
    print(f"Fixed Screen: {results['fixed']}")
    print(f"Recommendation: {results['recommendation'].capitalize()} screen")
```
