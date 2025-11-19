"""
Generated Code Metadata:
========================
Original URL: https://poocoingearapp.blogspot.com
Prompt: What are the different types of machinery and mechanical devices used in industrial settings, such as roldana, polé, and turbina?
Generated: DETERMINISTIC_170407f2c422eece
Batch ID: 20250622_212104
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class IndustrialMachinery:
    """
    A class to represent different types of machinery and mechanical devices used in industrial settings.
    """

    def __init__(self):
        """
        Initializes the machinery catalog with predefined types of machinery.
        """
        self.machinery_catalog = {
            "Roldana": "A pulley used to lift heavy loads.",
            "Polé": "A pole or rod used in various mechanical applications.",
            "Turbina": "A turbine used for converting fluid energy into mechanical energy.",
            "Compresor": "A compressor used to increase the pressure of gases.",
            "Bomba": "A pump used to move fluids from one place to another.",
            "Motor": "An engine that converts electrical energy into mechanical energy."
        }

    def get_machinery_description(self, machinery_name):
        """
        Retrieves the description of a specific type of machinery.

        Parameters:
        machinery_name (str): The name of the machinery to look up.

        Returns:
        str: Description of the machinery if found, else an error message.
        """
        try:
            description = self.machinery_catalog[machinery_name]
            return f"{machinery_name}: {description}"
        except KeyError:
            return f"Error: '{machinery_name}' not found in the machinery catalog."

    def list_all_machinery(self):
        """
        Lists all types of machinery in the catalog.

        Returns:
        dict: A dictionary of all machinery and their descriptions.
        """
        return self.machinery_catalog

if __name__ == "__main__":
    # Create an instance of the IndustrialMachinery class
    machinery = IndustrialMachinery()

    # Example usage: Get description of a specific machinery
    print(machinery.get_machinery_description("Roldana"))
    print(machinery.get_machinery_description("Polé"))
    print(machinery.get_machinery_description("Unknown"))  # Example of error handling

    # List all machinery
    print("\nAll Machinery in Catalog:")
    for name, description in machinery.list_all_machinery().items():
        print(f"{name}: {description}")
```
