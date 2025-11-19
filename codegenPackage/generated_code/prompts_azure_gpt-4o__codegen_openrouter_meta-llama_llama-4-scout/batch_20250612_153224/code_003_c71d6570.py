"""
Generated Code Metadata:
========================
Original URL: https://nuevaciudad.com.co
Prompt: Generate a Python script to query and filter properties by type, neighborhood, and price range, mimicking the search functionality described in the "Buscar Propietarios Arrendatarios Consignación" section of the Nueva Ciudad website.
Generated: DETERMINISTIC_c71d6570b4187352
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# properties.py

class Property:
    def __init__(self, id, type, neighborhood, price):
        """
        Initialize a Property object.

        Args:
            id (int): Unique identifier for the property.
            type (str): Type of property (e.g., apartment, house).
            neighborhood (str): Neighborhood where the property is located.
            price (float): Price of the property.
        """
        self.id = id
        self.type = type
        self.neighborhood = neighborhood
        self.price = price

    def __repr__(self):
        return f"Property(id={self.id}, type='{self.type}', neighborhood='{self.neighborhood}', price={self.price})"


class PropertyDatabase:
    def __init__(self):
        """
        Initialize an in-memory property database.
        """
        self.properties = []

    def add_property(self, property):
        """
        Add a property to the database.

        Args:
            property (Property): Property object to add.
        """
        self.properties.append(property)

    def query_properties(self, type=None, neighborhood=None, min_price=None, max_price=None):
        """
        Query properties based on filters.

        Args:
            type (str, optional): Filter by property type. Defaults to None.
            neighborhood (str, optional): Filter by neighborhood. Defaults to None.
            min_price (float, optional): Minimum price filter. Defaults to None.
            max_price (float, optional): Maximum price filter. Defaults to None.

        Returns:
            list[Property]: List of filtered properties.
        """
        filtered_properties = self.properties.copy()

        if type:
            filtered_properties = [p for p in filtered_properties if p.type.lower() == type.lower()]
        if neighborhood:
            filtered_properties = [p for p in filtered_properties if p.neighborhood.lower() == neighborhood.lower()]
        if min_price:
            filtered_properties = [p for p in filtered_properties if p.price >= min_price]
        if max_price:
            filtered_properties = [p for p in filtered_properties if p.price <= max_price]

        return filtered_properties


def main():
    # Create a sample property database
    db = PropertyDatabase()

    # Add some sample properties
    db.add_property(Property(1, "Apartment", "Centro", 100000))
    db.add_property(Property(2, "House", "Centro", 200000))
    db.add_property(Property(3, "Apartment", "La Aurora", 80000))
    db.add_property(Property(4, "House", "La Aurora", 300000))

    try:
        # Query properties
        type_filter = "Apartment"
        neighborhood_filter = "Centro"
        min_price_filter = 50000
        max_price_filter = 150000

        filtered_properties = db.query_properties(
            type=type_filter,
            neighborhood=neighborhood_filter,
            min_price=min_price_filter,
            max_price=max_price_filter,
        )

        print("Filtered Properties:")
        for prop in filtered_properties:
            print(prop)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
