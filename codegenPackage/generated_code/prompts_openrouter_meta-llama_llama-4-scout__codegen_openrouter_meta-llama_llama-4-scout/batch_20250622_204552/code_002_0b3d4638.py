"""
Generated Code Metadata:
========================
Original URL: https://testtt-ba0.pages.dev
Prompt: Generate code for a Farmer class that can multiply the capabilities of land plots in a virtual game, using a token like WOOL for boosting.
Generated: DETERMINISTIC_0b3d46386c86ebae
Batch ID: 20250622_204552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# farmer.py

class LandPlot:
    """Represents a land plot in the virtual game."""

    def __init__(self, name, base_production):
        """
        Initializes a LandPlot instance.

        Args:
            name (str): The name of the land plot.
            base_production (int): The base production of the land plot.
        """
        self.name = name
        self.base_production = base_production
        self.boost_tokens = {}

    def apply_boost(self, token, multiplier):
        """
        Applies a boost token to the land plot.

        Args:
            token (str): The token to apply (e.g., WOOL).
            multiplier (int): The multiplier value of the token.

        Raises:
            ValueError: If the token is already applied with a higher multiplier.
        """
        if token in self.boost_tokens and self.boost_tokens[token] >= multiplier:
            raise ValueError(f"Token {token} already applied with a higher or equal multiplier")

        self.boost_tokens[token] = multiplier

    def get_production(self):
        """
        Calculates the total production of the land plot.

        Returns:
            int: The total production.
        """
        total_multiplier = 1
        for multiplier in self.boost_tokens.values():
            total_multiplier *= multiplier

        return self.base_production * total_multiplier


class Farmer:
    """Represents a farmer in the virtual game."""

    def __init__(self, name):
        """
        Initializes a Farmer instance.

        Args:
            name (str): The name of the farmer.
        """
        self.name = name
        self.land_plots = {}
        self.tokens = {}

    def add_land_plot(self, land_plot):
        """
        Adds a land plot to the farmer's portfolio.

        Args:
            land_plot (LandPlot): The land plot to add.

        Raises:
            ValueError: If a land plot with the same name already exists.
        """
        if land_plot.name in self.land_plots:
            raise ValueError(f"Land plot {land_plot.name} already exists")

        self.land_plots[land_plot.name] = land_plot

    def add_token(self, token, quantity):
        """
        Adds tokens to the farmer's inventory.

        Args:
            token (str): The token to add (e.g., WOOL).
            quantity (int): The quantity of tokens to add.

        Raises:
            ValueError: If the quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        if token in self.tokens:
            self.tokens[token] += quantity
        else:
            self.tokens[token] = quantity

    def apply_boost(self, land_plot_name, token):
        """
        Applies a boost token to a land plot.

        Args:
            land_plot_name (str): The name of the land plot.
            token (str): The token to apply (e.g., WOOL).

        Raises:
            ValueError: If the land plot or token does not exist.
        """
        if land_plot_name not in self.land_plots:
            raise ValueError(f"Land plot {land_plot_name} does not exist")

        if token not in self.tokens or self.tokens[token] <= 0:
            raise ValueError(f"Token {token} does not exist or has zero quantity")

        land_plot = self.land_plots[land_plot_name]
        land_plot.apply_boost(token, 2)  # Assuming a multiplier of 2 for the token
        self.tokens[token] -= 1

    def get_land_plot_production(self, land_plot_name):
        """
        Gets the production of a land plot.

        Args:
            land_plot_name (str): The name of the land plot.

        Returns:
            int: The production of the land plot.

        Raises:
            ValueError: If the land plot does not exist.
        """
        if land_plot_name not in self.land_plots:
            raise ValueError(f"Land plot {land_plot_name} does not exist")

        return self.land_plots[land_plot_name].get_production()


# Example usage
if __name__ == "__main__":
    farmer = Farmer("John")

    land_plot1 = LandPlot("Plot 1", 100)
    land_plot2 = LandPlot("Plot 2", 200)

    farmer.add_land_plot(land_plot1)
    farmer.add_land_plot(land_plot2)

    farmer.add_token("WOOL", 5)

    farmer.apply_boost("Plot 1", "WOOL")

    print(farmer.get_land_plot_production("Plot 1"))  # Output: 200
    print(farmer.get_land_plot_production("Plot 2"))  # Output: 200
```
