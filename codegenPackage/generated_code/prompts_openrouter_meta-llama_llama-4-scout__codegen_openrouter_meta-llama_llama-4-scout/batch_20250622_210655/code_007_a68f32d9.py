"""
Generated Code Metadata:
========================
Original URL: https://bolle.com.co
Prompt: Design a product configurator for Bollé's sports eyewear products, allowing customers to customize their gear with different lens technologies and frame styles.
Generated: DETERMINISTIC_a68f32d9f5476fa9
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import List, Dict

# Define an Enum for lens technologies
class LensTechnology(Enum):
    """Enum for lens technologies"""
    PHOTOCHROMIC = "Photochromic"
    POLARIZED = "Polarized"
    MIRROR_COATED = "Mirror Coated"
    BASE = "Base"

# Define an Enum for frame styles
class FrameStyle(Enum):
    """Enum for frame styles"""
    SLEEK = "Sleek"
    SPORTY = "Sporty"
    CLASSIC = "Classic"

# Define a class for Lens
class Lens:
    """Class representing a lens"""
    def __init__(self, technology: LensTechnology, color: str, price: float):
        """
        Initialize a Lens object

        Args:
        technology (LensTechnology): The lens technology
        color (str): The lens color
        price (float): The lens price
        """
        self.technology = technology
        self.color = color
        self.price = price

# Define a class for Frame
class Frame:
    """Class representing a frame"""
    def __init__(self, style: FrameStyle, color: str, price: float):
        """
        Initialize a Frame object

        Args:
        style (FrameStyle): The frame style
        color (str): The frame color
        price (float): The frame price
        """
        self.style = style
        self.color = color
        self.price = price

# Define a class for EyewearProduct
class EyewearProduct:
    """Class representing an eyewear product"""
    def __init__(self, name: str, frame: Frame, lens: Lens):
        """
        Initialize an EyewearProduct object

        Args:
        name (str): The product name
        frame (Frame): The frame
        lens (Lens): The lens
        """
        self.name = name
        self.frame = frame
        self.lens = lens

    def calculate_price(self) -> float:
        """
        Calculate the total price of the eyewear product

        Returns:
        float: The total price
        """
        return self.frame.price + self.lens.price

    def __str__(self):
        return f"{self.name} - Frame: {self.frame.style.value} {self.frame.color}, Lens: {self.lens.technology.value} {self.lens.color}"

# Define a class for ProductConfigurator
class ProductConfigurator:
    """Class representing a product configurator"""
    def __init__(self):
        self.lenses: List[Lens] = []
        self.frames: List[Frame] = []
        self.products: Dict[str, EyewearProduct] = {}

    def add_lens(self, lens: Lens):
        """
        Add a lens to the configurator

        Args:
        lens (Lens): The lens to add
        """
        self.lenses.append(lens)

    def add_frame(self, frame: Frame):
        """
        Add a frame to the configurator

        Args:
        frame (Frame): The frame to add
        """
        self.frames.append(frame)

    def create_product(self, name: str, frame_style: FrameStyle, lens_technology: LensTechnology):
        """
        Create a new eyewear product

        Args:
        name (str): The product name
        frame_style (FrameStyle): The frame style
        lens_technology (LensTechnology): The lens technology

        Returns:
        EyewearProduct: The created product or None if not found
        """
        frame = next((f for f in self.frames if f.style == frame_style), None)
        lens = next((l for l in self.lenses if l.technology == lens_technology), None)

        if frame and lens:
            product = EyewearProduct(name, frame, lens)
            self.products[name] = product
            return product
        else:
            return None

    def get_product(self, name: str) -> EyewearProduct:
        """
        Get a product by name

        Args:
        name (str): The product name

        Returns:
        EyewearProduct: The product or None if not found
        """
        return self.products.get(name)

def main():
    configurator = ProductConfigurator()

    # Add lenses
    configurator.add_lens(Lens(LensTechnology.PHOTOCHROMIC, "Gray", 100.0))
    configurator.add_lens(Lens(LensTechnology.POLARIZED, "Brown", 150.0))
    configurator.add_lens(Lens(LensTechnology.MIRROR_COATED, "Blue", 200.0))

    # Add frames
    configurator.add_frame(Frame(FrameStyle.SLEEK, "Black", 50.0))
    configurator.add_frame(Frame(FrameStyle.SPORTY, "Red", 75.0))
    configurator.add_frame(Frame(FrameStyle.CLASSIC, "White", 40.0))

    # Create products
    product1 = configurator.create_product("Bollé 1", FrameStyle.SLEEK, LensTechnology.PHOTOCHROMIC)
    product2 = configurator.create_product("Bollé 2", FrameStyle.SPORTY, LensTechnology.POLARIZED)

    # Print products
    if product1:
        print(product1)
        print(f"Price: ${product1.calculate_price():.2f}")
    else:
        print("Product not found")

    if product2:
        print(product2)
        print(f"Price: ${product2.calculate_price():.2f}")
    else:
        print("Product not found")

if __name__ == "__main__":
    main()
```
