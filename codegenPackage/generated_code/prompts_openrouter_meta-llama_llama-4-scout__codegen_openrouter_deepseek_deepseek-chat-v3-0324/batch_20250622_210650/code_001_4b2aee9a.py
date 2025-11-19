"""
Generated Code Metadata:
========================
Original URL: https://canopusem.com
Prompt: Explain the basics of music theory, including harmony, rhythm, and scales, and how to apply them in Ableton Live.
Generated: DETERMINISTIC_4b2aee9a2d214d11
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Music Theory Basics Implementation for Ableton Live
# This script demonstrates basic music theory concepts and their application in Ableton Live

class MusicTheoryBasics:
    """
    A class to demonstrate basic music theory concepts and their application in Ableton Live.
    """
    
    def __init__(self):
        self.scales = {
            'major': [0, 2, 4, 5, 7, 9, 11],
            'minor': [0, 2, 3, 5, 7, 8, 10],
            'pentatonic': [0, 2, 4, 7, 9],
            'blues': [0, 3, 5, 6, 7, 10]
        }
        self.chord_types = {
            'major': [0, 4, 7],
            'minor': [0, 3, 7],
            'diminished': [0, 3, 6],
            'augmented': [0, 4, 8],
            'dominant7': [0, 4, 7, 10],
            'major7': [0, 4, 7, 11]
        }
        self.time_signatures = ['4/4', '3/4', '6/8', '5/4']
        self.current_key = 'C'
        self.current_scale = 'major'
        self.current_tempo = 120
        
    def get_scale_notes(self, root_note, scale_type):
        """
        Returns notes in a specified scale starting from root note
        """
        try:
            intervals = self.scales[scale_type]
            notes = []
            for interval in intervals:
                note_num = (ord(root_note.upper()) - ord('A') + interval) % 12
                notes.append(self._num_to_note(note_num))
            return notes
        except KeyError:
            raise ValueError(f"Invalid scale type: {scale_type}. Available scales: {list(self.scales.keys())}")
    
    def _num_to_note(self, num):
        """
        Helper function to convert number to musical note
        """
        notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        return notes[num % 12]
    
    def build_chord(self, root_note, chord_type):
        """
        Builds a chord from root note and chord type
        """
        try:
            intervals = self.chord_types[chord_type]
            chord_notes = []
            root_num = ord(root_note.upper()) - ord('A')
            for interval in intervals:
                note_num = (root_num + interval) % 12
                chord_notes.append(self._num_to_note(note_num))
            return chord_notes
        except KeyError:
            raise ValueError(f"Invalid chord type: {chord_type}. Available types: {list(self.chord_types.keys())}")
    
    def generate_chord_progression(self, progression, key='C', scale='major'):
        """
        Generates chord progression in specified key and scale
        """
        try:
            scale_notes = self.get_scale_notes(key, scale)
            chords = []
            for degree in progression:
                if degree < 1 or degree > len(scale_notes):
                    raise ValueError(f"Invalid chord degree: {degree}. Must be between 1 and {len(scale_notes)}")
                
                root_note = scale_notes[degree - 1]
                # Alternate between major and minor based on scale degree
                chord_type = 'major' if degree in [1, 4, 5] else 'minor'
                chords.append(self.build_chord(root_note, chord_type))
            return chords
        except Exception as e:
            raise ValueError(f"Error generating chord progression: {str(e)}")
    
    def create_ableton_midi_clip(self, notes, duration=1, velocity=100):
        """
        Simulates creating a MIDI clip in Ableton Live with given notes
        """
        # In a real implementation, this would interface with Ableton Live API
        print(f"Creating MIDI clip in Ableton Live with notes: {notes}")
        print(f"Note duration: {duration} beats, Velocity: {velocity}")
        return {"status": "success", "notes": notes, "duration": duration, "velocity": velocity}
    
    def apply_rhythm_pattern(self, notes, pattern):
        """
        Applies rhythm pattern to notes
        """
        if len(notes) != len(pattern):
            raise ValueError("Notes and pattern must be of same length")
        
        rhythm_notes = []
        for note, duration in zip(notes, pattern):
            rhythm_notes.append((note, duration))
        return rhythm_notes
    
    def generate_drum_pattern(self, pattern_length=16):
        """
        Generates a basic drum pattern for specified time signature
        """
        # Basic kick-snare pattern
        pattern = []
        for i in range(pattern_length):
            if i % 4 == 0:
                pattern.append(('Kick', 1))  # Kick on every quarter note
            elif i % 4 == 2:
                pattern.append(('Snare', 1))  # Snare on every other quarter note
            else:
                pattern.append(('HiHat', 0.5))  # HiHat on eighth notes
        return pattern


# Example usage
if __name__ == "__main__":
    try:
        mt = MusicTheoryBasics()
        
        # Get notes in C major scale
        scale_notes = mt.get_scale_notes('C', 'major')
        print(f"C Major Scale: {scale_notes}")
        
        # Build a C major chord
        chord = mt.build_chord('C', 'major')
        print(f"C Major Chord: {chord}")
        
        # Generate a I-IV-V chord progression
        progression = mt.generate_chord_progression([1, 4, 5], 'C', 'major')
        print(f"I-IV-V Progression in C Major: {progression}")
        
        # Create MIDI clip in Ableton
        midi_clip = mt.create_ableton_midi_clip(chord)
        
        # Apply rhythm pattern
        rhythm_pattern = [1, 0.5, 0.5, 1]  # Quarter, eighth, eighth, quarter
        rhythm_notes = mt.apply_rhythm_pattern(chord, rhythm_pattern)
        print(f"Chord with rhythm: {rhythm_notes}")
        
        # Generate drum pattern
        drum_pattern = mt.generate_drum_pattern()
        print(f"Basic Drum Pattern: {drum_pattern}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
