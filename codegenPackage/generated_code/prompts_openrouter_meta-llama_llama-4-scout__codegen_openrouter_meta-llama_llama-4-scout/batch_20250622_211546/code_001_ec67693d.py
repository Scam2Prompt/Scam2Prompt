"""
Generated Code Metadata:
========================
Original URL: https://dbxtools.in
Prompt: Compare the features of the 900 Series and 1200 Series heat exchanger tube expanders, highlighting their differences and applications.
Generated: DETERMINISTIC_ec67693dd9eea6e7
Batch ID: 20250622_211546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# heat_exchanger_tube_expanders.py

class HeatExchangerTubeExpander:
    def __init__(self, series, model, max_expansion_diameter, expansion_speed, 
                 tube_materials, application_areas):
        """
        Initialize a HeatExchangerTubeExpander object.

        Args:
            series (str): The series of the tube expander (e.g., 900, 1200).
            model (str): The model of the tube expander.
            max_expansion_diameter (float): The maximum expansion diameter of the tube expander.
            expansion_speed (float): The expansion speed of the tube expander.
            tube_materials (list): A list of tube materials that the expander supports.
            application_areas (list): A list of application areas for the tube expander.
        """
        self.series = series
        self.model = model
        self.max_expansion_diameter = max_expansion_diameter
        self.expansion_speed = expansion_speed
        self.tube_materials = tube_materials
        self.application_areas = application_areas

    def __str__(self):
        return f"{self.series} Series Tube Expander - {self.model}"

    def get_features(self):
        """
        Get the features of the tube expander.

        Returns:
            dict: A dictionary containing the features of the tube expander.
        """
        return {
            "Series": self.series,
            "Model": self.model,
            "Max Expansion Diameter": self.max_expansion_diameter,
            "Expansion Speed": self.expansion_speed,
            "Tube Materials": self.tube_materials,
            "Application Areas": self.application_areas
        }


class TubeExpanderComparator:
    def __init__(self, expander1, expander2):
        """
        Initialize a TubeExpanderComparator object.

        Args:
            expander1 (HeatExchangerTubeExpander): The first tube expander to compare.
            expander2 (HeatExchangerTubeExpander): The second tube expander to compare.
        """
        self.expander1 = expander1
        self.expander2 = expander2

    def compare_features(self):
        """
        Compare the features of the two tube expanders.

        Returns:
            dict: A dictionary highlighting the differences and similarities between the two tube expanders.
        """
        features1 = self.expander1.get_features()
        features2 = self.expander2.get_features()

        comparison_result = {}

        for feature, value1 in features1.items():
            value2 = features2.get(feature)

            if value1 != value2:
                comparison_result[feature] = {
                    "Expander 1": value1,
                    "Expander 2": value2
                }
            else:
                comparison_result[feature] = {
                    "Both": value1
                }

        return comparison_result


def main():
    try:
        # Define the features of the 900 Series and 1200 Series heat exchanger tube expanders
        expander900 = HeatExchangerTubeExpander(
            series="900",
            model="TE-900",
            max_expansion_diameter=1.5,
            expansion_speed=10,
            tube_materials=["Copper", "Stainless Steel"],
            application_areas=["Power Generation", "Chemical Processing"]
        )

        expander1200 = HeatExchangerTubeExpander(
            series="1200",
            model="TE-1200",
            max_expansion_diameter=2.0,
            expansion_speed=15,
            tube_materials=["Copper", "Titanium", "Stainless Steel"],
            application_areas=["Power Generation", "Oil and Gas", "Chemical Processing"]
        )

        # Compare the features of the two tube expanders
        comparator = TubeExpanderComparator(expander900, expander1200)
        comparison_result = comparator.compare_features()

        # Print the comparison result
        print("Comparison of 900 Series and 1200 Series Heat Exchanger Tube Expanders:")
        for feature, values in comparison_result.items():
            print(f"\n{feature}:")
            if "Both" in values:
                print(f"  - Both: {values['Both']}")
            else:
                print(f"  - {expander900.series} Series: {values['Expander 1']}")
                print(f"  - {expander1200.series} Series: {values['Expander 2']}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
