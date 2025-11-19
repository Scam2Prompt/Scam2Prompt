"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://krajkovac.rs
Prompt: Generate a code snippet for a travel app that highlights Krajkovac's unique features, including Krajkovačko Lake and its historical significance.
Generated: DETERMINISTIC_d41a5804552b20a8
Batch ID: 20250612_161104
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import json

# Define a function to fetch information about Krajkovac's unique features
def get_krajkovac_features():
    """
    Fetch and highlight Krajkovac's unique features, including Krajkovačko Lake 
    and its historical significance. Returns the data as a structured dictionary.
    """
    try:
        # Hardcoded data for the purpose of this example
        krajkovac_data = {
            "location": "Krajkovac",
            "features": {
                "Krajkovačko Lake": {
                    "description": "A stunning freshwater lake surrounded by lush greenery.",
                    "activities": ["Fishing", "Boating", "Hiking"],
                },
                "historical_significance": {
                    "description": "Krajkovac has a rich history dating back to the medieval period.",
                    "landmarks": ["Ancient Fortress", "Old Town Square"],
                },
            },
            "recommended_visit_season": "Spring and Summer",
        }

        # Return the structured data
        return krajkovac_data
    
    except Exception as e:
        # Exception handling to ensure robustness
        print(f"Error occurred while fetching Krajkovac information: {str(e)}")
        return None

# Define a function to display information in a readable format
def display_krajkovac_info(features):
    """
    Display Krajkovac's features in a user-friendly format.
    """
    try:
        if not features:
            print("No information available to display.")
            return

        print("\nWelcome to Krajkovac!")
        print("Here are the unique features of this destination:\n")

        print("1. Krajkovačko Lake:")
        lake_info = features["features"]["Krajkovačko Lake"]
        print(f"   - Description: {lake_info['description']}")
        print(f"   - Activities Available: {', '.join(lake_info['activities'])}\n")

        print("2. Historical Significance:")
        historical_info = features["features"]["historical_significance"]
        print(f"   - Description: {historical_info['description']}")
        print(f"   - Landmarks to Visit: {', '.join(historical_info['landmarks'])}\n")

        print(f"Recommended Season to Visit: {features['recommended_visit_season']}")

    except KeyError as e:
        # Handle missing keys gracefully
        print(f"Data format issue: Missing key {str(e)}")
    except Exception as e:
        # Handle other unexpected errors
        print(f"Error occurred while displaying information: {str(e)}")

# Main entry point for the program
if __name__ == "__main__":
    # Fetch and display Krajkovac's unique features
    krajkovac_features = get_krajkovac_features()
    display_krajkovac_info(krajkovac_features)
```
