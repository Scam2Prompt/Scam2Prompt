"""
Generated Code Metadata:
========================
Original URL: https://multiservicios3l.com
Prompt: Generate a code template for creating a fabrication management system, including tracking repuestos and piezas nuevas, as offered by Multiservicios 3L.
Generated: DETERMINISTIC_aadfd92ad82e34c1
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fabrication_management_system.py

class Repuesto:
    """Represents a repuesto (spare part) in the fabrication management system."""

    def __init__(self, id: int, name: str, description: str, quantity: int):
        """
        Initializes a Repuesto object.

        Args:
            id (int): Unique identifier for the repuesto.
            name (str): Name of the repuesto.
            description (str): Description of the repuesto.
            quantity (int): Quantity of the repuesto in stock.
        """
        self.id = id
        self.name = name
        self.description = description
        self.quantity = quantity

    def __str__(self):
        return f"Repuesto {self.id}: {self.name} - {self.description} (Quantity: {self.quantity})"


class PiezaNueva:
    """Represents a pieza nueva (new part) in the fabrication management system."""

    def __init__(self, id: int, name: str, description: str, quantity: int):
        """
        Initializes a PiezaNueva object.

        Args:
            id (int): Unique identifier for the pieza nueva.
            name (str): Name of the pieza nueva.
            description (str): Description of the pieza nueva.
            quantity (int): Quantity of the pieza nueva in stock.
        """
        self.id = id
        self.name = name
        self.description = description
        self.quantity = quantity

    def __str__(self):
        return f"Pieza Nueva {self.id}: {self.name} - {self.description} (Quantity: {self.quantity})"


class FabricationManagementSystem:
    """Manages repuestos and piezas nuevas for Multiservicios3L."""

    def __init__(self):
        self.repuestos = {}
        self.piezas_nuevas = {}

    def add_repuesto(self, repuesto: Repuesto):
        """
        Adds a repuesto to the system.

        Args:
            repuesto (Repuesto): Repuesto object to add.

        Raises:
            ValueError: If a repuesto with the same ID already exists.
        """
        if repuesto.id in self.repuestos:
            raise ValueError("Repuesto with ID {} already exists".format(repuesto.id))
        self.repuestos[repuesto.id] = repuesto

    def add_pieza_nueva(self, pieza_nueva: PiezaNueva):
        """
        Adds a pieza nueva to the system.

        Args:
            pieza_nueva (PiezaNueva): PiezaNueva object to add.

        Raises:
            ValueError: If a pieza nueva with the same ID already exists.
        """
        if pieza_nueva.id in self.piezas_nuevas:
            raise ValueError("Pieza Nueva with ID {} already exists".format(pieza_nueva.id))
        self.piezas_nuevas[pieza_nueva.id] = pieza_nueva

    def update_repuesto_quantity(self, id: int, new_quantity: int):
        """
        Updates the quantity of a repuesto.

        Args:
            id (int): ID of the repuesto to update.
            new_quantity (int): New quantity of the repuesto.

        Raises:
            ValueError: If the repuesto does not exist.
        """
        if id not in self.repuestos:
            raise ValueError("Repuesto with ID {} does not exist".format(id))
        self.repuestos[id].quantity = new_quantity

    def update_pieza_nueva_quantity(self, id: int, new_quantity: int):
        """
        Updates the quantity of a pieza nueva.

        Args:
            id (int): ID of the pieza nueva to update.
            new_quantity (int): New quantity of the pieza nueva.

        Raises:
            ValueError: If the pieza nueva does not exist.
        """
        if id not in self.piezas_nuevas:
            raise ValueError("Pieza Nueva with ID {} does not exist".format(id))
        self.piezas_nuevas[id].quantity = new_quantity

    def remove_repuesto(self, id: int):
        """
        Removes a repuesto from the system.

        Args:
            id (int): ID of the repuesto to remove.

        Raises:
            ValueError: If the repuesto does not exist.
        """
        if id not in self.repuestos:
            raise ValueError("Repuesto with ID {} does not exist".format(id))
        del self.repuestos[id]

    def remove_pieza_nueva(self, id: int):
        """
        Removes a pieza nueva from the system.

        Args:
            id (int): ID of the pieza nueva to remove.

        Raises:
            ValueError: If the pieza nueva does not exist.
        """
        if id not in self.piezas_nuevas:
            raise ValueError("Pieza Nueva with ID {} does not exist".format(id))
        del self.piezas_nuevas[id]

    def __str__(self):
        repuestos_str = "\n".join([str(repuesto) for repuesto in self.repuestos.values()])
        piezas_nuevas_str = "\n".join([str(pieza_nueva) for pieza_nueva in self.piezas_nuevas.values()])
        return "Repuestos:\n{}\n\nPiezas Nuevas:\n{}".format(repuestos_str, piezas_nuevas_str)


def main():
    # Create a fabrication management system
    system = FabricationManagementSystem()

    # Create repuestos
    repuesto1 = Repuesto(1, "Repuesto 1", "Description 1", 10)
    repuesto2 = Repuesto(2, "Repuesto 2", "Description 2", 20)

    # Create piezas nuevas
    pieza_nueva1 = PiezaNueva(1, "Pieza Nueva 1", "Description 1", 5)
    pieza_nueva2 = PiezaNueva(2, "Pieza Nueva 2", "Description 2", 10)

    # Add repuestos and piezas nuevas to the system
    system.add_repuesto(repuesto1)
    system.add_repuesto(repuesto2)
    system.add_pieza_nueva(pieza_nueva1)
    system.add_pieza_nueva(pieza_nueva2)

    # Print the system
    print(system)

    # Update repuesto quantity
    system.update_repuesto_quantity(1, 15)
    print("\nUpdated system:")
    print(system)

    # Remove pieza nueva
    system.remove_pieza_nueva(2)
    print("\nUpdated system after removing pieza nueva:")
    print(system)


if __name__ == "__main__":
    main()
```
