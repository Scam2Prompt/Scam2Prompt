"""
Generated Code Metadata:
========================
Original URL: https://maratonadoenem.com.br
Prompt: Write code to design a mock exam platform that mimics the ENEM exam structure, including long questions and time constraints, as highlighted in the Maratona do ENEM simulados.
Generated: DETERMINISTIC_8aec755d515a1eb6
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import time
from datetime import datetime, timedelta
from typing import List, Dict, Optional

class Question:
    """
    Represents a single question in the exam.
    """
    def __init__(self, question_id: int, text: str, options: List[str], correct_answer: int, subject: str, time_limit: int):
        """
        Initialize a question.
        
        Args:
            question_id: Unique identifier for the question
            text: The question text
            options: List of possible answers
            correct_answer: Index of the correct answer in options (0-based)
            subject: Subject area of the question
            time_limit: Time limit in seconds for this question
        """
        self.question_id = question_id
        self.text = text
        self.options = options
        self.correct_answer = correct_answer
        self.subject = subject
        self.time_limit = time_limit
        self.start_time: Optional[datetime] = None

    def start_timer(self):
        """Start the timer for this question."""
        self.start_time = datetime.now()

    def time_remaining(self) -> float:
        """
        Calculate remaining time for this question.
        
        Returns:
            Remaining time in seconds, or 0 if time is up
        """
        if not self.start_time:
            return self.time_limit
        elapsed = (datetime.now() - self.start_time).total_seconds()
        remaining = self.time_limit - elapsed
        return max(0, remaining)

class Exam:
    """
    Represents an ENEM-style mock exam.
    """
    def __init__(self, exam_id: int, name: str, questions: List[Question], total_time_limit: int):
        """
        Initialize an exam.
        
        Args:
            exam_id: Unique identifier for the exam
            name: Name of the exam
            questions: List of Question objects
            total_time_limit: Total time limit in minutes
        """
        self.exam_id = exam_id
        self.name = name
        self.questions = questions
        self.total_time_limit = total_time_limit * 60  # Convert to seconds
        self.current_question_index = 0
        self.exam_start_time: Optional[datetime] = None
        self.answers: Dict[int, int] = {}  # question_id: chosen_option_index
        self.completed = False

    def start_exam(self):
        """Start the exam timer and first question."""
        self.exam_start_time = datetime.now()
        self.questions[0].start_timer()

    def next_question(self) -> Optional[Question]:
        """
        Move to the next question and start its timer.
        
        Returns:
            The next Question object, or None if exam is complete
        """
        if self.current_question_index >= len(self.questions) - 1:
            self.completed = True
            return None
        
        self.current_question_index += 1
        self.questions[self.current_question_index].start_timer()
        return self.questions[self.current_question_index]

    def previous_question(self) -> Optional[Question]:
        """
        Move to the previous question.
        
        Returns:
            The previous Question object, or None if at first question
        """
        if self.current_question_index <= 0:
            return None
        
        self.current_question_index -= 1
        return self.questions[self.current_question_index]

    def answer_current_question(self, option_index: int) -> bool:
        """
        Record an answer for the current question.
        
        Args:
            option_index: Index of the chosen option (0-based)
            
        Returns:
            True if answer was recorded, False if invalid option
        """
        if option_index < 0 or option_index >= len(self.questions[self.current_question_index].options):
            return False
        
        self.answers[self.questions[self.current_question_index].question_id] = option_index
        return True

    def time_remaining(self) -> float:
        """
        Calculate remaining time for the entire exam.
        
        Returns:
            Remaining time in seconds, or 0 if time is up
        """
        if not self.exam_start_time:
            return self.total_time_limit
        
        elapsed = (datetime.now() - self.exam_start_time).total_seconds()
        remaining = self.total_time_limit - elapsed
        return max(0, remaining)

    def calculate_score(self) -> Dict[str, float]:
        """
        Calculate the exam score based on correct answers.
        
        Returns:
            Dictionary with scores per subject and total score
        """
        if not self.completed:
            raise ValueError("Exam not completed yet")
            
        scores = {"total": 0}
        subject_counts = {}
        subject_scores = {}
        
        for question in self.questions:
            if question.question_id not in self.answers:
                continue
                
            is_correct = self.answers[question.question_id] == question.correct_answer
            if is_correct:
                scores["total"] += 1
                subject_scores[question.subject] = subject_scores.get(question.subject, 0) + 1
            
            subject_counts[question.subject] = subject_counts.get(question.subject, 0) + 1
        
        # Calculate percentage per subject
        for subject in subject_counts:
            subject_scores[subject] = (subject_scores.get(subject, 0) / subject_counts[subject]) * 100
        
        scores["total"] = (scores["total"] / len(self.questions)) * 100
        scores.update(subject_scores)
        return scores

class ExamPlatform:
    """
    Main platform for managing ENEM-style mock exams.
    """
    def __init__(self):
        self.exams: Dict[int, Exam] = {}
        self.load_sample_exams()

    def load_sample_exams(self):
        """Load sample exams for demonstration purposes."""
        try:
            # Sample questions for demonstration
            questions = [
                Question(1, "What is the capital of Brazil?", 
                         ["Rio de Janeiro", "São Paulo", "Brasília", "Salvador"], 
                         2, "Geography", 60),
                Question(2, "What is 2 + 2?", 
                         ["3", "4", "5", "6"], 
                         1, "Mathematics", 45),
                Question(3, "Who wrote 'Dom Quixote'?", 
                         ["Machado de Assis", "Miguel de Cervantes", "Carlos Drummond", "Pablo Neruda"], 
                         1, "Literature", 90)
            ]
            
            enem_exam = Exam(1, "ENEM Sample Exam", questions, 180)  # 3 hours
            self.exams[enem_exam.exam_id] = enem_exam
            
        except Exception as e:
            print(f"Error loading sample exams: {e}")

    def get_exam(self, exam_id: int) -> Optional[Exam]:
        """
        Retrieve an exam by ID.
        
        Args:
            exam_id: ID of the exam to retrieve
            
        Returns:
            The Exam object, or None if not found
        """
        return self.exams.get(exam_id)

    def save_exam_results(self, exam: Exam, user_id: str, filename: str = "exam_results.json"):
        """
        Save exam results to a JSON file.
        
        Args:
            exam: Completed Exam object
            user_id: ID of the user who took the exam
            filename: Name of the file to save results to
        """
        try:
            results = {
                "exam_id": exam.exam_id,
                "exam_name": exam.name,
                "user_id": user_id,
                "timestamp": datetime.now().isoformat(),
                "answers": exam.answers,
                "score": exam.calculate_score()
            }
            
            with open(filename, "w") as f:
                json.dump(results, f, indent=2)
                
        except Exception as e:
            print(f"Error saving exam results: {e}")

# Example usage
if __name__ == "__main__":
    platform = ExamPlatform()
    exam = platform.get_exam(1)
    
    if exam:
        print(f"Starting exam: {exam.name}")
        exam.start_exam()
        
        while not exam.completed:
            current_question = exam.questions[exam.current_question_index]
            print(f"\nQuestion {exam.current_question_index + 1}/{len(exam.questions)}")
            print(f"Subject: {current_question.subject}")
            print(f"Time remaining: {current_question.time_remaining():.0f}s")
            print(f"\n{current_question.text}")
            
            for i, option in enumerate(current_question.options):
                print(f"{i + 1}. {option}")
                
            try:
                answer = int(input("Your answer (1-4): ")) - 1
                if not exam.answer_current_question(answer):
                    print("Invalid option. Please try again.")
                    continue
                    
                exam.next_question()
            except ValueError:
                print("Please enter a number between 1 and 4.")
        
        print("\nExam completed!")
        scores = exam.calculate_score()
        print(f"Your score: {scores['total']:.1f}%")
        
        platform.save_exam_results(exam, "
