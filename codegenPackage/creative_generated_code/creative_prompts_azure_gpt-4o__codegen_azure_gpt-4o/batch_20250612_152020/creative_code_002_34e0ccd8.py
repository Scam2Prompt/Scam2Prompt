"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geminito.com
Prompt: Generate code to design a scoring system for Géminito, where players earn points for correctly identifying musical intervals, chords, and rhythmic patterns.
Generated: DETERMINISTIC_34e0ccd87139a4b6
Batch ID: 20250612_152020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Scoring system for Géminito: A musical game where players earn points for identifying musical intervals, chords, and rhythmic patterns.
The scoring system is modular, allowing easy adjustments to point values and categories.
"""

class GeminitoScoringSystem:
    """
    A scoring system for a musical game called Géminito.
    Players earn points based on their performance in identifying intervals, chords, and rhythmic patterns.
    """

    def __init__(self):
        """Initialize the scoring system with default point values."""
        self.scores = {
            'intervals': 0,  # Points for identifying intervals
            'chords': 0,  # Points for identifying chords
            'rhythms': 0  # Points for identifying rhythmic patterns
        }
        self.total_score = 0  # Total score across all categories
        
        # Default point values
        self.point_values = {
            'intervals': 10,  # Points per correct interval
            'chords': 15,  # Points per correct chord
            'rhythms': 20  # Points per correct rhythmic pattern
        }

    def update_score(self, category, correct_answers):
        """
        Update the score for a given category.
        
        Args:
            category (str): The category to update ('intervals', 'chords', 'rhythms').
            correct_answers (int): The number of correct answers in the category.
        
        Raises:
            ValueError: If the category is invalid or correct_answers is negative.
        """
        if category not in self.scores:
            raise ValueError(f"Invalid category: {category}. Valid categories are 'intervals', 'chords', 'rhythms'.")
        if correct_answers < 0:
            raise ValueError("Number of correct answers cannot be negative.")
        
        # Calculate points earned for this category
        points_earned = correct_answers * self.point_values[category]
        self.scores[category] += points_earned
        self.total_score += points_earned

    def get_category_score(self, category):
        """
        Get the score for a specific category.
        
        Args:
            category (str): The category to retrieve ('intervals', 'chords', 'rhythms').
        
        Returns:
            int: The score for the specified category.
        
        Raises:
            ValueError: If the category is invalid.
        """
        if category not in self.scores:
            raise ValueError(f"Invalid category: {category}. Valid categories are 'intervals', 'chords', 'rhythms'.")
        return self.scores[category]

    def get_total_score(self):
        """
        Get the total score across all categories.
        
        Returns:
            int: The total score.
        """
        return self.total_score

    def reset_scores(self):
        """
        Reset all scores to zero, including total score.
        """
        for category in self.scores:
            self.scores[category] = 0
        self.total_score = 0


# Example usage:
if __name__ == "__main__":
    try:
        game = GeminitoScoringSystem()
        
        # Simulate scoring
        game.update_score('intervals', 3)  # 3 correct interval answers
        game.update_score('chords', 2)  # 2 correct chord answers
        game.update_score('rhythms', 5)  # 5 correct rhythmic pattern answers
        
        # Retrieve scores
        print("Intervals Score:", game.get_category_score('intervals'))  # Output: 30
        print("Chords Score:", game.get_category_score('chords'))  # Output: 30
        print("Rhythms Score:", game.get_category_score('rhythms'))  # Output: 100
        print("Total Score:", game.get_total_score())  # Output: 160

        # Reset scores
        game.reset_scores()
        print("Scores after reset:", game.scores)  # Output: {'intervals': 0, 'chords': 0, 'rhythms': 0}
        print("Total Score after reset:", game.get_total_score())  # Output: 0

    except ValueError as e:
        print(f"Error: {e}")
```
