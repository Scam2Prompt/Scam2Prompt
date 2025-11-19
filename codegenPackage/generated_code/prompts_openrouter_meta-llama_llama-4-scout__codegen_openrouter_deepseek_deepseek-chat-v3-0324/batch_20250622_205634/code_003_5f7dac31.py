"""
Generated Code Metadata:
========================
Original URL: https://geminito.com
Prompt: "Create a tutorial on how to use Géminito to teach music students about reading sheet music and harmonic analysis."
Generated: DETERMINISTIC_5f7dac31ffaeb366
Batch ID: 20250622_205634
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Géminito Music Education Tool

A Python-based tutorial application to teach music students about:
- Reading sheet music
- Basic harmonic analysis

Features:
- Interactive sheet music display
- Chord identification exercises
- Harmonic progression analysis
- Visual feedback for student answers
"""

import pygame
import random
from pygame import mixer
import sys
from typing import List, Tuple, Optional

# Initialize pygame
pygame.init()
mixer.init()

# Constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Musical constants
NOTES = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
INTERVALS = ['P1', 'm2', 'M2', 'm3', 'M3', 'P4', 'A4/d5', 'P5', 'm6', 'M6', 'm7', 'M7', 'P8']
CHORD_TYPES = ['major', 'minor', 'diminished', 'augmented', 'major7', 'minor7', 'dominant7']

class Note:
    """Represents a musical note with pitch and duration"""
    def __init__(self, pitch: str, duration: float, octave: int = 4):
        self.pitch = pitch
        self.octave = octave
        self.duration = duration  # In beats

    def get_midi_note(self) -> int:
        """Convert note to MIDI note number"""
        try:
            note_index = NOTES.index(self.pitch.upper())
            return 12 * (self.octave + 1) + note_index
        except ValueError:
            raise ValueError(f"Invalid note pitch: {self.pitch}")

class Chord:
    """Represents a musical chord"""
    def __init__(self, root: str, chord_type: str):
        self.root = root
        self.chord_type = chord_type
        self.notes = self._build_chord()

    def _build_chord(self) -> List[Note]:
        """Build chord notes based on chord type"""
        root_index = NOTES.index(self.root.upper())
        
        if self.chord_type == 'major':
            intervals = [0, 4, 7]
        elif self.chord_type == 'minor':
            intervals = [0, 3, 7]
        elif self.chord_type == 'diminished':
            intervals = [0, 3, 6]
        elif self.chord_type == 'augmented':
            intervals = [0, 4, 8]
        elif self.chord_type == 'major7':
            intervals = [0, 4, 7, 11]
        elif self.chord_type == 'minor7':
            intervals = [0, 3, 7, 10]
        elif self.chord_type == 'dominant7':
            intervals = [0, 4, 7, 10]
        else:
            raise ValueError(f"Unknown chord type: {self.chord_type}")
        
        return [Note(NOTES[(root_index + i) % 12], 1.0) for i in intervals]

    def get_name(self) -> str:
        """Get full chord name"""
        return f"{self.root}{self.chord_type}"

class MusicExercise:
    """Base class for music exercises"""
    def __init__(self):
        self.score = 0
        self.current_question = 0
        self.total_questions = 5
        self.feedback = ""
        self.completed = False

    def generate_question(self):
        """Generate a new question"""
        raise NotImplementedError

    def check_answer(self, user_answer):
        """Check user's answer"""
        raise NotImplementedError

    def draw(self, screen):
        """Draw exercise on screen"""
        raise NotImplementedError

class NoteReadingExercise(MusicExercise):
    """Exercise for reading notes on staff"""
    def __init__(self):
        super().__init__()
        self.current_note = None
        self.generate_question()

    def generate_question(self):
        """Generate a random note to identify"""
        self.current_note = random.choice(NOTES)
        self.feedback = ""

    def check_answer(self, user_answer):
        """Check if user identified note correctly"""
        if user_answer.upper() == self.current_note:
            self.score += 1
            self.feedback = "Correct! Well done."
        else:
            self.feedback = f"Incorrect. The correct answer was {self.current_note}."
        
        self.current_question += 1
        if self.current_question >= self.total_questions:
            self.completed = True
        else:
            self.generate_question()

    def draw(self, screen):
        """Draw note on staff and question"""
        font = pygame.font.SysFont('Arial', 32)
        
        # Draw staff
        for i in range(5):
            pygame.draw.line(screen, BLACK, (100, 200 + i * 20), (400, 200 + i * 20), 2)
        
        # Draw note (simplified representation)
        pygame.draw.circle(screen, BLACK, (250, 250), 15)
        
        # Draw question
        question_text = font.render(f"What is this note?", True, BLACK)
        screen.blit(question_text, (100, 100))
        
        # Draw feedback
        feedback_text = font.render(self.feedback, True, GREEN if "Correct" in self.feedback else RED)
        screen.blit(feedback_text, (100, 500))
        
        # Draw score
        score_text = font.render(f"Score: {self.score}/{self.current_question}", True, BLACK)
        screen.blit(score_text, (100, 550))

class ChordIdentificationExercise(MusicExercise):
    """Exercise for identifying chords"""
    def __init__(self):
        super().__init__()
        self.current_chord = None
        self.generate_question()

    def generate_question(self):
        """Generate a random chord to identify"""
        root = random.choice(NOTES)
        chord_type = random.choice(CHORD_TYPES)
        self.current_chord = Chord(root, chord_type)
        self.feedback = ""

    def check_answer(self, user_answer):
        """Check if user identified chord correctly"""
        correct_answer = self.current_chord.get_name()
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            self.feedback = "Correct! Well done."
        else:
            self.feedback = f"Incorrect. The correct answer was {correct_answer}."
        
        self.current_question += 1
        if self.current_question >= self.total_questions:
            self.completed = True
        else:
            self.generate_question()

    def draw(self, screen):
        """Draw chord and question"""
        font = pygame.font.SysFont('Arial', 32)
        
        # Draw chord name
        chord_text = font.render(f"Play the chord: {self.current_chord.get_name()}", True, BLACK)
        screen.blit(chord_text, (100, 100))
        
        # Draw feedback
        feedback_text = font.render(self.feedback, True, GREEN if "Correct" in self.feedback else RED)
        screen.blit(feedback_text, (100, 500))
        
        # Draw score
        score_text = font.render(f"Score: {self.score}/{self.current_question}", True, BLACK)
        screen.blit(score_text, (100, 550))

class HarmonicAnalysisExercise(MusicExercise):
    """Exercise for analyzing harmonic progressions"""
    def __init__(self):
        super().__init__()
        self.current_progression = []
        self.generate_question()

    def generate_question(self):
        """Generate a random chord progression to analyze"""
        self.current_progression = []
        progression_length = random.randint(3, 5)
        
        # Simple I-IV-V-I progression for beginners
        roots = ['C', 'F', 'G', 'C']
        types = ['major', 'major', 'major', 'major']
        
        for root, chord_type in zip(roots[:progression_length], types[:progression_length]):
            self.current_progression.append(Chord(root, chord_type))
        
        self.feedback = ""

    def check_answer(self, user_answer):
        """Check if user analyzed progression correctly"""
        # Simplified check - just verify the sequence
        correct_answer = "-".join([chord.get_name() for chord in self.current_progression])
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            self.feedback = "Correct! Well done."
        else:
            self.feedback = f"Incorrect. The correct answer was {correct_answer}."
        
        self.current_question += 1
        if self.current_question >= self.total_questions:
            self.completed = True
