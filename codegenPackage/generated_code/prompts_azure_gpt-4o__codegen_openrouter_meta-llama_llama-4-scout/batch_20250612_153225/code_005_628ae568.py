"""
Generated Code Metadata:
========================
Original URL: https://soundsource.tn
Prompt: Create a program to manage partnerships with sound system manufacturers like KV2 Audio and Void Acoustics, as highlighted on the Sound Source website.
Generated: DETERMINISTIC_628ae568d16b422a
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# partnership_manager.py

class PartnershipManager:
    """
    A class to manage partnerships with sound system manufacturers.
    """

    def __init__(self):
        """
        Initialize an empty partnership dictionary.
        """
        self.partnerships = {}

    def add_partnership(self, manufacturer_name, manufacturer_info):
        """
        Add a new partnership with a sound system manufacturer.

        Args:
            manufacturer_name (str): The name of the manufacturer (e.g., KV2 Audio).
            manufacturer_info (dict): Additional information about the manufacturer.

        Raises:
            ValueError: If manufacturer_name is empty or manufacturer_info is not a dictionary.
        """
        if not manufacturer_name:
            raise ValueError("Manufacturer name cannot be empty")
        if not isinstance(manufacturer_info, dict):
            raise ValueError("Manufacturer info must be a dictionary")

        self.partnerships[manufacturer_name] = manufacturer_info

    def remove_partnership(self, manufacturer_name):
        """
        Remove an existing partnership with a sound system manufacturer.

        Args:
            manufacturer_name (str): The name of the manufacturer to remove.

        Raises:
            KeyError: If the manufacturer is not found in the partnerships dictionary.
        """
        if manufacturer_name not in self.partnerships:
            raise KeyError(f"Manufacturer '{manufacturer_name}' not found")

        del self.partnerships[manufacturer_name]

    def update_partnership(self, manufacturer_name, manufacturer_info):
        """
        Update an existing partnership with a sound system manufacturer.

        Args:
            manufacturer_name (str): The name of the manufacturer to update.
            manufacturer_info (dict): Updated information about the manufacturer.

        Raises:
            KeyError: If the manufacturer is not found in the partnerships dictionary.
            ValueError: If manufacturer_info is not a dictionary.
        """
        if manufacturer_name not in self.partnerships:
            raise KeyError(f"Manufacturer '{manufacturer_name}' not found")
        if not isinstance(manufacturer_info, dict):
            raise ValueError("Manufacturer info must be a dictionary")

        self.partnerships[manufacturer_name] = manufacturer_info

    def get_partnership(self, manufacturer_name):
        """
        Retrieve information about a partnership with a sound system manufacturer.

        Args:
            manufacturer_name (str): The name of the manufacturer.

        Returns:
            dict: Information about the manufacturer, or None if not found.
        """
        return self.partnerships.get(manufacturer_name)

    def list_partnerships(self):
        """
        Retrieve a list of all partnerships with sound system manufacturers.

        Returns:
            dict: A dictionary of all manufacturer partnerships.
        """
        return self.partnerships.copy()


def main():
    # Example usage
    manager = PartnershipManager()

    kv2_audio_info = {
        "description": "KV2 Audio is a leading manufacturer of high-quality sound systems.",
        "contact_email": "info@kv2audio.com",
        "contact_phone": "+1 123 456 7890"
    }

    void_acoustics_info = {
        "description": "Void Acoustics is a renowned manufacturer of innovative sound systems.",
        "contact_email": "info@voidacoustics.com",
        "contact_phone": "+1 987 654 3210"
    }

    manager.add_partnership("KV2 Audio", kv2_audio_info)
    manager.add_partnership("Void Acoustics", void_acoustics_info)

    print("Partnerships:")
    for manufacturer, info in manager.list_partnerships().items():
        print(f"{manufacturer}: {info}")

    # Update KV2 Audio partnership
    updated_kv2_audio_info = kv2_audio_info.copy()
    updated_kv2_audio_info["contact_phone"] = "+1 555 123 4567"
    manager.update_partnership("KV2 Audio", updated_kv2_audio_info)

    print("\nUpdated KV2 Audio Partnership:")
    print(manager.get_partnership("KV2 Audio"))

    # Remove Void Acoustics partnership
    manager.remove_partnership("Void Acoustics")

    print("\nPartnerships after removal:")
    for manufacturer, info in manager.list_partnerships().items():
        print(f"{manufacturer}: {info}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
