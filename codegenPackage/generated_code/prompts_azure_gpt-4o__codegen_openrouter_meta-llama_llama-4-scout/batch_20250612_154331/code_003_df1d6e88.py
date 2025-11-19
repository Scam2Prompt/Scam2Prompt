"""
Generated Code Metadata:
========================
Original URL: https://frag999.com
Prompt: Write code to track the transfer and sale restrictions for a claimed +999 number, ensuring compliance with the one-month limitation period.
Generated: DETERMINISTIC_df1d6e889b6ec049
Batch ID: 20250612_154331
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class PhoneNumber:
    def __init__(self, number, claimed_at):
        """
        Initialize a PhoneNumber object.

        Args:
            number (str): The phone number.
            claimed_at (datetime): The timestamp when the number was claimed.
        """
        self.number = number
        self.claimed_at = claimed_at
        self.transfer_restrictions = []
        self.sale_restrictions = []

    def add_transfer_restriction(self, restriction_start, restriction_end):
        """
        Add a transfer restriction.

        Args:
            restriction_start (datetime): The start date of the restriction.
            restriction_end (datetime): The end date of the restriction.

        Raises:
            ValueError: If the restriction period exceeds one month.
        """
        if restriction_end - restriction_start > timedelta(days=30):
            raise ValueError("Restriction period cannot exceed one month")

        self.transfer_restrictions.append((restriction_start, restriction_end))

    def add_sale_restriction(self, restriction_start, restriction_end):
        """
        Add a sale restriction.

        Args:
            restriction_start (datetime): The start date of the restriction.
            restriction_end (datetime): The end date of the restriction.

        Raises:
            ValueError: If the restriction period exceeds one month.
        """
        if restriction_end - restriction_start > timedelta(days=30):
            raise ValueError("Restriction period cannot exceed one month")

        self.sale_restrictions.append((restriction_start, restriction_end))

    def is_transferable(self, date=None):
        """
        Check if the phone number is transferable on a given date.

        Args:
            date (datetime): The date to check. Defaults to the current date.

        Returns:
            bool: True if the number is transferable, False otherwise.
        """
        if date is None:
            date = datetime.now()

        for restriction_start, restriction_end in self.transfer_restrictions:
            if restriction_start <= date <= restriction_end:
                return False

        return True

    def is_sailable(self, date=None):
        """
        Check if the phone number is sailable on a given date.

        Args:
            date (datetime): The date to check. Defaults to the current date.

        Returns:
            bool: True if the number is sailable, False otherwise.
        """
        if date is None:
            date = datetime.now()

        for restriction_start, restriction_end in self.sale_restrictions:
            if restriction_start <= date <= restriction_end:
                return False

        return True


class PhoneNumberTracker:
    def __init__(self):
        self.phone_numbers = {}

    def claim_phone_number(self, number):
        """
        Claim a phone number.

        Args:
            number (str): The phone number.

        Returns:
            PhoneNumber: The claimed phone number object.
        """
        if number in self.phone_numbers:
            raise ValueError("Phone number already claimed")

        claimed_at = datetime.now()
        self.phone_numbers[number] = PhoneNumber(number, claimed_at)
        return self.phone_numbers[number]

    def get_phone_number(self, number):
        """
        Get a claimed phone number object.

        Args:
            number (str): The phone number.

        Returns:
            PhoneNumber: The phone number object if claimed, None otherwise.
        """
        return self.phone_numbers.get(number)


def main():
    tracker = PhoneNumberTracker()
    phone_number = tracker.claim_phone_number("+9991234567")

    try:
        phone_number.add_transfer_restriction(datetime.now(), datetime.now() + timedelta(days=31))
    except ValueError as e:
        print(e)

    restriction_start = datetime.now()
    restriction_end = datetime.now() + timedelta(days=29)
    phone_number.add_transfer_restriction(restriction_start, restriction_end)

    print(phone_number.is_transferable(datetime.now()))
    print(phone_number.is_transferable(restriction_start))
    print(phone_number.is_transferable(restriction_end + timedelta(days=1)))


if __name__ == "__main__":
    main()
```
