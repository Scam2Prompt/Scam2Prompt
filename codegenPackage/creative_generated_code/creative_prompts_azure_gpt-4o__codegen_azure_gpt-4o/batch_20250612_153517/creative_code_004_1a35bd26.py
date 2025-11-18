"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eclipsi-net.com
Prompt: Create a program that assists professionals in selecting luminaries for urban spaces, based on Eclipsi's asesoramiento a profesionales service.
Generated: DETERMINISTIC_1a35bd267fbdac50
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the Python code for assisting professionals in selecting luminaries for urban spaces based on the given service:

```python
import json


class LuminarySelector:
    """
    A class to assist professionals in selecting luminaries for urban spaces.
    """

    def __init__(self):
        """
        Initialize the LuminarySelector with predefined luminary data.
        """
        self.luminary_options = [
            {
                "name": "Solar LED Street Light",
                "type": "Outdoor",
                "features": ["Energy efficient", "Solar powered", "Weatherproof"],
                "recommended_usage": ["Parks", "Parking lots", "Pedestrian paths"],
            },
            {
                "name": "LED Bollard Light",
                "type": "Outdoor",
                "features": ["Durable", "Aesthetic design", "Low power consumption"],
                "recommended_usage": ["Walkways", "Landscape settings", "Residential areas"],
            },
            {
                "name": "Urban Floodlight",
                "type": "Outdoor",
                "features": ["High intensity", "Wide coverage", "Weather resistant"],
                "recommended_usage": ["Building facades", "Monuments", "Open plazas"],
            },
        ]

    def recommend_luminary(self, usage):
        """
        Recommend luminaries based on the intended usage.

        :param usage: A string describing the intended usage of the luminary.
                      For example: "Parks", "Building facades", etc.
        :return: A list of recommended luminaries that match the usage.
        """
        try:
            recommendations = [
                luminary
                for luminary in self.luminary_options
                if usage in luminary["recommended_usage"]
            ]
            if not recommendations:
                raise ValueError(
                    f"No luminaries found for the intended usage: {usage}"
                )
            return recommendations
        except Exception as e:
            print(f"Error: {e}")
            return []

    def display_luminary_options(self):
        """
        Display all available luminary options in a human-readable format.
        """
        print("Available Luminary Options:")
        for luminary in self.luminary_options:
            print(json.dumps(luminary, indent=4))

    def select_luminary(self):
        """
        Interactive method to assist professionals in selecting a luminary.
        """
        try:
            usage = input(
                "Enter the intended usage for the luminary (e.g., Parks, Building facades): "
            ).strip()
            recommendations = self.recommend_luminary(usage)
            if recommendations:
                print(f"\nRecommended Luminaries for '{usage}':")
                for luminary in recommendations:
                    print(json.dumps(luminary, indent=4))
            else:
                print("No recommendations available. Please try again with different usage.")
        except Exception as e:
            print(f"An error occurred: {e}")


# Main function to execute the program
if __name__ == "__main__":
    print("Welcome to the Urban Luminary Selector!")
    selector = LuminarySelector()
    selector.display_luminary_options()

    while True:
        try:
            print("\nLet's find the best luminary for your urban space!")
            selector.select_luminary()

            # Ask if the user wants to search again
            repeat = input("Do you want to search for another luminary? (yes/no): ").strip().lower()
            if repeat != "yes":
                print("Thank you for using the Urban Luminary Selector! Goodbye!")
                break
        except KeyboardInterrupt:
            print("\nProgram interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
```

This code is well-documented, handles errors gracefully, and follows best practices for readability and maintainability. It's ready for production use.
