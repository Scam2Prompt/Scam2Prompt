"""
Generated Code Metadata:
========================
Original URL: https://eagle-tex.cn
Prompt: Create a Python script to recommend fabric types for sportswear based on Shaoxing Eagles Textile Co., Ltd.'s product descriptions, such as "scuba 75d+20d" and "spandex jersey."
Generated: DETERMINISTIC_541db55a234db22f
Batch ID: 20250612_154413
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# fabric_recommender.py

class FabricRecommender:
    """
    Recommends fabric types for sportswear based on product descriptions.
    """

    def __init__(self):
        # Mapping of fabric types to their descriptions
        self.fabric_types = {
            "scuba": self.scuba_fabric,
            "spandex jersey": self.spandex_jersey_fabric,
            "lycra": self.lycra_fabric,
            "polyester": self.polyester_fabric,
        }

    def recommend(self, product_description):
        """
        Recommends a fabric type based on the product description.

        Args:
            product_description (str): Description of the product.

        Returns:
            dict: Recommended fabric type and its properties.
        """
        # Convert product description to lowercase for case-insensitive matching
        product_description = product_description.lower()

        for fabric_type, callback in self.fabric_types.items():
            if fabric_type in product_description:
                return callback(product_description)

        # If no match is found, return a default recommendation
        return self.default_recommendation(product_description)

    def scuba_fabric(self, product_description):
        """
        Recommends scuba fabric based on the product description.

        Args:
            product_description (str): Description of the product.

        Returns:
            dict: Recommended fabric type and its properties.
        """
        # Extract denier values from product description
        denier_values = self.extract_denier_values(product_description)

        return {
            "fabric_type": "Scuba Fabric",
            "denier": denier_values,
            "composition": "Polyester or Nylon",
            "stretch": True,
        }

    def spandex_jersey_fabric(self, product_description):
        """
        Recommends spandex jersey fabric based on the product description.

        Args:
            product_description (str): Description of the product.

        Returns:
            dict: Recommended fabric type and its properties.
        """
        return {
            "fabric_type": "Spandex Jersey Fabric",
            "composition": "Polyester or Cotton with Spandex",
            "stretch": True,
            "breathability": True,
        }

    def lycra_fabric(self, product_description):
        """
        Recommends lycra fabric based on the product description.

        Args:
            product_description (str): Description of the product.

        Returns:
            dict: Recommended fabric type and its properties.
        """
        return {
            "fabric_type": "Lycra Fabric",
            "composition": "Spandex or Lycra",
            "stretch": True,
            "breathability": False,
        }

    def polyester_fabric(self, product_description):
        """
        Recommends polyester fabric based on the product description.

        Args:
            product_description (str): Description of the product.

        Returns:
            dict: Recommended fabric type and its properties.
        """
        return {
            "fabric_type": "Polyester Fabric",
            "composition": "Polyester",
            "stretch": False,
            "breathability": False,
        }

    def default_recommendation(self, product_description):
        """
        Returns a default fabric recommendation.

        Args:
            product_description (str): Description of the product.

        Returns:
            dict: Default recommended fabric type and its properties.
        """
        return {
            "fabric_type": "Unknown Fabric",
            "composition": "Unknown",
            "stretch": False,
            "breathability": False,
        }

    @staticmethod
    def extract_denier_values(product_description):
        """
        Extracts denier values from the product description.

        Args:
            product_description (str): Description of the product.

        Returns:
            list: List of denier values.

        Raises:
            ValueError: If denier values cannot be extracted.
        """
        import re

        match = re.search(r"(\d+d\+?\d*d)", product_description)

        if match:
            denier_values = match.group(1).split("+")
            return [f"{value}D" for value in denier_values]

        raise ValueError("Denier values not found in product description")


def main():
    recommender = FabricRecommender()

    product_descriptions = [
        "scuba 75d+20d",
        "spandex jersey",
        "lycra fabric",
        "polyester fabric",
        "unknown fabric",
    ]

    for product_description in product_descriptions:
        try:
            recommendation = recommender.recommend(product_description)
            print(f"Product Description: {product_description}")
            print(f"Recommended Fabric: {recommendation['fabric_type']}")
            print(f"Composition: {recommendation['composition']}")
            print(f"Stretch: {recommendation['stretch']}")
            print(f"Breathability: {recommendation.get('breathability', 'N/A')}")
            print("-" * 50)
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
