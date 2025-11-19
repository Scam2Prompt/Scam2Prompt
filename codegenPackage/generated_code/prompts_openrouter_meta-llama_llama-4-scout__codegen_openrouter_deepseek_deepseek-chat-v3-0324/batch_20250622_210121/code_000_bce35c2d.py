"""
Generated Code Metadata:
========================
Original URL: https://www.iepolitecnicomunicipalcali.edu.co
Prompt: What are the core values of the Institución Educativa Politécnico Municipal de Cali, and how do they relate to its mission and vision?
Generated: DETERMINISTIC_bce35c2d413c8f8a
Batch ID: 20250622_210121
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# This script models the core values of Institución Educativa Politécnico Municipal de Cali
# and demonstrates their relationship with the institution's mission and vision

class CoreValue:
    """Represents a core value of the institution"""
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __str__(self):
        return f"{self.name}: {self.description}"

class Institution:
    """Models the educational institution with its core values, mission, and vision"""
    
    def __init__(self, name):
        self.name = name
        self.core_values = []
        self.mission = ""
        self.vision = ""
    
    def add_core_value(self, name, description):
        """Add a core value to the institution"""
        self.core_values.append(CoreValue(name, description))
    
    def set_mission(self, mission):
        """Set the institution's mission statement"""
        self.mission = mission
    
    def set_vision(self, vision):
        """Set the institution's vision statement"""
        self.vision = vision
    
    def relate_values_to_mission_vision(self):
        """Demonstrate how core values relate to mission and vision"""
        if not self.core_values or not self.mission or not self.vision:
            raise ValueError("Missing core values, mission, or vision")
        
        print(f"\nCore Values of {self.name}:")
        for value in self.core_values:
            print(f"- {value}")
        
        print("\nMission:")
        print(self.mission)
        
        print("\nVision:")
        print(self.vision)
        
        print("\nRelationship:")
        print("The core values serve as foundational principles that guide")
        print("the institution in fulfilling its mission and achieving its vision.")

def main():
    """Main function to demonstrate the institution's values and their relationship"""
    try:
        # Create institution instance
        institution = Institution("Institución Educativa Politécnico Municipal de Cali")
        
        # Add core values
        institution.add_core_value(
            "Respect", 
            "Promoting mutual respect among all members of the educational community"
        )
        institution.add_core_value(
            "Responsibility", 
            "Encouraging personal and social responsibility in all actions"
        )
        institution.add_core_value(
            "Excellence", 
            "Striving for academic and personal excellence in all endeavors"
        )
        institution.add_core_value(
            "Solidarity", 
            "Fostering solidarity and cooperation within the community"
        )
        institution.add_core_value(
            "Integrity", 
            "Maintaining honesty and ethical behavior in all circumstances"
        )
        
        # Set mission and vision
        institution.set_mission(
            "To provide comprehensive, quality education that develops critical thinking, "
            "technical skills, and ethical values, preparing students to contribute "
            "positively to society."
        )
        
        institution.set_vision(
            "To be recognized as a leading educational institution that transforms lives "
            "through innovative education, forming competent and ethical professionals "
            "committed to social development."
        )
        
        # Demonstrate relationship
        institution.relate_values_to_mission_vision()
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
