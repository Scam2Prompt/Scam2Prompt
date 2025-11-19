"""
Generated Code Metadata:
========================
Original URL: https://metamask.raymasterbatch.com
Prompt: "Develop a simple algorithm to determine the compatibility of different masterbatches with specific polymers, such as PVC or EVA."
Generated: DETERMINISTIC_a2ebff428b8a9e14
Batch ID: 20250622_212010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class PolymerCompatibility:
    """
    A class to determine the compatibility of different masterbatches with specific polymers.
    """

    def __init__(self):
        # Define compatibility mapping for masterbatches and polymers
        self.compatibility_map = {
            'PVC': ['Masterbatch_A', 'Masterbatch_B', 'Masterbatch_C'],
            'EVA': ['Masterbatch_B', 'Masterbatch_D'],
            'PE': ['Masterbatch_A', 'Masterbatch_E'],
            # Add more polymers and their compatible masterbatches as needed
        }

    def check_compatibility(self, polymer, masterbatch):
        """
        Check if a given masterbatch is compatible with a specified polymer.

        :param polymer: The polymer to check compatibility for (str).
        :param masterbatch: The masterbatch to check compatibility with (str).
        :return: True if compatible, False otherwise.
        """
        try:
            # Validate input types
            if not isinstance(polymer, str) or not isinstance(masterbatch, str):
                raise ValueError("Both polymer and masterbatch must be strings.")

            # Check if the polymer exists in the compatibility map
            if polymer not in self.compatibility_map:
                raise KeyError(f"Polymer '{polymer}' not found in compatibility map.")

            # Check compatibility
            is_compatible = masterbatch in self.compatibility_map[polymer]
            return is_compatible

        except (ValueError, KeyError) as e:
            print(f"Error: {e}")
            return False

    def get_compatible_masterbatches(self, polymer):
        """
        Get a list of compatible masterbatches for a specified polymer.

        :param polymer: The polymer to get compatible masterbatches for (str).
        :return: List of compatible masterbatches or an error message.
        """
        try:
            # Validate input type
            if not isinstance(polymer, str):
                raise ValueError("Polymer must be a string.")

            # Check if the polymer exists in the compatibility map
            if polymer not in self.compatibility_map:
                raise KeyError(f"Polymer '{polymer}' not found in compatibility map.")

            # Return the list of compatible masterbatches
            return self.compatibility_map[polymer]

        except (ValueError, KeyError) as e:
            print(f"Error: {e}")
            return []

# Example usage
if __name__ == "__main__":
    compatibility_checker = PolymerCompatibility()

    # Check compatibility
    polymer_to_check = 'PVC'
    masterbatch_to_check = 'Masterbatch_A'
    is_compatible = compatibility_checker.check_compatibility(polymer_to_check, masterbatch_to_check)
    print(f"Is '{masterbatch_to_check}' compatible with '{polymer_to_check}'? {is_compatible}")

    # Get compatible masterbatches
    polymer_to_query = 'EVA'
    compatible_masterbatches = compatibility_checker.get_compatible_masterbatches(polymer_to_query)
    print(f"Compatible masterbatches for '{polymer_to_query}': {compatible_masterbatches}")
```
