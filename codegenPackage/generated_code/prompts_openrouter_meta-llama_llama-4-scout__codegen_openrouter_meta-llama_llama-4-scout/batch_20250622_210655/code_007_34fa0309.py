"""
Generated Code Metadata:
========================
Original URL: https://www.yanmaq.cl
Prompt: Provide a list of spare parts and filters compatible with Yanmar mini excavators, including their part numbers and descriptions.
Generated: DETERMINISTIC_34fa0309d9483198
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# yanmar_excavator_parts.py

class YanmarExcavatorPart:
    """Represents a spare part or filter compatible with Yanmar mini excavators."""

    def __init__(self, part_number, description):
        """
        Initializes a YanmarExcavatorPart object.

        Args:
            part_number (str): The part number of the spare part or filter.
            description (str): A brief description of the spare part or filter.
        """
        self.part_number = part_number
        self.description = description

    def __repr__(self):
        return f"YanmarExcavatorPart(part_number='{self.part_number}', description='{self.description}')"


class YanmarExcavatorPartsRepository:
    """Provides a list of spare parts and filters compatible with Yanmar mini excavators."""

    def __init__(self):
        """
        Initializes a YanmarExcavatorPartsRepository object.

        The repository is pre-populated with a list of spare parts and filters.
        """
        self.parts = [
            YanmarExcavatorPart("110001-000001", "Air Filter"),
            YanmarExcavatorPart("110002-000002", "Oil Filter"),
            YanmarExcavatorPart("110003-000003", "Fuel Filter"),
            YanmarExcavatorPart("120001-000001", "Hydraulic Filter"),
            YanmarExcavatorPart("130001-000001", "Engine Oil Filter"),
            # Add more parts here...
        ]

    def get_parts(self):
        """
        Retrieves the list of spare parts and filters.

        Returns:
            list[YanmarExcavatorPart]: A list of YanmarExcavatorPart objects.
        """
        return self.parts

    def get_part_by_number(self, part_number):
        """
        Retrieves a spare part or filter by its part number.

        Args:
            part_number (str): The part number of the spare part or filter.

        Returns:
            YanmarExcavatorPart: A YanmarExcavatorPart object if found, otherwise None.
        """
        for part in self.parts:
            if part.part_number == part_number:
                return part
        return None


def main():
    try:
        repository = YanmarExcavatorPartsRepository()
        print("Spare Parts and Filters:")
        for part in repository.get_parts():
            print(f"Part Number: {part.part_number}, Description: {part.description}")

        part_number = input("Enter a part number to search: ")
        part = repository.get_part_by_number(part_number)
        if part:
            print(f"Part Found: Part Number: {part.part_number}, Description: {part.description}")
        else:
            print("Part not found.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
