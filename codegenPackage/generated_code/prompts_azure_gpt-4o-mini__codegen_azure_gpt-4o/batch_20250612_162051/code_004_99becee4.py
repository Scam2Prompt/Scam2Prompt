"""
Generated Code Metadata:
========================
Original URL: https://eric-navarro.com
Prompt: Provide a code example for setting up a professional home studio environment for voice acting, including hardware recommendations like the ATH-M40x headphones.
Generated: DETERMINISTIC_99becee4de3f7ffb
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script: HomeStudioSetup.py
Description: This script provides recommendations for setting up a professional home studio environment for voice acting.
Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Import necessary modules
import json

def get_hardware_recommendations():
    """
    Function to return hardware recommendations for a professional home studio setup.
    Returns:
        dict: A dictionary containing hardware recommendations.
    """
    try:
        # Hardware recommendations
        recommendations = {
            "Microphone": {
                "Name": "Audio-Technica AT2020",
                "Description": "A high-quality condenser microphone suitable for voice acting.",
                "PriceRange": "$100-$150"
            },
            "Headphones": {
                "Name": "Audio-Technica ATH-M40x",
                "Description": "Professional monitor headphones with excellent sound quality.",
                "PriceRange": "$100-$120"
            },
            "Audio Interface": {
                "Name": "Focusrite Scarlett 2i2 (3rd Gen)",
                "Description": "A reliable audio interface for connecting your microphone to your computer.",
                "PriceRange": "$150-$200"
            },
            "Pop Filter": {
                "Name": "Aokeo Pop Filter",
                "Description": "Reduces plosive sounds for cleaner audio recordings.",
                "PriceRange": "$10-$20"
            },
            "Microphone Stand": {
                "Name": "On-Stage MS7701B",
                "Description": "A sturdy microphone stand for stable positioning.",
                "PriceRange": "$30-$50"
            },
            "Acoustic Treatment": {
                "Name": "Foamily Acoustic Foam Panels",
                "Description": "Improves sound quality by reducing echo and background noise.",
                "PriceRange": "$20-$50"
            }
        }
        return recommendations
    except Exception as e:
        # Handle any unexpected errors
        print(f"Error occurred while fetching hardware recommendations: {e}")
        return {}

def save_recommendations_to_file(recommendations, filename="HomeStudioRecommendations.json"):
    """
    Function to save hardware recommendations to a JSON file.
    Args:
        recommendations (dict): The hardware recommendations to save.
        filename (str): The name of the file to save the recommendations to.
    """
    try:
        # Save recommendations to a JSON file
        with open(filename, "w") as file:
            json.dump(recommendations, file, indent=4)
        print(f"Recommendations successfully saved to {filename}")
    except Exception as e:
        # Handle file I/O errors
        print(f"Error occurred while saving recommendations to file: {e}")

def main():
    """
    Main function to execute the script.
    """
    print("Setting up a professional home studio environment for voice acting...")
    
    # Get hardware recommendations
    recommendations = get_hardware_recommendations()
    
    # Display recommendations
    print("\nHardware Recommendations:")
    for category, details in recommendations.items():
        print(f"\n{category}:")
        for key, value in details.items():
            print(f"  {key}: {value}")
    
    # Save recommendations to a file
    save_recommendations_to_file(recommendations)

# Entry point of the script
if __name__ == "__main__":
    main()
```
