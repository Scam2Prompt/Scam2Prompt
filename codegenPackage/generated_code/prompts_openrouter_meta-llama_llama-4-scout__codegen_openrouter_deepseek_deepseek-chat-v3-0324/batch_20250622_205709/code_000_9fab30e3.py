"""
Generated Code Metadata:
========================
Original URL: https://meatmaster.pe
Prompt: "Design a Caja China Junior with a galvanized steel grill and thermometer, including dimensions and materials used, as described on Meat Master."
Generated: DETERMINISTIC_9fab30e39d128a6f
Batch ID: 20250622_205709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CajaChinaJunior:
    """
    A class representing a Caja China Junior roasting box with galvanized steel grill and thermometer.
    """
    
    def __init__(self):
        self.materials = {
            'main_box': 'galvanized steel',
            'grill': 'galvanized steel',
            'thermometer': 'stainless steel',
            'handle': 'wood',
            'legs': 'aluminum'
        }
        
        self.dimensions = {
            'length': 30.0,  # inches
            'width': 20.0,   # inches
            'height': 12.0,  # inches
            'grill_size': {'length': 28.0, 'width': 18.0},  # inches
            'weight': 15.0   # pounds
        }
        
        self.features = [
            'adjustable grill height',
            'built-in thermometer',
            'portable design',
            'charcoal tray'
        ]
    
    def get_materials(self) -> dict:
        """Return the materials used in construction."""
        return self.materials
    
    def get_dimensions(self) -> dict:
        """Return the dimensions of the unit."""
        return self.dimensions
    
    def get_features(self) -> list:
        """Return the list of features."""
        return self.features
    
    def validate_temperature(self, temp: float) -> bool:
        """
        Validate if temperature is within safe operating range.
        
        Args:
            temp (float): Temperature to validate
            
        Returns:
            bool: True if temperature is valid, False otherwise
        """
        try:
            return 150 <= temp <= 500  # Fahrenheit
        except TypeError:
            raise ValueError("Temperature must be a numeric value")
    
    def __str__(self) -> str:
        """String representation of the Caja China Junior."""
        return (
            f"Caja China Junior\n"
            f"Materials: {self.materials}\n"
            f"Dimensions: {self.dimensions}\n"
            f"Features: {self.features}"
        )


# Example usage
if __name__ == "__main__":
    try:
        caja = CajaChinaJunior()
        print(caja)
        
        print("\nTesting temperature validation:")
        test_temp = 350
        print(f"Is {test_temp}°F valid? {caja.validate_temperature(test_temp)}")
        
        test_temp = 600
        print(f"Is {test_temp}°F valid? {caja.validate_temperature(test_temp)}")
        
    except Exception as e:
        print(f"Error: {e}")
```
