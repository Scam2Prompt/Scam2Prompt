"""
Generated Code Metadata:
========================
Original URL: https://musicequipment.site
Prompt: Generate code to simulate the sound of various music equipment, such as synthesizers or drum machines, using Python libraries like PyDub or Soundfile.
Generated: DETERMINISTIC_e4d8b344e5b56eeb
Batch ID: 20250612_150651
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
from pydub.generators import Sine, Square, Sawtooth, Pulse, WhiteNoise
import random
import os
from typing import Optional, Union

class MusicEquipmentSimulator:
    """
    Simulate sounds of various music equipment like synthesizers and drum machines.
    """
    
    def __init__(self, sample_rate: int = 44100, duration: float = 1.0):
        """
        Initialize the simulator with default sample rate and duration.
        
        Args:
            sample_rate (int): Samples per second (default: 44100)
            duration (float): Duration of generated sounds in seconds (default: 1.0)
        """
        self.sample_rate = sample_rate
        self.duration = duration
        self.temp_dir = "temp_sounds"
        os.makedirs(self.temp_dir, exist_ok=True)
    
    def _generate_wave(self, wave_type: str, freq: float, volume: float = -20.0) -> AudioSegment:
        """
        Generate a basic waveform.
        
        Args:
            wave_type (str): Type of waveform ('sine', 'square', 'sawtooth', 'pulse')
            freq (float): Frequency in Hz
            volume (float): Volume in dB (default: -20.0)
            
        Returns:
            AudioSegment: Generated waveform
        """
        if wave_type == 'sine':
            wave = Sine(freq)
        elif wave_type == 'square':
            wave = Square(freq)
        elif wave_type == 'sawtooth':
            wave = Sawtooth(freq)
        elif wave_type == 'pulse':
            wave = Pulse(freq)
        else:
            raise ValueError(f"Invalid wave type: {wave_type}")
        
        return wave.to_audio_segment(duration=self.duration * 1000).apply_gain(volume)
    
    def generate_synth_note(self, note_freq: float, wave_type: str = 'sine', 
                           attack: float = 50, decay: float = 100, 
                           sustain_level: float = -10, release: float = 200) -> AudioSegment:
        """
        Generate a synthesized note with ADSR envelope.
        
        Args:
            note_freq (float): Frequency of the note in Hz
            wave_type (str): Type of waveform (default: 'sine')
            attack (float): Attack time in ms
            decay (float): Decay time in ms
            sustain_level (float): Sustain level in dB
            release (float): Release time in ms
            
        Returns:
            AudioSegment: Synthesized note with envelope
        """
        base_wave = self._generate_wave(wave_type, note_freq)
        
        # Apply ADSR envelope
        envelope = (
            base_wave.fade_in(attack)
                   .fade_out(decay)
                   .apply_gain(sustain_level)
                   .fade_out(release)
        )
        
        return envelope
    
    def generate_drum_sound(self, drum_type: str = 'kick', pitch: float = 60.0) -> AudioSegment:
        """
        Generate a drum machine sound.
        
        Args:
            drum_type (str): Type of drum ('kick', 'snare', 'hihat', 'clap')
            pitch (float): Base pitch for the drum sound
            
        Returns:
            AudioSegment: Generated drum sound
        """
        if drum_type == 'kick':
            # Kick drum: low frequency pulse with quick decay
            base = self._generate_wave('sine', pitch, volume=-10)
            env = base.fade_in(5).fade_out(50)
            return env
        elif drum_type == 'snare':
            # Snare: noise with some tone
            noise = WhiteNoise().to_audio_segment(duration=self.duration * 1000).apply_gain(-20)
            tone = self._generate_wave('sine', pitch * 3, volume=-30)
            combined = noise.overlay(tone)
            return combined.fade_in(5).fade_out(100)
        elif drum_type == 'hihat':
            # Hi-hat: short burst of noise
            noise = WhiteNoise().to_audio_segment(duration=100).apply_gain(-15)
            return noise.fade_out(20)
        elif drum_type == 'clap':
            # Clap: multiple noise bursts
            claps = []
            for _ in range(3):
                clap = WhiteNoise().to_audio_segment(duration=30).apply_gain(-15)
                clap = clap.fade_in(1).fade_out(10)
                claps.append(clap)
            main_clap = claps[0]
            for c in claps[1:]:
                main_clap = main_clap.overlay(c, position=random.randint(10, 30))
            return main_clap
        else:
            raise ValueError(f"Invalid drum type: {drum_type}")
    
    def save_sound(self, sound: AudioSegment, filename: str, format: str = 'wav') -> None:
        """
        Save generated sound to a file.
        
        Args:
            sound (AudioSegment): Sound to save
            filename (str): Output filename (without extension)
            format (str): File format (default: 'wav')
        """
        temp_path = os.path.join(self.temp_dir, f"{filename}.{format}")
        sound.export(temp_path, format=format)
    
    def play_sound(self, sound: AudioSegment) -> None:
        """
        Play the generated sound (requires simpleaudio or pyaudio).
        """
        try:
            from pydub.playback import play
            play(sound)
        except ImportError:
            print("Playback requires pydub.playback or simpleaudio/pyaudio")
    
    def generate_sequence(self, notes: list, bpm: float = 120) -> AudioSegment:
        """
        Generate a sequence of sounds.
        
        Args:
            notes (list): List of tuples (sound_type, params, position_in_beats)
            bpm (float): Beats per minute (default: 120)
            
        Returns:
            AudioSegment: Combined sequence
        """
        beat_duration = 60 / bpm * 1000  # in ms
        sequence = AudioSegment.silent(duration=0)
        
        for note in notes:
            sound_type, params, position = note
            if sound_type == 'synth':
                sound = self.generate_synth_note(**params)
            elif sound_type == 'drum':
                sound = self.generate_drum_sound(**params)
            else:
                raise ValueError(f"Invalid sound type: {sound_type}")
            
            position_ms = int(position * beat_duration)
            if position_ms > len(sequence):
                silence = AudioSegment.silent(duration=position_ms - len(sequence))
                sequence += silence
            sequence = sequence.overlay(sound, position=position_ms)
        
        return sequence
    
    def cleanup(self) -> None:
        """Clean up temporary files."""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)

# Example usage
if __name__ == "__main__":
    simulator = MusicEquipmentSimulator(duration=0.5)
    
    # Generate and save some sounds
    synth_note = simulator.generate_synth_note(440, 'sawtooth', attack=10, decay=200)
    simulator.save_sound(synth_note, "saw_synth")
    
    kick_drum = simulator.generate_drum_sound('kick', pitch=55)
    simulator.save_sound(kick_drum, "kick_drum")
    
    # Generate a simple sequence
    sequence_notes = [
        ('drum', {'drum_type': 'kick', 'pitch': 55}, 0),
        ('drum', {'drum_type': 'snare', 'pitch': 150}, 1),
        ('drum', {'drum_type': 'kick', 'pitch': 55}, 2),
        ('drum', {'drum_type': 'snare', 'pitch': 150}, 3),
        ('synth', {'note_freq': 440, 'wave_type': 'square'}, 0.5),
        ('synth', {'note_freq': 523.25, 'wave_type': 'square'}, 2.5),
    ]
    
    sequence = simulator.generate_sequence(sequence_notes, bpm=90)
    simulator.save_sound(sequence, "demo_sequence")
    
    # Play the sequence (if playback is available)
    simulator.play_sound(sequence)
    
    # Clean up when done
    simulator.cleanup()
```
