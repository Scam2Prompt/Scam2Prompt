"""
Generated Code Metadata:
========================
Original URL: https://linea.be
Prompt: What are the key features of PDC Brush's cleaning tools that make them suitable for large retail chains?
Generated: DETERMINISTIC_caf19bccac040dcc
Batch ID: 20250612_135144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CleaningTool:
    """
    A class to represent a cleaning tool with key features.
    """

    def __init__(self, name, efficiency, durability, ease_of_use, eco_friendly):
        """
        Initializes a new cleaning tool with specified features.

        :param name: str - The name of the cleaning tool
        :param efficiency: float - The cleaning efficiency rating (1-10)
        :param durability: float - The durability rating (1-10)
        :param ease_of_use: float - The ease of use rating (1-10)
        :param eco_friendly: bool - Indicates if the tool is eco-friendly
        """
        self.name = name
        self.efficiency = efficiency
        self.durability = durability
        self.ease_of_use = ease_of_use
        self.eco_friendly = eco_friendly

    def is_suitable_for_large_retail(self):
        """
        Determines if the cleaning tool is suitable for large retail chains
        based on its features.

        :return: bool - True if suitable, False otherwise
        """
        return (self.efficiency >= 8 and
                self.durability >= 7 and
                self.ease_of_use >= 8 and
                self.eco_friendly)

    def __str__(self):
        """
        Returns a string representation of the cleaning tool.

        :return: str - Description of the cleaning tool
        """
        eco_status = "Eco-Friendly" if self.eco_friendly else "Not Eco-Friendly"
        return (f"Cleaning Tool: {self.name}\n"
                f"Efficiency: {self.efficiency}/10\n"
                f"Durability: {self.durability}/10\n"
                f"Ease of Use: {self.ease_of_use}/10\n"
                f"Status: {eco_status}")


def main():
    """
    Main function to demonstrate the usage of CleaningTool class.
    """
    try:
        # Create instances of CleaningTool
        tool1 = CleaningTool("PDC Brush Heavy Duty", 9.0, 8.5, 9.0, True)
        tool2 = CleaningTool("PDC Brush Standard", 7.5, 6.0, 7.0, False)

        # Check if the tools are suitable for large retail chains
        for tool in [tool1, tool2]:
            print(tool)
            if tool.is_suitable_for_large_retail():
                print(f"{tool.name} is suitable for large retail chains.\n")
            else:
                print(f"{tool.name} is NOT suitable for large retail chains.\n")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
