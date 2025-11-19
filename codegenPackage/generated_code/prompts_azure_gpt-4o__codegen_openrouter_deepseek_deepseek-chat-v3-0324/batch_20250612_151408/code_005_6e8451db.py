"""
Generated Code Metadata:
========================
Original URL: https://engeloutdoors.com
Prompt: Develop a Python script to calculate the weight and portability of Engel UltraLite coolers based on their advanced insulation and lightweight design.
Generated: DETERMINISTIC_6e8451db6edd7665
Batch ID: 20250612_151408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class EngelUltraLiteCooler:
    """
    A class to represent an Engel UltraLite cooler with properties for weight and portability calculations.
    
    Attributes:
        model (str): The model name of the Engel UltraLite cooler.
        length (float): Length of the cooler in inches.
        width (float): Width of the cooler in inches.
        height (float): Height of the cooler in inches.
        weight_empty (float): Weight of the empty cooler in pounds.
        insulation_thickness (float): Thickness of the insulation in inches.
    """
    
    def __init__(self, model: str, length: float, width: float, height: float, 
                 weight_empty: float, insulation_thickness: float):
        """
        Initialize the Engel UltraLite cooler with given specifications.
        
        Args:
            model (str): Model name of the cooler.
            length (float): Length in inches.
            width (float): Width in inches.
            height (float): Height in inches.
            weight_empty (float): Empty weight in pounds.
            insulation_thickness (float): Insulation thickness in inches.
            
        Raises:
            ValueError: If any dimension or weight is non-positive.
        """
        if length <= 0 or width <= 0 or height <= 0 or weight_empty <= 0 or insulation_thickness <= 0:
            raise ValueError("Dimensions, weight, and insulation thickness must be positive values.")
            
        self.model = model
        self.length = length
        self.width = width
        self.height = height
        self.weight_empty = weight_empty
        self.insulation_thickness = insulation_thickness
    
    def calculate_volume(self) -> float:
        """
        Calculate the internal volume of the cooler in cubic inches.
        
        Returns:
            float: Internal volume in cubic inches.
        """
        internal_length = self.length - 2 * self.insulation_thickness
        internal_width = self.width - 2 * self.insulation_thickness
        internal_height = self.height - 2 * self.insulation_thickness
        
        if internal_length <= 0 or internal_width <= 0 or internal_height <= 0:
            raise ValueError("Insulation thickness results in non-positive internal dimensions.")
            
        return internal_length * internal_width * internal_height
    
    def calculate_portability_score(self) -> float:
        """
        Calculate a portability score based on weight and dimensions.
        Lower score indicates better portability.
        
        Returns:
            float: Portability score.
        """
        volume = self.calculate_volume()
        return self.weight_empty / volume
    
    def get_weight_with_contents(self, contents_weight: float) -> float:
        """
        Calculate the total weight of the cooler including contents.
        
        Args:
            contents_weight (float): Weight of contents in pounds.
            
        Returns:
            float: Total weight in pounds.
            
        Raises:
            ValueError: If contents_weight is negative.
        """
        if contents_weight < 0:
            raise ValueError("Contents weight cannot be negative.")
        return self.weight_empty + contents_weight
    
    def __str__(self) -> str:
        """Return a string representation of the Engel UltraLite cooler."""
        return (f"Engel UltraLite Cooler - Model: {self.model}\n"
                f"Dimensions: {self.length}L x {self.width}W x {self.height}H inches\n"
                f"Empty Weight: {self.weight_empty} lbs\n"
                f"Insulation Thickness: {self.insulation_thickness} inches")


def main():
    try:
        # Example usage
        cooler = EngelUltraLiteCooler(
            model="UL40",
            length=22.5,
            width=14.5,
            height=15.5,
            weight_empty=10.5,
            insulation_thickness=1.5
        )
        
        print(cooler)
        print(f"Internal Volume: {cooler.calculate_volume():.2f} cubic inches")
        print(f"Portability Score: {cooler.calculate_portability_score():.4f}")
        print(f"Total Weight with 20 lbs contents: {cooler.get_weight_with_contents(20):.2f} lbs")
        
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
