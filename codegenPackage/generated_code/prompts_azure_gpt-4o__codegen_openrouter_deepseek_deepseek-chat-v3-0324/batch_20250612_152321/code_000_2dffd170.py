"""
Generated Code Metadata:
========================
Original URL: https://apnhardware.co.th
Prompt: Write Python code to calculate the weight and quantity of steel screws based on specifications provided by APN Hardware, such as gauge size and material type.
Generated: DETERMINISTIC_2dffd1700bc18efa
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SteelScrewCalculator:
    """
    A class to calculate the weight and quantity of steel screws based on specifications.
    Uses data from APN Hardware for gauge sizes and material densities.
    """
    
    # Density of steel in g/cm³ (typical value for carbon steel)
    STEEL_DENSITY = 7.85
    
    # Screw gauge to diameter mapping (in mm) - APN Hardware specifications
    GAUGE_TO_DIAMETER = {
        '0': 1.52, '1': 1.85, '2': 2.18, '3': 2.51, '4': 2.84,
        '5': 3.18, '6': 3.51, '7': 3.84, '8': 4.17, '9': 4.50,
        '10': 4.83, '11': 5.16, '12': 5.49, '14': 6.15
    }
    
    def __init__(self, gauge: str, length_mm: float, head_type: str = 'flat'):
        """
        Initialize the calculator with screw specifications.
        
        Args:
            gauge (str): Screw gauge number (0-14, skipping 13 as per APN specs)
            length_mm (float): Length of screw in millimeters
            head_type (str): Type of screw head (affects volume calculation)
        """
        self.gauge = gauge
        self.length_mm = length_mm
        self.head_type = head_type.lower()
        
        if gauge not in self.GAUGE_TO_DIAMETER:
            raise ValueError(f"Invalid gauge. Must be one of: {list(self.GAUGE_TO_DIAMETER.keys())}")
        if length_mm <= 0:
            raise ValueError("Length must be positive")
    
    def calculate_single_screw_weight(self) -> float:
        """
        Calculate the weight of a single screw in grams.
        
        Returns:
            float: Weight in grams
        """
        diameter_mm = self.GAUGE_TO_DIAMETER[self.gauge]
        radius_mm = diameter_mm / 2
        
        # Calculate shank volume (cylinder)
        shank_volume_mm3 = 3.14159 * (radius_mm ** 2) * self.length_mm
        
        # Approximate head volume based on type
        if self.head_type == 'flat':
            head_volume_mm3 = 0  # Negligible for flat head
        elif self.head_type == 'pan':
            head_volume_mm3 = 0.5 * shank_volume_mm3  # Approximation
        elif self.head_type == 'round':
            head_volume_mm3 = 0.8 * shank_volume_mm3  # Approximation
        else:
            raise ValueError(f"Unknown head type: {self.head_type}")
        
        total_volume_mm3 = shank_volume_mm3 + head_volume_mm3
        volume_cm3 = total_volume_mm3 / 1000  # Convert mm³ to cm³
        
        return volume_cm3 * self.STEEL_DENSITY
    
    def calculate_total_weight(self, quantity: int) -> float:
        """
        Calculate total weight for a given quantity of screws.
        
        Args:
            quantity (int): Number of screws
            
        Returns:
            float: Total weight in grams
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        
        single_weight = self.calculate_single_screw_weight()
        return single_weight * quantity
    
    def calculate_quantity_for_weight(self, target_weight_g: float) -> int:
        """
        Calculate how many screws are needed to reach a target weight.
        
        Args:
            target_weight_g (float): Desired total weight in grams
            
        Returns:
            int: Number of screws needed (rounded up)
        """
        if target_weight_g <= 0:
            raise ValueError("Target weight must be positive")
        
        single_weight = self.calculate_single_screw_weight()
        return int(target_weight_g // single_weight) + (target_weight_g % single_weight > 0)


# Example usage
if __name__ == "__main__":
    try:
        # Create a screw calculator for gauge 8, 50mm long flat head screws
        calculator = SteelScrewCalculator(gauge='8', length_mm=50)
        
        # Calculate single screw weight
        weight = calculator.calculate_single_screw_weight()
        print(f"Single screw weight: {weight:.2f} grams")
        
        # Calculate total weight for 100 screws
        total_weight = calculator.calculate_total_weight(100)
        print(f"Total weight for 100 screws: {total_weight:.2f} grams")
        
        # Calculate how many screws make 1kg
        quantity = calculator.calculate_quantity_for_weight(1000)
        print(f"Screws needed for 1kg: {quantity}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
