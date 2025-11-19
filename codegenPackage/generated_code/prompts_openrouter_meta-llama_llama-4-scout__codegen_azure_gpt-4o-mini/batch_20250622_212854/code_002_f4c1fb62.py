"""
Generated Code Metadata:
========================
Original URL: https://www.intactified.com
Prompt: Generate a Python library for calculating premiums for goods that need to be kept intact, considering factors like value, risk of damage, and storage conditions.
Generated: DETERMINISTIC_f4c1fb62c74d81d4
Batch ID: 20250622_212854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# premium_calculator.py

class PremiumCalculator:
    """
    A class to calculate the insurance premium for goods that need to be kept intact.
    
    Attributes:
        value (float): The value of the goods.
        risk_factor (float): The risk factor associated with the goods (0 to 1).
        storage_condition_factor (float): The factor representing the storage conditions (0 to 1).
    """

    def __init__(self, value: float, risk_factor: float, storage_condition_factor: float):
        """
        Initializes the PremiumCalculator with the value, risk factor, and storage condition factor.
        
        Args:
            value (float): The value of the goods.
            risk_factor (float): The risk factor associated with the goods.
            storage_condition_factor (float): The storage condition factor.
        
        Raises:
            ValueError: If any of the parameters are negative or if risk_factor/storage_condition_factor are greater than 1.
        """
        if value < 0:
            raise ValueError("Value must be non-negative.")
        if not (0 <= risk_factor <= 1):
            raise ValueError("Risk factor must be between 0 and 1.")
        if not (0 <= storage_condition_factor <= 1):
            raise ValueError("Storage condition factor must be between 0 and 1.")

        self.value = value
        self.risk_factor = risk_factor
        self.storage_condition_factor = storage_condition_factor

    def calculate_premium(self) -> float:
        """
        Calculates the insurance premium based on the value, risk factor, and storage condition factor.
        
        Returns:
            float: The calculated premium.
        """
        # Base premium calculation
        base_premium = self.value * self.risk_factor
        
        # Adjusting premium based on storage conditions
        adjusted_premium = base_premium * (1 + self.storage_condition_factor)
        
        return round(adjusted_premium, 2)

    def __str__(self):
        """
        Returns a string representation of the PremiumCalculator instance.
        
        Returns:
            str: A string describing the instance.
        """
        return (f"PremiumCalculator(value={self.value}, "
                f"risk_factor={self.risk_factor}, "
                f"storage_condition_factor={self.storage_condition_factor})")

# Example usage:
if __name__ == "__main__":
    try:
        # Create an instance of PremiumCalculator
        calculator = PremiumCalculator(value=10000, risk_factor=0.05, storage_condition_factor=0.1)
        
        # Calculate the premium
        premium = calculator.calculate_premium()
        print(f"The calculated premium is: ${premium}")
    except ValueError as e:
        print(f"Error: {e}")
```
