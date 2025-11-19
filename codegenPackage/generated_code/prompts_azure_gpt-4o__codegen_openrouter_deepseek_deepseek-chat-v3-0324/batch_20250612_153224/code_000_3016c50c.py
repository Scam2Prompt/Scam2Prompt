"""
Generated Code Metadata:
========================
Original URL: https://atilumber.com
Prompt: Write a Python script to calculate the volume of sawn timber required for a construction project, using dimensions and specifications similar to those described by Askar Trading International.
Generated: DETERMINISTIC_3016c50c924556bd
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class TimberVolumeCalculator:
    """
    A class to calculate the volume of sawn timber required for a construction project.
    The calculations are based on dimensions and specifications similar to Askar Trading International.
    """
    
    def __init__(self):
        """Initialize the calculator with default values."""
        self.timber_data = []
    
    def add_timber_piece(self, length, width, height, quantity=1):
        """
        Add a timber piece to the calculation.
        
        Args:
            length (float): Length of the timber piece in meters.
            width (float): Width of the timber piece in meters.
            height (float): Height (thickness) of the timber piece in meters.
            quantity (int, optional): Number of pieces with these dimensions. Defaults to 1.
            
        Raises:
            ValueError: If any dimension is not positive or quantity is not positive.
        """
        if length <= 0 or width <= 0 or height <= 0:
            raise ValueError("All dimensions must be positive numbers.")
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
            
        self.timber_data.append({
            'length': length,
            'width': width,
            'height': height,
            'quantity': quantity
        })
    
    def calculate_total_volume(self):
        """
        Calculate the total volume of all timber pieces in cubic meters.
        
        Returns:
            float: Total volume in cubic meters.
        """
        total_volume = 0.0
        for piece in self.timber_data:
            volume = piece['length'] * piece['width'] * piece['height'] * piece['quantity']
            total_volume += volume
        return total_volume
    
    def calculate_total_volume_with_wastage(self, wastage_percentage=10):
        """
        Calculate total volume including wastage percentage.
        
        Args:
            wastage_percentage (float, optional): Percentage of wastage to add. Defaults to 10.
            
        Returns:
            float: Total volume including wastage in cubic meters.
            
        Raises:
            ValueError: If wastage percentage is negative.
        """
        if wastage_percentage < 0:
            raise ValueError("Wastage percentage cannot be negative.")
            
        base_volume = self.calculate_total_volume()
        wastage_factor = 1 + (wastage_percentage / 100)
        return base_volume * wastage_factor
    
    def reset_calculator(self):
        """Clear all stored timber data."""
        self.timber_data = []


def main():
    """Main function to demonstrate the TimberVolumeCalculator."""
    calculator = TimberVolumeCalculator()
    
    try:
        # Example usage
        calculator.add_timber_piece(2.4, 0.1, 0.05, 10)  # 10 pieces of 2.4m x 0.1m x 0.05m
        calculator.add_timber_piece(3.0, 0.15, 0.1, 5)   # 5 pieces of 3.0m x 0.15m x 0.1m
        
        total_volume = calculator.calculate_total_volume()
        total_with_wastage = calculator.calculate_total_volume_with_wastage()
        
        print(f"Total timber volume: {total_volume:.3f} m³")
        print(f"Total volume including 10% wastage: {total_with_wastage:.3f} m³")
        
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
