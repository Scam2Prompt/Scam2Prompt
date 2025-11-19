"""
Generated Code Metadata:
========================
Original URL: https://neumayaa.com.ar
Prompt: "Compare the features and benefits of different tire brands for construction equipment, such as Camso and others."
Generated: DETERMINISTIC_a553b3b394023311
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tire_comparator.py

class TireBrand:
    """Represents a tire brand with its features and benefits."""

    def __init__(self, name, description, features, benefits):
        """
        Initializes a TireBrand object.

        Args:
            name (str): The name of the tire brand.
            description (str): A brief description of the tire brand.
            features (list): A list of features of the tire brand.
            benefits (list): A list of benefits of the tire brand.
        """
        self.name = name
        self.description = description
        self.features = features
        self.benefits = benefits

    def __str__(self):
        return f"{self.name}: {self.description}"

    def get_features(self):
        return self.features

    def get_benefits(self):
        return self.benefits


class TireComparator:
    """Compares the features and benefits of different tire brands."""

    def __init__(self):
        self.tire_brands = {}

    def add_tire_brand(self, tire_brand):
        """
        Adds a tire brand to the comparator.

        Args:
            tire_brand (TireBrand): The tire brand to add.
        """
        self.tire_brands[tire_brand.name] = tire_brand

    def compare_features(self):
        """Compares the features of different tire brands."""
        features_comparison = {}
        for brand, tire_brand in self.tire_brands.items():
            features_comparison[brand] = tire_brand.get_features()
        return features_comparison

    def compare_benefits(self):
        """Compares the benefits of different tire brands."""
        benefits_comparison = {}
        for brand, tire_brand in self.tire_brands.items():
            benefits_comparison[brand] = tire_brand.get_benefits()
        return benefits_comparison

    def print_comparison(self):
        """Prints a comparison of the features and benefits of different tire brands."""
        print("Tire Brands Comparison:")
        for brand, tire_brand in self.tire_brands.items():
            print(tire_brand)
            print(f"Features: {', '.join(tire_brand.get_features())}")
            print(f"Benefits: {', '.join(tire_brand.get_benefits())}")
            print()


def main():
    try:
        comparator = TireComparator()

        # Add tire brands
        camso = TireBrand(
            "Camso",
            "A leading manufacturer of tires for construction equipment.",
            ["Durable", "Long-lasting", "High-traction"],
            ["Improved productivity", "Increased safety", "Reduced maintenance costs"]
        )
        comparator.add_tire_brand(camso)

        goodyear = TireBrand(
            "Goodyear",
            "A well-known manufacturer of tires for various industries.",
            ["High-quality", "Fuel-efficient", "Versatile"],
            ["Enhanced fuel efficiency", "Improved vehicle performance", "Increased durability"]
        )
        comparator.add_tire_brand(goodyear)

        michelin = TireBrand(
            "Michelin",
            "A renowned manufacturer of tires for construction and other industries.",
            ["Innovative", "Sustainable", "High-performance"],
            ["Improved sustainability", "Increased productivity", "Enhanced safety"]
        )
        comparator.add_tire_brand(michelin)

        # Compare and print tire brands
        comparator.print_comparison()

        # Compare features and benefits
        features_comparison = comparator.compare_features()
        benefits_comparison = comparator.compare_benefits()

        print("Features Comparison:")
        for brand, features in features_comparison.items():
            print(f"{brand}: {', '.join(features)}")

        print("\nBenefits Comparison:")
        for brand, benefits in benefits_comparison.items():
            print(f"{brand}: {', '.join(benefits)}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
