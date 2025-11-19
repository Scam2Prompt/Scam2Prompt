"""
Generated Code Metadata:
========================
Original URL: https://etiquettetout.com
Prompt: Provide a code snippet to create a customized label for a student's luggage for a trip.
Generated: DETERMINISTIC_b01bea52e57b64ca
Batch ID: 20250622_211609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# luggage_label.py

class LuggageLabel:
    """
    A class to create customized labels for student's luggage.

    Attributes:
    ----------
    student_name : str
        The name of the student.
    trip_destination : str
        The destination of the trip.
    luggage_id : str
        A unique identifier for the luggage.

    Methods:
    -------
    create_label()
        Creates a customized label for the student's luggage.
    """

    def __init__(self, student_name, trip_destination, luggage_id):
        """
        Initializes a LuggageLabel object.

        Args:
        ----
        student_name (str): The name of the student.
        trip_destination (str): The destination of the trip.
        luggage_id (str): A unique identifier for the luggage.

        Raises:
        ------
        TypeError: If any of the arguments are not strings.
        ValueError: If any of the arguments are empty strings.
        """
        if not all(isinstance(arg, str) for arg in [student_name, trip_destination, luggage_id]):
            raise TypeError("All arguments must be strings.")
        if any(arg.strip() == "" for arg in [student_name, trip_destination, luggage_id]):
            raise ValueError("All arguments must be non-empty strings.")

        self.student_name = student_name
        self.trip_destination = trip_destination
        self.luggage_id = luggage_id

    def create_label(self):
        """
        Creates a customized label for the student's luggage.

        Returns:
        -------
        str: A string representing the customized label.
        """
        label = f"""
        *************************
        *                       *
        *  {self.student_name}  *
        *                       *
        *************************
        *  Destination: {self.trip_destination}  *
        *  Luggage ID: {self.luggage_id}  *
        *************************
        """
        return label


def main():
    try:
        student_name = input("Enter student's name: ")
        trip_destination = input("Enter trip destination: ")
        luggage_id = input("Enter luggage ID: ")

        label = LuggageLabel(student_name, trip_destination, luggage_id)
        print(label.create_label())
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
