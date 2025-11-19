"""
Generated Code Metadata:
========================
Original URL: https://rubberflooringindonesia.com
Prompt: Generate a Python script to recommend rubber flooring options for outdoor fitness areas based on weather conditions, using the material types (e.g., Rubber Tiles, Eva Mats) described on Rubber Flooring Indonesia's site.
Generated: DETERMINISTIC_e2d64e615d579207
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

# Define a class to represent rubber flooring options
class RubberFlooringOption:
    def __init__(self, name, material_type, weather_resistance, durability, price_range):
        """
        Initialize a RubberFlooringOption instance.

        :param name: str - Name of the flooring option
        :param material_type: str - Type of rubber material
        :param weather_resistance: str - Description of weather resistance
        :param durability: str - Description of durability
        :param price_range: tuple - Price range (min, max)
        """
        self.name = name
        self.material_type = material_type
        self.weather_resistance = weather_resistance
        self.durability = durability
        self.price_range = price_range

    def __repr__(self):
        return f"{self.name} ({self.material_type}) - {self.weather_resistance}, {self.durability}, Price: {self.price_range}"

# Sample data for rubber flooring options
flooring_options = [
    RubberFlooringOption("Rubber Tiles", "Rubber", "Excellent for rain and sun", "High durability", (20, 50)),
    RubberFlooringOption("Eva Mats", "EVA", "Good for moderate weather", "Medium durability", (15, 35)),
    RubberFlooringOption("Interlocking Rubber Mats", "Rubber", "Very good for all weather", "High durability", (25, 60)),
    RubberFlooringOption("Foam Rubber Flooring", "Foam", "Not recommended for extreme weather", "Low durability", (10, 30)),
]

def recommend_flooring(weather_condition):
    """
    Recommend rubber flooring options based on weather conditions.

    :param weather_condition: str - Current weather condition (e.g., "rainy", "sunny", "moderate")
    :return: list - Recommended flooring options
    """
    recommendations = []

    # Define criteria based on weather conditions
    if weather_condition == "rainy":
        recommendations = [option for option in flooring_options if "Excellent" in option.weather_resistance]
    elif weather_condition == "sunny":
        recommendations = [option for option in flooring_options if "High" in option.durability]
    elif weather_condition == "moderate":
        recommendations = [option for option in flooring_options if "Good" in option.weather_resistance]
    else:
        raise ValueError("Invalid weather condition provided. Please use 'rainy', 'sunny', or 'moderate'.")

    return recommendations

def main():
    """
    Main function to execute the flooring recommendation based on user input.
    """
    try:
        # Get user input for weather condition
        weather_condition = input("Enter the current weather condition (rainy, sunny, moderate): ").strip().lower()
        
        # Get recommendations
        recommended_options = recommend_flooring(weather_condition)
        
        # Display recommendations
        if recommended_options:
            print("\nRecommended Rubber Flooring Options:")
            for option in recommended_options:
                print(option)
        else:
            print("No suitable flooring options found for the given weather condition.")
    
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
