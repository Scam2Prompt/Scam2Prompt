"""
Generated Code Metadata:
========================
Original URL: https://himsaral.com
Prompt: What are the steps to develop a question paper generation feature like the one in Him Saral's school software?
Generated: DETERMINISTIC_b8b1c2d2f358da66
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from typing import List, Dict, Optional
from dataclasses import dataclass
import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class Question:
    id: str
    text: str
    marks: int
    difficulty: str  # 'easy', 'medium', 'hard'
    subject: str
    chapter: str
    tags: List[str]

@dataclass
class QuestionPaperSpec:
    total_marks: int
    difficulty_distribution: Dict[str, float]  # {'easy': 0.3, 'medium': 0.5, 'hard': 0.2}
    subject: str
    chapters: List[str]
    tags: Optional[List[str]] = None

class QuestionBank:
    def __init__(self):
        self.questions: List[Question] = []
    
    def add_question(self, question: Question) -> None:
        """Add a question to the question bank."""
        self.questions.append(question)
        logger.info(f"Added question with ID: {question.id}")
    
    def load_from_json(self, file_path: str) -> None:
        """Load questions from a JSON file."""
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                for item in data:
                    question = Question(
                        id=item['id'],
                        text=item['text'],
                        marks=item['marks'],
                        difficulty=item['difficulty'],
                        subject=item['subject'],
                        chapter=item['chapter'],
                        tags=item.get('tags', [])
                    )
                    self.add_question(question)
            logger.info(f"Successfully loaded questions from {file_path}")
        except FileNotFoundError:
            logger.error(f"File not found: {file_path}")
            raise
        except json.JSONDecodeError:
            logger.error(f"Invalid JSON format in file: {file_path}")
            raise
        except KeyError as e:
            logger.error(f"Missing required field in JSON: {e}")
            raise
    
    def filter_questions(self, subject: str, chapters: List[str], difficulty: Optional[str] = None, tags: Optional[List[str]] = None) -> List[Question]:
        """Filter questions based on criteria."""
        filtered = [
            q for q in self.questions 
            if q.subject == subject and 
            q.chapter in chapters and
            (difficulty is None or q.difficulty == difficulty) and
            (tags is None or any(tag in q.tags for tag in tags))
        ]
        return filtered

class QuestionPaperGenerator:
    def __init__(self, question_bank: QuestionBank):
        self.question_bank = question_bank
    
    def generate_question_paper(self, spec: QuestionPaperSpec) -> List[Question]:
        """Generate a question paper based on the specification."""
        try:
            # Validate difficulty distribution
            if not self._validate_distribution(spec.difficulty_distribution):
                raise ValueError("Invalid difficulty distribution")
            
            # Calculate marks per difficulty level
            marks_distribution = self._calculate_marks_distribution(spec)
            
            # Select questions
            selected_questions = []
            for difficulty, marks in marks_distribution.items():
                questions = self._select_questions(
                    subject=spec.subject,
                    chapters=spec.chapters,
                    difficulty=difficulty,
                    required_marks=marks,
                    tags=spec.tags
                )
                selected_questions.extend(questions)
            
            # Verify total marks
            total = sum(q.marks for q in selected_questions)
            if total != spec.total_marks:
                logger.warning(f"Total marks mismatch. Expected: {spec.total_marks}, Got: {total}")
            
            return selected_questions
        except Exception as e:
            logger.error(f"Error generating question paper: {e}")
            raise
    
    def _validate_distribution(self, distribution: Dict[str, float]) -> bool:
        """Validate that difficulty distribution sums to 1.0."""
        return abs(sum(distribution.values()) - 1.0) < 0.001
    
    def _calculate_marks_distribution(self, spec: QuestionPaperSpec) -> Dict[str, int]:
        """Calculate marks per difficulty level."""
        marks_dist = {}
        remaining_marks = spec.total_marks
        
        # Sort by difficulty to ensure we handle rounding correctly
        sorted_difficulties = sorted(spec.difficulty_distribution.items(), key=lambda x: x[1], reverse=True)
        
        for i, (difficulty, percentage) in enumerate(sorted_difficulties):
            if i == len(sorted_difficulties) - 1:
                marks = remaining_marks  # Assign remaining marks to last difficulty
            else:
                marks = round(spec.total_marks * percentage)
                remaining_marks -= marks
            marks_dist[difficulty] = marks
        
        return marks_dist
    
    def _select_questions(self, subject: str, chapters: List[str], difficulty: str, required_marks: int, tags: Optional[List[str]] = None) -> List[Question]:
        """Select questions for a specific difficulty level."""
        filtered = self.question_bank.filter_questions(
            subject=subject,
            chapters=chapters,
            difficulty=difficulty,
            tags=tags
        )
        
        if not filtered:
            raise ValueError(f"No questions found for difficulty: {difficulty}")
        
        # Simple selection algorithm - can be enhanced with more sophisticated logic
        selected = []
        current_marks = 0
        random.shuffle(filtered)  # Randomize selection
        
        for question in filtered:
            if current_marks + question.marks <= required_marks:
                selected.append(question)
                current_marks += question.marks
                if current_marks == required_marks:
                    break
        
        if current_marks < required_marks:
            logger.warning(f"Could not meet required marks ({required_marks}) for difficulty {difficulty}. Got {current_marks}")
        
        return selected

# Example usage
if __name__ == "__main__":
    # Initialize question bank
    qb = QuestionBank()
    
    # Load questions (in a real scenario, this would be from a database or file)
    try:
        qb.load_from_json("questions.json")
    except Exception as e:
        logger.error(f"Failed to load questions: {e}")
        exit(1)
    
    # Define question paper specification
    spec = QuestionPaperSpec(
        total_marks=100,
        difficulty_distribution={'easy': 0.2, 'medium': 0.5, 'hard': 0.3},
        subject="Mathematics",
        chapters=["Algebra", "Geometry"],
        tags=["important"]
    )
    
    # Generate question paper
    generator = QuestionPaperGenerator(qb)
    try:
        paper = generator.generate_question_paper(spec)
        print("Generated Question Paper:")
        for i, question in enumerate(paper, 1):
            print(f"{i}. {question.text} ({question.marks} marks, {question.difficulty})")
    except Exception as e:
        logger.error(f"Failed to generate question paper: {e}")
```
