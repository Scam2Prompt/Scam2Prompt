"""
Generated Code Metadata:
========================
Original URL: https://www.ablakvaros.hu
Prompt: Develop a script to automate the selection of redőny (blinds) types, such as külsőtokos redőny (external box blinds), based on user preferences and building specifications.
Generated: DETERMINISTIC_0f13462cadd96090
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# blind_selector.py

class Blind:
    def __init__(self, name, description, is_external):
        """
        Initialize a Blind object.

        Args:
            name (str): Name of the blind type.
            description (str): Description of the blind type.
            is_external (bool): Whether the blind is external or not.
        """
        self.name = name
        self.description = description
        self.is_external = is_external

class Building:
    def __init__(self, window_size, window_type, has_external_space):
        """
        Initialize a Building object.

        Args:
            window_size (str): Size of the window.
            window_type (str): Type of the window.
            has_external_space (bool): Whether the building has external space or not.
        """
        self.window_size = window_size
        self.window_type = window_type
        self.has_external_space = has_external_space

def get_blind_types():
    """
    Return a list of available blind types.

    Returns:
        list[Blind]: List of Blind objects.
    """
    blind_types = [
        Blind("külsőtokos redőny", "External box blinds", True),
        Blind("beltéri redőny", "Internal blinds", False),
        Blind("zsaluzia", "Venetian blinds", False),
    ]
    return blind_types

def select_blind(user_preferences, building_specs):
    """
    Select a blind type based on user preferences and building specifications.

    Args:
        user_preferences (dict): Dictionary containing user preferences.
        building_specs (Building): Building specifications.

    Returns:
        Blind: Selected blind type.

    Raises:
        ValueError: If no suitable blind type is found.
    """
    blind_types = get_blind_types()

    # Filter blind types based on user preferences
    preferred_blind_types = [
        blind for blind in blind_types
        if user_preferences.get("blind_type") == blind.name
    ]

    if not preferred_blind_types:
        # If no preferred blind type is specified, consider all blind types
        preferred_blind_types = blind_types

    # Filter blind types based on building specifications
    suitable_blind_types = [
        blind for blind in preferred_blind_types
        if (building_specs.has_external_space and blind.is_external)
        or not blind.is_external
    ]

    if not suitable_blind_types:
        raise ValueError("No suitable blind type found")

    # Return the first suitable blind type
    return suitable_blind_types[0]

def main():
    try:
        user_preferences = {
            "blind_type": "külsőtokos redőny",
            "color": "white",
        }

        building_specs = Building(
            window_size="large",
            window_type="casement",
            has_external_space=True,
        )

        selected_blind = select_blind(user_preferences, building_specs)
        print(f"Selected blind type: {selected_blind.name} ({selected_blind.description})")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
