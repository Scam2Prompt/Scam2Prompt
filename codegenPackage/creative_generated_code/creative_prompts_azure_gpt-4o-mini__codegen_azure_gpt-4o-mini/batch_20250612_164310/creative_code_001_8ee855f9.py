"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yexinerangel.com
Prompt: Write a Python function that calculates insurance premiums based on the risk factors outlined in Yexine Rangel's portfolio of solutions for personal and patrimonial risks.
Generated: DETERMINISTIC_8ee855f9c20f6a61
Batch ID: 20250612_164310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InsuranceCalculator:
    """
    A class to calculate insurance premiums based on risk factors.
    """

    def __init__(self, base_premium: float):
        """
        Initializes the InsuranceCalculator with a base premium.

        :param base_premium: A float representing the base premium amount.
        """
        if base_premium <= 0:
            raise ValueError("Base premium must be a positive number.")
        
        self.base_premium = base_premium

    def calculate_premium(self, risk_factors: dict) -> float:
        """
        Calculates the insurance premium based on risk factors.

        :param risk_factors: A dictionary containing risk factors with their respective weights.
                             Expected format: {'factor_name': weight, ...}
        :return: The calculated insurance premium as a float.
        """
        if not isinstance(risk_factors, dict):
            raise TypeError("Risk factors must be provided as a dictionary.")

        total_risk = 0.0
        
        for factor, weight in risk_factors.items():
            if not isinstance(weight, (int, float)):
                raise ValueError(f"Weight for '{factor}' must be a numeric value.")
            if weight < 0:
                raise ValueError(f"Weight for '{factor}' cannot be negative.")
            
            total_risk += weight
        
        # Calculate the final premium based on total risk weight
        final_premium = self.base_premium * (1 + total_risk)
        
        # Ensure the final premium is not negative
        if final_premium < 0:
            raise ValueError("Calculated premium cannot be negative.")
        
        return round(final_premium, 2)

# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the insurance calculator with a base premium
        calculator = InsuranceCalculator(base_premium=500.0)

        # Define risk factors and their weights
        risk_factors = {
            'fire_risk': 0.2,
            'theft_risk': 0.15,
            'natural_disaster_risk': 0.1
        }

        # Calculate the insurance premium
        premium = calculator.calculate_premium(risk_factors)
        print(f"The calculated insurance premium is: ${premium}")

    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
```
