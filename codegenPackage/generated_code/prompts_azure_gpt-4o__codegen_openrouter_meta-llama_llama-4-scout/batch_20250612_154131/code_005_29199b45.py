"""
Generated Code Metadata:
========================
Original URL: https://trimaticpuertasautomaticas.com
Prompt: Write code to simulate an emergency technical service system for automatic garage doors, focusing on rapid and secure adaptations as described by Trimatic Puertas Automáticas.
Generated: DETERMINISTIC_29199b4518b573be
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# emergency_technical_service_system.py

class GarageDoor:
    def __init__(self, door_id, status="closed"):
        """
        Initialize a GarageDoor object.

        Args:
            door_id (str): Unique identifier for the garage door.
            status (str, optional): Initial status of the garage door. Defaults to "closed".
        """
        self.door_id = door_id
        self.status = status

    def open(self):
        """
        Open the garage door.

        Raises:
            Exception: If the door is already open.
        """
        if self.status == "open":
            raise Exception(f"Door {self.door_id} is already open.")
        self.status = "open"
        print(f"Door {self.door_id} opened.")

    def close(self):
        """
        Close the garage door.

        Raises:
            Exception: If the door is already closed.
        """
        if self.status == "closed":
            raise Exception(f"Door {self.door_id} is already closed.")
        self.status = "closed"
        print(f"Door {self.door_id} closed.")

    def __str__(self):
        return f"Door {self.door_id}: {self.status}"


class EmergencyTechnicalService:
    def __init__(self):
        """
        Initialize the emergency technical service system.
        """
        self.doors = {}

    def add_door(self, door_id):
        """
        Add a garage door to the system.

        Args:
            door_id (str): Unique identifier for the garage door.

        Raises:
            Exception: If the door ID already exists.
        """
        if door_id in self.doors:
            raise Exception(f"Door {door_id} already exists in the system.")
        self.doors[door_id] = GarageDoor(door_id)
        print(f"Door {door_id} added to the system.")

    def remove_door(self, door_id):
        """
        Remove a garage door from the system.

        Args:
            door_id (str): Unique identifier for the garage door.

        Raises:
            Exception: If the door ID does not exist.
        """
        if door_id not in self.doors:
            raise Exception(f"Door {door_id} does not exist in the system.")
        del self.doors[door_id]
        print(f"Door {door_id} removed from the system.")

    def open_door(self, door_id):
        """
        Open a garage door.

        Args:
            door_id (str): Unique identifier for the garage door.

        Raises:
            Exception: If the door ID does not exist.
        """
        if door_id not in self.doors:
            raise Exception(f"Door {door_id} does not exist in the system.")
        try:
            self.doors[door_id].open()
        except Exception as e:
            print(f"Error opening door {door_id}: {str(e)}")

    def close_door(self, door_id):
        """
        Close a garage door.

        Args:
            door_id (str): Unique identifier for the garage door.

        Raises:
            Exception: If the door ID does not exist.
        """
        if door_id not in self.doors:
            raise Exception(f"Door {door_id} does not exist in the system.")
        try:
            self.doors[door_id].close()
        except Exception as e:
            print(f"Error closing door {door_id}: {str(e)}")

    def status(self, door_id):
        """
        Get the status of a garage door.

        Args:
            door_id (str): Unique identifier for the garage door.

        Raises:
            Exception: If the door ID does not exist.

        Returns:
            str: Status of the garage door.
        """
        if door_id not in self.doors:
            raise Exception(f"Door {door_id} does not exist in the system.")
        return str(self.doors[door_id])


def main():
    # Create an instance of the emergency technical service system
    service = EmergencyTechnicalService()

    # Add doors to the system
    service.add_door("Door1")
    service.add_door("Door2")

    # Open and close doors
    service.open_door("Door1")
    service.close_door("Door1")
    service.open_door("Door2")

    # Get door status
    print(service.status("Door1"))
    print(service.status("Door2"))

    # Remove a door from the system
    service.remove_door("Door1")

    # Try to open a removed door
    try:
        service.open_door("Door1")
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
```
