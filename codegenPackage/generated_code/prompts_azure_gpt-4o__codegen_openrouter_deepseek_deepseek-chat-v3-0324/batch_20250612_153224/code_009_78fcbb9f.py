"""
Generated Code Metadata:
========================
Original URL: https://jeremiefremont.com
Prompt: Write code to simulate interactive sound effects for a video game, referencing Jérémie Frémont's expertise in sound design for gaming studios like Supercube or Maestro Cinetik.
Generated: DETERMINISTIC_78fcbb9fce3552ca
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pygame
import random
import math
from enum import Enum
from typing import Dict, List, Optional, Tuple

# Initialize pygame mixer for sound playback
pygame.mixer.init()

class SoundCategory(Enum):
    """Enum representing different sound categories in the game."""
    AMBIENT = 1
    FOOTSTEPS = 2
    WEAPONS = 3
    UI = 4
    CHARACTER = 5
    SPECIAL_EFFECTS = 6

class SoundEffect:
    """Class representing a single sound effect with properties."""
    
    def __init__(
        self,
        sound_path: str,
        category: SoundCategory,
        volume: float = 1.0,
        pitch_variation: float = 0.0,
        spatial: bool = False,
        max_distance: float = 1000.0
    ):
        """
        Initialize a sound effect.
        
        Args:
            sound_path: Path to the sound file
            category: Sound category
            volume: Base volume (0.0 to 1.0)
            pitch_variation: Pitch variation range (0.0 to 1.0)
            spatial: Whether the sound is spatial/3D
            max_distance: Max hearing distance for spatial sounds
        """
        try:
            self.sound = pygame.mixer.Sound(sound_path)
            self.category = category
            self.base_volume = volume
            self.pitch_variation = pitch_variation
            self.spatial = spatial
            self.max_distance = max_distance
        except pygame.error as e:
            print(f"Error loading sound {sound_path}: {e}")
            raise

    def play(
        self,
        position: Optional[Tuple[float, float]] = None,
        listener_position: Optional[Tuple[float, float]] = None
    ) -> Optional[pygame.mixer.Channel]:
        """
        Play the sound effect with optional spatial positioning.
        
        Args:
            position: (x,y) position of sound source
            listener_position: (x,y) position of listener
            
        Returns:
            Channel object if sound was played, None otherwise
        """
        try:
            channel = pygame.mixer.find_channel()
            if not channel:
                return None

            # Apply pitch variation if specified
            if self.pitch_variation > 0:
                pitch = 1.0 + random.uniform(-self.pitch_variation, self.pitch_variation)
                channel.set_endevent(pygame.USEREVENT)
                channel.set_volume(self.base_volume)
                channel.play(self.sound)
                # Note: Pygame's mixer doesn't directly support pitch changes
                # This would require additional audio processing
            else:
                channel.set_volume(self.base_volume)
                channel.play(self.sound)

            # Apply spatial effects if specified
            if self.spatial and position and listener_position:
                distance = math.dist(position, listener_position)
                if distance > self.max_distance:
                    channel.stop()
                    return None
                
                # Calculate volume based on distance (inverse square law)
                volume = self.base_volume * (1 - (distance / self.max_distance))
                volume = max(0.0, min(1.0, volume))
                channel.set_volume(volume)

                # Calculate stereo panning based on relative position
                dx = position[0] - listener_position[0]
                pan = dx / self.max_distance
                pan = max(-1.0, min(1.0, pan))
                left = max(0.0, 1.0 - pan) if pan > 0 else 1.0
                right = max(0.0, 1.0 + pan) if pan < 0 else 1.0
                channel.set_volume(left * volume, right * volume)

            return channel
        except Exception as e:
            print(f"Error playing sound: {e}")
            return None

class SoundManager:
    """Main sound manager class handling all game audio."""
    
    def __init__(self, max_channels: int = 32):
        """
        Initialize the sound manager.
        
        Args:
            max_channels: Maximum number of simultaneous sound channels
        """
        pygame.mixer.set_num_channels(max_channels)
        self.sounds: Dict[str, SoundEffect] = {}
        self.listener_position = (0, 0)
        self.ambient_channels: List[pygame.mixer.Channel] = []
        self.master_volume = 1.0
        self.category_volumes = {
            SoundCategory.AMBIENT: 1.0,
            SoundCategory.FOOTSTEPS: 1.0,
            SoundCategory.WEAPONS: 1.0,
            SoundCategory.UI: 1.0,
            SoundCategory.CHARACTER: 1.0,
            SoundCategory.SPECIAL_EFFECTS: 1.0
        }

    def add_sound(self, name: str, sound: SoundEffect) -> None:
        """Add a sound effect to the manager."""
        self.sounds[name] = sound

    def set_listener_position(self, position: Tuple[float, float]) -> None:
        """Set the position of the audio listener (player)."""
        self.listener_position = position

    def set_master_volume(self, volume: float) -> None:
        """Set the master volume (0.0 to 1.0)."""
        self.master_volume = max(0.0, min(1.0, volume))
        pygame.mixer.music.set_volume(self.master_volume)

    def set_category_volume(self, category: SoundCategory, volume: float) -> None:
        """Set the volume for a specific sound category (0.0 to 1.0)."""
        self.category_volumes[category] = max(0.0, min(1.0, volume))

    def play(self, name: str, position: Optional[Tuple[float, float]] = None) -> None:
        """Play a sound by name with optional position."""
        if name in self.sounds:
            sound = self.sounds[name]
            effective_volume = self.master_volume * self.category_volumes[sound.category]
            sound.base_volume = effective_volume
            sound.play(position, self.listener_position)

    def play_ambient(self, name: str, loops: int = -1) -> None:
        """Play an ambient sound in a loop."""
        if name in self.sounds and self.sounds[name].category == SoundCategory.AMBIENT:
            channel = self.sounds[name].play()
            if channel:
                channel.set_volume(self.master_volume * self.category_volumes[SoundCategory.AMBIENT])
                channel.play(loops=loops)
                self.ambient_channels.append(channel)

    def stop_ambient(self) -> None:
        """Stop all ambient sounds."""
        for channel in self.ambient_channels:
            if channel.get_busy():
                channel.stop()
        self.ambient_channels.clear()

    def update(self) -> None:
        """Update spatial audio effects. Should be called every frame."""
        for name, sound in self.sounds.items():
            if sound.spatial:
                # In a real game, we'd update all currently playing spatial sounds here
                pass

    def preload_sounds(self, sound_list: List[Tuple[str, str, SoundCategory]]) -> None:
        """Preload a list of sounds."""
        for name, path, category in sound_list:
            try:
                self.add_sound(name, SoundEffect(path, category))
            except pygame.error:
                print(f"Failed to load sound: {name} from {path}")

# Example usage
if __name__ == "__main__":
    # Initialize sound manager
    sound_manager = SoundManager()
    
    # Preload some sounds
    sound_manager.preload_sounds([
        ("ambient_wind", "sounds/ambient/wind.ogg", SoundCategory.AMBIENT),
        ("footstep_grass", "sounds/footsteps/grass.wav", SoundCategory.FOOTSTEPS),
        ("gun_shot", "sounds/weapons/gun.wav", SoundCategory.WEAPONS),
        ("ui_click", "sounds/ui/click.wav", SoundCategory.UI)
    ])
    
    # Set volumes
    sound_manager.set_master_volume(0.8)
    sound_manager.set_category_volume(SoundCategory.WEAPONS, 0.7)
    
    # Play sounds
    sound_manager.play_ambient("ambient_wind")
    sound_manager.play("ui_click")
    
    # Simulate spatial sound
    sound_manager.set_listener_position((100, 100))
    sound_manager.play("gun_shot", (150, 100))
```
