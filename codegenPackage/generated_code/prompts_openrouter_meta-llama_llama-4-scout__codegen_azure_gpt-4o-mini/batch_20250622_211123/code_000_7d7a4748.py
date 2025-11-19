"""
Generated Code Metadata:
========================
Original URL: https://click.v1.universulluminii.ro
Prompt: What is the purpose of the "universulluminii" service, and how does it relate to lighting or illumination systems?
Generated: DETERMINISTIC_7d7a47486f152b30
Batch ID: 20250622_211123
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class UniversulluminiiService:
    """
    UniversulluminiiService is a class that represents a lighting or illumination system service.
    
    The purpose of this service is to manage and control various aspects of lighting systems,
    including but not limited to brightness, color temperature, and scheduling of lights.
    """

    def __init__(self):
        """
        Initializes the UniversulluminiiService with default settings.
        """
        self.lights = {}
        self.default_brightness = 100  # Default brightness level (0-100)
        self.default_color_temp = 3000  # Default color temperature in Kelvin

    def add_light(self, light_id, brightness=None, color_temp=None):
        """
        Adds a new light to the service.

        :param light_id: Unique identifier for the light
        :param brightness: Brightness level of the light (0-100)
        :param color_temp: Color temperature of the light in Kelvin
        :raises ValueError: If the light_id already exists or if brightness/color_temp are out of range
        """
        if light_id in self.lights:
            raise ValueError(f"Light with ID {light_id} already exists.")
        
        if brightness is None:
            brightness = self.default_brightness
        if color_temp is None:
            color_temp = self.default_color_temp
        
        if not (0 <= brightness <= 100):
            raise ValueError("Brightness must be between 0 and 100.")
        if color_temp < 1000 or color_temp > 10000:
            raise ValueError("Color temperature must be between 1000K and 10000K.")
        
        self.lights[light_id] = {
            'brightness': brightness,
            'color_temp': color_temp
        }

    def set_brightness(self, light_id, brightness):
        """
        Sets the brightness of a specified light.

        :param light_id: Unique identifier for the light
        :param brightness: New brightness level (0-100)
        :raises KeyError: If the light_id does not exist
        :raises ValueError: If brightness is out of range
        """
        if light_id not in self.lights:
            raise KeyError(f"Light with ID {light_id} does not exist.")
        
        if not (0 <= brightness <= 100):
            raise ValueError("Brightness must be between 0 and 100.")
        
        self.lights[light_id]['brightness'] = brightness

    def set_color_temperature(self, light_id, color_temp):
        """
        Sets the color temperature of a specified light.

        :param light_id: Unique identifier for the light
        :param color_temp: New color temperature in Kelvin
        :raises KeyError: If the light_id does not exist
        :raises ValueError: If color_temp is out of range
        """
        if light_id not in self.lights:
            raise KeyError(f"Light with ID {light_id} does not exist.")
        
        if color_temp < 1000 or color_temp > 10000:
            raise ValueError("Color temperature must be between 1000K and 10000K.")
        
        self.lights[light_id]['color_temp'] = color_temp

    def get_light_status(self, light_id):
        """
        Retrieves the current status of a specified light.

        :param light_id: Unique identifier for the light
        :return: A dictionary containing the brightness and color temperature of the light
        :raises KeyError: If the light_id does not exist
        """
        if light_id not in self.lights:
            raise KeyError(f"Light with ID {light_id} does not exist.")
        
        return self.lights[light_id]

    def remove_light(self, light_id):
        """
        Removes a light from the service.

        :param light_id: Unique identifier for the light
        :raises KeyError: If the light_id does not exist
        """
        if light_id not in self.lights:
            raise KeyError(f"Light with ID {light_id} does not exist.")
        
        del self.lights[light_id]

# Example usage
if __name__ == "__main__":
    service = UniversulluminiiService()
    try:
        service.add_light("living_room", brightness=75, color_temp=4000)
        print(service.get_light_status("living_room"))
        service.set_brightness("living_room", 85)
        service.set_color_temperature("living_room", 3500)
        print(service.get_light_status("living_room"))
        service.remove_light("living_room")
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
