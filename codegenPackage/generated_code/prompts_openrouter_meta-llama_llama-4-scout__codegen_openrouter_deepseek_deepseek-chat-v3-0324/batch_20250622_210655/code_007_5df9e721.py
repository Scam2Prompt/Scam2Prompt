"""
Generated Code Metadata:
========================
Original URL: https://jogos.portaldesaltinho.com.br
Prompt: "Write a script in a programming language of your choice to generate worksheets for kids to practice their typing skills, using exercises and games from Portal de Saltinho as inspiration."
Generated: DETERMINISTIC_5df9e721fcbfd28f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import string
import json
import os
from datetime import datetime
from typing import List, Dict, Optional

class TypingWorksheetGenerator:
    """
    A class to generate typing practice worksheets for kids with exercises and games.
    Inspired by Portal de Saltinho typing exercises.
    """
    
    def __init__(self):
        self.exercises = self._load_exercises()
        self.difficulty_levels = ['easy', 'medium', 'hard']
        
    def _load_exercises(self) -> Dict[str, List[str]]:
        """Load predefined typing exercises from a JSON file."""
        try:
            with open('exercises.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            # Default exercises if file not found
            return {
                'words': ['cat', 'dog', 'sun', 'hat', 'run', 'fun', 'big', 'red', 'box', 'joy'],
                'sentences': [
                    'The quick brown fox jumps over the lazy dog.',
                    'Pack my box with five dozen liquor jugs.',
                    'How vexingly quick daft zebras jump!',
                    'Bright vixens jump; dozy fowl quack.'
                ],
                'paragraphs': [
                    'Learning to type is fun and important. Practice every day to get better. '
                    'Start slow and focus on accuracy before speed. Soon you will type like a pro!',
                    'The quick brown fox jumps over the lazy dog. Pack my box with five dozen liquor jugs. '
                    'How vexingly quick daft zebras jump! Bright vixens jump; dozy fowl quack.'
                ]
            }
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in exercises file")
    
    def generate_random_word(self, length: Optional[int] = None) -> str:
        """Generate a random word of given length or random length between 3-7."""
        if length is None:
            length = random.randint(3, 7)
        return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
    
    def generate_word_list(self, count: int = 10, difficulty: str = 'easy') -> List[str]:
        """Generate a list of words for typing practice."""
        if difficulty not in self.difficulty_levels:
            raise ValueError(f"Invalid difficulty level. Choose from {self.difficulty_levels}")
            
        if difficulty == 'easy':
            return random.sample(self.exercises['words'], min(count, len(self.exercises['words'])))
        elif difficulty == 'medium':
            return [self.generate_random_word(random.randint(4, 6)) for _ in range(count)]
        else:  # hard
            return [self.generate_random_word(random.randint(6, 10)) for _ in range(count)]
    
    def generate_sentence(self, difficulty: str = 'easy') -> str:
        """Generate a typing sentence based on difficulty."""
        if difficulty not in self.difficulty_levels:
            raise ValueError(f"Invalid difficulty level. Choose from {self.difficulty_levels}")
            
        if difficulty == 'easy':
            return random.choice(self.exercises['sentences'])
        else:
            words = self.generate_word_list(random.randint(8, 12), difficulty)
            return ' '.join(words).capitalize() + '.'
    
    def generate_paragraph(self, difficulty: str = 'medium') -> str:
        """Generate a typing paragraph based on difficulty."""
        if difficulty not in self.difficulty_levels:
            raise ValueError(f"Invalid difficulty level. Choose from {self.difficulty_levels}")
            
        if difficulty == 'easy':
            return random.choice(self.exercises['paragraphs'])
        else:
            sentences = [self.generate_sentence(difficulty) for _ in range(random.randint(3, 5))]
            return ' '.join(sentences)
    
    def generate_worksheet(self, exercises: List[str] = None, output_file: str = None) -> str:
        """
        Generate a complete worksheet with various typing exercises.
        Returns the worksheet content and optionally saves to file.
        """
        if exercises is None:
            exercises = ['words', 'sentence', 'paragraph']
            
        worksheet = []
        worksheet.append(f"Typing Practice Worksheet - {datetime.now().strftime('%Y-%m-%d')}")
        worksheet.append("=" * 50)
        worksheet.append("")
        
        if 'words' in exercises:
            worksheet.append("1. Type these words:")
            worksheet.append("-" * 30)
            for word in self.generate_word_list(10, 'easy'):
                worksheet.append(word)
            worksheet.append("")
            
        if 'sentence' in exercises:
            worksheet.append("2. Type this sentence:")
            worksheet.append("-" * 30)
            worksheet.append(self.generate_sentence('medium'))
            worksheet.append("")
            
        if 'paragraph' in exercises:
            worksheet.append("3. Type this paragraph:")
            worksheet.append("-" * 30)
            worksheet.append(self.generate_paragraph('medium'))
            worksheet.append("")
            
        worksheet_content = '\n'.join(worksheet)
        
        if output_file:
            try:
                with open(output_file, 'w') as f:
                    f.write(worksheet_content)
            except IOError as e:
                print(f"Error saving worksheet: {e}")
        
        return worksheet_content
    
    def generate_game(self, game_type: str = 'word_race') -> str:
        """Generate a simple typing game."""
        if game_type == 'word_race':
            words = self.generate_word_list(20, 'medium')
            instructions = (
                "Word Race Game:\n"
                "Type the following words as fast as you can!\n"
                "Press Enter after each word.\n"
                "Ready? Go!\n\n"
            )
            return instructions + '\n'.join(words)
        else:
            sentence = self.generate_sentence('hard')
            instructions = (
                "Sentence Challenge:\n"
                "Type the following sentence perfectly.\n"
                "You have 3 attempts to get it right!\n\n"
            )
            return instructions + sentence

def main():
    """Main function to demonstrate worksheet generation."""
    try:
        generator = TypingWorksheetGenerator()
        
        print("Generating a typing practice worksheet...")
        worksheet = generator.generate_worksheet()
        print(worksheet)
        
        print("\nGenerating a typing game...")
        game = generator.generate_game()
        print(game)
        
        # Save to files
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        generator.generate_worksheet(output_file=f"typing_worksheet_{timestamp}.txt")
        with open(f"typing_game_{timestamp}.txt", 'w') as f:
            f.write(generator.generate_game())
            
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
