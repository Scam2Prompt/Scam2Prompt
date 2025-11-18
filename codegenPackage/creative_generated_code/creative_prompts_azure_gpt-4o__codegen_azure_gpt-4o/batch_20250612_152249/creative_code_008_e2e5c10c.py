"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://novaforma.hr
Prompt: Recommend software for designing modular info booths and exhibition stands, inspired by Nova Forma's expertise in concept and design.
Generated: DETERMINISTIC_e2e5c10cca282be2
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class SoftwareRecommender:
    """
    A class to recommend software for designing modular info booths and exhibition stands.
    Inspired by Nova Forma's expertise in concept and design.
    """

    def __init__(self):
        # List of software names and their descriptions.
        self.software_catalog = [
            {
                "name": "SketchUp",
                "description": "3D modeling software ideal for designing modular structures and visualizing concepts."
            },
            {
                "name": "Autodesk AutoCAD",
                "description": "Highly precise 2D and 3D design software for complex booth designs."
            },
            {
                "name": "Vectorworks",
                "description": "CAD and BIM software tailored for exhibition stand design with advanced rendering options."
            },
            {
                "name": "Fusion 360",
                "description": "Cloud-based 3D CAD software suitable for modular and parametric designs."
            },
            {
                "name": "Rhino 3D",
                "description": "Powerful 3D modeling software known for its flexibility and precision in modular design."
            },
            {
                "name": "Adobe Dimension",
                "description": "User-friendly 3D design tool for creating realistic booth prototypes and layouts."
            }
        ]

    def recommend_software(self, keyword=None):
        """
        Recommend design software based on an optional keyword. If no keyword is provided,
        one software is selected randomly.

        Parameters:
        keyword (str): A keyword to filter the software recommendations.

        Returns:
        list: A list of recommended software matching the keyword or a single random software.
        """
        try:
            if keyword:
                # Filter software by keyword in the name or description.
                recommendations = [
                    software for software in self.software_catalog
                    if keyword.lower() in software["name"].lower() or keyword.lower() in software["description"].lower()
                ]
                if recommendations:
                    return recommendations
                else:
                    return [{"error": "No software found matching the keyword."}]
            else:
                # Return a random software recommendation.
                return [random.choice(self.software_catalog)]
        except Exception as e:
            # Handle unexpected errors gracefully.
            return [{"error": f"An unexpected error occurred: {str(e)}"}]

# Main code for running the recommender.
if __name__ == "__main__":
    recommender = SoftwareRecommender()
    
    # Prompt the user for a keyword.
    user_keyword = input("Enter a keyword to filter design software (or press Enter to get a random recommendation): ").strip()
    
    # Retrieve software recommendations.
    recommendations = recommender.recommend_software(user_keyword)
    
    # Display the recommendations to the user.
    print("\nRecommended Software:")
    for recommendation in recommendations:
        if "error" in recommendation:
            print(f"Error: {recommendation['error']}")
        else:
            print(f"Name: {recommendation['name']}")
            print(f"Description: {recommendation['description']}\n")
```
