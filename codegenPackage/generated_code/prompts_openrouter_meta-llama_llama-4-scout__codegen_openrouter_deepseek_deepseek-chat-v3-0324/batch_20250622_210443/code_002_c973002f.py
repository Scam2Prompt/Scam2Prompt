"""
Generated Code Metadata:
========================
Original URL: https://pavingblockcirebon.com
Prompt: "Generate a Python code snippet to calculate the total cost of paving block installation for a garden path, considering factors like block size, design, and quantity, as discussed on Komando Block Cirebon's website."
Generated: DETERMINISTIC_c973002f96e468fc
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Garden Path Paving Cost Calculator

This script calculates the total cost of paving block installation for a garden path
based on block size, design type, quantity, and additional installation factors.

Inspired by Komando Block Cirebon's paving block specifications.
"""

class PavingCostCalculator:
    """
    Calculates the total cost of paving block installation.
    
    Attributes:
        block_prices (dict): Price per unit for each block size and design
        installation_rate (float): Installation cost per square meter
        waste_factor (float): Percentage of additional blocks for waste/cutting
    """
    
    def __init__(self):
        """Initialize with default pricing and rates."""
        # Prices in IDR per unit (example values)
        self.block_prices = {
            'hexagon': {'6cm': 15000, '8cm': 18000},
            'rectangle': {'6cm': 12000, '8cm': 15000},
            'square': {'6cm': 10000, '8cm': 13000}
        }
        
        # Installation cost per square meter
        self.installation_rate = 50000
        
        # Additional 5% for waste/cutting
        self.waste_factor = 1.05
    
    def calculate_area(self, length: float, width: float) -> float:
        """
        Calculate the area to be paved in square meters.
        
        Args:
            length: Path length in meters
            width: Path width in meters
            
        Returns:
            Area in square meters
            
        Raises:
            ValueError: If length or width is not positive
        """
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive numbers")
        return length * width
    
    def calculate_block_quantity(self, area: float, block_size: str) -> int:
        """
        Calculate number of blocks needed based on area and block size.
        
        Args:
            area: Area in square meters
            block_size: Thickness ('6cm' or '8cm')
            
        Returns:
            Number of blocks needed (rounded up)
            
        Raises:
            ValueError: If invalid block size or non-positive area
        """
        if area <= 0:
            raise ValueError("Area must be a positive number")
            
        if block_size not in ['6cm', '8cm']:
            raise ValueError("Block size must be either '6cm' or '8cm'")
            
        # Coverage per block in square meters (example values)
        coverage = {'6cm': 0.04, '8cm': 0.05}
        
        blocks_needed = area / coverage[block_size]
        return int(blocks_needed * self.waste_factor) + 1
    
    def calculate_total_cost(
        self,
        length: float,
        width: float,
        design: str,
        block_size: str
    ) -> dict:
        """
        Calculate total paving cost including materials and installation.
        
        Args:
            length: Path length in meters
            width: Path width in meters
            design: Block design ('hexagon', 'rectangle', 'square')
            block_size: Block thickness ('6cm' or '8cm')
            
        Returns:
            Dictionary containing cost breakdown
            
        Raises:
            ValueError: If invalid parameters are provided
        """
        try:
            if design not in self.block_prices:
                raise ValueError(f"Invalid design. Must be one of: {list(self.block_prices.keys())}")
                
            area = self.calculate_area(length, width)
            quantity = self.calculate_block_quantity(area, block_size)
            
            material_cost = quantity * self.block_prices[design][block_size]
            installation_cost = area * self.installation_rate
            
            return {
                'area_sqm': round(area, 2),
                'block_quantity': quantity,
                'material_cost': material_cost,
                'installation_cost': installation_cost,
                'total_cost': material_cost + installation_cost
            }
            
        except KeyError as e:
            raise ValueError(f"Invalid block size or design combination: {str(e)}")
        except Exception as e:
            raise ValueError(f"Error in calculation: {str(e)}")


# Example usage
if __name__ == "__main__":
    calculator = PavingCostCalculator()
    
    try:
        result = calculator.calculate_total_cost(
            length=10,
            width=1.5,
            design='hexagon',
            block_size='6cm'
        )
        
        print("Paving Cost Breakdown:")
        print(f"Area: {result['area_sqm']} m²")
        print(f"Blocks needed: {result['block_quantity']}")
        print(f"Material cost: IDR {result['material_cost']:,}")
        print(f"Installation cost: IDR {result['installation_cost']:,}")
        print(f"Total cost: IDR {result['total_cost']:,}")
        
    except ValueError as e:
        print(f"Error: {str(e)}")
```
