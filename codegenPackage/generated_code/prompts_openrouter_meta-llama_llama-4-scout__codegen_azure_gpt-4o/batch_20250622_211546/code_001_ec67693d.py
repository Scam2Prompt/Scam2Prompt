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
# Import necessary libraries
import json

# Define a class to represent a heat exchanger tube expander
class TubeExpander:
    def __init__(self, series, features, applications):
        """
        Initialize a TubeExpander object.

        :param series: The series name (e.g., "900 Series", "1200 Series")
        :param features: A list of features for the series
        :param applications: A list of applications for the series
        """
        self.series = series
        self.features = features
        self.applications = applications

    def compare(self, other):
        """
        Compare the features and applications of this TubeExpander with another.

        :param other: Another TubeExpander object to compare against
        :return: A dictionary containing the differences in features and applications
        """
        if not isinstance(other, TubeExpander):
            raise TypeError("Comparison must be made with another TubeExpander object.")

        # Compare features
        unique_features_self = set(self.features) - set(other.features)
        unique_features_other = set(other.features) - set(self.features)

        # Compare applications
        unique_applications_self = set(self.applications) - set(other.applications)
        unique_applications_other = set(other.applications) - set(self.applications)

        return {
            "series_comparison": f"{self.series} vs {other.series}",
            "unique_features": {
                self.series: list(unique_features_self),
                other.series: list(unique_features_other),
            },
            "unique_applications": {
                self.series: list(unique_applications_self),
                other.series: list(unique_applications_other),
            },
        }

# Create instances for the 900 Series and 1200 Series
series_900 = TubeExpander(
    series="900 Series",
    features=["Compact design", "High durability", "Cost-effective"],
    applications=["Small-scale heat exchangers", "Low-pressure systems"]
)

series_1200 = TubeExpander(
    series="1200 Series",
    features=["Advanced technology", "High precision", "Suitable for large tubes"],
    applications=["Large-scale heat exchangers", "High-pressure systems"]
)

# Compare the two series
comparison_result = series_900.compare(series_1200)

# Output the comparison result in a readable format
def display_comparison(result):
    """
    Display the comparison result in a readable format.

    :param result: The comparison result dictionary
    """
    print("Comparison of Heat Exchanger Tube Expanders:")
    print(f"Series: {result['series_comparison']}")
    print("\nUnique Features:")
    for series, features in result["unique_features"].items():
        print(f"  {series}: {', '.join(features) if features else 'None'}")
    print("\nUnique Applications:")
    for series, applications in result["unique_applications"].items():
        print(f"  {series}: {', '.join(applications) if applications else 'None'}")

# Display the comparison result
display_comparison(comparison_result)
```
