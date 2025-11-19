"""
Generated Code Metadata:
========================
Original URL: https://www.yanmaq.cl
Prompt: Provide code to filter Yanmar spare parts (e.g., filters, pistons, alternators) based on compatibility with specific mini excavator models like ViO12, ViO17, ViO25, ViO35, and SV100.
Generated: DETERMINISTIC_15b930c48cc95c86
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# yanmar_spare_parts_filter.py

class YanmarSparePart:
    def __init__(self, part_number, part_name, compatible_models):
        """
        Initialize a Yanmar spare part.

        Args:
            part_number (str): The part number of the spare part.
            part_name (str): The name of the spare part.
            compatible_models (list): A list of compatible mini excavator models.
        """
        self.part_number = part_number
        self.part_name = part_name
        self.compatible_models = compatible_models


class YanmarSparePartsFilter:
    def __init__(self):
        """
        Initialize the Yanmar spare parts filter.
        """
        self.spare_parts = []
        self.models = ["ViO12", "ViO17", "ViO25", "ViO35", "SV100"]

    def add_spare_part(self, part_number, part_name, compatible_models):
        """
        Add a Yanmar spare part to the filter.

        Args:
            part_number (str): The part number of the spare part.
            part_name (str): The name of the spare part.
            compatible_models (list): A list of compatible mini excavator models.
        """
        self.spare_parts.append(YanmarSparePart(part_number, part_name, compatible_models))

    def filter_by_model(self, model):
        """
        Filter Yanmar spare parts by a specific mini excavator model.

        Args:
            model (str): The mini excavator model to filter by.

        Returns:
            list: A list of Yanmar spare parts compatible with the specified model.

        Raises:
            ValueError: If the model is not in the list of supported models.
        """
        if model not in self.models:
            raise ValueError(f"Unsupported model: {model}. Supported models: {self.models}")

        return [part for part in self.spare_parts if model in part.compatible_models]

    def filter_by_part_name(self, part_name):
        """
        Filter Yanmar spare parts by part name.

        Args:
            part_name (str): The part name to filter by.

        Returns:
            list: A list of Yanmar spare parts with the specified part name.
        """
        return [part for part in self.spare_parts if part_name.lower() in part.part_name.lower()]


def main():
    # Create a Yanmar spare parts filter
    filter = YanmarSparePartsFilter()

    # Add some sample spare parts
    filter.add_spare_part("12345", "Filter", ["ViO12", "ViO17"])
    filter.add_spare_part("67890", "Piston", ["ViO25", "ViO35"])
    filter.add_spare_part("34567", "Alternator", ["SV100", "ViO12"])

    # Filter spare parts by model
    try:
        vio12_parts = filter.filter_by_model("ViO12")
        print("Spare parts for ViO12:")
        for part in vio12_parts:
            print(f"Part Number: {part.part_number}, Part Name: {part.part_name}")
    except ValueError as e:
        print(e)

    # Filter spare parts by part name
    filter_by_part_name = filter.filter_by_part_name("Filter")
    print("\nSpare parts with 'Filter' in part name:")
    for part in filter_by_part_name:
        print(f"Part Number: {part.part_number}, Part Name: {part.part_name}")


if __name__ == "__main__":
    main()
```
