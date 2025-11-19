"""
Generated Code Metadata:
========================
Original URL: https://ocuvana.com
Prompt: Write a Python script to calculate the estimated lifespan of magnetic eyelashes based on user care habits, using the "1–2 years with good care" guideline mentioned on Ocuvana's site.
Generated: DETERMINISTIC_20a67da679fe1587
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class MagneticEyelashLifespanEstimator:
    """
    A class to estimate the lifespan of magnetic eyelashes based on user care habits.
    """

    def __init__(self, care_level: str):
        """
        Initializes the estimator with the user's care level.

        :param care_level: A string indicating the level of care ('good', 'average', 'poor').
        """
        self.care_level = care_level.lower()
        self.lifespan_years = self._calculate_lifespan()

    def _calculate_lifespan(self) -> int:
        """
        Calculates the estimated lifespan in years based on care level.

        :return: Estimated lifespan in years.
        :raises ValueError: If the care level is not recognized.
        """
        if self.care_level == 'good':
            return 2  # 1-2 years with good care
        elif self.care_level == 'average':
            return 1  # Estimated lifespan for average care
        elif self.care_level == 'poor':
            return 0  # Minimal lifespan for poor care
        else:
            raise ValueError("Invalid care level. Please use 'good', 'average', or 'poor'.")

    def get_lifespan(self) -> str:
        """
        Returns a formatted string with the estimated lifespan.

        :return: A string indicating the estimated lifespan.
        """
        return f"Estimated lifespan of magnetic eyelashes with '{self.care_level}' care: {self.lifespan_years} year(s)."


def main():
    """
    Main function to run the lifespan estimator.
    """
    try:
        # User input for care level
        care_level = input("Enter your care level for magnetic eyelashes (good, average, poor): ")
        
        # Create an instance of the estimator
        estimator = MagneticEyelashLifespanEstimator(care_level)
        
        # Output the estimated lifespan
        print(estimator.get_lifespan())
    
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
