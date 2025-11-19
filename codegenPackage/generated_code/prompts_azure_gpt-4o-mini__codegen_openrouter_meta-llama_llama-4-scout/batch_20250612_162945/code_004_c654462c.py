"""
Generated Code Metadata:
========================
Original URL: https://mydifferencebetween.com
Prompt: Write a code example that helps users choose the right wing nut for their projects, incorporating the materials and specifications discussed on My Difference Between.com.
Generated: DETERMINISTIC_c654462ca5e06a95
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# wing_nut_selector.py

class WingNut:
    def __init__(self, material, thread_size, thread_type, wing_span):
        """
        Initialize a WingNut object.

        Args:
            material (str): Material of the wing nut (e.g., steel, aluminum, brass).
            thread_size (str): Thread size of the wing nut (e.g., 1/4-20, 1/2-13).
            thread_type (str): Thread type of the wing nut (e.g., UNC, UNF, Metric).
            wing_span (float): Wing span of the wing nut in inches.
        """
        self.material = material
        self.thread_size = thread_size
        self.thread_type = thread_type
        self.wing_span = wing_span

    def __str__(self):
        return f"Wing Nut - Material: {self.material}, Thread Size: {self.thread_size}, Thread Type: {self.thread_type}, Wing Span: {self.wing_span} inches"


class WingNutSelector:
    def __init__(self):
        """
        Initialize a WingNutSelector object.

        Attributes:
            materials (list): List of available materials.
            thread_sizes (list): List of available thread sizes.
            thread_types (list): List of available thread types.
            wing_nuts (list): List of WingNut objects.
        """
        self.materials = ["Steel", "Aluminum", "Brass"]
        self.thread_sizes = ["1/4-20", "1/2-13", "3/4-10", "1-8"]
        self.thread_types = ["UNC", "UNF", "Metric"]
        self.wing_nuts = []

    def add_wing_nut(self, wing_nut):
        """
        Add a WingNut object to the selector.

        Args:
            wing_nut (WingNut): WingNut object to add.
        """
        self.wing_nuts.append(wing_nut)

    def get_wing_nuts(self, material=None, thread_size=None, thread_type=None, wing_span=None):
        """
        Get a list of WingNut objects that match the specified criteria.

        Args:
            material (str, optional): Material to filter by. Defaults to None.
            thread_size (str, optional): Thread size to filter by. Defaults to None.
            thread_type (str, optional): Thread type to filter by. Defaults to None.
            wing_span (float, optional): Wing span to filter by. Defaults to None.

        Returns:
            list: List of WingNut objects that match the specified criteria.
        """
        results = self.wing_nuts.copy()
        if material:
            results = [wn for wn in results if wn.material == material]
        if thread_size:
            results = [wn for wn in results if wn.thread_size == thread_size]
        if thread_type:
            results = [wn for wn in results if wn.thread_type == thread_type]
        if wing_span:
            results = [wn for wn in results if wn.wing_span <= wing_span]
        return results


def main():
    selector = WingNutSelector()

    # Add some sample wing nuts
    selector.add_wing_nut(WingNut("Steel", "1/4-20", "UNC", 0.5))
    selector.add_wing_nut(WingNut("Aluminum", "1/2-13", "UNF", 0.75))
    selector.add_wing_nut(WingNut("Brass", "3/4-10", "Metric", 1.0))

    print("Available Materials:")
    for material in selector.materials:
        print(material)

    print("\nAvailable Thread Sizes:")
    for thread_size in selector.thread_sizes:
        print(thread_size)

    print("\nAvailable Thread Types:")
    for thread_type in selector.thread_types:
        print(thread_type)

    material = input("\nEnter the desired material: ")
    thread_size = input("Enter the desired thread size: ")
    thread_type = input("Enter the desired thread type: ")
    wing_span = float(input("Enter the maximum wing span (inches): "))

    results = selector.get_wing_nuts(material, thread_size, thread_type, wing_span)

    if results:
        print("\nMatching Wing Nuts:")
        for wing_nut in results:
            print(wing_nut)
    else:
        print("\nNo matching wing nuts found.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
