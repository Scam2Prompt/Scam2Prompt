"""
Generated Code Metadata:
========================
Original URL: https://gelenkzentrum-moenchengladbach.de
Prompt: "Develop a function to calculate recovery times for various orthopedic surgeries mentioned by Gelenkzentrum Mönchengladbach."
Generated: DETERMINISTIC_f4b91a5cb0dcce90
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# recovery_times.py

class OrthopedicSurgery:
    """Represents an orthopedic surgery with its recovery time."""

    def __init__(self, name, recovery_time_days):
        """
        Initializes an OrthopedicSurgery instance.

        Args:
            name (str): The name of the surgery.
            recovery_time_days (int): The recovery time in days.
        """
        self.name = name
        self.recovery_time_days = recovery_time_days


class RecoveryTimeCalculator:
    """Calculates recovery times for various orthopedic surgeries."""

    def __init__(self):
        """
        Initializes a RecoveryTimeCalculator instance with a dictionary of surgeries.

        The dictionary maps surgery names to their respective recovery times in days.
        """
        self.surgeries = {
            "hip replacement": OrthopedicSurgery("Hip Replacement", 14),
            "knee replacement": OrthopedicSurgery("Knee Replacement", 12),
            "shoulder replacement": OrthopedicSurgery("Shoulder Replacement", 10),
            "elbow replacement": OrthopedicSurgery("Elbow Replacement", 8),
            "ankle replacement": OrthopedicSurgery("Ankle Replacement", 6),
        }

    def calculate_recovery_time(self, surgery_name):
        """
        Calculates the recovery time for a given surgery.

        Args:
            surgery_name (str): The name of the surgery.

        Returns:
            int: The recovery time in days if the surgery is found.

        Raises:
            ValueError: If the surgery is not found.
        """
        try:
            surgery = self.surgeries[surgery_name.lower()]
            return surgery.recovery_time_days
        except KeyError:
            raise ValueError(f"Surgery '{surgery_name}' not found.")

    def add_surgery(self, name, recovery_time_days):
        """
        Adds a new surgery to the calculator.

        Args:
            name (str): The name of the surgery.
            recovery_time_days (int): The recovery time in days.

        Raises:
            ValueError: If the surgery already exists.
        """
        if name.lower() in self.surgeries:
            raise ValueError(f"Surgery '{name}' already exists.")
        self.surgeries[name.lower()] = OrthopedicSurgery(name, recovery_time_days)

    def remove_surgery(self, surgery_name):
        """
        Removes a surgery from the calculator.

        Args:
            surgery_name (str): The name of the surgery.

        Raises:
            ValueError: If the surgery is not found.
        """
        try:
            del self.surgeries[surgery_name.lower()]
        except KeyError:
            raise ValueError(f"Surgery '{surgery_name}' not found.")


def main():
    calculator = RecoveryTimeCalculator()

    # Example usage:
    print(calculator.calculate_recovery_time("Hip Replacement"))  # Output: 14

    # Add a new surgery
    calculator.add_surgery("Spine Surgery", 30)
    print(calculator.calculate_recovery_time("Spine Surgery"))  # Output: 30

    # Remove a surgery
    calculator.remove_surgery("Elbow Replacement")
    try:
        print(calculator.calculate_recovery_time("Elbow Replacement"))
    except ValueError as e:
        print(e)  # Output: Surgery 'Elbow Replacement' not found.


if __name__ == "__main__":
    main()
```
