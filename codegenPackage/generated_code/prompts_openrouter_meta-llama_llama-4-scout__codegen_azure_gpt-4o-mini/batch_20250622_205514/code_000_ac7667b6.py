"""
Generated Code Metadata:
========================
Original URL: https://zentocosmetic.com
Prompt: Write a product description for a hair volume shampoo that contains natural oil complex and provides a protective layer for hair, similar to ZENTO VOLUME ŞAMPUAN.
Generated: DETERMINISTIC_ac7667b62f7bdf5b
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class HairVolumeShampoo:
    """
    A class to represent a hair volume shampoo product.

    Attributes:
        name (str): The name of the shampoo.
        natural_oil_complex (bool): Indicates if the shampoo contains a natural oil complex.
        protective_layer (bool): Indicates if the shampoo provides a protective layer for hair.
        volume_boost (bool): Indicates if the shampoo boosts hair volume.
    """

    def __init__(self, name: str, natural_oil_complex: bool, protective_layer: bool, volume_boost: bool):
        """
        Initializes the HairVolumeShampoo with the given attributes.

        Args:
            name (str): The name of the shampoo.
            natural_oil_complex (bool): Indicates if the shampoo contains a natural oil complex.
            protective_layer (bool): Indicates if the shampoo provides a protective layer for hair.
            volume_boost (bool): Indicates if the shampoo boosts hair volume.
        """
        self.name = name
        self.natural_oil_complex = natural_oil_complex
        self.protective_layer = protective_layer
        self.volume_boost = volume_boost

    def get_description(self) -> str:
        """
        Generates a product description for the shampoo.

        Returns:
            str: A description of the shampoo.
        """
        try:
            description = f"{self.name} is a premium hair volume shampoo designed to enhance your hair's natural beauty. "
            if self.natural_oil_complex:
                description += "Infused with a natural oil complex, it nourishes and revitalizes your hair. "
            if self.protective_layer:
                description += "It forms a protective layer around each strand, shielding your hair from damage. "
            if self.volume_boost:
                description += "Experience fuller, thicker hair with every wash, as it effectively boosts volume. "
            description += "Transform your hair care routine with this luxurious shampoo."
            return description
        except Exception as e:
            return f"An error occurred while generating the description: {str(e)}"

# Example usage
if __name__ == "__main__":
    try:
        shampoo = HairVolumeShampoo(
            name="ZENTO VOLUME ŞAMPUAN",
            natural_oil_complex=True,
            protective_layer=True,
            volume_boost=True
        )
        print(shampoo.get_description())
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
