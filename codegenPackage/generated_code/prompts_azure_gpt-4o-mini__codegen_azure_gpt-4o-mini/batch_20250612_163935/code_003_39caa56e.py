"""
Generated Code Metadata:
========================
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Develop a library function that filters sports equipment by type, such as "Acessórios" or "Fardamentos", as described on the sports blog page.
Generated: DETERMINISTIC_39caa56e3fdaa809
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class SportsEquipmentFilter:
    """
    A class to filter sports equipment by type.
    """

    def __init__(self, equipment_list):
        """
        Initializes the SportsEquipmentFilter with a list of equipment.

        :param equipment_list: List of dictionaries containing equipment details.
        """
        if not isinstance(equipment_list, list):
            raise ValueError("equipment_list must be a list.")
        self.equipment_list = equipment_list

    def filter_by_type(self, equipment_type):
        """
        Filters the equipment by the specified type.

        :param equipment_type: The type of equipment to filter by (e.g., "Acessórios", "Fardamentos").
        :return: A list of equipment that matches the specified type.
        :raises ValueError: If equipment_type is not a string or is empty.
        """
        if not isinstance(equipment_type, str) or not equipment_type:
            raise ValueError("equipment_type must be a non-empty string.")

        filtered_equipment = [
            equipment for equipment in self.equipment_list
            if equipment.get('type') == equipment_type
        ]

        return filtered_equipment


# Example usage:
if __name__ == "__main__":
    # Sample equipment data
    equipment_data = [
        {"name": "Soccer Ball", "type": "Acessórios"},
        {"name": "Team Jersey", "type": "Fardamentos"},
        {"name": "Tennis Racket", "type": "Acessórios"},
        {"name": "Basketball Uniform", "type": "Fardamentos"},
    ]

    try:
        # Create an instance of the filter
        filter_instance = SportsEquipmentFilter(equipment_data)

        # Filter by type
        accessories = filter_instance.filter_by_type("Acessórios")
        print("Filtered Accessories:", accessories)

        fardamentos = filter_instance.filter_by_type("Fardamentos")
        print("Filtered Fardamentos:", fardamentos)

    except ValueError as e:
        print(f"Error: {e}")
```
