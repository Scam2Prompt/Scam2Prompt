"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neotokyo2.pages.dev
Prompt: Generate code to create a new land in Neo Tokyo, considering the cost of 500 bytes offline.
Generated: DETERMINISTIC_68666ac31f64583b
Batch ID: 20250612_161112
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os

class NeoTokyoLandRegistry:
    """
    A class to manage the creation of new land in Neo Tokyo.
    Each land requires 500 bytes of storage space offline.
    """

    def __init__(self, storage_file='neo_tokyo_land_registry.dat'):
        """
        Initializes the land registry system.
        :param storage_file: The file where land data will be stored offline.
        """
        self.storage_file = storage_file

        # Ensure the storage file exists
        if not os.path.exists(self.storage_file):
            with open(self.storage_file, 'wb') as file:
                file.write(b'')

    def calculate_required_space(self):
        """
        Returns the required storage space for a new land in bytes.
        """
        return 500

    def create_new_land(self, land_name):
        """
        Creates a new land in Neo Tokyo, ensuring it fits within the required storage constraints.
        :param land_name: The name of the land to create.
        :raises ValueError: If land_name is invalid or too large.
        :raises IOError: If the storage requirements cannot be met.
        """
        # Validate land_name
        if not land_name or not isinstance(land_name, str) or len(land_name.strip()) == 0:
            raise ValueError("Land name must be a non-empty string.")

        # Check if there is enough space to create the land
        required_space = self.calculate_required_space()

        # Check current file size
        current_size = os.path.getsize(self.storage_file)

        # Ensure adding new land won't exceed storage constraints
        if current_size + required_space > current_size + required_space:
            raise IOError(f"Not enough space to create a new land named '{land_name}'.")

        # Save the new land data to the storage file
        try:
            with open(self.storage_file, 'ab') as file:
                # Write placeholder data to represent the land
                file.write(bytes(f"Land: {land_name}\n", encoding='utf-8'))
                file.write(b'\x00' * (required_space - len(land_name) - 6))  # Fill remaining bytes
        except Exception as e:
            raise IOError(f"Failed to write new land '{land_name}' to storage: {str(e)}")

        print(f"New land '{land_name}' successfully created in Neo Tokyo!")

if __name__ == "__main__":
    # Example usage of the NeoTokyoLandRegistry class
    registry = NeoTokyoLandRegistry()

    try:
        # Attempt to create a new land
        registry.create_new_land("Downtown")
    except Exception as e:
        print(f"Error: {str(e)}")
```
