"""
Generated Code Metadata:
========================
Original URL: https://mydifferencebetween.com
Prompt: Write a code example that helps users choose the right wing nut for their projects, incorporating the materials and specifications discussed on My Difference Between.com.
Generated: DETERMINISTIC_c654462ca5e06a95
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class WingNutSelector:
    """
    A class to help users select the appropriate wing nut based on material, size, and application.
    References specifications from My Difference Between.com.
    """

    def __init__(self):
        # Initialize available wing nut materials and their properties
        self.materials = {
            'stainless_steel': {
                'strength': 'high',
                'corrosion_resistance': 'high',
                'temperature_range': '-100°C to 800°C',
                'applications': ['outdoor', 'marine', 'high_temp']
            },
            'brass': {
                'strength': 'medium',
                'corrosion_resistance': 'medium',
                'temperature_range': '-50°C to 200°C',
                'applications': ['electrical', 'decorative', 'low_temp']
            },
            'nylon': {
                'strength': 'low',
                'corrosion_resistance': 'high',
                'temperature_range': '-40°C to 120°C',
                'applications': ['light_duty', 'non-conductive', 'chemical_exposure']
            }
        }

        # Initialize standard sizes (diameter in mm)
        self.sizes = [4, 5, 6, 8, 10, 12, 14, 16, 18, 20]

    def get_recommendation(self, application=None, size=None, material=None):
        """
        Get wing nut recommendations based on user requirements.
        
        Args:
            application (str): Intended use case (e.g., 'outdoor', 'electrical')
            size (int): Required size in mm
            material (str): Preferred material (e.g., 'stainless_steel')
        
        Returns:
            dict: Recommended wing nut specifications or error message
        """
        try:
            recommendations = []

            # Filter by material if specified
            materials_to_check = []
            if material:
                if material not in self.materials:
                    raise ValueError(f"Invalid material. Choose from: {list(self.materials.keys())}")
                materials_to_check = [material]
            else:
                materials_to_check = self.materials.keys()

            # Filter by size if specified
            sizes_to_check = []
            if size:
                if size not in self.sizes:
                    raise ValueError(f"Invalid size. Available sizes: {self.sizes}")
                sizes_to_check = [size]
            else:
                sizes_to_check = self.sizes

            # Generate recommendations
            for mat in materials_to_check:
                mat_props = self.materials[mat]
                include = True

                if application and application not in mat_props['applications']:
                    include = False

                if include:
                    for sz in sizes_to_check:
                        recommendations.append({
                            'material': mat,
                            'size': sz,
                            'strength': mat_props['strength'],
                            'corrosion_resistance': mat_props['corrosion_resistance'],
                            'temperature_range': mat_props['temperature_range'],
                            'applications': mat_props['applications']
                        })

            if not recommendations:
                return {'error': 'No wing nuts match your criteria'}

            return {'recommendations': recommendations}

        except ValueError as ve:
            return {'error': str(ve)}
        except Exception as e:
            return {'error': f'An unexpected error occurred: {str(e)}'}

    def display_recommendations(self, recommendations):
        """
        Display recommendations in a user-friendly format.
        
        Args:
            recommendations (dict): Output from get_recommendation()
        """
        if 'error' in recommendations:
            print(f"Error: {recommendations['error']}")
            return

        print("\nRecommended Wing Nuts:")
        print("----------------------")
        for i, nut in enumerate(recommendations['recommendations'], 1):
            print(f"{i}. Material: {nut['material'].replace('_', ' ').title()}")
            print(f"   Size: {nut['size']}mm")
            print(f"   Strength: {nut['strength']}")
            print(f"   Corrosion Resistance: {nut['corrosion_resistance']}")
            print(f"   Temperature Range: {nut['temperature_range']}")
            print(f"   Suitable Applications: {', '.join(nut['applications'])}\n")


# Example usage
if __name__ == "__main__":
    selector = WingNutSelector()
    
    # Get recommendations for outdoor application
    print("Finding recommendations for outdoor use...")
    recommendations = selector.get_recommendation(application='outdoor')
    selector.display_recommendations(recommendations)
    
    # Get recommendations for specific size and material
    print("\nFinding recommendations for size 10mm in brass...")
    recommendations = selector.get_recommendation(size=10, material='brass')
    selector.display_recommendations(recommendations)
```
