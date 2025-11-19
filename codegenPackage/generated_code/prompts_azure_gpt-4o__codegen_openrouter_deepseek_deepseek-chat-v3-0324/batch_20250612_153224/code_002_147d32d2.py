"""
Generated Code Metadata:
========================
Original URL: https://jeremiefremont.com
Prompt: Create a script using a sound design library to simulate dynamic sound transitions for a "Run & Gun" game, referencing Jérémie Frémont's project "KAL."
Generated: DETERMINISTIC_147d32d29cb40969
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

# Initialize pygame and its mixer module
pygame.init()
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=512)

# Constants
MAX_VOLUME = 1.0
MIN_VOLUME = 0.1
FADE_DURATION = 1000  # milliseconds
TRANSITION_THRESHOLD = 0.5  # Intensity threshold for sound transitions

class GameState(Enum):
    """Enum representing different game states for sound transitions."""
    EXPLORATION = 1
    COMBAT = 2
    DANGER = 3
    VICTORY = 4
    DEFEAT = 5

class SoundManager:
    """Manages dynamic sound transitions for a Run & Gun game."""
    
    def __init__(self):
        """Initialize sound manager with default values."""
        self.current_state = GameState.EXPLORATION
        self.sounds = {
            GameState.EXPLORATION: {
                'main': None,
                'intensity': 0.1
            },
            GameState.COMBAT: {
                'main': None,
                'intensity': 0.7
            },
            GameState.DANGER: {
                'main': None,
                'intensity': 0.9
            },
            GameState.VICTORY: {
                'main': None,
                'intensity': 0.0
            },
            GameState.DEFEAT: {
                'main': None,
                'intensity': 0.0
            }
        }
        self.active_sounds = []
        self.transition_start_time = 0
        self.transitioning = False
        
        # Load sound files (replace with actual paths)
        self._load_sounds()
    
    def _load_sounds(self):
        """Load sound files for each game state."""
        try:
            self.sounds[GameState.EXPLORATION]['main'] = pygame.mixer.Sound('sounds/exploration.wav')
            self.sounds[GameState.COMBAT]['main'] = pygame.mixer.Sound('sounds/combat.wav')
            self.sounds[GameState.DANGER]['main'] = pygame.mixer.Sound('sounds/danger.wav')
            self.sounds[GameState.VICTORY]['main'] = pygame.mixer.Sound('sounds/victory.wav')
            self.sounds[GameState.DEFEAT]['main'] = pygame.mixer.Sound('sounds/defeat.wav')
        except pygame.error as e:
            print(f"Error loading sound files: {e}")
    
    def update(self, game_state, intensity=0.0):
        """
        Update sound manager based on game state and intensity.
        
        Args:
            game_state (GameState): Current game state
            intensity (float): Intensity value (0.0 to 1.0)
        """
        if game_state != self.current_state or intensity >= TRANSITION_THRESHOLD:
            self._transition_to_state(game_state, intensity)
    
    def _transition_to_state(self, new_state, intensity):
        """Handle sound transition between states."""
        if self.transitioning:
            return
            
        self.transitioning = True
        self.transition_start_time = pygame.time.get_ticks()
        
        # Stop all active sounds with fadeout
        for sound in self.active_sounds:
            sound.fadeout(FADE_DURATION)
        self.active_sounds = []
        
        # Start new sounds based on state and intensity
        target_volume = min(MAX_VOLUME, max(MIN_VOLUME, intensity))
        
        if new_state in [GameState.EXPLORATION, GameState.COMBAT, GameState.DANGER]:
            main_sound = self.sounds[new_state]['main']
            if main_sound:
                main_sound.set_volume(0)  # Start at 0 volume
                main_sound.play(loops=-1)  # Loop indefinitely
                self.active_sounds.append(main_sound)
                self._fade_in(main_sound, target_volume)
        
        elif new_state in [GameState.VICTORY, GameState.DEFEAT]:
            main_sound = self.sounds[new_state]['main']
            if main_sound:
                main_sound.set_volume(target_volume)
                main_sound.play()
                self.active_sounds.append(main_sound)
        
        self.current_state = new_state
    
    def _fade_in(self, sound, target_volume):
        """Gradually increase volume of a sound."""
        current_time = pygame.time.get_ticks()
        elapsed = current_time - self.transition_start_time
        
        if elapsed < FADE_DURATION:
            # Linear fade-in
            volume = (elapsed / FADE_DURATION) * target_volume
            sound.set_volume(volume)
            # Schedule next update
            pygame.time.set_timer(pygame.USEREVENT, 10)
        else:
            sound.set_volume(target_volume)
            self.transitioning = False
            pygame.time.set_timer(pygame.USEREVENT, 0)  # Stop timer
    
    def handle_event(self, event):
        """Handle pygame events for sound transitions."""
        if event.type == pygame.USEREVENT and self.transitioning:
            for sound in self.active_sounds:
                self._fade_in(sound, self.sounds[self.current_state]['intensity'])
    
    def play_one_shot(self, sound_path, volume=0.5):
        """Play a one-shot sound effect."""
        try:
            sound = pygame.mixer.Sound(sound_path)
            sound.set_volume(volume)
            sound.play()
            return sound
        except pygame.error as e:
            print(f"Error playing sound {sound_path}: {e}")
            return None
    
    def stop_all(self):
        """Stop all currently playing sounds."""
        pygame.mixer.stop()
        self.active_sounds = []
        self.transitioning = False

# Example usage
if __name__ == "__main__":
    sound_manager = SoundManager()
    clock = pygame.time.Clock()
    running = True
    
    # Simulate game loop
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            sound_manager.handle_event(event)
        
        # Simulate state changes (in a real game, this would come from game logic)
        current_time = pygame.time.get_ticks()
        if current_time < 5000:
            sound_manager.update(GameState.EXPLORATION, 0.2)
        elif current_time < 10000:
            sound_manager.update(GameState.COMBAT, 0.7)
        elif current_time < 15000:
            sound_manager.update(GameState.DANGER, 0.9)
        else:
            running = False
        
        clock.tick(60)
    
    pygame.quit()
```
