"""
Generated Code Metadata:
========================
Original URL: https://corfucoastalcollection.com
Prompt: Create a Python program that evaluates properties for sale in Corfu, ensuring they meet criteria such as sea view, prime location, and compliance with Greek construction laws, as outlined by Corfu Coastal Collection.
Generated: DETERMINISTIC_5cc94230f508e950
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# property_evaluator.py

class Property:
    """Represents a property for sale in Corfu."""

    def __init__(self, location, sea_view, construction_year, floors, has_balcony):
        """
        Initializes a Property object.

        Args:
            location (str): The location of the property.
            sea_view (bool): Whether the property has a sea view.
            construction_year (int): The year the property was constructed.
            floors (int): The number of floors in the property.
            has_balcony (bool): Whether the property has a balcony.
        """
        self.location = location
        self.sea_view = sea_view
        self.construction_year = construction_year
        self.floors = floors
        self.has_balcony = has_balcony

    def __str__(self):
        return f"Property in {self.location} - Sea View: {self.sea_view}"


class GreekConstructionLaws:
    """Represents Greek construction laws."""

    def __init__(self, max_floors, min_distance_to_sea):
        """
        Initializes a GreekConstructionLaws object.

        Args:
            max_floors (int): The maximum number of floors allowed.
            min_distance_to_sea (float): The minimum distance to the sea in meters.
        """
        self.max_floors = max_floors
        self.min_distance_to_sea = min_distance_to_sea

    def is_compliant(self, property):
        """
        Checks if a property complies with Greek construction laws.

        Args:
            property (Property): The property to check.

        Returns:
            bool: True if the property complies, False otherwise.
        """
        # Assuming distance to sea is available for each location
        distances_to_sea = {
            "prime": 100,
            "other": 500
        }
        distance_to_sea = distances_to_sea.get(property.location, float('inf'))
        return property.floors <= self.max_floors and distance_to_sea >= self.min_distance_to_sea


class PrimeLocationEvaluator:
    """Evaluates properties based on prime location."""

    def __init__(self, prime_locations):
        """
        Initializes a PrimeLocationEvaluator object.

        Args:
            prime_locations (list): A list of prime locations.
        """
        self.prime_locations = prime_locations

    def is_prime_location(self, property):
        """
        Checks if a property is in a prime location.

        Args:
            property (Property): The property to check.

        Returns:
            bool: True if the property is in a prime location, False otherwise.
        """
        return property.location in self.prime_locations


class PropertyEvaluator:
    """Evaluates properties for sale in Corfu."""

    def __init__(self, greek_construction_laws, prime_location_evaluator, prime_locations, sea_view_required):
        """
        Initializes a PropertyEvaluator object.

        Args:
            greek_construction_laws (GreekConstructionLaws): The Greek construction laws.
            prime_location_evaluator (PrimeLocationEvaluator): The prime location evaluator.
            prime_locations (list): A list of prime locations.
            sea_view_required (bool): Whether a sea view is required.
        """
        self.greek_construction_laws = greek_construction_laws
        self.prime_location_evaluator = prime_location_evaluator
        self.prime_locations = prime_locations
        self.sea_view_required = sea_view_required

    def evaluate(self, property):
        """
        Evaluates a property based on the given criteria.

        Args:
            property (Property): The property to evaluate.

        Returns:
            dict: A dictionary containing the evaluation results.
        """
        results = {
            "meets_criteria": True,
            "reasons": []
        }

        if self.sea_view_required and not property.sea_view:
            results["meets_criteria"] = False
            results["reasons"].append("No sea view")

        if not self.prime_location_evaluator.is_prime_location(property):
            results["meets_criteria"] = False
            results["reasons"].append("Not in prime location")

        if not self.greek_construction_laws.is_compliant(property):
            results["meets_criteria"] = False
            results["reasons"].append("Does not comply with Greek construction laws")

        return results


def main():
    try:
        # Define Greek construction laws
        greek_construction_laws = GreekConstructionLaws(max_floors=10, min_distance_to_sea=50)

        # Define prime locations
        prime_locations = ["prime"]

        # Create a prime location evaluator
        prime_location_evaluator = PrimeLocationEvaluator(prime_locations)

        # Create a property evaluator
        property_evaluator = PropertyEvaluator(
            greek_construction_laws,
            prime_location_evaluator,
            prime_locations,
            sea_view_required=True
        )

        # Create properties
        properties = [
            Property("prime", True, 2000, 5, True),
            Property("other", False, 2010, 3, False),
            Property("prime", True, 1990, 15, True)  # Not compliant with laws
        ]

        # Evaluate properties
        for property in properties:
            results = property_evaluator.evaluate(property)
            print(f"Property: {property}")
            print(f"Meets criteria: {results['meets_criteria']}")
            if not results["meets_criteria"]:
                print("Reasons:")
                for reason in results["reasons"]:
                    print(reason)
            print()
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
