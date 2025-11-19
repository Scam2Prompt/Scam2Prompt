"""
Generated Code Metadata:
========================
Original URL: https://libointeriors.net
Prompt: "Create a specification sheet for a gypsum board partition system for an IT building."
Generated: DETERMINISTIC_4d4df78cfe4a09df
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Gypsum Board Partition System Specification Sheet Generator

class GypsumBoardPartitionSystem:
    def __init__(self, 
                 partition_height: float, 
                 partition_length: float, 
                 stud_type: str, 
                 stud_spacing: float, 
                 gypsum_board_thickness: float, 
                 gypsum_board_type: str):
        """
        Initialize a Gypsum Board Partition System.

        Args:
        - partition_height (float): The height of the partition in meters.
        - partition_length (float): The length of the partition in meters.
        - stud_type (str): The type of stud (e.g., steel, wood).
        - stud_spacing (float): The spacing between studs in meters.
        - gypsum_board_thickness (float): The thickness of the gypsum board in meters.
        - gypsum_board_type (str): The type of gypsum board (e.g., regular, fire-resistant).
        """

        self.partition_height = partition_height
        self.partition_length = partition_length
        self.stud_type = stud_type
        self.stud_spacing = stud_spacing
        self.gypsum_board_thickness = gypsum_board_thickness
        self.gypsum_board_type = gypsum_board_type

    def calculate_stud_quantity(self) -> int:
        """
        Calculate the quantity of studs required.

        Returns:
        - int: The quantity of studs required.
        """
        try:
            stud_quantity = int(self.partition_length / self.stud_spacing) + 1
            return stud_quantity
        except ZeroDivisionError:
            print("Error: Stud spacing cannot be zero.")
            return None

    def generate_specification_sheet(self) -> dict:
        """
        Generate a specification sheet for the gypsum board partition system.

        Returns:
        - dict: A dictionary containing the specification sheet details.
        """
        specification_sheet = {
            "Partition Height": f"{self.partition_height} meters",
            "Partition Length": f"{self.partition_length} meters",
            "Stud Type": self.stud_type,
            "Stud Spacing": f"{self.stud_spacing} meters",
            "Gypsum Board Thickness": f"{self.gypsum_board_thickness} meters",
            "Gypsum Board Type": self.gypsum_board_type,
            "Stud Quantity": self.calculate_stud_quantity()
        }
        return specification_sheet


def main():
    try:
        partition_system = GypsumBoardPartitionSystem(
            partition_height=3.5, 
            partition_length=10.0, 
            stud_type="steel", 
            stud_spacing=0.6, 
            gypsum_board_thickness=0.0125, 
            gypsum_board_type="fire-resistant"
        )

        specification_sheet = partition_system.generate_specification_sheet()
        for key, value in specification_sheet.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
