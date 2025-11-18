"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://somcivil.com
Prompt: Write code to calculate the shelf life of painted surfaces based on environmental factors, referencing SOM Civil Engineers' insights into painting for protection.
Generated: DETERMINISTIC_64f20380d2484fe7
Batch ID: 20250612_151429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class PaintedSurface:
    def __init__(self, paint_type: str, application_date: datetime.date, exposure_conditions: dict):
        """
        Initialize a PaintedSurface instance.

        Parameters:
            paint_type (str): Type of paint used (e.g., 'oil-based', 'water-based').
            application_date (datetime.date): Date when the paint was applied.
            exposure_conditions (dict): Environmental factors affecting shelf life, e.g.,
                                         {'UV': int, 'Humidity': int, 'Temperature': int}
        """
        self.paint_type = paint_type
        self.application_date = application_date
        self.exposure_conditions = exposure_conditions

    def calculate_shelf_life(self) -> int:
        """
        Calculate the estimated shelf life of the painted surface in months
        based on the paint type and environmental factors.

        Returns:
            int: Estimated shelf life in months.
        """
        # Base shelf life in months for different paint types
        base_shelf_life = {
            'oil-based': 60,
            'water-based': 36,
            'latex': 48
        }
        
        # Fetch base shelf life
        shelf_life = base_shelf_life.get(self.paint_type.lower(), 0)
        
        if shelf_life == 0:
            raise ValueError(f"Unknown paint type: {self.paint_type}")

        # Adjust shelf life based on environmental conditions
        shelf_life -= self.exposure_conditions.get('UV', 0) // 10
        shelf_life -= self.exposure_conditions.get('Humidity', 0) // 5
        shelf_life -= self.exposure_conditions.get('Temperature', 0) // 2

        # Ensure shelf life does not drop below zero
        return max(shelf_life, 0)

    def remaining_life(self) -> int:
        """
        Calculate the remaining life of the painted surface.

        Returns:
            int: Remaining life in months.
        """
        try:
            total_shelf_life = self.calculate_shelf_life()
            months_since_application = (datetime.date.today() - self.application_date).days // 30
            remaining_life = total_shelf_life - months_since_application

            return max(remaining_life, 0)  # Ensure remaining life is not negative
        except Exception as e:
            print(f"Error calculating remaining life: {e}")
            return 0


# Example usage
if __name__ == "__main__":
    try:
        # Define environmental factors
        exposure = {'UV': 30, 'Humidity': 70, 'Temperature': 80}  # Example values
        application_date = datetime.date(2020, 1, 1)  # Example application date

        # Create instance of PaintedSurface
        surface = PaintedSurface(paint_type='water-based', application_date=application_date, exposure_conditions=exposure)

        # Calculate remaining life
        remaining_months = surface.remaining_life()
        print(f"Remaining shelf life of the painted surface: {remaining_months} months")
    except Exception as e:
        print(f"Failed to calculate remaining shelf life: {e}")
```
