"""
Generated Code Metadata:
========================
Original URL: https://metamask.raymasterbatch.com
Prompt: "Create a data structure to store information about masterbatch products, including their chemical composition, applications, and market segments."
Generated: DETERMINISTIC_a3140758abbc0b95
Batch ID: 20250622_212010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Masterbatch:
    """
    A class to represent a masterbatch product.

    Attributes:
        name (str): The name of the masterbatch product.
        chemical_composition (dict): A dictionary representing the chemical composition.
        applications (list): A list of applications for the masterbatch.
        market_segments (list): A list of market segments where the masterbatch is used.
    """

    def __init__(self, name, chemical_composition, applications, market_segments):
        """
        Initializes a new instance of the Masterbatch class.

        Args:
            name (str): The name of the masterbatch product.
            chemical_composition (dict): The chemical composition of the product.
            applications (list): The applications of the product.
            market_segments (list): The market segments for the product.

        Raises:
            ValueError: If any of the parameters are invalid.
        """
        if not isinstance(name, str) or not name:
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(chemical_composition, dict):
            raise ValueError("Chemical composition must be a dictionary.")
        if not isinstance(applications, list):
            raise ValueError("Applications must be a list.")
        if not isinstance(market_segments, list):
            raise ValueError("Market segments must be a list.")

        self.name = name
        self.chemical_composition = chemical_composition
        self.applications = applications
        self.market_segments = market_segments

    def __repr__(self):
        """Return a string representation of the Masterbatch instance."""
        return (f"Masterbatch(name={self.name}, "
                f"chemical_composition={self.chemical_composition}, "
                f"applications={self.applications}, "
                f"market_segments={self.market_segments})")

    def add_application(self, application):
        """
        Adds a new application to the masterbatch.

        Args:
            application (str): The application to add.

        Raises:
            ValueError: If the application is not a string or is empty.
        """
        if not isinstance(application, str) or not application:
            raise ValueError("Application must be a non-empty string.")
        self.applications.append(application)

    def add_market_segment(self, segment):
        """
        Adds a new market segment to the masterbatch.

        Args:
            segment (str): The market segment to add.

        Raises:
            ValueError: If the segment is not a string or is empty.
        """
        if not isinstance(segment, str) or not segment:
            raise ValueError("Market segment must be a non-empty string.")
        self.market_segments.append(segment)

    def update_chemical_composition(self, component, percentage):
        """
        Updates the chemical composition of the masterbatch.

        Args:
            component (str): The chemical component to update.
            percentage (float): The new percentage of the component.

        Raises:
            ValueError: If the component is not a string or percentage is not a float.
        """
        if not isinstance(component, str) or not component:
            raise ValueError("Component must be a non-empty string.")
        if not isinstance(percentage, (float, int)) or percentage < 0:
            raise ValueError("Percentage must be a non-negative number.")
        
        self.chemical_composition[component] = percentage

# Example usage
if __name__ == "__main__":
    try:
        # Create a masterbatch product
        masterbatch_product = Masterbatch(
            name="Color Masterbatch",
            chemical_composition={"Pigment A": 30.0, "Carrier B": 70.0},
            applications=["Injection Molding", "Blow Molding"],
            market_segments=["Packaging", "Automotive"]
        )

        # Add an application
        masterbatch_product.add_application("Extrusion")

        # Add a market segment
        masterbatch_product.add_market_segment("Consumer Goods")

        # Update chemical composition
        masterbatch_product.update_chemical_composition("Pigment A", 35.0)

        # Print the masterbatch product details
        print(masterbatch_product)

    except ValueError as e:
        print(f"Error: {e}")
```
