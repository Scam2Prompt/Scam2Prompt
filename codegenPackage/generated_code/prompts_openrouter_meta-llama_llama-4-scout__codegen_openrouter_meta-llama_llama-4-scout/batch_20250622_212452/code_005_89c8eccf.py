"""
Generated Code Metadata:
========================
Original URL: https://playland.co.ke
Prompt: "Write a Python script to determine the most cost-effective Playland Kenya service for a child aged 10, considering the prices of Trampoline Park, Soft Play Area, and Virtual Reality."
Generated: DETERMINISTIC_89c8eccff1ad05b1
Batch ID: 20250622_212452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# playland_kenya.py

class PlaylandKenyaService:
    """Represents a Playland Kenya service with a name and price."""

    def __init__(self, name: str, price: float):
        """
        Initializes a PlaylandKenyaService instance.

        Args:
            name (str): The name of the service.
            price (float): The price of the service.
        """
        self.name = name
        self.price = price


class PlaylandKenya:
    """Provides methods to determine the most cost-effective Playland Kenya service."""

    def __init__(self):
        """Initializes a PlaylandKenya instance with services and child age."""
        self.services = [
            PlaylandKenyaService("Trampoline Park", 800.0),
            PlaylandKenyaService("Soft Play Area", 600.0),
            PlaylandKenyaService("Virtual Reality", 1200.0),
        ]
        self.child_age = 10

    def get_most_cost_effective_service(self) -> PlaylandKenyaService:
        """
        Determines the most cost-effective Playland Kenya service for a child.

        Returns:
            PlaylandKenyaService: The most cost-effective service.

        Raises:
            ValueError: If no services are available or child age is invalid.
        """
        if not self.services:
            raise ValueError("No services available")

        if self.child_age < 0:
            raise ValueError("Invalid child age")

        # Assume a discount for children under 12 years old
        if self.child_age < 12:
            discounted_services = [
                PlaylandKenyaService(service.name, service.price * 0.8)
                for service in self.services
            ]
        else:
            discounted_services = self.services

        most_cost_effective_service = min(discounted_services, key=lambda service: service.price)

        return most_cost_effective_service


def main():
    try:
        playland_kenya = PlaylandKenya()
        most_cost_effective_service = playland_kenya.get_most_cost_effective_service()
        print(f"The most cost-effective service for a {playland_kenya.child_age} year old is:")
        print(f"{most_cost_effective_service.name} - KES {most_cost_effective_service.price:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
