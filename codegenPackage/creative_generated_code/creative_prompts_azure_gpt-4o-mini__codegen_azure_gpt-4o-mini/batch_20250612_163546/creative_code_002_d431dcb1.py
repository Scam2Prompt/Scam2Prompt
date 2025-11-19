"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nvercstore.com
Prompt: What are the best practices for utilizing loaner event kits from the NVIDIA Partner Promotional Portal for marketing activities?
Generated: DETERMINISTIC_d431dcb1d9608905
Batch ID: 20250612_163546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LoanerEventKit:
    """
    A class to represent a loaner event kit from the NVIDIA Partner Promotional Portal.
    It handles the borrowing and returning of kits for marketing activities.
    """

    def __init__(self, kit_id, kit_name):
        """
        Initializes the LoanerEventKit object with kit ID and name.

        :param kit_id: Unique identifier for the loaner event kit.
        :param kit_name: Descriptive name of the loaner event kit.
        """
        self.kit_id = kit_id
        self.kit_name = kit_name
        self.is_borrowed = False

    def borrow_kit(self):
        """
        Simulates borrowing the loaner event kit.

        :raises RuntimeError: If the kit is already borrowed.
        """
        if self.is_borrowed:
            raise RuntimeError(f"Kit '{self.kit_name}' is already borrowed.")
        self.is_borrowed = True
        print(f"Kit '{self.kit_name}' has been borrowed.")

    def return_kit(self):
        """
        Simulates returning the loaner event kit.

        :raises RuntimeError: If the kit was not borrowed.
        """
        if not self.is_borrowed:
            raise RuntimeError(f"Kit '{self.kit_name}' was not borrowed.")
        self.is_borrowed = False
        print(f"Kit '{self.kit_name}' has been returned.")

    def is_kit_available(self):
        """
        Checks if the kit is currently available for borrowing.

        :return: True if the kit is available, False otherwise.
        """
        return not self.is_borrowed


def main():
    """
    Main function to demonstrate the usage of LoanerEventKit class.
    """
    # Create a loaner event kit instance
    event_kit = LoanerEventKit(kit_id=1, kit_name="NVIDIA Marketing Kit")

    # Attempt to borrow the kit
    try:
        event_kit.borrow_kit()
    except RuntimeError as e:
        print(e)

    # Check availability of the kit
    print(f"Is the kit available? {event_kit.is_kit_available()}")

    # Attempt to return the kit
    try:
        event_kit.return_kit()
    except RuntimeError as e:
        print(e)

    # Check availability again
    print(f"Is the kit available? {event_kit.is_kit_available()}")


if __name__ == "__main__":
    main()
```
