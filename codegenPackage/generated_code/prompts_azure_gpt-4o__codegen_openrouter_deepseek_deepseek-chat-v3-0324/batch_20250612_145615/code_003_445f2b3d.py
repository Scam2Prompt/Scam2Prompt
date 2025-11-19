"""
Generated Code Metadata:
========================
Original URL: https://l2lusty.site
Prompt: Provide code to simulate the enchantment process on the L2Lusty server, incorporating the enchant rates (50% for +3 to +16) and B.Enchant rates (60% for +3 to +16).
Generated: DETERMINISTIC_445f2b3df4990c6d
Batch ID: 20250612_145615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class EnchantmentSimulator:
    """
    Simulates the enchantment process for L2Lusty server.
    Handles both regular and B.Enchant rates.
    """
    
    def __init__(self):
        self.regular_success_rate = 0.5  # 50% success rate for regular enchant
        self.blessed_success_rate = 0.6  # 60% success rate for B.Enchant
        
    def regular_enchant(self, current_level):
        """
        Simulates a regular enchant attempt.
        Returns True if successful, False if failed.
        Valid for +3 to +16 only.
        """
        if current_level < 3 or current_level > 15:
            raise ValueError("Regular enchant only valid for +3 to +16 (current +15)")
        
        return random.random() < self.regular_success_rate
    
    def blessed_enchant(self, current_level):
        """
        Simulates a B.Enchant attempt.
        Returns True if successful, False if failed.
        Valid for +3 to +16 only.
        """
        if current_level < 3 or current_level > 15:
            raise ValueError("B.Enchant only valid for +3 to +16 (current +15)")
        
        return random.random() < self.blessed_success_rate
    
    def simulate_enchantment(self, start_level, target_level, use_blessed=False):
        """
        Simulates full enchantment process from start_level to target_level.
        Returns the final achieved level and enchantment history.
        """
        if start_level < 3 or start_level > 16:
            raise ValueError("Start level must be between +3 and +16")
        if target_level < 3 or target_level > 16:
            raise ValueError("Target level must be between +3 and +16")
        if start_level >= target_level:
            raise ValueError("Start level must be lower than target level")
        
        current_level = start_level
        history = []
        
        while current_level < target_level:
            try:
                if use_blessed:
                    success = self.blessed_enchant(current_level)
                else:
                    success = self.regular_enchant(current_level)
                
                if success:
                    current_level += 1
                    history.append((current_level, "Success"))
                else:
                    current_level -= 1
                    history.append((current_level, "Fail"))
                    
                # Ensure we don't go below +3
                if current_level < 3:
                    current_level = 3
                    
            except Exception as e:
                print(f"Error during enchantment: {e}")
                break
        
        return current_level, history

# Example usage
if __name__ == "__main__":
    simulator = EnchantmentSimulator()
    
    # Simulate regular enchant from +3 to +10
    final_level, history = simulator.simulate_enchantment(3, 10)
    print(f"Regular enchant result: +{final_level}")
    print("History:", history)
    
    # Simulate B.Enchant from +3 to +10
    final_level, history = simulator.simulate_enchantment(3, 10, use_blessed=True)
    print(f"B.Enchant result: +{final_level}")
    print("History:", history)
```
