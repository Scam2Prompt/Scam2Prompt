"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://simemes.vercel.app
Prompt: Write a Python script to simulate the resource collection and leveling-up mechanics described in the SIMemes game, specifically focusing on collecting "poop" as currency and defending resources.
Generated: DETERMINISTIC_91e72474e438dabe
Batch ID: 20250612_155042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time

class ResourceCollector:
    """
    A class to simulate resource collection and leveling mechanics in the SIMemes game.
    """

    def __init__(self):
        self.poop = 0  # Currency in the form of poop
        self.level = 1  # Starting level
        self.collect_rate = 1  # Amount of poop collected per second
        self.defense_strength = 0  # Initial defense strength
        self.is_defended = False  # Defense state

    def collect_resources(self):
        """
        Simulates the collection of resources (poop) over time.
        """
        try:
            while True:
                self.poop += self.collect_rate
                print(f"Collected {self.collect_rate} poop. Total: {self.poop} poop.")
                time.sleep(1)  # Wait for 1 second before collecting again
        except KeyboardInterrupt:
            print("\nResource collection stopped.")

    def level_up(self):
        """
        Levels up the collector, increasing the collection rate and defense strength.
        """
        if self.poop >= 10 * self.level:  # Cost to level up
            self.poop -= 10 * self.level
            self.level += 1
            self.collect_rate += 1  # Increase collection rate
            self.defense_strength += 5  # Increase defense strength
            print(f"Leveled up to Level {self.level}! Collection rate: {self.collect_rate}, Defense strength: {self.defense_strength}.")
        else:
            print(f"Not enough poop to level up. You need {10 * self.level - self.poop} more poop.")

    def defend_resources(self):
        """
        Activates defense mode to protect resources from being stolen.
        """
        if not self.is_defended:
            self.is_defended = True
            print("Defense mode activated!")
        else:
            print("Defense mode is already active.")

    def enemy_attack(self):
        """
        Simulates an enemy attack. Resources can be stolen if not defended.
        """
        if not self.is_defended:
            stolen_amount = random.randint(1, 5)
            if self.poop >= stolen_amount:
                self.poop -= stolen_amount
                print(f"Enemy stole {stolen_amount} poop! Remaining poop: {self.poop}.")
            else:
                print("Enemy tried to steal poop, but you don't have enough!")
        else:
            print("Your resources are safe! Enemy cannot steal while defended.")

def main():
    """
    Main function to run the resource collection simulation.
    """
    collector = ResourceCollector()

    # Start resource collection in a separate thread
    import threading
    collection_thread = threading.Thread(target=collector.collect_resources)
    collection_thread.start()

    # Simulation loop for leveling up and defending
    try:
        while True:
            action = input("Enter 'level up' to level up, 'defend' to activate defense, or 'exit' to quit: ").strip().lower()
            if action == 'level up':
                collector.level_up()
            elif action == 'defend':
                collector.defend_resources()
            elif action == 'exit':
                print("Exiting the simulation.")
                break
            else:
                print("Invalid action. Please try again.")
            
            # Random enemy attack every 5 seconds
            if random.random() < 0.2:  # 20% chance
                collector.enemy_attack()

    except KeyboardInterrupt:
        print("\nSimulation stopped.")

if __name__ == "__main__":
    main()
```
