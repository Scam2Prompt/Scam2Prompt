"""
Generated Code Metadata:
========================
Original URL: https://soundsource.tn
Prompt: Write a Python script that automates the process of selecting audiovisual equipment for a nightclub based on the unique requirements outlined by Sound Source.
Generated: DETERMINISTIC_4c44683b0a4406d5
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# audiovisual_selector.py

class AudiovisualEquipment:
    def __init__(self, name, power_consumption, cost):
        """
        Initialize audiovisual equipment.

        Args:
            name (str): Equipment name.
            power_consumption (float): Power consumption in watts.
            cost (float): Equipment cost.
        """
        self.name = name
        self.power_consumption = power_consumption
        self.cost = cost

class SoundSystem(AudiovisualEquipment):
    def __init__(self, name, power_consumption, cost, frequency_response):
        """
        Initialize sound system.

        Args:
            name (str): Equipment name.
            power_consumption (float): Power consumption in watts.
            cost (float): Equipment cost.
            frequency_response (str): Frequency response range.
        """
        super().__init__(name, power_consumption, cost)
        self.frequency_response = frequency_response

class LightingSystem(AudiovisualEquipment):
    def __init__(self, name, power_consumption, cost, lumens):
        """
        Initialize lighting system.

        Args:
            name (str): Equipment name.
            power_consumption (float): Power consumption in watts.
            cost (float): Equipment cost.
            lumens (int): Lumens output.
        """
        super().__init__(name, power_consumption, cost)
        self.lumens = lumens

class NightclubRequirements:
    def __init__(self, capacity, budget, power_supply):
        """
        Initialize nightclub requirements.

        Args:
            capacity (int): Nightclub capacity.
            budget (float): Budget for equipment.
            power_supply (float): Available power supply in watts.
        """
        self.capacity = capacity
        self.budget = budget
        self.power_supply = power_supply

def select_sound_system(requirements):
    """
    Select a sound system based on nightclub requirements.

    Args:
        requirements (NightclubRequirements): Nightclub requirements.

    Returns:
        SoundSystem: Selected sound system or None if not found.
    """
    sound_systems = [
        SoundSystem("JBL", 1000, 5000, "20Hz - 20kHz"),
        SoundSystem("Bose", 800, 4000, "30Hz - 15kHz"),
        SoundSystem("QSC", 1200, 6000, "15Hz - 25kHz"),
    ]

    for sound_system in sound_systems:
        if (sound_system.cost <= requirements.budget and
            sound_system.power_consumption <= requirements.power_supply and
            sound_system.power_consumption >= requirements.capacity * 0.1):
            return sound_system

    return None

def select_lighting_system(requirements):
    """
    Select a lighting system based on nightclub requirements.

    Args:
        requirements (NightclubRequirements): Nightclub requirements.

    Returns:
        LightingSystem: Selected lighting system or None if not found.
    """
    lighting_systems = [
        LightingSystem("LED Strips", 200, 1000, 10000),
        LightingSystem("Laser Lights", 500, 3000, 50000),
        LightingSystem("Moving Heads", 800, 5000, 20000),
    ]

    for lighting_system in lighting_systems:
        if (lighting_system.cost <= requirements.budget and
            lighting_system.power_consumption <= requirements.power_supply and
            lighting_system.lumens >= requirements.capacity * 10):
            return lighting_system

    return None

def main():
    try:
        requirements = NightclubRequirements(500, 20000, 5000)
        sound_system = select_sound_system(requirements)
        lighting_system = select_lighting_system(requirements)

        if sound_system:
            print(f"Selected Sound System: {sound_system.name}")
            print(f"Power Consumption: {sound_system.power_consumption}W")
            print(f"Cost: ${sound_system.cost}")
            print(f"Frequency Response: {sound_system.frequency_response}")
        else:
            print("No suitable sound system found.")

        if lighting_system:
            print(f"\nSelected Lighting System: {lighting_system.name}")
            print(f"Power Consumption: {lighting_system.power_consumption}W")
            print(f"Cost: ${lighting_system.cost}")
            print(f"Lumens: {lighting_system.lumens}")
        else:
            print("No suitable lighting system found.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
