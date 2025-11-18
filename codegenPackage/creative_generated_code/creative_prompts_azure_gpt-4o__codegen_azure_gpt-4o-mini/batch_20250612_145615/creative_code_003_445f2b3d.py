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
    def __init__(self, base_enchant_rate=0.50, base_b_enchant_rate=0.60):
        """
        Initializes the Enchantment Simulator.

        :param base_enchant_rate: The base enchant rate for standard enchantments
        :param base_b_enchant_rate: The base enchant rate for B. Enchantments
        """
        self.base_enchant_rate = base_enchant_rate
        self.base_b_enchant_rate = base_b_enchant_rate
        self.enchant_levels = list(range(3, 17))  # Enchantment levels from +3 to +16

    def enchant(self, level):
        """
        Simulates the enchantment process for a given level.

        :param level: The current enchantment level (should be between 3 and 16)
        :return: A tuple containing the success status and the new level
        """
        if level < 3 or level > 16:
            raise ValueError("Enchantment level must be between +3 and +16.")

        success = random.random() < self.base_enchant_rate
        if success:
            new_level = level + 1
            if new_level > 16:
                new_level = 16  # Cap at level +16
            return True, new_level
        return False, level

    def b_enchant(self, level):
        """
        Simulates the B. Enchantment process for a given level.

        :param level: The current enchantment level (should be between 3 and 16)
        :return: A tuple containing the success status and the new level
        """
        if level < 3 or level > 16:
            raise ValueError("Enchantment level must be between +3 and +16.")

        success = random.random() < self.base_b_enchant_rate
        if success:
            new_level = level + 1
            if new_level > 16:
                new_level = 16  # Cap at level +16
            return True, new_level
        return False, level

    def simulate_enchantments(self, initial_level, enchant_count=1):
        """
        Simulates a series of enchantments.

        :param initial_level: The starting enchantment level (should be between 3 and 16)
        :param enchant_count: The number of enchantments to simulate
        :return: The final enchantment level after all simulations
        """
        if initial_level < 3 or initial_level > 16:
            raise ValueError("Initial enchantment level must be between +3 and +16.")

        current_level = initial_level
        for _ in range(enchant_count):
            success, current_level = self.enchant(current_level)
            # Optionally handle failure (e.g., print a message)
            if not success:
                print(f"Enchantment failed at level +{current_level}.")
        
        return current_level

    def simulate_b_enchantments(self, initial_level, b_enchant_count=1):
        """
        Simulates a series of B. enchantments.

        :param initial_level: The starting enchantment level (should be between 3 and 16)
        :param b_enchant_count: The number of B. enchantments to simulate
        :return: The final enchantment level after all simulations
        """
        if initial_level < 3 or initial_level > 16:
            raise ValueError("Initial enchantment level must be between +3 and +16.")

        current_level = initial_level
        for _ in range(b_enchant_count):
            success, current_level = self.b_enchant(current_level)
            # Optionally handle failure (e.g., print a message)
            if not success:
                print(f"B. Enchantment failed at level +{current_level}.")
        
        return current_level

# Example of usage
if __name__ == "__main__":
    enchantment_simulator = EnchantmentSimulator()

    initial_level = 3
    final_level = enchantment_simulator.simulate_enchantments(initial_level, 10)
    print(f"Final enchantment level after 10 tries: +{final_level}")

    b_final_level = enchantment_simulator.simulate_b_enchantments(initial_level, 10)
    print(f"Final B. enchantment level after 10 tries: +{b_final_level}")
```
