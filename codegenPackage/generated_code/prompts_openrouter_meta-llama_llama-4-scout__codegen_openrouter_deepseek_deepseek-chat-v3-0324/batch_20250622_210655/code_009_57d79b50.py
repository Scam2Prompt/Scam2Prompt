"""
Generated Code Metadata:
========================
Original URL: https://www.yanmaq.cl
Prompt: What are the benefits of using Yanmar's AMS technology and proportional control in mini excavators for construction and excavation projects?
Generated: DETERMINISTIC_57d79b50e6b0ab61
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script demonstrates the benefits of Yanmar's AMS technology and proportional control in mini excavators.
It simulates a construction project scenario where these technologies are utilized.
"""

class MiniExcavator:
    """Class representing a mini excavator with AMS and proportional control features."""
    
    def __init__(self, model_name, has_ams=True, has_proportional_control=True):
        """
        Initialize the mini excavator with specified features.
        
        Args:
            model_name (str): Name of the excavator model
            has_ams (bool): Whether it has AMS technology (default: True)
            has_proportional_control (bool): Whether it has proportional control (default: True)
        """
        self.model_name = model_name
        self.has_ams = has_ams
        self.has_proportional_control = has_proportional_control
        self.fuel_efficiency = 0
        self.operating_costs = 0
        self.precision_level = 0
        self.productivity = 0
        
    def calculate_benefits(self):
        """Calculate the benefits based on the excavator's features."""
        try:
            if self.has_ams:
                self.fuel_efficiency = 0.15  # 15% improvement
                self.operating_costs = -0.10  # 10% reduction
            
            if self.has_proportional_control:
                self.precision_level = 0.20  # 20% improvement
                self.productivity = 0.25  # 25% improvement
            
            return {
                'fuel_efficiency': self.fuel_efficiency,
                'operating_costs': self.operating_costs,
                'precision_level': self.precision_level,
                'productivity': self.productivity
            }
        except Exception as e:
            print(f"Error calculating benefits: {e}")
            return None
    
    def generate_report(self):
        """Generate a report of the excavator's benefits."""
        benefits = self.calculate_benefits()
        if not benefits:
            return "Unable to generate report due to calculation errors."
        
        report = f"""
        Yanmar Mini Excavator {self.model_name} Benefits Report:
        --------------------------------------------------
        AMS Technology Enabled: {'Yes' if self.has_ams else 'No'}
        Proportional Control Enabled: {'Yes' if self.has_proportional_control else 'No'}
        
        Key Benefits:
        - Fuel Efficiency Improvement: {benefits['fuel_efficiency']*100:.0f}%
        - Operating Cost Reduction: {abs(benefits['operating_costs'])*100:.0f}%
        - Precision Level Improvement: {benefits['precision_level']*100:.0f}%
        - Productivity Increase: {benefits['productivity']*100:.0f}%
        """
        return report


def demonstrate_excavator_benefits():
    """Demonstrate the benefits of AMS and proportional control."""
    try:
        # Create excavator with both technologies
        advanced_excavator = MiniExcavator("SV40")
        print(advanced_excavator.generate_report())
        
        # Create excavator without these technologies for comparison
        basic_excavator = MiniExcavator("Basic Model", False, False)
        print("\nComparison with basic model:")
        print(basic_excavator.generate_report())
        
    except Exception as e:
        print(f"Error demonstrating excavator benefits: {e}")


if __name__ == "__main__":
    demonstrate_excavator_benefits()
```
