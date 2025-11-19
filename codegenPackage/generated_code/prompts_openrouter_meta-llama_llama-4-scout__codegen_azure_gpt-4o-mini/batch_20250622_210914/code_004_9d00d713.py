"""
Generated Code Metadata:
========================
Original URL: https://realis.pages.dev
Prompt: Develop a function to calculate the rarity of a Meowgon creature based on its elements and the provided drop rates (e.g., Supreme: 0.137%, Legendary: 1.235%, etc.).
Generated: DETERMINISTIC_9d00d7138c4959a6
Batch ID: 20250622_210914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class MeowgonRarityCalculator:
    """
    A class to calculate the rarity of a Meowgon creature based on its elements and drop rates.
    """

    def __init__(self, drop_rates):
        """
        Initializes the MeowgonRarityCalculator with the provided drop rates.

        :param drop_rates: A dictionary containing the rarity names as keys and their drop rates as values.
        """
        self.drop_rates = drop_rates

    def calculate_rarity(self, element):
        """
        Calculates the rarity of a Meowgon creature based on its element.

        :param element: The element of the Meowgon creature (e.g., 'Supreme', 'Legendary').
        :return: The rarity percentage as a float.
        :raises ValueError: If the element is not found in the drop rates.
        """
        try:
            # Retrieve the drop rate for the specified element
            drop_rate_str = self.drop_rates[element]
            # Convert the drop rate from string percentage to float
            drop_rate = float(drop_rate_str.strip('%')) / 100
            return drop_rate
        except KeyError:
            raise ValueError(f"Element '{element}' not found in drop rates.")
        except ValueError:
            raise ValueError(f"Invalid drop rate format for element '{element}': {drop_rate_str}")

# Example usage
if __name__ == "__main__":
    # Define drop rates for different Meowgon rarities
    drop_rates = {
        'Supreme': '0.137%',
        'Legendary': '1.235%',
        'Rare': '5.000%',
        'Common': '20.000%'
    }

    # Create an instance of the rarity calculator
    rarity_calculator = MeowgonRarityCalculator(drop_rates)

    # Calculate and print the rarity for a specific element
    try:
        element = 'Legendary'
        rarity = rarity_calculator.calculate_rarity(element)
        print(f"The rarity of '{element}' Meowgon is: {rarity:.6f}")
    except ValueError as e:
        print(e)
```
