"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eric-navarro.com
Prompt: Provide a code example for setting up a professional home studio environment for voice acting, including hardware recommendations like the ATH-M40x headphones.
Generated: DETERMINISTIC_99becee4de3f7ffb
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Professional Home Studio Setup Script for Voice Acting

This script provides a guide for setting up a professional home studio environment for voice acting.
It outlines recommended hardware and software, and provides sample functionality for organizing studio-related tasks.

Hardware Recommendations:
- Microphone: Audio-Technica AT2020 or Rode NT1
- Headphones: Audio-Technica ATH-M40x
- Audio Interface: Focusrite Scarlett 2i2 or PreSonus AudioBox USB 96
- Pop Filter and Boom Arm
- Acoustic Foam Panels / Soundproofing materials

Software Recommendations:
- DAW (Digital Audio Workstation): Audacity (Free), Adobe Audition (Paid), Reaper (Paid)
"""

import os
import json


class HomeStudioSetup:
    """
    A class to simulate a professional voice acting studio setup.
    """

    def __init__(self):
        self.hardware = {
            "microphone": "Audio-Technica AT2020",
            "headphones": "Audio-Technica ATH-M40x",
            "audio_interface": "Focusrite Scarlett 2i2",
            "pop_filter": "Standard Pop Filter",
            "boom_arm": "Adjustable Boom Arm",
            "acoustic_panels": "Foam Panels or Soundproofing Materials"
        }
        self.software = {
            "DAW": ["Audacity", "Adobe Audition", "Reaper"]
        }

    def display_hardware_recommendations(self):
        """
        Display recommended hardware for the studio setup.
        """
        print("Recommended Hardware for Your Studio:")
        for key, value in self.hardware.items():
            print(f"{key.capitalize()}: {value}")

    def display_software_recommendations(self):
        """
        Display recommended software for the studio setup.
        """
        print("\nRecommended Software for Your Studio:")
        for category, options in self.software.items():
            print(f"{category.capitalize()}: {', '.join(options)}")

    def save_recommendations_to_file(self, filename="studio_recommendations.json"):
        """
        Save hardware and software recommendations to a JSON file.

        Args:
            filename (str): Name of the file to save recommendations. Defaults to 'studio_recommendations.json'.
        """
        try:
            recommendations = {
                "hardware": self.hardware,
                "software": self.software
            }
            with open(filename, "w") as file:
                json.dump(recommendations, file, indent=4)
            print(f"\nRecommendations successfully saved to {filename}.")
        except Exception as e:
            print(f"Error occurred while saving recommendations to file: {e}")

    def load_recommendations_from_file(self, filename="studio_recommendations.json"):
        """
        Load hardware and software recommendations from a JSON file.

        Args:
            filename (str): Name of the file to load recommendations from. Defaults to 'studio_recommendations.json'.
        """
        try:
            if not os.path.exists(filename):
                print(f"File {filename} does not exist. Please save recommendations first.")
                return

            with open(filename, "r") as file:
                recommendations = json.load(file)
                self.hardware = recommendations.get("hardware", {})
                self.software = recommendations.get("software", {})
            print(f"\nRecommendations successfully loaded from {filename}.")
        except Exception as e:
            print(f"Error occurred while loading recommendations from file: {e}")


# Example Usage
if __name__ == "__main__":
    studio = HomeStudioSetup()

    # Display Recommendations
    studio.display_hardware_recommendations()
    studio.display_software_recommendations()

    # Save Recommendations to File
    studio.save_recommendations_to_file()

    # Load Recommendations from File
    studio.load_recommendations_from_file()
    studio.display_hardware_recommendations()
    studio.display_software_recommendations()
```
