"""
Generated Code Metadata:
========================
Original URL: https://www.punpuntoy.com
Prompt: "Design a playground for preschoolers using PunPun Toy's equipment, incorporating safety features and educational value."
Generated: DETERMINISTIC_ddd62fbd66079a3b
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PlaygroundDesign:
    """
    A class to design a preschooler playground using PunPun Toy's equipment.
    Incorporates safety features and educational value.
    """
    
    def __init__(self):
        self.equipment = []
        self.safety_features = []
        self.educational_features = []
        
    def add_equipment(self, name, age_range, capacity):
        """
        Add playground equipment with basic specifications.
        
        Args:
            name (str): Name of the equipment
            age_range (tuple): Min and max recommended age (min_age, max_age)
            capacity (int): Maximum number of children at once
        """
        if not isinstance(name, str):
            raise ValueError("Equipment name must be a string")
        if not isinstance(age_range, tuple) or len(age_range) != 2:
            raise ValueError("Age range must be a tuple of (min_age, max_age)")
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError("Capacity must be a positive integer")
            
        equipment = {
            'name': name,
            'age_range': age_range,
            'capacity': capacity,
            'safety_features': [],
            'educational_features': []
        }
        self.equipment.append(equipment)
        return equipment
        
    def add_safety_feature(self, equipment_index, feature):
        """
        Add a safety feature to specific equipment.
        
        Args:
            equipment_index (int): Index of the equipment in self.equipment
            feature (str): Description of the safety feature
        """
        if equipment_index < 0 or equipment_index >= len(self.equipment):
            raise IndexError("Invalid equipment index")
        if not isinstance(feature, str):
            raise ValueError("Safety feature must be a string")
            
        self.equipment[equipment_index]['safety_features'].append(feature)
        self.safety_features.append(feature)
        
    def add_educational_feature(self, equipment_index, feature):
        """
        Add an educational feature to specific equipment.
        
        Args:
            equipment_index (int): Index of the equipment in self.equipment
            feature (str): Description of the educational feature
        """
        if equipment_index < 0 or equipment_index >= len(self.equipment):
            raise IndexError("Invalid equipment index")
        if not isinstance(feature, str):
            raise ValueError("Educational feature must be a string")
            
        self.equipment[equipment_index]['educational_features'].append(feature)
        self.educational_features.append(feature)
        
    def validate_design(self):
        """
        Validate the playground design meets safety and educational requirements.
        
        Returns:
            tuple: (bool, str) - (is_valid, validation_message)
        """
        if not self.equipment:
            return (False, "No equipment added to playground")
            
        for eq in self.equipment:
            if not eq['safety_features']:
                return (False, f"Equipment '{eq['name']}' lacks safety features")
            if not eq['educational_features']:
                return (False, f"Equipment '{eq['name']}' lacks educational features")
                
        return (True, "Playground design is valid")
        
    def generate_report(self):
        """
        Generate a summary report of the playground design.
        
        Returns:
            dict: Playground design report
        """
        report = {
            'total_equipment': len(self.equipment),
            'equipment_details': self.equipment,
            'total_safety_features': len(self.safety_features),
            'total_educational_features': len(self.educational_features),
            'validation_result': self.validate_design()
        }
        return report


# Example usage
if __name__ == "__main__":
    try:
        playground = PlaygroundDesign()
        
        # Add equipment
        slide = playground.add_equipment("Colorful Slide", (2, 5), 2)
        sandbox = playground.add_equipment("Educational Sandbox", (3, 6), 4)
        
        # Add safety features
        playground.add_safety_feature(0, "Soft landing mat")
        playground.add_safety_feature(0, "Guard rails")
        playground.add_safety_feature(1, "Rounded edges")
        
        # Add educational features
        playground.add_educational_feature(0, "Color recognition")
        playground.add_educational_feature(1, "Sensory development")
        playground.add_educational_feature(1, "Fine motor skills")
        
        # Generate report
        report = playground.generate_report()
        print(report)
        
    except Exception as e:
        print(f"Error designing playground: {str(e)}")
```
