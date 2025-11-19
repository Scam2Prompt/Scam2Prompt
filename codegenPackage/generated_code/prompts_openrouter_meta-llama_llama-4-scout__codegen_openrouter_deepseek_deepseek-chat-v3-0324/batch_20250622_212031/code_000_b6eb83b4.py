"""
Generated Code Metadata:
========================
Original URL: https://frigoterm.ro
Prompt: "Write a Python code snippet to compare the features of Gree Bora A4 Silver air conditioners with different BTU ratings."
Generated: DETERMINISTIC_b6eb83b48822c5b1
Batch ID: 20250622_212031
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class AirConditioner:
    """
    Represents an air conditioner with various features.
    """
    def __init__(self, model: str, btu_rating: int, price: float, 
                 energy_efficiency: str, noise_level: float, 
                 features: list):
        """
        Initialize an air conditioner instance.
        
        Args:
            model: Model name of the AC
            btu_rating: BTU rating (cooling capacity)
            price: Price in USD
            energy_efficiency: Energy efficiency rating
            noise_level: Noise level in dB
            features: List of special features
        """
        self.model = model
        self.btu_rating = btu_rating
        self.price = price
        self.energy_efficiency = energy_efficiency
        self.noise_level = noise_level
        self.features = features
    
    def __str__(self):
        return f"{self.model} ({self.btu_rating} BTU)"

def compare_ac_units(ac_units: list):
    """
    Compare multiple air conditioner units and display results in a table.
    
    Args:
        ac_units: List of AirConditioner objects to compare
    """
    try:
        if not ac_units:
            raise ValueError("No AC units provided for comparison")
            
        comparison_data = []
        for ac in ac_units:
            comparison_data.append({
                'Model': ac.model,
                'BTU Rating': ac.btu_rating,
                'Price ($)': ac.price,
                'Energy Efficiency': ac.energy_efficiency,
                'Noise Level (dB)': ac.noise_level,
                'Features': ', '.join(ac.features)
            })
        
        df = pd.DataFrame(comparison_data)
        df.set_index('Model', inplace=True)
        
        print("\nComparison of Gree Bora A4 Silver Air Conditioners:")
        print(df.to_markdown(tablefmt="grid"))
        
    except Exception as e:
        print(f"Error during comparison: {str(e)}")

if __name__ == "__main__":
    # Sample data for Gree Bora A4 Silver models with different BTU ratings
    ac_units = [
        AirConditioner(
            model="Gree Bora A4 Silver 8000 BTU",
            btu_rating=8000,
            price=299.99,
            energy_efficiency="A++",
            noise_level=42.5,
            features=["WiFi Control", "Self-Cleaning", "Sleep Mode"]
        ),
        AirConditioner(
            model="Gree Bora A4 Silver 12000 BTU",
            btu_rating=12000,
            price=399.99,
            energy_efficiency="A+",
            noise_level=45.0,
            features=["WiFi Control", "Self-Cleaning", "Turbo Mode"]
        ),
        AirConditioner(
            model="Gree Bora A4 Silver 18000 BTU",
            btu_rating=18000,
            price=499.99,
            energy_efficiency="A",
            noise_level=48.0,
            features=["WiFi Control", "Self-Cleaning", "Turbo Mode", "Ionizer"]
        )
    ]
    
    compare_ac_units(ac_units)
```
