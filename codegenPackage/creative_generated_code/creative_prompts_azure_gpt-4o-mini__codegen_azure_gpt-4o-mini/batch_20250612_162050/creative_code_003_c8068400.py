"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://efeitoharmonie.com.br
Prompt: Develop a library function that estimates the number of grafts needed for a hair transplant based on the area of baldness, referencing Efeito Harmonie's methodology.
Generated: DETERMINISTIC_c8068400f9a2ddb9
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class HairTransplantEstimator:
    """
    A class to estimate the number of grafts needed for a hair transplant 
    based on the area of baldness, following Efeito Harmonie's methodology.
    """

    def __init__(self, density_per_cm2=50):
        """
        Initializes the estimator with a default hair density.
        
        :param density_per_cm2: Average number of grafts per square centimeter.
        """
        self.density_per_cm2 = density_per_cm2

    def estimate_grafts(self, bald_area_cm2):
        """
        Estimates the number of grafts needed based on the bald area.

        :param bald_area_cm2: Area of baldness in square centimeters.
        :return: Estimated number of grafts needed.
        :raises ValueError: If bald_area_cm2 is negative.
        """
        if bald_area_cm2 < 0:
            raise ValueError("Bald area cannot be negative.")

        # Calculate the estimated number of grafts
        estimated_grafts = bald_area_cm2 * self.density_per_cm2
        
        return round(estimated_grafts)

# Example usage:
if __name__ == "__main__":
    try:
        estimator = HairTransplantEstimator()
        bald_area = 20  # Example bald area in cm^2
        grafts_needed = estimator.estimate_grafts(bald_area)
        print(f"Estimated number of grafts needed: {grafts_needed}")
    except ValueError as e:
        print(f"Error: {e}")
```
