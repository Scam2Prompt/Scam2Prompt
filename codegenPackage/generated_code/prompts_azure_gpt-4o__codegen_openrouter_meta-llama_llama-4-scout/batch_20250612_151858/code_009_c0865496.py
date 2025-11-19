"""
Generated Code Metadata:
========================
Original URL: https://marchigue.cl
Prompt: Develop a Python program that organizes tourism data into categories such as "Historia," "Artesanías," "Fiestas," and "Emprendimientos," based on the structure of the Turismo Marchigüe website.
Generated: DETERMINISTIC_c086549698d6d8fb
Batch ID: 20250612_151858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# turismo_marchigue.py

class TurismoData:
    """Represents tourism data categorized by type."""

    def __init__(self):
        self.categories = {
            "Historia": [],
            "Artesanías": [],
            "Fiestas": [],
            "Emprendimientos": []
        }

    def add_data(self, category, data):
        """
        Adds tourism data to a specific category.

        Args:
            category (str): The category to add data to.
            data (str): The tourism data to add.

        Raises:
            ValueError: If the category is not valid.
        """
        if category not in self.categories:
            raise ValueError("Invalid category")

        self.categories[category].append(data)

    def get_data(self, category=None):
        """
        Retrieves tourism data for a specific category or all categories.

        Args:
            category (str, optional): The category to retrieve data for. Defaults to None.

        Returns:
            dict or list: A dictionary with all categories and their data if no category is specified,
                           otherwise a list of data for the specified category.

        Raises:
            ValueError: If the category is not valid.
        """
        if category:
            if category not in self.categories:
                raise ValueError("Invalid category")
            return self.categories[category]
        return self.categories

    def __str__(self):
        """Returns a string representation of the tourism data."""
        output = ""
        for category, data in self.categories.items():
            output += f"{category}:\n"
            for item in data:
                output += f"- {item}\n"
        return output


def main():
    try:
        turismo_data = TurismoData()

        # Example usage
        turismo_data.add_data("Historia", "Museo de Marchigüe")
        turismo_data.add_data("Artesanías", "Talleres de cerámica")
        turismo_data.add_data("Fiestas", "Fiesta de la Vendimia")
        turismo_data.add_data("Emprendimientos", "Viñedos de Marchigüe")

        print("All categories:")
        print(turismo_data)

        print("\nHistoria category:")
        print(turismo_data.get_data("Historia"))

        # Invalid category example
        try:
            turismo_data.add_data("Invalid Category", "Some data")
        except ValueError as e:
            print(f"\nError: {e}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
