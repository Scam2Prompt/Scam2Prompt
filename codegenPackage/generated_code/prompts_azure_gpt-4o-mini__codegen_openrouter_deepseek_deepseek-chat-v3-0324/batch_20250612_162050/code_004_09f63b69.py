"""
Generated Code Metadata:
========================
Original URL: https://soundsource.tn
Prompt: Create a code snippet that simulates an immersive audio experience for an event, inspired by the projects showcased in Sound Source's portfolio.
Generated: DETERMINISTIC_09f63b69de3d95c4
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from enum import Enum
from typing import List, Dict, Optional

class AudioEffectType(Enum):
    """Enum representing different types of audio effects."""
    AMBIENT = "ambient"
    SPATIAL = "spatial"
    REVERB = "reverb"
    ECHO = "echo"
    DISTORTION = "distortion"

class AudioSource:
    """Represents an audio source with position and effects."""
    
    def __init__(self, name: str, x: float, y: float, z: float):
        """
        Initialize an audio source.
        
        Args:
            name: Name of the audio source
            x: X coordinate in 3D space
            y: Y coordinate in 3D space
            z: Z coordinate in 3D space
        """
        self.name = name
        self.x = x
        self.y = y
        self.z = z
        self.effects: List[AudioEffectType] = []
        self.volume = 1.0  # Default volume (0.0 to 1.0)
    
    def add_effect(self, effect: AudioEffectType) -> None:
        """Add an audio effect to this source."""
        if effect not in self.effects:
            self.effects.append(effect)
    
    def remove_effect(self, effect: AudioEffectType) -> None:
        """Remove an audio effect from this source."""
        if effect in self.effects:
            self.effects.remove(effect)
    
    def set_volume(self, volume: float) -> None:
        """Set the volume of this source (0.0 to 1.0)."""
        if 0.0 <= volume <= 1.0:
            self.volume = volume
        else:
            raise ValueError("Volume must be between 0.0 and 1.0")
    
    def get_position(self) -> tuple:
        """Get the 3D position of this source."""
        return (self.x, self.y, self.z)
    
    def __str__(self) -> str:
        """String representation of the audio source."""
        return f"AudioSource(name={self.name}, position=({self.x}, {self.y}, {self.z}), effects={self.effects}, volume={self.volume})"

class AudioEngine:
    """Main audio engine that manages all audio sources and effects."""
    
    def __init__(self):
        """Initialize the audio engine."""
        self.sources: Dict[str, AudioSource] = {}
        self.master_volume = 1.0
        self.listener_position = (0.0, 0.0, 0.0)
    
    def add_source(self, source: AudioSource) -> None:
        """Add an audio source to the engine."""
        if source.name in self.sources:
            raise ValueError(f"Audio source with name '{source.name}' already exists")
        self.sources[source.name] = source
    
    def remove_source(self, name: str) -> None:
        """Remove an audio source from the engine."""
        if name in self.sources:
            del self.sources[name]
    
    def get_source(self, name: str) -> Optional[AudioSource]:
        """Get an audio source by name."""
        return self.sources.get(name)
    
    def set_listener_position(self, x: float, y: float, z: float) -> None:
        """Set the position of the listener in 3D space."""
        self.listener_position = (x, y, z)
    
    def set_master_volume(self, volume: float) -> None:
        """Set the master volume (0.0 to 1.0)."""
        if 0.0 <= volume <= 1.0:
            self.master_volume = volume
        else:
            raise ValueError("Volume must be between 0.0 and 1.0")
    
    def calculate_distance_volume(self, source: AudioSource) -> float:
        """
        Calculate volume based on distance from listener.
        Implements inverse square law for realistic attenuation.
        """
        listener_x, listener_y, listener_z = self.listener_position
        distance = ((source.x - listener_x) ** 2 + 
                    (source.y - listener_y) ** 2 + 
                    (source.z - listener_z) ** 2) ** 0.5
        
        # Avoid division by zero
        if distance < 0.1:
            return source.volume * self.master_volume
        
        # Inverse square law with a minimum distance
        attenuation = min(1.0, 1.0 / (distance ** 2))
        return source.volume * self.master_volume * attenuation
    
    def play_all(self) -> None:
        """Simulate playing all audio sources with their effects and positions."""
        print("\n--- Playing immersive audio experience ---")
        print(f"Listener position: {self.listener_position}")
        print(f"Master volume: {self.master_volume}")
        
        for name, source in self.sources.items():
            effective_volume = self.calculate_distance_volume(source)
            print(f"\nPlaying '{name}' at position {source.get_position()}")
            print(f"Effective volume: {effective_volume:.2f}")
            print(f"Effects applied: {', '.join([e.value for e in source.effects])}")
            
            # Simulate audio playback with effects
            time.sleep(0.5)
            print(f"🎵 {name} is playing with {effective_volume:.2f} volume")

def simulate_event_audio():
    """Simulate an immersive audio experience for an event."""
    engine = AudioEngine()
    
    # Set listener position (e.g., center of the event space)
    engine.set_listener_position(0, 0, 0)
    
    # Create audio sources for different parts of the event
    main_stage = AudioSource("Main Stage", 10, 0, 0)
    main_stage.add_effect(AudioEffectType.REVERB)
    main_stage.add_effect(AudioEffectType.SPATIAL)
    main_stage.set_volume(0.9)
    
    lounge_area = AudioSource("Lounge Area", -5, 8, 0)
    lounge_area.add_effect(AudioEffectType.AMBIENT)
    lounge_area.set_volume(0.6)
    
    entrance = AudioSource("Entrance", 0, -15, 0)
    entrance.add_effect(AudioEffectType.ECHO)
    entrance.set_volume(0.7)
    
    # Add sources to engine
    engine.add_source(main_stage)
    engine.add_source(lounge_area)
    engine.add_source(entrance)
    
    # Simulate dynamic changes during the event
    print("Starting event audio simulation...")
    for i in range(3):
        print(f"\n=== Event Phase {i+1} ===")
        
        # Randomly adjust some parameters
        for source in engine.sources.values():
            if random.random() > 0.5:
                source.set_volume(max(0.1, source.volume + random.uniform(-0.2, 0.2)))
            
            if random.random() > 0.7 and source.effects:
                effect_to_toggle = random.choice(source.effects)
                source.remove_effect(effect_to_toggle)
                print(f"Toggled off {effect_to_toggle.value} effect for {source.name}")
            elif random.random() > 0.7:
                new_effect = random.choice(list(AudioEffectType))
                source.add_effect(new_effect)
                print(f"Added {new_effect.value} effect to {source.name}")
        
        # Play all sources
        engine.play_all()
        time.sleep(1)
    
    print("\nEvent audio simulation complete.")

if __name__ == "__main__":
    simulate_event_audio()
```
