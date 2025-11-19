"""
Generated Code Metadata:
========================
Original URL: https://cartoansurperu.com
Prompt: Compare the benefits and features of Cartonerías Andinas del Sur's stretch film products, including their different sizes (9, 18, and 20 inches) and applications.
Generated: DETERMINISTIC_be4c7ab2e8ca29b3
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class StretchFilmProduct:
    """
    Represents a stretch film product with its features and benefits.
    """
    
    def __init__(self, width_inches, thickness_microns, core_diameter_inches, 
                 roll_length_feet, max_stretch_percent, applications):
        """
        Initialize a stretch film product with its specifications.
        
        Args:
            width_inches (float): Width of the film in inches
            thickness_microns (float): Film thickness in microns
            core_diameter_inches (float): Core diameter in inches
            roll_length_feet (float): Roll length in feet
            max_stretch_percent (int): Maximum stretch percentage
            applications (list[str]): List of common applications
        """
        self.width_inches = width_inches
        self.thickness_microns = thickness_microns
        self.core_diameter_inches = core_diameter_inches
        self.roll_length_feet = roll_length_feet
        self.max_stretch_percent = max_stretch_percent
        self.applications = applications
    
    def get_features(self):
        """
        Returns a dictionary of all product features.
        """
        return {
            'width_inches': self.width_inches,
            'thickness_microns': self.thickness_microns,
            'core_diameter_inches': self.core_diameter_inches,
            'roll_length_feet': self.roll_length_feet,
            'max_stretch_percent': self.max_stretch_percent
        }
    
    def get_benefits(self):
        """
        Returns a list of benefits based on product specifications.
        """
        benefits = []
        
        if self.width_inches >= 18:
            benefits.append("Ideal for wrapping large pallets")
        else:
            benefits.append("Perfect for smaller loads and hand wrapping")
            
        if self.thickness_microns >= 20:
            benefits.append("High puncture resistance")
        else:
            benefits.append("Excellent clarity and cost efficiency")
            
        benefits.append(f"Up to {self.max_stretch_percent}% stretch for maximum efficiency")
        benefits.append("Protects products from dust and moisture")
        
        return benefits
    
    def __str__(self):
        return f"{self.width_inches}\" Stretch Film"


class StretchFilmComparison:
    """
    Compares different stretch film products from Cartonerías Andinas del Sur.
    """
    
    def __init__(self):
        self.products = {
            '9_inch': StretchFilmProduct(
                width_inches=9,
                thickness_microns=17,
                core_diameter_inches=3,
                roll_length_feet=2000,
                max_stretch_percent=250,
                applications=["small packages", "hand wrapping", "light loads"]
            ),
            '18_inch': StretchFilmProduct(
                width_inches=18,
                thickness_microns=20,
                core_diameter_inches=3,
                roll_length_feet=5000,
                max_stretch_percent=300,
                applications=["standard pallets", "machine wrapping", "medium loads"]
            ),
            '20_inch': StretchFilmProduct(
                width_inches=20,
                thickness_microns=23,
                core_diameter_inches=3,
                roll_length_feet=5000,
                max_stretch_percent=300,
                applications=["large pallets", "heavy loads", "industrial wrapping"]
            )
        }
    
    def compare_features(self):
        """
        Returns a comparison table of all product features.
        """
        comparison = []
        
        for name, product in self.products.items():
            features = product.get_features()
            features['name'] = name.replace('_', ' ')
            features['applications'] = ', '.join(product.applications)
            features['benefits'] = ', '.join(product.get_benefits())
            comparison.append(features)
            
        return comparison
    
    def get_recommendation(self, load_size, wrapping_method, load_weight):
        """
        Recommends the best stretch film based on usage requirements.
        
        Args:
            load_size (str): 'small', 'medium', or 'large'
            wrapping_method (str): 'hand' or 'machine'
            load_weight (str): 'light', 'medium', or 'heavy'
            
        Returns:
            StretchFilmProduct: Recommended product
        """
        if wrapping_method == 'hand':
            return self.products['9_inch']
        
        if load_size == 'small' or load_weight == 'light':
            return self.products['9_inch']
        elif load_size == 'medium' or load_weight == 'medium':
            return self.products['18_inch']
        else:
            return self.products['20_inch']


def main():
    """Main function to demonstrate the comparison."""
    comparison = StretchFilmComparison()
    
    print("Product Features Comparison:")
    for product in comparison.compare_features():
        print(f"\n{product['name'].title()} Film:")
        print(f"Width: {product['width_inches']}\"")
        print(f"Thickness: {product['thickness_microns']} microns")
        print(f"Core Diameter: {product['core_diameter_inches']}\"")
        print(f"Roll Length: {product['roll_length_feet']} ft")
        print(f"Max Stretch: {product['max_stretch_percent']}%")
        print(f"Applications: {product['applications']}")
        print(f"Key Benefits: {product['benefits']}")
    
    print("\nRecommendation for large load with machine wrapping:")
    recommended = comparison.get_recommendation('large', 'machine', 'heavy')
    print(f"Recommended product: {recommended}")


if __name__ == "__main__":
    main()
```
