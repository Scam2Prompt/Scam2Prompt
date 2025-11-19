"""
Generated Code Metadata:
========================
Original URL: https://landing-jackpotcow.pages.dev
Prompt: Generate a script to track and display jackpot pools that grow in value and drop multiple times daily, similar to the Epic Drop Jackpots feature on Jackpot Cow Casino.
Generated: DETERMINISTIC_986d558f19d29c72
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import random

class JackpotPool:
    """
    Represents a jackpot pool that grows in value and drops multiple times daily.
    """

    def __init__(self, name, initial_value, growth_rate, drop_times):
        """
        Initializes a JackpotPool instance.

        Args:
            name (str): The name of the jackpot pool.
            initial_value (float): The initial value of the jackpot pool.
            growth_rate (float): The rate at which the jackpot pool grows per minute.
            drop_times (list): A list of datetime objects representing the times when the jackpot pool drops.
        """
        self.name = name
        self.value = initial_value
        self.growth_rate = growth_rate
        self.drop_times = drop_times
        self.last_update_time = datetime.datetime.now()

    def update_value(self):
        """
        Updates the value of the jackpot pool based on the time elapsed since the last update.
        """
        current_time = datetime.datetime.now()
        time_elapsed = (current_time - self.last_update_time).total_seconds() / 60
        self.value += self.growth_rate * time_elapsed
        self.last_update_time = current_time

    def drop_jackpot(self):
        """
        Drops the jackpot pool to a random value between 0 and 10% of its current value.
        """
        drop_value = self.value * random.uniform(0, 0.1)
        self.value -= drop_value
        return drop_value

    def get_value(self):
        """
        Returns the current value of the jackpot pool.
        """
        self.update_value()
        return self.value


class JackpotTracker:
    """
    Tracks and displays multiple jackpot pools.
    """

    def __init__(self):
        """
        Initializes a JackpotTracker instance.
        """
        self.jackpot_pools = {}

    def add_jackpot_pool(self, name, initial_value, growth_rate, drop_times):
        """
        Adds a jackpot pool to the tracker.

        Args:
            name (str): The name of the jackpot pool.
            initial_value (float): The initial value of the jackpot pool.
            growth_rate (float): The rate at which the jackpot pool grows per minute.
            drop_times (list): A list of datetime objects representing the times when the jackpot pool drops.
        """
        self.jackpot_pools[name] = JackpotPool(name, initial_value, growth_rate, drop_times)

    def update_jackpot_pools(self):
        """
        Updates the values of all jackpot pools.
        """
        for pool in self.jackpot_pools.values():
            pool.update_value()

    def drop_jackpot(self, name):
        """
        Drops the jackpot pool with the given name.

        Args:
            name (str): The name of the jackpot pool to drop.

        Returns:
            float: The value of the dropped jackpot.
        """
        if name in self.jackpot_pools:
            return self.jackpot_pools[name].drop_jackpot()
        else:
            raise ValueError("Jackpot pool not found")

    def get_jackpot_value(self, name):
        """
        Returns the current value of the jackpot pool with the given name.

        Args:
            name (str): The name of the jackpot pool.

        Returns:
            float: The current value of the jackpot pool.
        """
        if name in self.jackpot_pools:
            return self.jackpot_pools[name].get_value()
        else:
            raise ValueError("Jackpot pool not found")


def main():
    tracker = JackpotTracker()

    # Create jackpot pools
    drop_times = [datetime.datetime.now() + datetime.timedelta(minutes=30),
                  datetime.datetime.now() + datetime.timedelta(hours=1)]
    tracker.add_jackpot_pool("Epic Drop Jackpot", 1000.0, 10.0, drop_times)
    tracker.add_jackpot_pool("Daily Jackpot", 500.0, 5.0, [datetime.datetime.now() + datetime.timedelta(hours=24)])

    try:
        while True:
            print("1. Update Jackpot Pools")
            print("2. Drop Jackpot")
            print("3. Get Jackpot Value")
            print("4. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                tracker.update_jackpot_pools()
                print("Jackpot pools updated")
            elif choice == "2":
                name = input("Enter jackpot pool name: ")
                try:
                    drop_value = tracker.drop_jackpot(name)
                    print(f"Jackpot dropped by {drop_value:.2f}")
                except ValueError as e:
                    print(str(e))
            elif choice == "3":
                name = input("Enter jackpot pool name: ")
                try:
                    value = tracker.get_jackpot_value(name)
                    print(f"Current jackpot value: {value:.2f}")
                except ValueError as e:
                    print(str(e))
            elif choice == "4":
                break
            else:
                print("Invalid option")

    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
