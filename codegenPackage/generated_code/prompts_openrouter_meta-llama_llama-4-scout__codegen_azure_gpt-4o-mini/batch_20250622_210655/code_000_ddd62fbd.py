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
class Playground:
    def __init__(self, name):
        """
        Initialize the Playground with a name and an empty list of equipment.
        
        :param name: str - The name of the playground
        """
        self.name = name
        self.equipment = []
        self.safety_features = []
    
    def add_equipment(self, equipment):
        """
        Add equipment to the playground.
        
        :param equipment: dict - A dictionary containing equipment details
        """
        if not isinstance(equipment, dict):
            raise ValueError("Equipment must be a dictionary.")
        
        self.equipment.append(equipment)
        print(f"Added equipment: {equipment['name']}")

    def add_safety_feature(self, feature):
        """
        Add a safety feature to the playground.
        
        :param feature: str - A description of the safety feature
        """
        if not isinstance(feature, str):
            raise ValueError("Safety feature must be a string.")
        
        self.safety_features.append(feature)
        print(f"Added safety feature: {feature}")

    def display_playground_info(self):
        """
        Display the information about the playground, including equipment and safety features.
        """
        print(f"Playground Name: {self.name}")
        print("Equipment:")
        for eq in self.equipment:
            print(f"- {eq['name']} (Educational Value: {eq['educational_value']})")
        print("Safety Features:")
        for sf in self.safety_features:
            print(f"- {sf}")

# Example usage
if __name__ == "__main__":
    try:
        # Create a new playground
        my_playground = Playground("PunPun Toy's Adventure Playground")

        # Add equipment with educational value
        my_playground.add_equipment({"name": "Climbing Frame", "educational_value": "Physical coordination"})
        my_playground.add_equipment({"name": "Sand Pit", "educational_value": "Creativity and sensory play"})
        
        # Add safety features
        my_playground.add_safety_feature("Soft rubber flooring")
        my_playground.add_safety_feature("Rounded edges on all equipment")

        # Display playground information
        my_playground.display_playground_info()
    
    except Exception as e:
        print(f"An error occurred: {e}")
```
