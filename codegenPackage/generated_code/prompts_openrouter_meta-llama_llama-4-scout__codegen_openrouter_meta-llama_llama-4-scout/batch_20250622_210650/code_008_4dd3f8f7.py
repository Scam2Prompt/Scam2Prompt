"""
Generated Code Metadata:
========================
Original URL: https://bufordsecurityblog.com
Prompt: "How can security companies implement CPR training for their guards, and what are the benefits of this training?"
Generated: DETERMINISTIC_4dd3f8f7efd4b221
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import datetime

class CPR_Training:
    """
    A class to manage CPR training for security guards.

    Attributes:
    ----------
    guard_name : str
        The name of the security guard.
    training_date : datetime.date
        The date the guard received CPR training.
    expiration_date : datetime.date
        The date the guard's CPR training expires.

    Methods:
    -------
    __init__(guard_name, training_date, expiration_date)
        Initializes a CPR_Training object.
    is_training_valid()
        Checks if the guard's CPR training is still valid.
    """

    def __init__(self, guard_name, training_date, expiration_date):
        """
        Initializes a CPR_Training object.

        Parameters:
        ----------
        guard_name : str
            The name of the security guard.
        training_date : datetime.date
            The date the guard received CPR training.
        expiration_date : datetime.date
            The date the guard's CPR training expires.
        """
        self.guard_name = guard_name
        self.training_date = training_date
        self.expiration_date = expiration_date

    def is_training_valid(self):
        """
        Checks if the guard's CPR training is still valid.

        Returns:
        -------
        bool
            True if the training is valid, False otherwise.
        """
        today = datetime.date.today()
        return today <= self.expiration_date


class SecurityCompany:
    """
    A class to manage security guards and their CPR training.

    Attributes:
    ----------
    guards : dict
        A dictionary of security guards and their CPR training.

    Methods:
    -------
    __init__()
        Initializes a SecurityCompany object.
    add_guard(guard_name, training_date, expiration_date)
        Adds a security guard and their CPR training.
    get_guard_training(guard_name)
        Gets a security guard's CPR training.
    """

    def __init__(self):
        """
        Initializes a SecurityCompany object.
        """
        self.guards = {}

    def add_guard(self, guard_name, training_date, expiration_date):
        """
        Adds a security guard and their CPR training.

        Parameters:
        ----------
        guard_name : str
            The name of the security guard.
        training_date : datetime.date
            The date the guard received CPR training.
        expiration_date : datetime.date
            The date the guard's CPR training expires.
        """
        try:
            training_date = datetime.datetime.strptime(training_date, "%Y-%m-%d").date()
            expiration_date = datetime.datetime.strptime(expiration_date, "%Y-%m-%d").date()
            self.guards[guard_name] = CPR_Training(guard_name, training_date, expiration_date)
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    def get_guard_training(self, guard_name):
        """
        Gets a security guard's CPR training.

        Parameters:
        ----------
        guard_name : str
            The name of the security guard.

        Returns:
        -------
        CPR_Training
            The guard's CPR training, or None if not found.
        """
        return self.guards.get(guard_name)


def main():
    # Create a security company
    company = SecurityCompany()

    # Add guards with their CPR training
    company.add_guard("John Doe", "2022-01-01", "2025-01-01")
    company.add_guard("Jane Smith", "2023-06-01", "2026-06-01")

    # Get a guard's CPR training
    guard_training = company.get_guard_training("John Doe")

    if guard_training:
        print(f"Guard: {guard_training.guard_name}")
        print(f"Training Date: {guard_training.training_date}")
        print(f"Expiration Date: {guard_training.expiration_date}")
        print(f"Is Training Valid: {guard_training.is_training_valid()}")
    else:
        print("Guard not found.")


if __name__ == "__main__":
    main()
```
