"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stellarcropgame.fun
Prompt: Generate a Python script that models the interactions between different soil types and crop yields, reflecting the dynamic ecosystem system mentioned on the Stellar Crop website.
Generated: DETERMINISTIC_c0d26dadc56b37a8
Batch ID: 20250612_162535
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class Soil:
    """
    Represents a soil type with specific attributes that impact crop yields.
    """
    def __init__(self, name, fertility, moisture_retention, pH):
        """
        Initialize a soil type.

        :param name: Name of the soil type (e.g., "Loamy", "Clay", "Sandy").
        :param fertility: Fertility score (1-10 scale).
        :param moisture_retention: Moisture retention score (1-10 scale).
        :param pH: Soil pH level (acidic, neutral, alkaline).
        """
        self.name = name
        self.fertility = fertility
        self.moisture_retention = moisture_retention
        self.pH = pH

    def __str__(self):
        return f"Soil Type: {self.name}, Fertility: {self.fertility}, Moisture Retention: {self.moisture_retention}, pH: {self.pH}"


class Crop:
    """
    Represents a crop type with specific requirements for optimal yield.
    """
    def __init__(self, name, ideal_fertility, ideal_moisture, ideal_pH):
        """
        Initialize a crop type.

        :param name: Name of the crop (e.g., "Wheat", "Corn", "Rice").
        :param ideal_fertility: Ideal fertility score (1-10 scale).
        :param ideal_moisture: Ideal moisture score (1-10 scale).
        :param ideal_pH: Ideal pH level (acidic, neutral, alkaline).
        """
        self.name = name
        self.ideal_fertility = ideal_fertility
        self.ideal_moisture = ideal_moisture
        self.ideal_pH = ideal_pH

    def __str__(self):
        return f"Crop Type: {self.name}, Ideal Fertility: {self.ideal_fertility}, Ideal Moisture: {self.ideal_moisture}, Ideal pH: {self.ideal_pH}"

    def calculate_yield(self, soil):
        """
        Calculate crop yield based on soil properties.

        :param soil: Soil object to evaluate against crop requirements.
        :return: Yield percentage (0-100%).
        """
        try:
            fertility_score = max(0, 100 - abs(soil.fertility - self.ideal_fertility) * 10)
            moisture_score = max(0, 100 - abs(soil.moisture_retention - self.ideal_moisture) * 10)
            pH_score = 100 if soil.pH == self.ideal_pH else 50  # Either ideal or suboptimal.

            # Combine scores to calculate weighted yield
            yield_percentage = (fertility_score * 0.4 + moisture_score * 0.4 + pH_score * 0.2)
            return round(yield_percentage, 2)
        except Exception as e:
            logging.error(f"Error calculating yield: {e}")
            return 0


def demo():
    """
    Demonstrates the interaction between soil types and crop yields.
    """
    logging.info("Initializing soil types...")
    loamy_soil = Soil(name="Loamy", fertility=8, moisture_retention=7, pH="neutral")
    clay_soil = Soil(name="Clay", fertility=6, moisture_retention=9, pH="acidic")
    sandy_soil = Soil(name="Sandy", fertility=4, moisture_retention=3, pH="alkaline")

    logging.info("Initializing crop types...")
    wheat = Crop(name="Wheat", ideal_fertility=7, ideal_moisture=6, ideal_pH="neutral")
    corn = Crop(name="Corn", ideal_fertility=8, ideal_moisture=8, ideal_pH="neutral")
    rice = Crop(name="Rice", ideal_fertility=6, ideal_moisture=9, ideal_pH="acidic")

    logging.info("Calculating crop yields...")
    soil_types = [loamy_soil, clay_soil, sandy_soil]
    crops = [wheat, corn, rice]

    for crop in crops:
        for soil in soil_types:
            yield_percentage = crop.calculate_yield(soil)
            logging.info(f"Crop: {crop.name} | Soil: {soil.name} | Yield: {yield_percentage}%")

if __name__ == "__main__":
    demo()
```
