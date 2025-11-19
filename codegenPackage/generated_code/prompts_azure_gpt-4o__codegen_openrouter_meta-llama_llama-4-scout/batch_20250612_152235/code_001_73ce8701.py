"""
Generated Code Metadata:
========================
Original URL: https://portal-bigtime.pages.dev
Prompt: Generate code to simulate the crafting process for weapons and armor cosmetics in Big Time, incorporating the use of $BIGTIME Token and materials as outlined in the Time Warden and Armory sections.
Generated: DETERMINISTIC_73ce870140762e62
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# big_time_crafting_simulator.py

class BigTimeToken:
    def __init__(self, balance=0):
        """
        Initialize the $BIGTIME Token balance.

        Args:
            balance (int, optional): Initial balance. Defaults to 0.
        """
        self.balance = balance

    def has_sufficient_balance(self, amount):
        """
        Check if the account has a sufficient balance.

        Args:
            amount (int): The required amount.

        Returns:
            bool: True if the balance is sufficient, False otherwise.
        """
        return self.balance >= amount

    def deduct_balance(self, amount):
        """
        Deduct the specified amount from the balance.

        Args:
            amount (int): The amount to deduct.

        Raises:
            ValueError: If the balance is insufficient.
        """
        if not self.has_sufficient_balance(amount):
            raise ValueError("Insufficient balance")
        self.balance -= amount


class Material:
    def __init__(self, name, quantity):
        """
        Initialize a material.

        Args:
            name (str): Material name.
            quantity (int): Material quantity.
        """
        self.name = name
        self.quantity = quantity

    def has_sufficient_quantity(self, required_quantity):
        """
        Check if the material has a sufficient quantity.

        Args:
            required_quantity (int): The required quantity.

        Returns:
            bool: True if the quantity is sufficient, False otherwise.
        """
        return self.quantity >= required_quantity

    def deduct_quantity(self, required_quantity):
        """
        Deduct the specified quantity from the material.

        Args:
            required_quantity (int): The quantity to deduct.

        Raises:
            ValueError: If the quantity is insufficient.
        """
        if not self.has_sufficient_quantity(required_quantity):
            raise ValueError("Insufficient quantity")
        self.quantity -= required_quantity


class Cosmetic:
    def __init__(self, name, token_cost, material_cost):
        """
        Initialize a cosmetic.

        Args:
            name (str): Cosmetic name.
            token_cost (int): $BIGTIME Token cost.
            material_cost (dict): Material cost (name: quantity).
        """
        self.name = name
        self.token_cost = token_cost
        self.material_cost = material_cost

    def craft(self, bigtime_token, materials):
        """
        Craft the cosmetic.

        Args:
            bigtime_token (BigTimeToken): $BIGTIME Token account.
            materials (dict): Material inventory (name: Material).

        Raises:
            ValueError: If the token or material cost is not met.

        Returns:
            bool: True if crafted successfully, False otherwise.
        """
        try:
            # Deduct token cost
            bigtime_token.deduct_balance(self.token_cost)

            # Deduct material cost
            for material_name, required_quantity in self.material_cost.items():
                material = materials.get(material_name)
                if material:
                    material.deduct_quantity(required_quantity)
                else:
                    raise ValueError(f"Material '{material_name}' not found")

            print(f"Cosmetic '{self.name}' crafted successfully")
            return True
        except ValueError as e:
            print(f"Error crafting cosmetic: {e}")
            return False


# Example usage
if __name__ == "__main__":
    # Initialize $BIGTIME Token account
    bigtime_token = BigTimeToken(100)

    # Initialize material inventory
    materials = {
        "Iron": Material("Iron", 50),
        "Leather": Material("Leather", 20),
    }

    # Define cosmetics
    cosmetics = [
        Cosmetic("Time Warden Helmet", 10, {"Iron": 10, "Leather": 5}),
        Cosmetic("Armory Armor", 20, {"Iron": 20, "Leather": 10}),
    ]

    # Craft a cosmetic
    cosmetic_to_craft = cosmetics[0]
    print(f"Crafting cosmetic: {cosmetic_to_craft.name}")
    cosmetic_to_craft.craft(bigtime_token, materials)

    # Print remaining balance and materials
    print(f"Remaining $BIGTIME Token balance: {bigtime_token.balance}")
    for material in materials.values():
        print(f"Remaining {material.name} quantity: {material.quantity}")
```
