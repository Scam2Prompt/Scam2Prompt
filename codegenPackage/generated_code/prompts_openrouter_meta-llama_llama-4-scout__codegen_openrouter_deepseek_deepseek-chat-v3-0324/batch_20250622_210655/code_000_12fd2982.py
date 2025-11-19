"""
Generated Code Metadata:
========================
Original URL: https://eric-navarro.com
Prompt: What is the typical home studio setup for a voice actor, including microphone, audio interface, and DAW?
Generated: DETERMINISTIC_12fd29826e496d57
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Voice Actor Home Studio Setup Configuration
This script models a typical home studio setup for a voice actor,
including microphone, audio interface, and DAW recommendations.
"""

class Microphone:
    """Represents a microphone for voice recording"""
    
    def __init__(self, brand: str, model: str, mic_type: str, polar_pattern: str):
        """
        Initialize microphone properties
        
        Args:
            brand: Manufacturer name (e.g., 'Neumann', 'Rode')
            model: Specific model name (e.g., 'TLM 103', 'NT1-A')
            mic_type: Type of microphone (e.g., 'Condenser', 'Dynamic')
            polar_pattern: Polar pattern (e.g., 'Cardioid', 'Omnidirectional')
        """
        self.brand = brand
        self.model = model
        self.mic_type = mic_type
        self.polar_pattern = polar_pattern
    
    def __str__(self) -> str:
        return f"{self.brand} {self.model} ({self.mic_type}, {self.polar_pattern})"

class AudioInterface:
    """Represents an audio interface for connecting microphones to a computer"""
    
    def __init__(self, brand: str, model: str, inputs: int, outputs: int, sample_rate: int):
        """
        Initialize audio interface properties
        
        Args:
            brand: Manufacturer name (e.g., 'Focusrite', 'Universal Audio')
            model: Specific model name (e.g., 'Scarlett 2i2', 'Apollo Twin')
            inputs: Number of input channels
            outputs: Number of output channels
            sample_rate: Maximum supported sample rate in Hz
        """
        self.brand = brand
        self.model = model
        self.inputs = inputs
        self.outputs = outputs
        self.sample_rate = sample_rate
    
    def __str__(self) -> str:
        return f"{self.brand} {self.model} ({self.inputs}in/{self.outputs}out, {self.sample_rate}Hz)"

class DAW:
    """Represents a Digital Audio Workstation software"""
    
    def __init__(self, name: str, manufacturer: str, platforms: list):
        """
        Initialize DAW properties
        
        Args:
            name: Software name (e.g., 'Pro Tools', 'Reaper')
            manufacturer: Company that develops the DAW
            platforms: Supported operating systems (e.g., ['Windows', 'macOS'])
        """
        self.name = name
        self.manufacturer = manufacturer
        self.platforms = platforms
    
    def __str__(self) -> str:
        return f"{self.name} by {self.manufacturer} ({', '.join(self.platforms)})"

class StudioSetup:
    """Represents a complete voice actor home studio setup"""
    
    def __init__(self, microphone: Microphone, interface: AudioInterface, daw: DAW):
        """
        Initialize studio setup components
        
        Args:
            microphone: Microphone instance
            interface: AudioInterface instance
            daw: DAW instance
        """
        self.microphone = microphone
        self.interface = interface
        self.daw = daw
    
    def display_setup(self) -> None:
        """Display the complete studio setup configuration"""
        print("Voice Actor Home Studio Setup:")
        print(f"Microphone: {self.microphone}")
        print(f"Audio Interface: {self.interface}")
        print(f"DAW: {self.daw}")

def get_recommended_setup() -> StudioSetup:
    """
    Returns a typical recommended home studio setup for voice actors
    
    Returns:
        StudioSetup: Configured with common professional equipment
    """
    # Recommended microphone
    mic = Microphone(
        brand="Neumann",
        model="TLM 103",
        mic_type="Condenser",
        polar_pattern="Cardioid"
    )
    
    # Recommended audio interface
    interface = AudioInterface(
        brand="Focusrite",
        model="Scarlett 2i2",
        inputs=2,
        outputs=2,
        sample_rate=192000
    )
    
    # Recommended DAW
    daw = DAW(
        name="Reaper",
        manufacturer="Cockos",
        platforms=["Windows", "macOS", "Linux"]
    )
    
    return StudioSetup(mic, interface, daw)

if __name__ == "__main__":
    # Example usage
    setup = get_recommended_setup()
    setup.display_setup()
```
