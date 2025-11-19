"""
Generated Code Metadata:
========================
Original URL: https://mandosecurity.com
Prompt: "Write a Python script to manage security personnel and surveillance cameras for a mall security company like Mando Security."
Generated: DETERMINISTIC_57661e417b1ade88
Batch ID: 20250622_205929
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# security_management.py

class SecurityPersonnel:
    """Represents a security personnel."""

    def __init__(self, personnel_id, name, role):
        """
        Initializes a SecurityPersonnel object.

        Args:
            personnel_id (int): Unique ID for the personnel.
            name (str): Name of the personnel.
            role (str): Role of the personnel (e.g., guard, supervisor).
        """
        self.personnel_id = personnel_id
        self.name = name
        self.role = role

    def __str__(self):
        return f"Personnel ID: {self.personnel_id}, Name: {self.name}, Role: {self.role}"


class SurveillanceCamera:
    """Represents a surveillance camera."""

    def __init__(self, camera_id, location):
        """
        Initializes a SurveillanceCamera object.

        Args:
            camera_id (int): Unique ID for the camera.
            location (str): Location of the camera in the mall.
        """
        self.camera_id = camera_id
        self.location = location
        self.is_online = False

    def toggle_status(self):
        """Toggles the online status of the camera."""
        self.is_online = not self.is_online

    def __str__(self):
        status = "Online" if self.is_online else "Offline"
        return f"Camera ID: {self.camera_id}, Location: {self.location}, Status: {status}"


class SecurityManagementSystem:
    """Manages security personnel and surveillance cameras."""

    def __init__(self):
        self.personnel = {}
        self.cameras = {}

    def add_personnel(self, personnel_id, name, role):
        """
        Adds a security personnel to the system.

        Args:
            personnel_id (int): Unique ID for the personnel.
            name (str): Name of the personnel.
            role (str): Role of the personnel.

        Raises:
            ValueError: If personnel ID already exists.
        """
        if personnel_id in self.personnel:
            raise ValueError("Personnel ID already exists")
        self.personnel[personnel_id] = SecurityPersonnel(personnel_id, name, role)

    def remove_personnel(self, personnel_id):
        """
        Removes a security personnel from the system.

        Args:
            personnel_id (int): Unique ID for the personnel.

        Raises:
            KeyError: If personnel ID does not exist.
        """
        if personnel_id not in self.personnel:
            raise KeyError("Personnel ID does not exist")
        del self.personnel[personnel_id]

    def add_camera(self, camera_id, location):
        """
        Adds a surveillance camera to the system.

        Args:
            camera_id (int): Unique ID for the camera.
            location (str): Location of the camera.

        Raises:
            ValueError: If camera ID already exists.
        """
        if camera_id in self.cameras:
            raise ValueError("Camera ID already exists")
        self.cameras[camera_id] = SurveillanceCamera(camera_id, location)

    def remove_camera(self, camera_id):
        """
        Removes a surveillance camera from the system.

        Args:
            camera_id (int): Unique ID for the camera.

        Raises:
            KeyError: If camera ID does not exist.
        """
        if camera_id not in self.cameras:
            raise KeyError("Camera ID does not exist")
        del self.cameras[camera_id]

    def toggle_camera_status(self, camera_id):
        """
        Toggles the online status of a surveillance camera.

        Args:
            camera_id (int): Unique ID for the camera.

        Raises:
            KeyError: If camera ID does not exist.
        """
        if camera_id not in self.cameras:
            raise KeyError("Camera ID does not exist")
        self.cameras[camera_id].toggle_status()

    def print_personnel(self):
        """Prints all security personnel."""
        for personnel in self.personnel.values():
            print(personnel)

    def print_cameras(self):
        """Prints all surveillance cameras."""
        for camera in self.cameras.values():
            print(camera)


def main():
    try:
        system = SecurityManagementSystem()

        while True:
            print("\nSecurity Management System")
            print("1. Add security personnel")
            print("2. Remove security personnel")
            print("3. Add surveillance camera")
            print("4. Remove surveillance camera")
            print("5. Toggle camera status")
            print("6. Print personnel")
            print("7. Print cameras")
            print("8. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                personnel_id = int(input("Enter personnel ID: "))
                name = input("Enter name: ")
                role = input("Enter role: ")
                system.add_personnel(personnel_id, name, role)
            elif choice == "2":
                personnel_id = int(input("Enter personnel ID: "))
                system.remove_personnel(personnel_id)
            elif choice == "3":
                camera_id = int(input("Enter camera ID: "))
                location = input("Enter location: ")
                system.add_camera(camera_id, location)
            elif choice == "4":
                camera_id = int(input("Enter camera ID: "))
                system.remove_camera(camera_id)
            elif choice == "5":
                camera_id = int(input("Enter camera ID: "))
                system.toggle_camera_status(camera_id)
            elif choice == "6":
                system.print_personnel()
            elif choice == "7":
                system.print_cameras()
            elif choice == "8":
                break
            else:
                print("Invalid option. Please choose a valid option.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
