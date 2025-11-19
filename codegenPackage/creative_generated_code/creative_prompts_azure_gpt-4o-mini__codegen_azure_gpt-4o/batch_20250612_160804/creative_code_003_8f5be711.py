"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://meatmaster.pe
Prompt: Develop a script that filters "Cajas Chinas" by size and material, using the unique features listed on the Meat Master site.
Generated: DETERMINISTIC_8f5be7111f36f69a
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

# Define a class for the Caja China
class CajaChina:
    def __init__(self, name, size, material, features):
        """
        Initializes a Caja China object.

        :param name: Name of the Caja China.
        :param size: Size of the Caja China (e.g., 'small', 'medium', 'large').
        :param material: Material of the Caja China (e.g., 'wood', 'metal').
        :param features: List of unique features of the Caja China.
        """
        self.name = name
        self.size = size
        self.material = material
        self.features = features

    def __repr__(self):
        """
        String representation of the Caja China object.
        """
        return f"CajaChina(name={self.name}, size={self.size}, material={self.material}, features={self.features})"


def filter_cajas_chinas(cajas, size=None, material=None):
    """
    Filters the list of Cajas Chinas based on size and material.

    :param cajas: List of Caja China objects.
    :param size: Desired size to filter by (e.g., 'small', 'medium', 'large'). Default is None.
    :param material: Desired material to filter by (e.g., 'wood', 'metal'). Default is None.
    :return: Filtered list of Caja China objects.
    """
    try:
        filtered = [
            caja for caja in cajas
            if (size is None or caja.size.lower() == size.lower()) and
               (material is None or caja.material.lower() == material.lower())
        ]
        return filtered
    except AttributeError as e:
        raise ValueError("Invalid attributes provided for filtering") from e


def main():
    """
    Main function to demonstrate the filtering of Cajas Chinas.
    """
    # Sample data (replace with actual data from the Meat Master site)
    sample_data = [
        {"name": "Caja China Pro", "size": "large", "material": "metal", "features": ["durable", "easy to clean"]},
        {"name": "Caja China Classic", "size": "medium", "material": "wood", "features": ["traditional look", "lightweight"]},
        {"name": "Caja China Mini", "size": "small", "material": "metal", "features": ["portable", "compact"]},
        {"name": "Caja China XL", "size": "large", "material": "wood", "features": ["spacious", "high capacity"]}
    ]

    # Convert sample data to Caja China objects
    cajas = [CajaChina(**item) for item in sample_data]

    print("All Cajas Chinas:")
    print(cajas)

    # Filter by size and material
    filtered_cajas = filter_cajas_chinas(cajas, size="large", material="wood")

    print("\nFiltered Cajas Chinas (size='large', material='wood'):")
    print(filtered_cajas)


# Entry point for the script
if __name__ == "__main__":
    main()
```
