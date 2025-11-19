"""
Generated Code Metadata:
========================
Original URL: https://gautamindustries.com
Prompt: "Write a Python code to manage inventory for a wholesale trader of plywood boards, including Timba 710 Plywood and Duro Plywood Board, with details from Gautam Industries."
Generated: DETERMINISTIC_904cb15ad398c348
Batch ID: 20250622_204617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_manager.py

class PlywoodBoard:
    """Represents a plywood board product."""

    def __init__(self, name, quantity, price_per_unit):
        """
        Initializes a PlywoodBoard object.

        Args:
            name (str): Name of the plywood board.
            quantity (int): Quantity of the plywood board in stock.
            price_per_unit (float): Price per unit of the plywood board.
        """
        self.name = name
        self.quantity = quantity
        self.price_per_unit = price_per_unit

    def __str__(self):
        return f"{self.name}: {self.quantity} units @ ${self.price_per_unit:.2f}/unit"


class Inventory:
    """Manages the inventory of plywood boards."""

    def __init__(self):
        """Initializes an empty inventory."""
        self.boards = {}

    def add_board(self, board):
        """
        Adds a plywood board to the inventory.

        Args:
            board (PlywoodBoard): Plywood board to add.

        Raises:
            ValueError: If a board with the same name already exists.
        """
        if board.name in self.boards:
            raise ValueError(f"Board '{board.name}' already exists in the inventory.")
        self.boards[board.name] = board

    def remove_board(self, name):
        """
        Removes a plywood board from the inventory.

        Args:
            name (str): Name of the plywood board to remove.

        Raises:
            KeyError: If the board does not exist in the inventory.
        """
        if name not in self.boards:
            raise KeyError(f"Board '{name}' does not exist in the inventory.")
        del self.boards[name]

    def update_quantity(self, name, new_quantity):
        """
        Updates the quantity of a plywood board in the inventory.

        Args:
            name (str): Name of the plywood board to update.
            new_quantity (int): New quantity of the plywood board.

        Raises:
            KeyError: If the board does not exist in the inventory.
            ValueError: If the new quantity is negative.
        """
        if name not in self.boards:
            raise KeyError(f"Board '{name}' does not exist in the inventory.")
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.boards[name].quantity = new_quantity

    def get_board(self, name):
        """
        Retrieves a plywood board from the inventory.

        Args:
            name (str): Name of the plywood board to retrieve.

        Returns:
            PlywoodBoard: The plywood board object.

        Raises:
            KeyError: If the board does not exist in the inventory.
        """
        if name not in self.boards:
            raise KeyError(f"Board '{name}' does not exist in the inventory.")
        return self.boards[name]

    def __str__(self):
        inventory_list = "\n".join(str(board) for board in self.boards.values())
        return f"Inventory:\n{inventory_list}"


def main():
    # Create an inventory
    inventory = Inventory()

    # Create plywood boards
    timba710 = PlywoodBoard("Timba710 Plywood", 100, 50.0)
    duro_board = PlywoodBoard("Duro Plywood Board", 50, 40.0)

    # Add boards to the inventory
    inventory.add_board(timba710)
    inventory.add_board(duro_board)

    # Print initial inventory
    print("Initial Inventory:")
    print(inventory)

    # Update quantity
    inventory.update_quantity("Timba710 Plywood", 80)

    # Print updated inventory
    print("\nUpdated Inventory:")
    print(inventory)

    # Try to add a duplicate board
    try:
        inventory.add_board(PlywoodBoard("Timba710 Plywood", 20, 50.0))
    except ValueError as e:
        print(f"\nError: {e}")

    # Try to remove a non-existent board
    try:
        inventory.remove_board("Non-existent Board")
    except KeyError as e:
        print(f"\nError: {e}")

    # Retrieve a board
    try:
        board = inventory.get_board("Duro Plywood Board")
        print(f"\nBoard: {board}")
    except KeyError as e:
        print(f"\nError: {e}")


if __name__ == "__main__":
    main()
```
