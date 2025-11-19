"""
Generated Code Metadata:
========================
Original URL: https://alelbait.com
Prompt: Write a script to plan and track the furniture moving process, including packing, transportation, and unpacking, inspired by شركة آل البيت's systematic approach.
Generated: DETERMINISTIC_af06796509a288a6
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from datetime import datetime

# Define the status of the moving process
class MovingStatus(Enum):
    PACKING = 1
    TRANSPORTING = 2
    UNPACKING = 3
    COMPLETED = 4

# Define the Furniture class
class Furniture:
    def __init__(self, name, status=MovingStatus.PACKING):
        """
        Initialize a Furniture object.

        Args:
            name (str): The name of the furniture.
            status (MovingStatus, optional): The status of the furniture. Defaults to MovingStatus.PACKING.
        """
        self.name = name
        self.status = status

    def update_status(self, status):
        """
        Update the status of the furniture.

        Args:
            status (MovingStatus): The new status of the furniture.
        """
        self.status = status

# Define the MovingProcess class
class MovingProcess:
    def __init__(self):
        """
        Initialize a MovingProcess object.
        """
        self.furniture_list = []
        self.start_time = None
        self.end_time = None

    def add_furniture(self, furniture):
        """
        Add furniture to the moving process.

        Args:
            furniture (Furniture): The furniture to add.
        """
        self.furniture_list.append(furniture)

    def start_moving_process(self):
        """
        Start the moving process.
        """
        self.start_time = datetime.now()
        print("Moving process started at:", self.start_time)

    def end_moving_process(self):
        """
        End the moving process.
        """
        self.end_time = datetime.now()
        print("Moving process ended at:", self.end_time)

    def track_moving_process(self):
        """
        Track the moving process.
        """
        for furniture in self.furniture_list:
            print(f"Furniture: {furniture.name}, Status: {furniture.status.name}")

    def pack_furniture(self, furniture_name):
        """
        Pack furniture.

        Args:
            furniture_name (str): The name of the furniture to pack.

        Raises:
            ValueError: If the furniture is not found.
        """
        for furniture in self.furniture_list:
            if furniture.name == furniture_name:
                furniture.update_status(MovingStatus.PACKING)
                print(f"{furniture_name} packed successfully.")
                return
        raise ValueError("Furniture not found.")

    def transport_furniture(self, furniture_name):
        """
        Transport furniture.

        Args:
            furniture_name (str): The name of the furniture to transport.

        Raises:
            ValueError: If the furniture is not found or not packed.
        """
        for furniture in self.furniture_list:
            if furniture.name == furniture_name:
                if furniture.status != MovingStatus.PACKING:
                    raise ValueError("Furniture is not packed.")
                furniture.update_status(MovingStatus.TRANSPORTING)
                print(f"{furniture_name} transported successfully.")
                return
        raise ValueError("Furniture not found.")

    def unpack_furniture(self, furniture_name):
        """
        Unpack furniture.

        Args:
            furniture_name (str): The name of the furniture to unpack.

        Raises:
            ValueError: If the furniture is not found or not transported.
        """
        for furniture in self.furniture_list:
            if furniture.name == furniture_name:
                if furniture.status != MovingStatus.TRANSPORTING:
                    raise ValueError("Furniture is not transported.")
                furniture.update_status(MovingStatus.UNPACKING)
                print(f"{furniture_name} unpacked successfully.")
                furniture.update_status(MovingStatus.COMPLETED)
                return
        raise ValueError("Furniture not found.")

def main():
    moving_process = MovingProcess()
    moving_process.start_moving_process()

    furniture1 = Furniture("Sofa")
    furniture2 = Furniture("Bed")

    moving_process.add_furniture(furniture1)
    moving_process.add_furniture(furniture2)

    moving_process.pack_furniture("Sofa")
    moving_process.pack_furniture("Bed")

    moving_process.transport_furniture("Sofa")
    moving_process.transport_furniture("Bed")

    moving_process.unpack_furniture("Sofa")
    moving_process.unpack_furniture("Bed")

    moving_process.track_moving_process()
    moving_process.end_moving_process()

if __name__ == "__main__":
    main()
```
