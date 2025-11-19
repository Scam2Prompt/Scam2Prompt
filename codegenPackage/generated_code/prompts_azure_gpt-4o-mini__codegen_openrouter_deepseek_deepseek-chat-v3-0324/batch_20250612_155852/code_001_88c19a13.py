"""
Generated Code Metadata:
========================
Original URL: https://blur.today
Prompt: Write a code snippet that simulates daily self-discovery questions for users to enhance their AI avatars on blur.today.
Generated: DETERMINISTIC_88c19a13d3314f86
Batch ID: 20250612_155852
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from datetime import datetime, timedelta
from typing import Dict, List, Optional

class SelfDiscoveryQuestionGenerator:
    """
    A class to generate daily self-discovery questions for users to enhance their AI avatars.
    """
    
    def __init__(self, questions_db: Optional[Dict[str, List[str]]] = None):
        """
        Initialize the question generator with a database of questions.
        
        Args:
            questions_db: A dictionary mapping categories to lists of questions.
                         If None, a default set will be used.
        """
        self.questions_db = questions_db or self._get_default_questions()
        self.user_progress: Dict[str, datetime] = {}  # Maps user_id to last question date
        
    def _get_default_questions(self) -> Dict[str, List[str]]:
        """
        Returns a default set of questions categorized by themes.
        
        Returns:
            Dictionary of categories mapping to lists of questions.
        """
        return {
            "introspection": [
                "What's something you learned about yourself recently?",
                "What values are most important to you right now?",
                "How have your priorities changed in the past year?"
            ],
            "creativity": [
                "What creative activity makes you lose track of time?",
                "How would you describe your ideal creative environment?",
                "What's a creative project you've been putting off?"
            ],
            "relationships": [
                "Who in your life brings out the best in you?",
                "What quality do you appreciate most in your closest relationships?",
                "How do you show appreciation to people you care about?"
            ],
            "growth": [
                "What's a skill you'd like to develop this year?",
                "What's one limiting belief you'd like to overcome?",
                "How do you handle setbacks or failures?"
            ]
        }
    
    def _get_random_question(self, category: str) -> str:
        """
        Get a random question from a specified category.
        
        Args:
            category: The category to select a question from.
            
        Returns:
            A random question from the category.
            
        Raises:
            ValueError: If the category doesn't exist or has no questions.
        """
        if category not in self.questions_db:
            raise ValueError(f"Category '{category}' not found in questions database")
            
        questions = self.questions_db[category]
        if not questions:
            raise ValueError(f"No questions available in category '{category}'")
            
        return random.choice(questions)
    
    def get_daily_question(self, user_id: str, force_new: bool = False) -> str:
        """
        Get a daily question for a user, ensuring they don't get repeats too soon.
        
        Args:
            user_id: Unique identifier for the user.
            force_new: If True, ignores the cooldown period and returns a new question.
            
        Returns:
            A daily self-discovery question.
            
        Raises:
            ValueError: If no questions are available.
        """
        # Check if user already got a question today
        last_question_date = self.user_progress.get(user_id)
        today = datetime.now().date()
        
        if not force_new and last_question_date and last_question_date.date() == today:
            raise ValueError("User has already received a question today")
        
        # Select a random category and question
        available_categories = list(self.questions_db.keys())
        random.shuffle(available_categories)
        
        for category in available_categories:
            try:
                question = self._get_random_question(category)
                self.user_progress[user_id] = datetime.now()
                return question
            except ValueError:
                continue
                
        raise ValueError("No questions available in any category")
    
    def add_questions(self, category: str, questions: List[str]) -> None:
        """
        Add new questions to a category.
        
        Args:
            category: The category to add questions to.
            questions: List of questions to add.
            
        Raises:
            ValueError: If category doesn't exist or questions list is empty.
        """
        if not questions:
            raise ValueError("Questions list cannot be empty")
            
        if category not in self.questions_db:
            raise ValueError(f"Category '{category}' not found")
            
        self.questions_db[category].extend(questions)
    
    def get_user_cooldown(self, user_id: str) -> Optional[timedelta]:
        """
        Get remaining time until user can receive a new question.
        
        Args:
            user_id: The user to check.
            
        Returns:
            timedelta until next question is available, or None if ready.
        """
        if user_id not in self.user_progress:
            return None
            
        last_question_time = self.user_progress[user_id]
        next_question_time = last_question_time + timedelta(days=1)
        now = datetime.now()
        
        if now >= next_question_time:
            return None
        return next_question_time - now


# Example usage
if __name__ == "__main__":
    generator = SelfDiscoveryQuestionGenerator()
    
    try:
        # Simulate daily question for a user
        user_id = "user123"
        question = generator.get_daily_question(user_id)
        print(f"Today's question: {question}")
        
        # Check cooldown
        cooldown = generator.get_user_cooldown(user_id)
        if cooldown:
            print(f"Next question available in: {cooldown}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
