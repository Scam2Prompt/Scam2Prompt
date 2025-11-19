"""
Generated Code Metadata:
========================
Original URL: https://utkutantoglu.com
Prompt: Generate a Python function that simulates the process of a gastric sleeve surgery, focusing on the reduction of stomach size and its effects on appetite.
Generated: DETERMINISTIC_074cf0ec40f4b35b
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Patient:
    """
    Represents a patient undergoing gastric sleeve surgery.
    
    Attributes:
        name (str): Name of the patient.
        original_stomach_size (float): Original stomach size in milliliters.
        current_stomach_size (float): Current stomach size in milliliters.
        appetite_level (float): Appetite level from 0 (no appetite) to 10 (very hungry).
    """
    
    def __init__(self, name: str, original_stomach_size: float):
        """
        Initialize a Patient instance.
        
        Args:
            name: Name of the patient.
            original_stomach_size: Original stomach size in milliliters.
        """
        self.name = name
        self.original_stomach_size = original_stomach_size
        self.current_stomach_size = original_stomach_size
        self.appetite_level = 8.0  # Default starting appetite level
    
    def perform_surgery(self, reduction_percentage: float):
        """
        Simulate gastric sleeve surgery by reducing stomach size.
        
        Args:
            reduction_percentage: Percentage of stomach to remove (0-100).
            
        Raises:
            ValueError: If reduction_percentage is not between 0 and 100.
        """
        if not 0 <= reduction_percentage <= 100:
            raise ValueError("Reduction percentage must be between 0 and 100")
        
        reduction_factor = reduction_percentage / 100
        self.current_stomach_size = self.original_stomach_size * (1 - reduction_factor)
        self._update_appetite()
    
    def _update_appetite(self):
        """
        Update appetite level based on current stomach size.
        """
        size_ratio = self.current_stomach_size / self.original_stomach_size
        # Appetite decreases as stomach size decreases, but not linearly
        self.appetite_level = 10 * (size_ratio ** 0.5)  # Square root for non-linear relationship
    
    def eat(self, food_volume: float) -> str:
        """
        Simulate eating and return status.
        
        Args:
            food_volume: Volume of food consumed in milliliters.
            
        Returns:
            str: Status message indicating success or discomfort.
            
        Raises:
            ValueError: If food_volume is negative.
        """
        if food_volume < 0:
            raise ValueError("Food volume cannot be negative")
        
        if food_volume > self.current_stomach_size * 0.8:  # 80% capacity threshold
            return f"Discomfort: {self.name} feels overly full"
        elif food_volume > self.current_stomach_size * 0.5:  # 50% capacity warning
            return f"Warning: {self.name} is approaching fullness"
        else:
            return f"{self.name} ate comfortably"
    
    def get_status(self) -> dict:
        """
        Return current patient status.
        
        Returns:
            dict: Contains current stomach size and appetite level.
        """
        return {
            'name': self.name,
            'current_stomach_size_ml': round(self.current_stomach_size, 2),
            'appetite_level': round(self.appetite_level, 2),
            'original_stomach_size_ml': round(self.original_stomach_size, 2)
        }


def simulate_surgery(patient_name: str, original_size: float, reduction_percent: float) -> dict:
    """
    Simulate gastric sleeve surgery and return results.
    
    Args:
        patient_name: Name of the patient.
        original_size: Original stomach size in milliliters.
        reduction_percent: Percentage of stomach to remove (0-100).
        
    Returns:
        dict: Patient status before and after surgery.
        
    Raises:
        ValueError: If parameters are invalid.
    """
    try:
        patient = Patient(patient_name, original_size)
        pre_surgery = patient.get_status()
        
        patient.perform_surgery(reduction_percent)
        post_surgery = patient.get_status()
        
        return {
            'pre_surgery': pre_surgery,
            'post_surgery': post_surgery,
            'stomach_reduction_percent': reduction_percent
        }
    except ValueError as e:
        raise ValueError(f"Invalid simulation parameters: {str(e)}")


# Example usage
if __name__ == "__main__":
    try:
        results = simulate_surgery("John Doe", 1000.0, 75.0)
        print("Pre-surgery:", results['pre_surgery'])
        print("Post-surgery:", results['post_surgery'])
        
        # Test eating
        patient = Patient("Test Patient", 1000.0)
        patient.perform_surgery(75.0)  # Reduce to 25% of original size
        print("\nEating tests:")
        print(patient.eat(100))  # Comfortable
        print(patient.eat(150))  # Warning
        print(patient.eat(250))  # Discomfort
    except ValueError as e:
        print(f"Error: {str(e)}")
```
