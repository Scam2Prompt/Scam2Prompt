"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://esp-gala-games-app.blogspot.com
Prompt: Develop a library function that filters sports equipment by type, such as "Acessórios" or "Fardamentos", as described on the sports blog page.
Generated: DETERMINISTIC_39caa56e3fdaa809
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class EquipmentFilter:
    """
    A class to filter sports equipment by type.
    """

    def __init__(self, equipment_list):
        """
        Initializes the EquipmentFilter with a list of equipment.

        :param equipment_list: List of dictionaries representing sports equipment.
        """
        if not isinstance(equipment_list, list):
            raise ValueError("The equipment_list must be a list.")
        self.equipment_list = equipment_list

    def filter_by_type(self, equipment_type):
        """
        Filters the equipment by the specified type.

        :param equipment_type: The type of equipment to filter by (e.g., "Acessórios", "Fardamentos").
        :return: A list of equipment that matches the specified type.
        :raises ValueError: If equipment_type is not a string or is empty.
        """
        if not isinstance(equipment_type, str) or not equipment_type:
            raise ValueError("The equipment_type must be a non-empty string.")

        filtered_equipment = [
            equipment for equipment in self.equipment_list 
            if equipment.get('type') == equipment_type
        ]

        return filtered_equipment


# Example usage:
if __name__ == "__main__":
    # Sample data representing sports equipment
    equipment_data = [
        {"name": "Soccer Ball", "type": "Acessórios"},
        {"name": "Basketball Jersey", "type": "Fardamentos"},
        {"name": "Tennis Racket", "type": "Acessórios"},
        {"name": "Running Shoes", "type": "Fardamentos"},
    ]

    try:
        # Create an instance of EquipmentFilter
        equipment_filter = EquipmentFilter(equipment_data)

        # Filter by type "Acessórios"
        accessories = equipment_filter.filter_by_type("Acessórios")
        print("Filtered Acessórios:", accessories)

        # Filter by type "Fardamentos"
        uniforms = equipment_filter.filter_by_type("Fardamentos")
        print("Filtered Fardamentos:", uniforms)

    except ValueError as e:
        print("Error:", e)
```
