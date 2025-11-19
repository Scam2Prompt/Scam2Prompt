"""
Generated Code Metadata:
========================
Original URL: https://www.yanmaq.cl
Prompt: How do Yanmar mini excavators contribute to efficient and precise excavation tasks in confined spaces, and what technologies enable this capability?
Generated: DETERMINISTIC_40e698cd1cc54376
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# This script simulates the capabilities of Yanmar mini excavators in confined spaces
# by modeling their key technologies and operational parameters.

class MiniExcavator:
    """
    A class to represent a Yanmar mini excavator and its capabilities.
    """
    
    def __init__(self, model: str, weight: float, digging_depth: float, swing_radius: float):
        """
        Initialize the mini excavator with basic specifications.
        
        Args:
            model (str): Model name of the excavator
            weight (float): Operating weight in kg
            digging_depth (float): Maximum digging depth in meters
            swing_radius (float): Minimum swing radius in meters
        """
        self.model = model
        self.weight = weight
        self.digging_depth = digging_depth
        self.swing_radius = swing_radius
        self.technologies = []
        
    def add_technology(self, tech_name: str, description: str):
        """
        Add a technology feature to the excavator.
        
        Args:
            tech_name (str): Name of the technology
            description (str): Description of how it enhances performance
        """
        self.technologies.append({
            'name': tech_name,
            'description': description
        })
    
    def calculate_work_area(self, available_space: float) -> float:
        """
        Calculate the percentage of available space that can be effectively used.
        
        Args:
            available_space (float): Available space in square meters
            
        Returns:
            float: Percentage of space that can be effectively used (0-100)
            
        Raises:
            ValueError: If available_space is negative
        """
        if available_space < 0:
            raise ValueError("Available space cannot be negative")
            
        # Simplified calculation based on swing radius
        required_space = 3.14 * (self.swing_radius ** 2)
        efficiency = min(100, (available_space / required_space) * 100)
        return round(efficiency, 2)
    
    def simulate_excavation(self, task_complexity: int) -> dict:
        """
        Simulate an excavation task and return performance metrics.
        
        Args:
            task_complexity (int): Complexity level from 1 (simple) to 5 (complex)
            
        Returns:
            dict: Dictionary containing performance metrics
            
        Raises:
            ValueError: If task_complexity is not between 1 and 5
        """
        if task_complexity < 1 or task_complexity > 5:
            raise ValueError("Task complexity must be between 1 and 5")
            
        # Base performance values
        precision = 95 - (task_complexity * 5)
        speed = 100 - (task_complexity * 10)
        fuel_efficiency = 80 - (task_complexity * 3)
        
        # Apply technology bonuses
        for tech in self.technologies:
            if "precision" in tech['name'].lower():
                precision += 3
            if "speed" in tech['name'].lower():
                speed += 5
            if "efficiency" in tech['name'].lower():
                fuel_efficiency += 2
        
        # Ensure values stay within bounds
        precision = max(70, min(100, precision))
        speed = max(50, min(100, speed))
        fuel_efficiency = max(60, min(100, fuel_efficiency))
        
        return {
            'precision': precision,
            'speed': speed,
            'fuel_efficiency': fuel_efficiency,
            'technologies_used': [tech['name'] for tech in self.technologies]
        }


def demonstrate_excavator_capabilities():
    """
    Demonstrate the capabilities of a Yanmar mini excavator in confined spaces.
    """
    try:
        # Create a Yanmar mini excavator instance
        yanmar_sv40 = MiniExcavator(
            model="SV40",
            weight=4000,  # kg
            digging_depth=2.5,  # meters
            swing_radius=1.2  # meters
        )
        
        # Add key technologies
        yanmar_sv40.add_technology(
            "Zero Tail Swing",
            "Allows full rotation without extending beyond tracks, ideal for confined spaces"
        )
        yanmar_sv40.add_technology(
            "Auto-IDLE System",
            "Automatically reduces engine speed when not in use, improving fuel efficiency"
        )
        yanmar_sv40.add_technology(
            "Precision Control System",
            "Provides fine control over hydraulic movements for accurate digging"
        )
        
        # Demonstrate capabilities
        space_utilization = yanmar_sv40.calculate_work_area(available_space=10)
        print(f"Space utilization efficiency: {space_utilization}%")
        
        performance = yanmar_sv40.simulate_excavation(task_complexity=3)
        print("\nPerformance metrics:")
        for metric, value in performance.items():
            if metric != 'technologies_used':
                print(f"{metric.replace('_', ' ').title()}: {value}%")
        
        print("\nTechnologies utilized:")
        for tech in performance['technologies_used']:
            print(f"- {tech}")
            
    except ValueError as e:
        print(f"Error in demonstration: {str(e)}")


if __name__ == "__main__":
    demonstrate_excavator_capabilities()
```
