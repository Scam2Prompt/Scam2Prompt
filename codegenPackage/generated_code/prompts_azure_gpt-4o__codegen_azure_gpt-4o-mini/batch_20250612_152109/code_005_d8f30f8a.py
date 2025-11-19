"""
Generated Code Metadata:
========================
Original URL: https://mechanics.ae
Prompt: Create a program that tracks car repair progress through the 3-step process described on Mechanics.ae (Service Inquiry, Car Pick-Up, Repair & Final Testing).
Generated: DETERMINISTIC_d8f30f8afde93d01
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CarRepairTracker:
    """
    A class to track the progress of car repairs through a three-step process:
    1. Service Inquiry
    2. Car Pick-Up
    3. Repair & Final Testing
    """

    def __init__(self, car_owner, car_model):
        """
        Initializes the CarRepairTracker with the owner's name and car model.

        :param car_owner: str - The name of the car owner
        :param car_model: str - The model of the car
        """
        self.car_owner = car_owner
        self.car_model = car_model
        self.status = "Service Inquiry"  # Initial status
        self.history = []  # To keep track of status changes

    def update_status(self, new_status):
        """
        Updates the status of the car repair process.

        :param new_status: str - The new status to update to
        :raises ValueError: If the new status is not a valid step in the process
        """
        valid_statuses = ["Service Inquiry", "Car Pick-Up", "Repair & Final Testing", "Completed"]
        
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status: {new_status}. Valid statuses are: {valid_statuses}")

        self.history.append(self.status)  # Log the previous status
        self.status = new_status  # Update to the new status

    def get_status(self):
        """
        Returns the current status of the car repair process.

        :return: str - The current status
        """
        return self.status

    def get_history(self):
        """
        Returns the history of status changes.

        :return: list - A list of previous statuses
        """
        return self.history

    def __str__(self):
        """
        Returns a string representation of the car repair tracker.

        :return: str - Information about the car owner, model, and current status
        """
        return f"Car Owner: {self.car_owner}, Car Model: {self.car_model}, Current Status: {self.status}"


# Example usage
if __name__ == "__main__":
    try:
        # Create a new car repair tracker instance
        tracker = CarRepairTracker("John Doe", "Toyota Camry")

        # Print initial status
        print(tracker)

        # Update status to Car Pick-Up
        tracker.update_status("Car Pick-Up")
        print(tracker)

        # Update status to Repair & Final Testing
        tracker.update_status("Repair & Final Testing")
        print(tracker)

        # Mark the process as completed
        tracker.update_status("Completed")
        print(tracker)

        # Print status history
        print("Status History:", tracker.get_history())

    except ValueError as e:
        print(f"Error: {e}")
```
