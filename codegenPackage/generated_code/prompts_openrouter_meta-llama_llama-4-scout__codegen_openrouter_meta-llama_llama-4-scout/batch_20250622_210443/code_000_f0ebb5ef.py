"""
Generated Code Metadata:
========================
Original URL: https://opcsas.com
Prompt: "Write a Python script to manage cargo transportation services for refrigerated and dry cargo, considering the requirements of Operadora Portuaria del Caribe."
Generated: DETERMINISTIC_f0ebb5ef5ae20a86
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cargo_transportation.py

class Cargo:
    """Base class for cargo types."""

    def __init__(self, cargo_id, weight, volume):
        """
        Initialize cargo.

        Args:
            cargo_id (str): Unique identifier for the cargo.
            weight (float): Weight of the cargo in kilograms.
            volume (float): Volume of the cargo in cubic meters.
        """
        self.cargo_id = cargo_id
        self.weight = weight
        self.volume = volume

    def __str__(self):
        return f"Cargo ID: {self.cargo_id}, Weight: {self.weight} kg, Volume: {self.volume} m³"


class RefrigeratedCargo(Cargo):
    """Class for refrigerated cargo."""

    def __init__(self, cargo_id, weight, volume, temperature):
        """
        Initialize refrigerated cargo.

        Args:
            cargo_id (str): Unique identifier for the cargo.
            weight (float): Weight of the cargo in kilograms.
            volume (float): Volume of the cargo in cubic meters.
            temperature (float): Required temperature in degrees Celsius.
        """
        super().__init__(cargo_id, weight, volume)
        self.temperature = temperature

    def __str__(self):
        return super().__str__() + f", Temperature: {self.temperature}°C"


class DryCargo(Cargo):
    """Class for dry cargo."""

    def __init__(self, cargo_id, weight, volume):
        """
        Initialize dry cargo.

        Args:
            cargo_id (str): Unique identifier for the cargo.
            weight (float): Weight of the cargo in kilograms.
            volume (float): Volume of the cargo in cubic meters.
        """
        super().__init__(cargo_id, weight, volume)

    def __str__(self):
        return super().__str__()


class TransportationService:
    """Class for cargo transportation services."""

    def __init__(self):
        self.cargos = []

    def add_cargo(self, cargo):
        """
        Add cargo to the transportation service.

        Args:
            cargo (Cargo): Cargo to add.

        Raises:
            TypeError: If the cargo is not an instance of Cargo.
        """
        if not isinstance(cargo, Cargo):
            raise TypeError("Cargo must be an instance of Cargo")
        self.cargos.append(cargo)

    def remove_cargo(self, cargo_id):
        """
        Remove cargo from the transportation service.

        Args:
            cargo_id (str): ID of the cargo to remove.

        Raises:
            ValueError: If the cargo ID is not found.
        """
        for cargo in self.cargos:
            if cargo.cargo_id == cargo_id:
                self.cargos.remove(cargo)
                return
        raise ValueError("Cargo ID not found")

    def list_cargos(self):
        """List all cargos in the transportation service."""
        return self.cargos


def main():
    try:
        # Create a transportation service
        service = TransportationService()

        # Create refrigerated cargo
        refrigerated_cargo = RefrigeratedCargo("REF-001", 1000, 2, -20)
        print(refrigerated_cargo)

        # Create dry cargo
        dry_cargo = DryCargo("DRY-001", 500, 1)
        print(dry_cargo)

        # Add cargos to the transportation service
        service.add_cargo(refrigerated_cargo)
        service.add_cargo(dry_cargo)

        # List all cargos
        print("\nCargos:")
        for cargo in service.list_cargos():
            print(cargo)

        # Remove a cargo
        service.remove_cargo("REF-001")

        # List all cargos after removal
        print("\nCargos after removal:")
        for cargo in service.list_cargos():
            print(cargo)

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
