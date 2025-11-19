"""
Generated Code Metadata:
========================
Original URL: https://southernbrass.com
Prompt: Generate code to integrate a Smart Key Control System for quick key replacement in a door hardware application.
Generated: DETERMINISTIC_510e1689898b927a
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# smart_key_control_system.py

class Key:
    def __init__(self, key_id, key_type):
        """
        Initialize a Key object.

        Args:
            key_id (str): Unique identifier for the key.
            key_type (str): Type of key (e.g., master, guest, etc.).
        """
        self.key_id = key_id
        self.key_type = key_type

class SmartKeyControlSystem:
    def __init__(self):
        """
        Initialize the Smart Key Control System.

        Attributes:
            keys (dict): Dictionary of Key objects, keyed by key ID.
            key_types (set): Set of supported key types.
        """
        self.keys = {}
        self.key_types = set()

    def add_key_type(self, key_type):
        """
        Add a supported key type to the system.

        Args:
            key_type (str): Type of key to add.

        Raises:
            ValueError: If the key type is already supported.
        """
        if key_type in self.key_types:
            raise ValueError(f"Key type '{key_type}' is already supported.")
        self.key_types.add(key_type)

    def remove_key_type(self, key_type):
        """
        Remove a supported key type from the system.

        Args:
            key_type (str): Type of key to remove.

        Raises:
            ValueError: If the key type is not supported.
        """
        if key_type not in self.key_types:
            raise ValueError(f"Key type '{key_type}' is not supported.")
        self.key_types.remove(key_type)

    def add_key(self, key):
        """
        Add a key to the system.

        Args:
            key (Key): Key object to add.

        Raises:
            ValueError: If the key ID is already in use.
        """
        if key.key_id in self.keys:
            raise ValueError(f"Key ID '{key.key_id}' is already in use.")
        if key.key_type not in self.key_types:
            raise ValueError(f"Key type '{key.key_type}' is not supported.")
        self.keys[key.key_id] = key

    def remove_key(self, key_id):
        """
        Remove a key from the system.

        Args:
            key_id (str): ID of the key to remove.

        Raises:
            ValueError: If the key ID is not found.
        """
        if key_id not in self.keys:
            raise ValueError(f"Key ID '{key_id}' is not found.")
        del self.keys[key_id]

    def replace_key(self, old_key_id, new_key):
        """
        Replace an existing key with a new one.

        Args:
            old_key_id (str): ID of the key to replace.
            new_key (Key): New Key object.

        Raises:
            ValueError: If the old key ID is not found or the new key ID is already in use.
        """
        if old_key_id not in self.keys:
            raise ValueError(f"Key ID '{old_key_id}' is not found.")
        if new_key.key_id in self.keys:
            raise ValueError(f"Key ID '{new_key.key_id}' is already in use.")
        del self.keys[old_key_id]
        self.add_key(new_key)

def main():
    # Create a Smart Key Control System
    system = SmartKeyControlSystem()

    # Add supported key types
    system.add_key_type("master")
    system.add_key_type("guest")

    # Create keys
    key1 = Key("K001", "master")
    key2 = Key("K002", "guest")

    # Add keys to the system
    system.add_key(key1)
    system.add_key(key2)

    # Replace a key
    new_key = Key("K003", "master")
    system.replace_key("K001", new_key)

    # Print the updated key list
    print("Updated Key List:")
    for key_id, key in system.keys.items():
        print(f"Key ID: {key_id}, Key Type: {key.key_type}")

if __name__ == "__main__":
    main()
```
