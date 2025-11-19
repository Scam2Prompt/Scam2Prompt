"""
Generated Code Metadata:
========================
Original URL: https://gala-games-official-k.blogspot.com
Prompt: "Generate code to calculate the total cost of a computer build with RTX3050 and GTX1630 graphics cards."
Generated: DETERMINISTIC_ebc175cab340e293
Batch ID: 20250622_212342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class GraphicsCard:
    """Class to represent a graphics card with a name and price."""
    
    def __init__(self, name: str, price: float):
        """Initialize the graphics card with a name and price."""
        self.name = name
        self.price = price

    def __str__(self):
        """Return a string representation of the graphics card."""
        return f"{self.name}: ${self.price:.2f}"


class ComputerBuild:
    """Class to represent a computer build with multiple graphics cards."""
    
    def __init__(self):
        """Initialize the computer build with an empty list of graphics cards."""
        self.graphics_cards = []

    def add_graphics_card(self, card: GraphicsCard):
        """Add a graphics card to the computer build."""
        if not isinstance(card, GraphicsCard):
            raise ValueError("Only instances of GraphicsCard can be added.")
        self.graphics_cards.append(card)

    def total_cost(self) -> float:
        """Calculate the total cost of the computer build."""
        total = sum(card.price for card in self.graphics_cards)
        return total

    def __str__(self):
        """Return a string representation of the computer build."""
        card_list = "\n".join(str(card) for card in self.graphics_cards)
        return f"Computer Build:\n{card_list}\nTotal Cost: ${self.total_cost():.2f}"


def main():
    """Main function to create a computer build and calculate its total cost."""
    try:
        # Create graphics card instances
        rtx_3050 = GraphicsCard("RTX 3050", 249.99)
        gtx_1630 = GraphicsCard("GTX 1630", 169.99)

        # Create a computer build and add graphics cards
        build = ComputerBuild()
        build.add_graphics_card(rtx_3050)
        build.add_graphics_card(gtx_1630)

        # Print the details of the computer build
        print(build)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
