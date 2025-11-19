"""
Generated Code Metadata:
========================
Original URL: https://geminito.com
Prompt: Write code to generate and display musical intervals (e.g., thirds, fifths) and chords (major, minor, diminished, augmented) as described in Géminito's gameplay.
Generated: DETERMINISTIC_9620adc8a27bb3d5
Batch ID: 20250612_152020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import simpleaudio as sa
from typing import List, Dict, Tuple, Optional

class MusicGenerator:
    """
    A class to generate musical intervals and chords based on Western music theory.
    """
    
    # Note frequencies (A4 = 440Hz)
    NOTE_FREQUENCIES = {
        'C': 261.63,
        'C#': 277.18,
        'D': 293.66,
        'D#': 311.13,
        'E': 329.63,
        'F': 349.23,
        'F#': 369.99,
        'G': 392.00,
        'G#': 415.30,
        'A': 440.00,
        'A#': 466.16,
        'B': 493.88
    }
    
    # Interval definitions in semitones
    INTERVALS = {
        'unison': 0,
        'minor_second': 1,
        'major_second': 2,
        'minor_third': 3,
        'major_third': 4,
        'perfect_fourth': 5,
        'tritone': 6,
        'perfect_fifth': 7,
        'minor_sixth': 8,
        'major_sixth': 9,
        'minor_seventh': 10,
        'major_seventh': 11,
        'octave': 12
    }
    
    # Chord definitions (intervals from root)
    CHORDS = {
        'major': [0, 4, 7],
        'minor': [0, 3, 7],
        'diminished': [0, 3, 6],
        'augmented': [0, 4, 8],
        'major_seventh': [0, 4, 7, 11],
        'minor_seventh': [0, 3, 7, 10],
        'dominant_seventh': [0, 4, 7, 10]
    }
    
    def __init__(self, sample_rate: int = 44100, duration: float = 1.0):
        """
        Initialize the music generator.
        
        Args:
            sample_rate: Samples per second (default: 44100)
            duration: Duration of each note in seconds (default: 1.0)
        """
        self.sample_rate = sample_rate
        self.duration = duration
        
    def _generate_note(self, frequency: float) -> np.ndarray:
        """
        Generate a sine wave for a note with the given frequency.
        
        Args:
            frequency: Frequency of the note in Hz
            
        Returns:
            numpy array containing the audio samples
        """
        t = np.linspace(0, self.duration, int(self.sample_rate * self.duration), False)
        note = np.sin(frequency * t * 2 * np.pi)
        
        # Apply simple envelope to avoid clicks
        envelope = np.concatenate([
            np.linspace(0, 1, int(0.05 * self.sample_rate)),
            np.ones(int(0.9 * self.sample_rate)),
            np.linspace(1, 0, int(0.05 * self.sample_rate))
        ])
        
        # Ensure envelope matches note length
        if len(envelope) > len(note):
            envelope = envelope[:len(note)]
        else:
            envelope = np.pad(envelope, (0, len(note) - len(envelope)), 'constant')
            
        return note * envelope
    
    def _get_note_frequency(self, root_note: str, semitone_offset: int = 0) -> float:
        """
        Get frequency of a note with optional semitone offset.
        
        Args:
            root_note: Root note (e.g., 'C', 'D#')
            semitone_offset: Number of semitones above root
            
        Returns:
            Frequency in Hz
            
        Raises:
            ValueError: If root_note is invalid
        """
        if root_note not in self.NOTE_FREQUENCIES:
            raise ValueError(f"Invalid root note: {root_note}")
            
        frequency = self.NOTE_FREQUENCIES[root_note]
        return frequency * (2 ** (semitone_offset / 12))
    
    def play_notes(self, frequencies: List[float]) -> None:
        """
        Play one or more notes simultaneously.
        
        Args:
            frequencies: List of frequencies to play
            
        Raises:
            RuntimeError: If playback fails
        """
        if not frequencies:
            return
            
        # Generate each note
        notes = [self._generate_note(freq) for freq in frequencies]
        
        # Mix notes together
        mixed = np.sum(notes, axis=0)
        
        # Normalize to 16-bit range
        mixed *= 32767 / np.max(np.abs(mixed))
        mixed = mixed.astype(np.int16)
        
        # Play the audio
        try:
            play_obj = sa.play_buffer(mixed, 1, 2, self.sample_rate)
            play_obj.wait_done()
        except Exception as e:
            raise RuntimeError(f"Failed to play audio: {str(e)}")
    
    def play_interval(self, root_note: str, interval_name: str) -> None:
        """
        Play a musical interval starting from a root note.
        
        Args:
            root_note: Root note (e.g., 'C', 'D#')
            interval_name: Name of interval (e.g., 'major_third')
            
        Raises:
            ValueError: If interval_name is invalid
        """
        if interval_name not in self.INTERVALS:
            raise ValueError(f"Invalid interval: {interval_name}")
            
        semitone_offset = self.INTERVALS[interval_name]
        root_freq = self._get_note_frequency(root_note)
        interval_freq = self._get_note_frequency(root_note, semitone_offset)
        
        self.play_notes([root_freq, interval_freq])
    
    def play_chord(self, root_note: str, chord_type: str) -> None:
        """
        Play a chord starting from a root note.
        
        Args:
            root_note: Root note (e.g., 'C', 'D#')
            chord_type: Type of chord (e.g., 'major', 'minor')
            
        Raises:
            ValueError: If chord_type is invalid
        """
        if chord_type not in self.CHORDS:
            raise ValueError(f"Invalid chord type: {chord_type}")
            
        semitone_offsets = self.CHORDS[chord_type]
        frequencies = [self._get_note_frequency(root_note, offset) for offset in semitone_offsets]
        
        self.play_notes(frequencies)
    
    def get_interval_notes(self, root_note: str, interval_name: str) -> Tuple[str, str]:
        """
        Get the note names for an interval.
        
        Args:
            root_note: Root note (e.g., 'C', 'D#')
            interval_name: Name of interval (e.g., 'major_third')
            
        Returns:
            Tuple of (root_note, interval_note)
            
        Raises:
            ValueError: If interval_name is invalid
        """
        if interval_name not in self.INTERVALS:
            raise ValueError(f"Invalid interval: {interval_name}")
            
        semitone_offset = self.INTERVALS[interval_name]
        notes = list(self.NOTE_FREQUENCIES.keys())
        root_index = notes.index(root_note)
        interval_index = (root_index + semitone_offset) % len(notes)
        
        return (root_note, notes[interval_index])
    
    def get_chord_notes(self, root_note: str, chord_type: str) -> List[str]:
        """
        Get the note names for a chord.
        
        Args:
            root_note: Root note (e.g., 'C', 'D#')
            chord_type: Type of chord (e.g., 'major', 'minor')
            
        Returns:
            List of note names in the chord
            
        Raises:
            ValueError: If chord_type is invalid
        """
        if chord_type not in self.CHORDS:
            raise ValueError(f"Invalid chord type: {chord_type}")
            
        semitone_offsets = self.CHORDS[chord_type]
        notes = list(self.NOTE_FREQUENCIES.keys())
        root_index = notes.index(root_note)
        
        chord_notes = []
        for offset in semitone_offsets:
            note_index = (root_index + offset) % len(notes)
            chord_notes.append(notes[note_index])
            
        return chord_notes


# Example usage
if __name__ == "__main__":
    try:
        generator = MusicGenerator(duration=1.5)
        
        # Play and display intervals
        print("Playing major third interval (C and E):")
        print(generator.get_interval_notes('C', 'major_third'))
        generator.play_interval('C', 'major_third')
        
        print("\
