"""
Generated Code Metadata:
========================
Original URL: https://www.gbngroup.com.mx
Prompt: Write code to develop a communication strategy for a business, targeting multiple audiences (e.g., customers, suppliers, shareholders) to improve corporate reputation, as described by GBN Group.
Generated: DETERMINISTIC_a48f2d2f801f89a9
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# communication_strategy.py

from abc import ABC, abstractmethod
from typing import List

class Audience(ABC):
    """Abstract base class for different audiences."""

    def __init__(self, name: str):
        """
        Initialize an audience.

        Args:
        - name (str): The name of the audience.
        """
        self.name = name

    @abstractmethod
    def receive_message(self, message: str):
        """Receive a message from the business."""
        pass


class Customer(Audience):
    """Class representing customers."""

    def receive_message(self, message: str):
        """Receive a message from the business.

        Args:
        - message (str): The message from the business.
        """
        print(f"Customer: Received message - {message}")


class Supplier(Audience):
    """Class representing suppliers."""

    def receive_message(self, message: str):
        """Receive a message from the business.

        Args:
        - message (str): The message from the business.
        """
        print(f"Supplier: Received message - {message}")


class Shareholder(Audience):
    """Class representing shareholders."""

    def receive_message(self, message: str):
        """Receive a message from the business.

        Args:
        - message (str): The message from the business.
        """
        print(f"Shareholder: Received message - {message}")


class CommunicationStrategy:
    """Class representing a communication strategy."""

    def __init__(self):
        """
        Initialize a communication strategy.
        """
        self.audiences = []

    def add_audience(self, audience: Audience):
        """Add an audience to the communication strategy.

        Args:
        - audience (Audience): The audience to add.
        """
        self.audiences.append(audience)

    def send_message(self, message: str):
        """Send a message to all audiences.

        Args:
        - message (str): The message to send.
        """
        for audience in self.audiences:
            audience.receive_message(message)


class Business:
    """Class representing a business."""

    def __init__(self, name: str):
        """
        Initialize a business.

        Args:
        - name (str): The name of the business.
        """
        self.name = name
        self.communication_strategy = CommunicationStrategy()

    def set_communication_strategy(self, communication_strategy: CommunicationStrategy):
        """Set the communication strategy for the business.

        Args:
        - communication_strategy (CommunicationStrategy): The communication strategy.
        """
        self.communication_strategy = communication_strategy

    def send_message(self, message: str):
        """Send a message to all audiences.

        Args:
        - message (str): The message to send.
        """
        self.communication_strategy.send_message(message)


def main():
    try:
        # Create audiences
        customer = Customer("Customer")
        supplier = Supplier("Supplier")
        shareholder = Shareholder("Shareholder")

        # Create a communication strategy
        communication_strategy = CommunicationStrategy()
        communication_strategy.add_audience(customer)
        communication_strategy.add_audience(supplier)
        communication_strategy.add_audience(shareholder)

        # Create a business
        business = Business("GBN Group")
        business.set_communication_strategy(communication_strategy)

        # Send a message to all audiences
        message = "We are committed to improving our corporate reputation."
        business.send_message(message)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
