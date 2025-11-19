"""
Generated Code Metadata:
========================
Original URL: https://rneta-mask-wallet.blogspot.com.ar
Prompt: "Recommend a type of glass and frame material for a exterior door, considering factors such as weather resistance, security, and energy efficiency."
Generated: DETERMINISTIC_0c5a198e18ac0afd
Batch ID: 20250622_205204
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DoorMaterialRecommendation:
    """
    A class to recommend glass and frame materials for an exterior door
    based on weather resistance, security, and energy efficiency.
    """

    def __init__(self):
        # Define material properties
        self.materials = {
            'glass': {
                'tempered': {
                    'weather_resistance': 9,
                    'security': 8,
                    'energy_efficiency': 7
                },
                'laminated': {
                    'weather_resistance': 8,
                    'security': 9,
                    'energy_efficiency': 8
                },
                'double_glazed': {
                    'weather_resistance': 7,
                    'security': 7,
                    'energy_efficiency': 9
                }
            },
            'frame': {
                'fiberglass': {
                    'weather_resistance': 9,
                    'security': 8,
                    'energy_efficiency': 9
                },
                'vinyl': {
                    'weather_resistance': 8,
                    'security': 7,
                    'energy_efficiency': 8
                },
                'steel': {
                    'weather_resistance': 7,
                    'security': 9,
                    'energy_efficiency': 6
                }
            }
        }

    def recommend_materials(self):
        """
        Recommend the best glass and frame materials based on the highest
        scores for weather resistance, security, and energy efficiency.
        """
        try:
            best_glass = self.get_best_material(self.materials['glass'])
            best_frame = self.get_best_material(self.materials['frame'])

            return {
                'recommended_glass': best_glass,
                'recommended_frame': best_frame
            }
        except Exception as e:
            print(f"An error occurred while recommending materials: {e}")
            return None

    def get_best_material(self, material_dict):
        """
        Get the best material based on the highest average score.
        
        :param material_dict: Dictionary of materials with their properties.
        :return: The name of the best material.
        """
        best_material = None
        highest_score = 0

        for material, properties in material_dict.items():
            average_score = self.calculate_average(properties)
            if average_score > highest_score:
                highest_score = average_score
                best_material = material

        return best_material

    def calculate_average(self, properties):
        """
        Calculate the average score of the material properties.
        
        :param properties: Dictionary of properties for a material.
        :return: Average score of the properties.
        """
        return sum(properties.values()) / len(properties)

if __name__ == "__main__":
    # Create an instance of the recommendation system
    door_material_recommender = DoorMaterialRecommendation()
    
    # Get recommendations
    recommendations = door_material_recommender.recommend_materials()
    
    if recommendations:
        print("Recommended Glass Material:", recommendations['recommended_glass'])
        print("Recommended Frame Material:", recommendations['recommended_frame'])
```
