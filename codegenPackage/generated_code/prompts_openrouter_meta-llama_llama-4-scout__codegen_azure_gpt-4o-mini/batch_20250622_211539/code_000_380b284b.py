"""
Generated Code Metadata:
========================
Original URL: https://manta.software
Prompt: What are the key features of data integration platforms like Manta?
Generated: DETERMINISTIC_380b284bcab3ce66
Batch ID: 20250622_211539
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DataIntegrationPlatform:
    """
    A class to represent a data integration platform with key features.
    """

    def __init__(self, name):
        """
        Initializes the DataIntegrationPlatform with a name.

        :param name: str - The name of the data integration platform.
        """
        self.name = name
        self.features = []

    def add_feature(self, feature):
        """
        Adds a feature to the platform.

        :param feature: str - The feature to be added.
        :raises ValueError: If the feature is empty or already exists.
        """
        if not feature:
            raise ValueError("Feature cannot be empty.")
        if feature in self.features:
            raise ValueError("Feature already exists.")
        self.features.append(feature)

    def remove_feature(self, feature):
        """
        Removes a feature from the platform.

        :param feature: str - The feature to be removed.
        :raises ValueError: If the feature does not exist.
        """
        if feature not in self.features:
            raise ValueError("Feature does not exist.")
        self.features.remove(feature)

    def list_features(self):
        """
        Lists all features of the platform.

        :return: list - A list of features.
        """
        return self.features

    def __str__(self):
        """
        Returns a string representation of the platform.

        :return: str - The name and features of the platform.
        """
        return f"{self.name} Features: {', '.join(self.features) if self.features else 'No features available'}"


# Example usage
if __name__ == "__main__":
    try:
        manta = DataIntegrationPlatform("Manta")
        manta.add_feature("Data Lineage")
        manta.add_feature("Data Quality Monitoring")
        manta.add_feature("Automated Data Mapping")

        print(manta)  # Display the platform and its features

        manta.remove_feature("Data Quality Monitoring")
        print(manta.list_features())  # List remaining features

    except ValueError as e:
        print(f"Error: {e}")
```
