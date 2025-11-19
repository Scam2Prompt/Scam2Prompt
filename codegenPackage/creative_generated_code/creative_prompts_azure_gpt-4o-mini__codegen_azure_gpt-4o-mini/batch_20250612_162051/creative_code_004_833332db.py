"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jeremiefremont.com
Prompt: Suggest a library for composing music for audiovisual projects, taking inspiration from Jérémie Frémont's experience in short films and documentaries.
Generated: DETERMINISTIC_833332db39b93658
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
music_composition.py

This script demonstrates the usage of the 'music21' library for composing music suitable for audiovisual projects.
The library allows for creating, analyzing, and manipulating music in a variety of formats.
This example includes basic error handling and demonstrates how to create a simple melody.

Requirements:
- Install music21: pip install music21
"""

from music21 import stream, note, meter, tempo, instrument, metadata

def create_music_piece():
    """
    Create a simple music piece with a melody.

    Returns:
        stream.Score: A music21 Score object containing the composed piece.
    """
    # Create a score to hold the music piece
    score = stream.Score()

    # Add metadata to the score
    score.metadata = metadata.Metadata()
    score.metadata.title = "Short Film Soundtrack"
    score.metadata.composer = "Music Composer"

    # Create a part for the melody
    melody_part = stream.Part()
    melody_part.id = "melody"

    # Define the time signature and tempo
    melody_part.append(meter.TimeSignature('4/4'))
    melody_part.append(tempo.MetronomeMark(number=120))

    # Define the instrument for the melody part
    melody_part.append(instrument.Piano())

    # Create a simple melody
    melody_notes = [
        note.Note("C4", quarterLength=1),
        note.Note("E4", quarterLength=1),
        note.Note("G4", quarterLength=1),
        note.Note("C5", quarterLength=1),
        note.Note("B4", quarterLength=1),
        note.Note("A4", quarterLength=1),
        note.Note("G4", quarterLength=1),
        note.Note("F4", quarterLength=1)
    ]

    # Add notes to the melody part
    for n in melody_notes:
        melody_part.append(n)

    # Add the melody part to the score
    score.append(melody_part)

    return score

def save_music_to_file(score, filename):
    """
    Save the composed music piece to a MIDI file.

    Args:
        score (stream.Score): The music score to be saved.
        filename (str): The name of the file to save the score to.
    """
    try:
        # Write the score to a MIDI file
        score.write('midi', fp=filename)
        print(f"Music piece saved successfully to {filename}")
    except Exception as e:
        print(f"An error occurred while saving the music piece: {e}")

if __name__ == "__main__":
    music_piece = create_music_piece()
    save_music_to_file(music_piece, "short_film_soundtrack.mid")
```
