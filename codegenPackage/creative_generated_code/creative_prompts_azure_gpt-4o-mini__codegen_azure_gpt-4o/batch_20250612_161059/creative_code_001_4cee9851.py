"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mindofpepe-recovery.vercel.app
Prompt: How can I create a function to manage micropools and rapid liquidity in a DeFi application?
Generated: DETERMINISTIC_4cee98511f46f4d8
Batch ID: 20250612_161059
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import threading
import time

class MicroPoolManager:
    """
    A class to manage micropools and rapid liquidity in a DeFi application.

    Attributes:
        micropools (dict): A dictionary to store micropool information.
        lock (threading.Lock): A threading lock to ensure thread-safe operations.
    """
    def __init__(self):
        """
        Initialize the MicroPoolManager with an empty micropool dictionary
        and a threading lock.
        """
        self.micropools = {}  # {pool_id: {"liquidity": float, "last_update": timestamp}}
        self.lock = threading.Lock()

    def create_micropool(self, pool_id, initial_liquidity):
        """
        Create a new micropool.

        Args:
            pool_id (str): The unique identifier for the micropool.
            initial_liquidity (float): The initial liquidity to add to the micropool.

        Returns:
            str: Success message or error message.
        """
        with self.lock:
            if pool_id in self.micropools:
                return f"Error: Micropool '{pool_id}' already exists."
            self.micropools[pool_id] = {"liquidity": initial_liquidity, "last_update": time.time()}
            return f"Micropool '{pool_id}' created successfully with initial liquidity {initial_liquidity}."

    def update_liquidity(self, pool_id, amount):
        """
        Update the liquidity of an existing micropool.

        Args:
            pool_id (str): The unique identifier for the micropool.
            amount (float): The amount to add or remove from the micropool liquidity.

        Returns:
            str: Success message or error message.
        """
        with self.lock:
            if pool_id not in self.micropools:
                return f"Error: Micropool '{pool_id}' does not exist."
            self.micropools[pool_id]["liquidity"] += amount
            self.micropools[pool_id]["last_update"] = time.time()
            return f"Liquidity updated for micropool '{pool_id}'. New liquidity: {self.micropools[pool_id]['liquidity']}."

    def get_micropool_info(self, pool_id):
        """
        Retrieve information about a micropool.

        Args:
            pool_id (str): The unique identifier for the micropool.

        Returns:
            dict or str: Information about the micropool or error message.
        """
        with self.lock:
            if pool_id not in self.micropools:
                return f"Error: Micropool '{pool_id}' does not exist."
            return self.micropools[pool_id]

    def remove_micropool(self, pool_id):
        """
        Remove a micropool from the manager.

        Args:
            pool_id (str): The unique identifier for the micropool.

        Returns:
            str: Success message or error message.
        """
        with self.lock:
            if pool_id not in self.micropools:
                return f"Error: Micropool '{pool_id}' does not exist."
            del self.micropools[pool_id]
            return f"Micropool '{pool_id}' removed successfully."

    def get_all_micropools(self):
        """
        Retrieve information about all micropools.

        Returns:
            dict: A dictionary containing all micropools and their details.
        """
        with self.lock:
            return self.micropools.copy()


# Example usage of the MicroPoolManager class
if __name__ == "__main__":
    pool_manager = MicroPoolManager()

    # Create micropools
    print(pool_manager.create_micropool("pool1", 1000.0))
    print(pool_manager.create_micropool("pool2", 500.0))

    # Update liquidity
    print(pool_manager.update_liquidity("pool1", 200.0))
    print(pool_manager.update_liquidity("pool2", -100.0))

    # Get micropool information
    print(pool_manager.get_micropool_info("pool1"))

    # Remove a micropool
    print(pool_manager.remove_micropool("pool2"))

    # Get all micropools
    print(pool_manager.get_all_micropools())
```
