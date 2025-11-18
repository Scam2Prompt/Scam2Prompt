"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neumayaa.com.ar
Prompt: Create a program to analyze tire durability based on usage scenarios, referencing Neumayaa's advice on prolonging tire life and maintaining optimal performance.
Generated: DETERMINISTIC_41821532697b6f8a
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program: Tire Durability Analyzer
Description: This program analyzes tire durability based on usage scenarios, referencing Neumayaa's advice on prolonging tire life. 
The program takes inputs about tire usage and provides recommendations for maintaining optimal performance and prolonging tire life.
Language: Python
Author: Expert Programmer
"""

# Import necessary libraries for error handling and computations
import sys


class TireDurabilityAnalyzer:
    """
    TireDurabilityAnalyzer class to analyze tire durability based on usage scenarios.
    """

    def __init__(self, brand, model, mileage, terrain_type, tire_pressure, driving_style):
        """
        Initialize the tire analyzer with key attributes.
        
        :param brand: The brand of the tire.
        :param model: The model of the tire.
        :param mileage: Mileage of the tire in kilometers.
        :param terrain_type: Terrain type the tire is used on (e.g., highway, off-road).
        :param tire_pressure: Current tire pressure in psi.
        :param driving_style: Driving style (e.g., aggressive, moderate, cautious).
        """
        self.brand = brand
        self.model = model
        self.mileage = mileage
        self.terrain_type = terrain_type.lower()
        self.tire_pressure = tire_pressure
        self.driving_style = driving_style.lower()

    def analyze_durability(self):
        """
        Analyze the durability of the tire based on the input parameters.

        :return: Recommendations for prolonging tire life and maintaining optimal performance.
        """
        recommendations = []

        # Check mileage threshold
        if self.mileage > 40000:
            recommendations.append(
                "Consider replacing the tire as it has exceeded the recommended mileage threshold."
            )

        # Check terrain type
        if self.terrain_type == "off-road":
            recommendations.append(
                "Off-road driving can accelerate tire wear. Ensure the tire is designed for off-road usage."
            )
        elif self.terrain_type == "highway":
            recommendations.append(
                "Highway driving typically results in less wear. Ensure tire pressure is optimally maintained."
            )
        else:
            recommendations.append(
                "Unknown terrain type detected. Use caution and consult Neumayaa's advice for your specific condition."
            )

        # Check tire pressure
        if self.tire_pressure < 30 or self.tire_pressure > 35:
            recommendations.append(
                "Maintain tire pressure between 30-35 psi for optimal performance. Adjust immediately."
            )

        # Check driving style
        if self.driving_style == "aggressive":
            recommendations.append(
                "Aggressive driving can cause uneven wear. Adopt a more moderate style for better durability."
            )
        elif self.driving_style == "cautious":
            recommendations.append(
                "Cautious driving helps prolong tire life. Keep up the good habit!"
            )
        elif self.driving_style != "moderate":
            recommendations.append(
                "Unknown driving style detected. Refer to Neumayaa's guidelines for safe driving."
            )

        # If no issues are detected
        if not recommendations:
            return "The tire is in good condition. No further action needed."

        return recommendations


def main():
    """
    Main function to interact with the user and analyze tire durability.
    """
    try:
        print("Welcome to the Tire Durability Analyzer!")
        # Gather inputs from the user
        brand = input("Enter the tire brand: ").strip()
        model = input("Enter the tire model: ").strip()
        mileage = int(input("Enter the mileage of the tire (in kilometers): ").strip())
        terrain_type = input(
            "Enter the terrain type (e.g., highway, off-road): "
        ).strip()
        tire_pressure = float(
            input("Enter the current tire pressure (in psi): ").strip()
        )
        driving_style = input(
            "Enter your driving style (e.g., aggressive, moderate, cautious): "
        ).strip()

        # Validate inputs
        if mileage < 0 or tire_pressure < 0:
            raise ValueError("Mileage and tire pressure must be positive values.")

        # Create an analyzer instance
        analyzer = TireDurabilityAnalyzer(
            brand, model, mileage, terrain_type, tire_pressure, driving_style
        )

        # Analyze and display recommendations
        recommendations = analyzer.analyze_durability()

        print("\nTire Durability Analysis:")
        if isinstance(recommendations, list):
            for rec in recommendations:
                print(f"- {rec}")
        else:
            print(recommendations)

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
