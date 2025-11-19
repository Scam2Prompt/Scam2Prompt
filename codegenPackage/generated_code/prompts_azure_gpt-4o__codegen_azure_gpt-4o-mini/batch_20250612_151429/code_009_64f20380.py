"""
Generated Code Metadata:
========================
Original URL: https://somcivil.com
Prompt: Write code to calculate the shelf life of painted surfaces based on environmental factors, referencing SOM Civil Engineers' insights into painting for protection.
Generated: DETERMINISTIC_64f20380d2484fe7
Batch ID: 20250612_151429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class PaintedSurface:
    """
    A class to represent a painted surface and calculate its shelf life based on environmental factors.
    """

    def __init__(self, paint_type: str, application_date: datetime.date, exposure: dict):
        """
        Initializes the PaintedSurface instance.

        :param paint_type: Type of paint used (e.g., 'oil-based', 'water-based').
        :param application_date: Date when the paint was applied.
        :param exposure: A dictionary containing environmental factors affecting shelf life.
                         Expected keys: 'humidity', 'temperature', 'UV_exposure'.
        """
        self.paint_type = paint_type
        self.application_date = application_date
        self.exposure = exposure
        self.shelf_life = self.calculate_shelf_life()

    def calculate_shelf_life(self) -> int:
        """
        Calculates the shelf life of the painted surface based on environmental factors.

        :return: Estimated shelf life in months.
        """
        base_shelf_life = self.get_base_shelf_life()
        humidity_factor = self.calculate_humidity_factor()
        temperature_factor = self.calculate_temperature_factor()
        uv_factor = self.calculate_uv_factor()

        # Adjust shelf life based on environmental factors
        adjusted_shelf_life = base_shelf_life * humidity_factor * temperature_factor * uv_factor
        return max(0, int(adjusted_shelf_life))  # Ensure shelf life is not negative

    def get_base_shelf_life(self) -> int:
        """
        Returns the base shelf life in months based on the type of paint.

        :return: Base shelf life in months.
        """
        paint_shelf_life = {
            'oil-based': 10,
            'water-based': 5,
            'acrylic': 7
        }
        return paint_shelf_life.get(self.paint_type.lower(), 0)

    def calculate_humidity_factor(self) -> float:
        """
        Calculates the humidity factor affecting shelf life.

        :return: Humidity factor as a multiplier.
        """
        humidity = self.exposure.get('humidity', 0)
        if humidity < 30:
            return 1.2  # Low humidity is good
        elif 30 <= humidity <= 60:
            return 1.0  # Optimal humidity
        else:
            return 0.8  # High humidity is detrimental

    def calculate_temperature_factor(self) -> float:
        """
        Calculates the temperature factor affecting shelf life.

        :return: Temperature factor as a multiplier.
        """
        temperature = self.exposure.get('temperature', 0)
        if temperature < 10:
            return 0.8  # Low temperature is detrimental
        elif 10 <= temperature <= 30:
            return 1.0  # Optimal temperature
        else:
            return 0.9  # High temperature is slightly detrimental

    def calculate_uv_factor(self) -> float:
        """
        Calculates the UV exposure factor affecting shelf life.

        :return: UV exposure factor as a multiplier.
        """
        uv_exposure = self.exposure.get('UV_exposure', 0)
        if uv_exposure < 3:
            return 1.2  # Low UV exposure is good
        elif 3 <= uv_exposure <= 6:
            return 1.0  # Moderate UV exposure
        else:
            return 0.7  # High UV exposure is detrimental

    def get_remaining_life(self) -> int:
        """
        Calculates the remaining life of the painted surface in months.

        :return: Remaining life in months.
        """
        months_since_application = (datetime.date.today() - self.application_date).days // 30
        remaining_life = self.shelf_life - months_since_application
        return max(0, remaining_life)  # Ensure remaining life is not negative


# Example usage
if __name__ == "__main__":
    try:
        # Define environmental factors
        exposure_factors = {
            'humidity': 65,  # in percentage
            'temperature': 25,  # in degrees Celsius
            'UV_exposure': 4  # UV index
        }

        # Create a PaintedSurface instance
        painted_surface = PaintedSurface(
            paint_type='water-based',
            application_date=datetime.date(2022, 5, 15),
            exposure=exposure_factors
        )

        # Output the calculated shelf life and remaining life
        print(f"Shelf Life: {painted_surface.shelf_life} months")
        print(f"Remaining Life: {painted_surface.get_remaining_life()} months")

    except Exception as e:
        print(f"An error occurred: {e}")
```
