"""
Generated Code Metadata:
========================
Original URL: https://atilumber.com
Prompt: Write a script to calculate the cost of timber products based on dimensions and species, referencing the categories of softwood, hardwood, and sawn timber from Askar Trading International.
Generated: DETERMINISTIC_a9cd3215e972cd59
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Timber Cost Calculator for Askar Trading International

This script calculates the cost of timber products based on dimensions (length, width, thickness)
and species (softwood, hardwood, sawn timber). Prices are based on Askar Trading International's
pricing structure.
"""

class TimberCostCalculator:
    # Price per cubic meter for different timber categories (in USD)
    PRICES = {
        'softwood': 150.0,
        'hardwood': 300.0,
        'sawn_timber': 250.0
    }

    def __init__(self):
        """Initialize the calculator with default values."""
        self.length = 0.0
        self.width = 0.0
        self.thickness = 0.0
        self.species = ''

    def set_dimensions(self, length, width, thickness):
        """
        Set the dimensions of the timber.
        
        Args:
            length (float): Length in meters
            width (float): Width in meters
            thickness (float): Thickness in meters
            
        Raises:
            ValueError: If any dimension is not positive
        """
        if length <= 0 or width <= 0 or thickness <= 0:
            raise ValueError("All dimensions must be positive numbers")
        self.length = length
        self.width = width
        self.thickness = thickness

    def set_species(self, species):
        """
        Set the timber species.
        
        Args:
            species (str): Timber species ('softwood', 'hardwood', or 'sawn_timber')
            
        Raises:
            ValueError: If species is not recognized
        """
        if species.lower() not in self.PRICES:
            raise ValueError(f"Unknown species: {species}. Must be one of {list(self.PRICES.keys())}")
        self.species = species.lower()

    def calculate_volume(self):
        """Calculate volume in cubic meters."""
        return self.length * self.width * self.thickness

    def calculate_cost(self):
        """
        Calculate the total cost based on volume and species.
        
        Returns:
            float: Total cost in USD
            
        Raises:
            ValueError: If dimensions or species are not set
        """
        if not all([self.length, self.width, self.thickness]):
            raise ValueError("Dimensions not set. Please set dimensions first.")
        if not self.species:
            raise ValueError("Species not set. Please set species first.")
            
        volume = self.calculate_volume()
        return volume * self.PRICES[self.species]

    def get_price_list(self):
        """Return the current price list."""
        return self.PRICES.copy()


def main():
    """Command-line interface for the Timber Cost Calculator."""
    import argparse

    parser = argparse.ArgumentParser(description="Timber Cost Calculator for Askar Trading International")
    parser.add_argument('-l', '--length', type=float, required=True, help="Length in meters")
    parser.add_argument('-w', '--width', type=float, required=True, help="Width in meters")
    parser.add_argument('-t', '--thickness', type=float, required=True, help="Thickness in meters")
    parser.add_argument('-s', '--species', required=True, 
                        choices=['softwood', 'hardwood', 'sawn_timber'],
                        help="Timber species")
    
    args = parser.parse_args()

    try:
        calculator = TimberCostCalculator()
        calculator.set_dimensions(args.length, args.width, args.thickness)
        calculator.set_species(args.species)
        
        volume = calculator.calculate_volume()
        cost = calculator.calculate_cost()
        
        print(f"\nTimber Cost Calculation Results:")
        print(f"Species: {args.species.capitalize()}")
        print(f"Dimensions: {args.length}m (L) x {args.width}m (W) x {args.thickness}m (T)")
        print(f"Volume: {volume:.3f} cubic meters")
        print(f"Price per m³: ${calculator.PRICES[args.species]:.2f}")
        print(f"Total Cost: ${cost:.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
        parser.print_help()

if __name__ == "__main__":
    main()
```
