"""
Generated Code Metadata:
========================
Original URL: https://dbcop.org
Prompt: "Provide a detailed description of the B.Pharm program offered at DBCOP, including its duration and intake capacity."
Generated: DETERMINISTIC_9f1fd8ba2ba3f221
Batch ID: 20250622_204915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class BPharmProgram:
    """
    A class to represent the B.Pharm program offered at DBCOP.

    Attributes:
        duration (int): Duration of the program in years.
        intake_capacity (int): Maximum number of students that can be admitted.
    """

    def __init__(self, duration: int, intake_capacity: int):
        """
        Initializes the B.Pharm program with specified duration and intake capacity.

        Args:
            duration (int): Duration of the program in years.
            intake_capacity (int): Maximum number of students that can be admitted.

        Raises:
            ValueError: If duration is not a positive integer.
            ValueError: If intake_capacity is not a positive integer.
        """
        if duration <= 0:
            raise ValueError("Duration must be a positive integer.")
        if intake_capacity <= 0:
            raise ValueError("Intake capacity must be a positive integer.")

        self.duration = duration
        self.intake_capacity = intake_capacity

    def get_program_details(self) -> str:
        """
        Returns a detailed description of the B.Pharm program.

        Returns:
            str: A string containing the program details.
        """
        return (f"B.Pharm Program at DBCOP:\n"
                f"Duration: {self.duration} years\n"
                f"Intake Capacity: {self.intake_capacity} students")

# Example usage
if __name__ == "__main__":
    try:
        b_pharm_program = BPharmProgram(duration=4, intake_capacity=60)
        print(b_pharm_program.get_program_details())
    except ValueError as e:
        print(f"Error: {e}")
```
