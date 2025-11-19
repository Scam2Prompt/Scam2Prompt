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
# data_integration_platform.py

class DataIntegrationPlatform:
    """
    A class representing a data integration platform.

    Attributes:
    -----------
    name (str): The name of the platform.
    features (list): A list of key features of the platform.

    Methods:
    --------
    add_feature(feature): Adds a new feature to the platform.
    remove_feature(feature): Removes a feature from the platform.
    get_features(): Returns a list of key features of the platform.
    """

    def __init__(self, name):
        """
        Initializes a DataIntegrationPlatform object.

        Args:
        -----
        name (str): The name of the platform.

        Raises:
        ------
        TypeError: If the name is not a string.
        ValueError: If the name is empty.
        """
        if not isinstance(name, str):
            raise TypeError("Name must be a string.")
        if not name.strip():
            raise ValueError("Name cannot be empty.")

        self.name = name
        self.features = []

    def add_feature(self, feature):
        """
        Adds a new feature to the platform.

        Args:
        -----
        feature (str): The feature to add.

        Raises:
        ------
        TypeError: If the feature is not a string.
        ValueError: If the feature is empty.
        """
        if not isinstance(feature, str):
            raise TypeError("Feature must be a string.")
        if not feature.strip():
            raise ValueError("Feature cannot be empty.")

        self.features.append(feature)

    def remove_feature(self, feature):
        """
        Removes a feature from the platform.

        Args:
        -----
        feature (str): The feature to remove.

        Raises:
        ------
        ValueError: If the feature is not found.
        """
        if feature not in self.features:
            raise ValueError("Feature not found.")

        self.features.remove(feature)

    def get_features(self):
        """
        Returns a list of key features of the platform.

        Returns:
        -------
        list: A list of key features.
        """
        return self.features.copy()


class Manta(DataIntegrationPlatform):
    """
    A class representing Manta, a data integration platform.

    Attributes:
    -----------
    name (str): The name of the platform.
    features (list): A list of key features of the platform.
    """

    def __init__(self):
        """
        Initializes a Manta object.
        """
        super().__init__("Manta")

        # Initialize Manta's key features
        self.add_feature("Data Integration")
        self.add_feature("Data Quality")
        self.add_feature("Data Governance")
        self.add_feature("Metadata Management")


def main():
    try:
        # Create a Manta object
        manta = Manta()

        # Get Manta's key features
        features = manta.get_features()

        # Print Manta's key features
        print(f"Key features of {manta.name}:")
        for feature in features:
            print(f"- {feature}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
