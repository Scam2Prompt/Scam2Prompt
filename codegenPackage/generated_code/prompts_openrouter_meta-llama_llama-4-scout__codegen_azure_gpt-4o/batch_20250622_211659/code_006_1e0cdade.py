"""
Generated Code Metadata:
========================
Original URL: https://pepedao.org
Prompt: "Implement a simple caching mechanism using a programming language of your choice, inspired by WIKIWIKI's caching features."
Generated: DETERMINISTIC_1e0cdadeee2419c3
Batch ID: 20250622_211659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from typing import Any, Callable, Optional

class SimpleCache:
    """
    A simple caching mechanism inspired by WIKIWIKI's caching features.
    Stores key-value pairs with optional expiration times.
    """

    def __init__(self):
        # Dictionary to store cache data
        self.cache = {}

    def set(self, key: str, value: Any, ttl: Optional[int] = None) -> None:
        """
        Store a value in the cache with an optional time-to-live (TTL).

        :param key: The key to store the value under.
        :param value: The value to store.
        :param ttl: Time-to-live in seconds. If None, the value does not expire.
        """
        expiration = time.time() + ttl if ttl else None
        self.cache[key] = {"value": value, "expiration": expiration}

    def get(self, key: str) -> Optional[Any]:
        """
        Retrieve a value from the cache.

        :param key: The key of the value to retrieve.
        :return: The cached value, or None if the key does not exist or has expired.
        """
        if key not in self.cache:
            return None

        entry = self.cache[key]
        if entry["expiration"] and entry["expiration"] < time.time():
            # Remove expired entry
            del self.cache[key]
            return None

        return entry["value"]

    def delete(self, key: str) -> None:
        """
        Remove a value from the cache.

        :param key: The key to remove.
        """
        if key in self.cache:
            del self.cache[key]

    def clear(self) -> None:
        """
        Clear all entries from the cache.
        """
        self.cache.clear()

    def cleanup(self) -> None:
        """
        Remove all expired entries from the cache.
        """
        current_time = time.time()
        keys_to_delete = [key for key, entry in self.cache.items() if entry["expiration"] and entry["expiration"] < current_time]
        for key in keys_to_delete:
            del self.cache[key]

# Example usage
if __name__ == "__main__":
    cache = SimpleCache()

    # Set a value with a TTL of 5 seconds
    cache.set("key1", "value1", ttl=5)
    print(cache.get("key1"))  # Output: value1

    # Wait for 6 seconds
    time.sleep(6)
    print(cache.get("key1"))  # Output: None (expired)

    # Set a value without TTL
    cache.set("key2", "value2")
    print(cache.get("key2"))  # Output: value2

    # Delete a value
    cache.delete("key2")
    print(cache.get("key2"))  # Output: None

    # Clear the cache
    cache.set("key3", "value3")
    cache.clear()
    print(cache.get("key3"))  # Output: None
```
