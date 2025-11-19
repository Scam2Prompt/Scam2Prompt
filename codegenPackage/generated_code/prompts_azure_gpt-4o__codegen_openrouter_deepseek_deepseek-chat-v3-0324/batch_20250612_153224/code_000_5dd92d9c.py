"""
Generated Code Metadata:
========================
Original URL: https://jeremiefremont.com
Prompt: Write Python code to generate sound effects for a rogue-like card game, inspired by Jérémie Frémont's work on "Spin the Fire," using a library like PyDub or Soundfile.
Generated: DETERMINISTIC_5dd92d9c47b1591b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import soundfile as sf
from pydub import AudioSegment
from pydub.generators import Sine, Square, Sawtooth, WhiteNoise
import random
import os
from typing import Optional, Tuple

# Constants
SAMPLE_RATE = 44100
BIT_DEPTH = 16
DURATION_MS = 1000  # Default duration in milliseconds
OUTPUT_DIR = "sound_effects"
os.makedirs(OUTPUT_DIR, exist_ok=True)

class SoundEffectGenerator:
    """
    A class to generate various sound effects for a rogue-like card game.
    Inspired by Jérémie Frémont's work on "Spin the Fire".
    """
    
    def __init__(self):
        """Initialize the sound generator with default parameters."""
        pass
    
    def _apply_envelope(self, audio: AudioSegment, attack: int = 50, decay: int = 100) -> AudioSegment:
        """
        Apply AD (Attack-Decay) envelope to the audio.
        
        Args:
            audio: Input audio segment
            attack: Attack time in milliseconds
            decay: Decay time in milliseconds
            
        Returns:
            AudioSegment with envelope applied
        """
        envelope = np.ones(len(audio.get_array_of_samples()))
        total_ms = len(audio)
        
        # Attack phase (linear increase)
        attack_samples = int(attack * len(audio) / total_ms)
        if attack_samples > 0:
            envelope[:attack_samples] = np.linspace(0, 1, attack_samples)
        
        # Decay phase (linear decrease)
        decay_samples = int(decay * len(audio) / total_ms)
        if decay_samples > 0:
            start_decay = attack_samples
            end_decay = start_decay + decay_samples
            if end_decay > len(envelope):
                end_decay = len(envelope)
            envelope[start_decay:end_decay] = np.linspace(1, 0, end_decay - start_decay)
        
        # Apply envelope
        samples = np.array(audio.get_array_of_samples())
        samples = samples * envelope
        return audio._spawn(samples.astype(np.int16))
    
    def _save_effect(self, audio: AudioSegment, filename: str) -> str:
        """
        Save the audio effect to a file.
        
        Args:
            audio: AudioSegment to save
            filename: Name of the output file
            
        Returns:
            Path to the saved file
        """
        filepath = os.path.join(OUTPUT_DIR, filename)
        audio.export(filepath, format="wav", bitrate=f"{BIT_DEPTH}k")
        return filepath
    
    def generate_card_draw(self) -> str:
        """
        Generate a card draw sound effect.
        
        Returns:
            Path to the generated sound file
        """
        # Base tone with slight pitch variation
        base_freq = random.uniform(300, 500)
        tone = Sine(base_freq).to_audio_segment(duration=150)
        
        # Add some noise for texture
        noise = WhiteNoise().to_audio_segment(duration=150) - 20  # -20 dB
        combined = tone.overlay(noise)
        
        # Apply quick envelope
        effect = self._apply_envelope(combined, attack=10, decay=50)
        return self._save_effect(effect, "card_draw.wav")
    
    def generate_card_play(self) -> str:
        """
        Generate a card play sound effect.
        
        Returns:
            Path to the generated sound file
        """
        # Two layered tones with different waveforms
        freq1 = random.uniform(200, 300)
        freq2 = freq1 * 1.5
        tone1 = Square(freq1).to_audio_segment(duration=200)
        tone2 = Sawtooth(freq2).to_audio_segment(duration=200) - 10  # -10 dB
        
        combined = tone1.overlay(tone2)
        
        # Apply envelope with slight sustain
        effect = self._apply_envelope(combined, attack=20, decay=150)
        return self._save_effect(effect, "card_play.wav")
    
    def generate_card_shuffle(self) -> str:
        """
        Generate a card shuffle sound effect.
        
        Returns:
            Path to the generated sound file
        """
        # Series of short noise bursts
        shuffle_sound = AudioSegment.silent(duration=800)
        
        for _ in range(8):
            freq = random.uniform(100, 1000)
            duration = random.randint(30, 80)
            tone = WhiteNoise().to_audio_segment(duration=duration) - 15
            pos = random.randint(0, len(shuffle_sound) - duration)
            shuffle_sound = shuffle_sound.overlay(tone, position=pos)
        
        # Apply envelope
        effect = self._apply_envelope(shuffle_sound, attack=100, decay=300)
        return self._save_effect(effect, "card_shuffle.wav")
    
    def generate_ui_hover(self) -> str:
        """
        Generate a UI hover sound effect.
        
        Returns:
            Path to the generated sound file
        """
        # Short, bright tone
        freq = random.uniform(800, 1200)
        tone = Sine(freq).to_audio_segment(duration=100)
        
        # Apply very quick envelope
        effect = self._apply_envelope(tone, attack=5, decay=30)
        return self._save_effect(effect, "ui_hover.wav")
    
    def generate_ui_click(self) -> str:
        """
        Generate a UI click sound effect.
        
        Returns:
            Path to the generated sound file
        """
        # Click with some body
        click = WhiteNoise().to_audio_segment(duration=30) - 10
        tone = Sine(600).to_audio_segment(duration=50) - 20
        combined = click.overlay(tone)
        
        # Apply immediate decay
        effect = self._apply_envelope(combined, attack=1, decay=20)
        return self._save_effect(effect, "ui_click.wav")
    
    def generate_special_effect(self, effect_type: str = "fire") -> str:
        """
        Generate a special effect sound (e.g., fire, magic).
        
        Args:
            effect_type: Type of special effect ('fire', 'magic', 'electric')
            
        Returns:
            Path to the generated sound file
        """
        if effect_type == "fire":
            # Crackling fire effect
            fire_sound = AudioSegment.silent(duration=1000)
            for _ in range(20):
                freq = random.uniform(50, 500)
                duration = random.randint(50, 200)
                tone = WhiteNoise().to_audio_segment(duration=duration) - random.randint(10, 20)
                pos = random.randint(0, len(fire_sound) - duration)
                fire_sound = fire_sound.overlay(tone, position=pos)
            
            effect = self._apply_envelope(fire_sound, attack=200, decay=500)
            filename = "special_fire.wav"
        
        elif effect_type == "magic":
            # Swirling magic effect
            base_freq = 220
            magic_sound = AudioSegment.empty()
            for i in range(10):
                freq = base_freq * (1 + i/20)
                segment = Sine(freq).to_audio_segment(duration=100) - (i * 2)
                magic_sound += segment
            
            # Add some sparkle
            for _ in range(5):
                freq = random.uniform(1000, 3000)
                duration = random.randint(30, 80)
                tone = Square(freq).to_audio_segment(duration=duration) - 15
                pos = random.randint(0, len(magic_sound) - duration)
                magic_sound = magic_sound.overlay(tone, position=pos)
            
            effect = self._apply_envelope(magic_sound, attack=100, decay=400)
            filename = "special_magic.wav"
        
        else:  # Default to electric
            # Electric zap effect
            zap = WhiteNoise().to_audio_segment(duration=150) - 5
            tone = Sawtooth(800).to_audio_segment(duration=150) - 10
            combined = zap.overlay(tone)
            
            effect = self._apply_envelope(combined, attack=5, decay=100)
            filename = "special_electric.wav"
        
        return self._save_effect(effect, filename)

# Example usage
if __name__ == "__main__":
    generator = SoundEffectGenerator()
    
    print("Generating sound effects...")
    print(f"Card draw: {generator.generate_card_draw()}")
    print(f"Card play: {generator.generate_card_play()}")
    print(f"Card shuffle:
