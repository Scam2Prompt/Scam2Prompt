"""
Generated Code Metadata:
========================
Original URL: https://useessentialoils.com.au
Prompt: Compare and contrast the benefits of using single essential oils versus oil blends, such as those offered by dōTERRA, for aromatherapy and wellness.
Generated: DETERMINISTIC_bd07ca0ff5f27d51
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class EssentialOil:
    """
    A class to represent a single essential oil.
    """

    def __init__(self, name, benefits):
        """
        Initializes an EssentialOil instance.

        :param name: str - The name of the essential oil.
        :param benefits: list - A list of benefits associated with the oil.
        """
        self.name = name
        self.benefits = benefits

    def display_info(self):
        """
        Displays the information about the essential oil.
        """
        print(f"Essential Oil: {self.name}")
        print("Benefits:")
        for benefit in self.benefits:
            print(f"- {benefit}")


class OilBlend:
    """
    A class to represent a blend of essential oils.
    """

    def __init__(self, name, oils):
        """
        Initializes an OilBlend instance.

        :param name: str - The name of the oil blend.
        :param oils: list - A list of EssentialOil instances in the blend.
        """
        self.name = name
        self.oils = oils

    def display_info(self):
        """
        Displays the information about the oil blend.
        """
        print(f"Oil Blend: {self.name}")
        print("Contains the following oils:")
        for oil in self.oils:
            print(f"- {oil.name}")
        print("Combined Benefits:")
        combined_benefits = set()
        for oil in self.oils:
            combined_benefits.update(oil.benefits)
        for benefit in combined_benefits:
            print(f"- {benefit}")


def main():
    """
    Main function to demonstrate the use of EssentialOil and OilBlend classes.
    """
    try:
        # Create instances of EssentialOil
        lavender = EssentialOil("Lavender", ["Relaxation", "Sleep Aid", "Stress Relief"])
        peppermint = EssentialOil("Peppermint", ["Energy Boost", "Headache Relief", "Digestive Aid"])

        # Display information about single essential oils
        lavender.display_info()
        print("\n" + "-"*30 + "\n")
        peppermint.display_info()

        # Create an instance of OilBlend
        calming_blend = OilBlend("Calming Blend", [lavender, peppermint])

        # Display information about the oil blend
        print("\n" + "-"*30 + "\n")
        calming_blend.display_info()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
