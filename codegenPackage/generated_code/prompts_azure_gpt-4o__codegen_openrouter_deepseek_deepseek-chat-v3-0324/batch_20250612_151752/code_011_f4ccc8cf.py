"""
Generated Code Metadata:
========================
Original URL: https://kraken.media
Prompt: Write code to create a custom e-learning video series with interactive quizzes and progress tracking, inspired by Kraken Media’s approach to engaging training modules.
Generated: DETERMINISTIC_f4ccc8cffe48d30a
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from datetime import datetime
from typing import Dict, List, Optional

class VideoModule:
    """Represents a single video module in the e-learning series."""
    
    def __init__(self, title: str, video_path: str, duration: int, description: str = ""):
        """
        Initialize a video module.
        
        Args:
            title: Title of the video module
            video_path: Path to the video file
            duration: Duration in minutes
            description: Optional description
        """
        self.title = title
        self.video_path = video_path
        self.duration = duration
        self.description = description
        self.quiz = []
        self.completed = False
        self.completion_date = None
    
    def add_quiz_question(self, question: str, options: List[str], correct_answer: int) -> None:
        """
        Add a quiz question to the video module.
        
        Args:
            question: The question text
            options: List of possible answers
            correct_answer: Index of the correct answer (0-based)
        """
        if correct_answer < 0 or correct_answer >= len(options):
            raise ValueError("Correct answer index out of range")
        
        self.quiz.append({
            'question': question,
            'options': options,
            'correct_answer': correct_answer,
            'user_answer': None
        })
    
    def mark_completed(self) -> None:
        """Mark the module as completed with current timestamp."""
        self.completed = True
        self.completion_date = datetime.now().isoformat()

class ELearningSeries:
    """Main class for managing the e-learning video series."""
    
    def __init__(self, title: str, description: str = ""):
        """
        Initialize the e-learning series.
        
        Args:
            title: Title of the series
            description: Optional description
        """
        self.title = title
        self.description = description
        self.modules: List[VideoModule] = []
        self.current_module_index = 0
        self.progress_data = {
            'total_modules': 0,
            'completed_modules': 0,
            'quiz_scores': {}
        }
    
    def add_module(self, module: VideoModule) -> None:
        """Add a video module to the series."""
        self.modules.append(module)
        self.progress_data['total_modules'] = len(self.modules)
    
    def get_current_module(self) -> Optional[VideoModule]:
        """Get the current module being viewed."""
        if self.modules:
            return self.modules[self.current_module_index]
        return None
    
    def next_module(self) -> Optional[VideoModule]:
        """Move to the next module in the series."""
        if self.current_module_index < len(self.modules) - 1:
            self.current_module_index += 1
            return self.get_current_module()
        return None
    
    def previous_module(self) -> Optional[VideoModule]:
        """Move to the previous module in the series."""
        if self.current_module_index > 0:
            self.current_module_index -= 1
            return self.get_current_module()
        return None
    
    def record_quiz_answer(self, module_index: int, question_index: int, answer_index: int) -> bool:
        """
        Record a user's answer to a quiz question.
        
        Args:
            module_index: Index of the module
            question_index: Index of the question
            answer_index: Index of the selected answer
            
        Returns:
            bool: True if answer was correct, False otherwise
        """
        try:
            module = self.modules[module_index]
            question = module.quiz[question_index]
            question['user_answer'] = answer_index
            
            is_correct = (answer_index == question['correct_answer'])
            
            # Update progress tracking
            if module_index not in self.progress_data['quiz_scores']:
                self.progress_data['quiz_scores'][module_index] = {
                    'total': len(module.quiz),
                    'correct': 0
                }
            
            if is_correct:
                self.progress_data['quiz_scores'][module_index]['correct'] += 1
            
            return is_correct
        except (IndexError, KeyError) as e:
            raise ValueError("Invalid module or question index") from e
    
    def get_progress(self) -> Dict:
        """
        Get the user's overall progress in the series.
        
        Returns:
            Dict containing progress information
        """
        completed = sum(1 for m in self.modules if m.completed)
        self.progress_data['completed_modules'] = completed
        
        total_questions = 0
        correct_answers = 0
        
        for scores in self.progress_data['quiz_scores'].values():
            total_questions += scores['total']
            correct_answers += scores['correct']
        
        self.progress_data['quiz_accuracy'] = (
            (correct_answers / total_questions * 100) if total_questions > 0 else 0
        )
        
        return self.progress_data
    
    def save_progress(self, file_path: str) -> None:
        """Save progress data to a JSON file."""
        progress_data = {
            'series_title': self.title,
            'current_module': self.current_module_index,
            'modules': [
                {
                    'title': m.title,
                    'completed': m.completed,
                    'completion_date': m.completion_date,
                    'quiz': m.quiz
                } for m in self.modules
            ],
            'progress': self.get_progress()
        }
        
        try:
            with open(file_path, 'w') as f:
                json.dump(progress_data, f, indent=2)
        except IOError as e:
            raise IOError(f"Failed to save progress: {str(e)}") from e
    
    def load_progress(self, file_path: str) -> None:
        """Load progress data from a JSON file."""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            
            if data.get('series_title') != self.title:
                raise ValueError("Progress file doesn't match this series")
            
            self.current_module_index = data.get('current_module', 0)
            
            for i, module_data in enumerate(data.get('modules', [])):
                if i < len(self.modules):
                    self.modules[i].completed = module_data.get('completed', False)
                    self.modules[i].completion_date = module_data.get('completion_date')
                    
                    # Restore quiz answers
                    for q_idx, question in enumerate(module_data.get('quiz', [])):
                        if q_idx < len(self.modules[i].quiz):
                            self.modules[i].quiz[q_idx]['user_answer'] = question.get('user_answer')
            
            self.progress_data = data.get('progress', self.progress_data)
            
        except (IOError, json.JSONDecodeError) as e:
            raise IOError(f"Failed to load progress: {str(e)}") from e

# Example usage
if __name__ == "__main__":
    # Create a new e-learning series
    series = ELearningSeries(
        title="Python Programming Fundamentals",
        description="Learn core Python concepts through interactive videos and quizzes"
    )
    
    # Add modules
    module1 = VideoModule(
        title="Introduction to Python",
        video_path="videos/intro.mp4",
        duration=15,
        description="Overview of Python and its features"
    )
    module1.add_quiz_question(
        "What is Python primarily used for?",
        ["Web development", "Data analysis", "System programming", "All of the above"],
        3
    )
    series.add_module(module1)
    
    module2 = VideoModule(
        title="Variables and Data Types",
        video_path="variables.mp4",
        duration=20
    )
    module2.add_quiz_question(
        "Which of these is NOT a valid Python data type?",
        ["int", "float", "double", "str"],
        2
    )
    series.add_module(module2)
    
    # Simulate user interaction
    current_module = series.get_current_module()
    print(f"Starting module: {current_module.title}")
    
    # Answer quiz question
    series.record_quiz_answer(0, 0, 3)  # Correct answer
    current_module.mark_completed()
    
    # Move to next module
    next_module = series.next_module()
    print(f"Next module: {next_module.title if next_module else 'None'}")
    
    # Save progress
    try:
        series.save_progress("progress.json")
        print("Progress saved successfully")
    except IOError as e:
        print(f"Error saving progress: {e}")
    
    # Display progress
    progress = series.get_progress()
    print(f"Progress: {progress['completed_modules']}/{progress['total_modules']} modules completed")
```
