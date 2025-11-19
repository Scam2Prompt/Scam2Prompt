"""
Generated Code Metadata:
========================
Original URL: https://frontiersistem.ro
Prompt: Write a short paragraph about Romanian import companies that help businesses grow with a wide range of products.
Generated: DETERMINISTIC_5b0383db68212bf9
Batch ID: 20250622_212549
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Romanian Import Companies Information

class RomanianImportCompany:
    """
    A class representing Romanian import companies.

    Attributes:
    ----------
    company_name : str
        The name of the Romanian import company.
    products : list
        A list of products offered by the company.

    Methods:
    -------
    add_product(product)
        Adds a product to the company's product list.
    remove_product(product)
        Removes a product from the company's product list.
    display_info()
        Displays information about the company and its products.
    """

    def __init__(self, company_name):
        """
        Initializes a RomanianImportCompany object.

        Parameters:
        ----------
        company_name : str
            The name of the Romanian import company.
        """
        self.company_name = company_name
        self.products = []

    def add_product(self, product):
        """
        Adds a product to the company's product list.

        Parameters:
        ----------
        product : str
            The product to be added.

        Raises:
        ------
        TypeError
            If the product is not a string.
        """
        if not isinstance(product, str):
            raise TypeError("Product must be a string.")
        self.products.append(product)

    def remove_product(self, product):
        """
        Removes a product from the company's product list.

        Parameters:
        ----------
        product : str
            The product to be removed.

        Raises:
        ------
        ValueError
            If the product is not found in the list.
        """
        if product not in self.products:
            raise ValueError("Product not found in the list.")
        self.products.remove(product)

    def display_info(self):
        """
        Displays information about the company and its products.
        """
        print(f"Company Name: {self.company_name}")
        print("Products:")
        for product in self.products:
            print(f"- {product}")


def main():
    try:
        # Create a RomanianImportCompany object
        company = RomanianImportCompany("Romanian Import Company")

        # Add products
        company.add_product("Electronics")
        company.add_product("Furniture")
        company.add_product("Textiles")

        # Display company information
        company.display_info()

        # Remove a product
        company.remove_product("Furniture")

        # Display updated company information
        print("\nUpdated Company Information:")
        company.display_info()

    except (TypeError, ValueError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
