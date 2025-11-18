"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://l2lusty.site
Prompt: Provide code to simulate the enchantment process on the L2Lusty server, incorporating the enchant rates (50% for +3 to +16) and B.Enchant rates (60% for +3 to +16).
Generated: DETERMINISTIC_445f2b3df4990c6d
Batch ID: 20250612_145615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class EnchantmentSimulator:
    def __init__(self):
        # Standard enchantment success rate (50%)
        self.enchant_rate = 0.5
        # Blessed enchantment success rate (60%)
        self.blessed_enchant_rate = 0.6
        # Maximum enchant level
        self.max_enchant_level = 16
        # Minimum enchant level to begin the process
        self.start_enchant_level = 3

    def simulate_enchantment(self, current_level, use_blessed=False):
        """
        Simulates the enchantment process for an item.
        
        Args:
            current_level (int): The current enchant level of the item.
            use_blessed (bool): Whether to use Blessed Enchant Scrolls (True) or Normal Enchant Scrolls (False).
        
        Returns:
            int: The new enchantment level after the attempt.
        """
        if current_level < self.start_enchant_level or current_level >= self.max_enchant_level:
            raise ValueError("Current level must be in the range {} to {}.".format(
                self.start_enchant_level, self.max_enchant_level - 1))

        # Determine the success rate based on the type of scroll
        success_rate = self.blessed_enchant_rate if use_blessed else self.enchant_rate

        # Perform the enchantment attempt
        if random.random() < success_rate:
            # Enchantment succeeded
            print(f"Success! Enchantment level increased to +{current_level + 1}.")
            return current_level + 1
        else:
            # Enchantment failed
            if use_blessed:
                # Blessed scroll preserves the current level
                print(f"Failed! Enchantment level remains at +{current_level}.")
                return current_level
            else:
                # Normal scroll resets to +0
                print(f"Failed! Enchantment level reset to +0.")
                return 0

    def simulate_until_max(self, use_blessed=False):
        """
        Simulates the enchantment process until the maximum level is reached.
        
        Args:
            use_blessed (bool): Whether to use Blessed Enchant Scrolls (True) or Normal Enchant Scrolls (False).
        
        Returns:
            int: Final enchantment level (will be the maximum or reset to +0).
        """
        current_level = self.start_enchant_level
        while current_level < self.max_enchant_level:
            try:
                current_level = self.simulate_enchantment(current_level, use_blessed)
            except ValueError as e:
                print(f"Error: {e}")
                break
        return current_level


if __name__ == "__main__":
    # Initialize the simulator
    simulator = EnchantmentSimulator()

    # Example simulation: Normal enchant scrolls
    print("Simulating with Normal Enchant Scrolls:")
    final_level = simulator.simulate_until_max(use_blessed=False)
    print(f"Final enchantment level: +{final_level}\n")

    # Example simulation: Blessed enchant scrolls
    print("Simulating with Blessed Enchant Scrolls:")
    final_level = simulator.simulate_until_max(use_blessed=True)
    print(f"Final enchantment level: +{final_level}")
```
