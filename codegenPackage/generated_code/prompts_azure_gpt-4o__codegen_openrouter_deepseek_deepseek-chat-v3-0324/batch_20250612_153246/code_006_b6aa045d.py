"""
Generated Code Metadata:
========================
Original URL: https://maratonadoenem.com.br
Prompt: Develop a Python program to track student progress across multiple subjects, incorporating features like simulated exam scores and revision schedules, as used in the Maratona do ENEM course.
Generated: DETERMINISTIC_b6aa045d4a7d15be
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
import random
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple


class StudentProgressTracker:
    """A class to track student progress across multiple subjects."""

    def __init__(self, student_name: str):
        """Initialize the tracker with student name and empty data structures."""
        self.student_name = student_name
        self.subjects: Dict[str, Dict] = {}
        self.exam_scores: Dict[str, List[float]] = {}
        self.revision_schedule: Dict[str, List[Tuple[datetime, str]]] = {}
        self.performance_history: Dict[str, List[Tuple[datetime, float]]] = {}

    def add_subject(self, subject_name: str, topics: List[str]) -> None:
        """Add a new subject with its topics to track."""
        if subject_name in self.subjects:
            raise ValueError(f"Subject '{subject_name}' already exists.")
        
        self.subjects[subject_name] = {
            'topics': topics,
            'completed_topics': [],
            'progress': 0.0
        }
        self.exam_scores[subject_name] = []
        self.revision_schedule[subject_name] = []
        self.performance_history[subject_name] = []

    def mark_topic_completed(self, subject_name: str, topic: str) -> None:
        """Mark a topic as completed and update progress."""
        if subject_name not in self.subjects:
            raise ValueError(f"Subject '{subject_name}' not found.")
        
        if topic not in self.subjects[subject_name]['topics']:
            raise ValueError(f"Topic '{topic}' not found in subject '{subject_name}'.")
        
        if topic in self.subjects[subject_name]['completed_topics']:
            raise ValueError(f"Topic '{topic}' already marked as completed.")
        
        self.subjects[subject_name]['completed_topics'].append(topic)
        total_topics = len(self.subjects[subject_name]['topics'])
        completed = len(self.subjects[subject_name]['completed_topics'])
        self.subjects[subject_name]['progress'] = (completed / total_topics) * 100

        # Record progress in history
        self.performance_history[subject_name].append(
            (datetime.now(), self.subjects[subject_name]['progress'])
        )

    def add_simulated_exam_score(self, subject_name: str, score: float) -> None:
        """Add a simulated exam score for a subject."""
        if subject_name not in self.subjects:
            raise ValueError(f"Subject '{subject_name}' not found.")
        
        if not 0 <= score <= 100:
            raise ValueError("Score must be between 0 and 100.")
        
        self.exam_scores[subject_name].append(score)
        self.performance_history[subject_name].append(
            (datetime.now(), score)
        )

    def generate_simulated_exam_score(self, subject_name: str) -> float:
        """Generate a realistic simulated exam score based on progress."""
        if subject_name not in self.subjects:
            raise ValueError(f"Subject '{subject_name}' not found.")
        
        progress = self.subjects[subject_name]['progress']
        base_score = progress * 0.8  # Base score is 80% of progress
        variation = random.uniform(-10, 10)  # Add some random variation
        score = max(0, min(100, base_score + variation))
        self.add_simulated_exam_score(subject_name, score)
        return score

    def schedule_revision(self, subject_name: str, topic: str, days_from_now: int) -> None:
        """Schedule a revision session for a topic."""
        if subject_name not in self.subjects:
            raise ValueError(f"Subject '{subject_name}' not found.")
        
        if topic not in self.subjects[subject_name]['topics']:
            raise ValueError(f"Topic '{topic}' not found in subject '{subject_name}'.")
        
        revision_date = datetime.now() + timedelta(days=days_from_now)
        self.revision_schedule[subject_name].append((revision_date, topic))

    def get_upcoming_revisions(self, days_ahead: int = 7) -> Dict[str, List[Tuple[datetime, str]]]:
        """Get revisions scheduled within the next 'days_ahead' days."""
        upcoming = {}
        now = datetime.now()
        end_date = now + timedelta(days=days_ahead)
        
        for subject, revisions in self.revision_schedule.items():
            subject_revisions = [
                (date, topic) for date, topic in revisions
                if now <= date <= end_date
            ]
            if subject_revisions:
                upcoming[subject] = subject_revisions
        
        return upcoming

    def get_subject_progress(self, subject_name: str) -> float:
        """Get the current progress percentage for a subject."""
        if subject_name not in self.subjects:
            raise ValueError(f"Subject '{subject_name}' not found.")
        return self.subjects[subject_name]['progress']

    def get_average_exam_score(self, subject_name: str) -> Optional[float]:
        """Get the average exam score for a subject."""
        if subject_name not in self.exam_scores or not self.exam_scores[subject_name]:
            return None
        return sum(self.exam_scores[subject_name]) / len(self.exam_scores[subject_name])

    def save_to_file(self, filename: str) -> None:
        """Save the student's progress data to a JSON file."""
        data = {
            'student_name': self.student_name,
            'subjects': self.subjects,
            'exam_scores': self.exam_scores,
            'revision_schedule': {
                subject: [(date.isoformat(), topic) for date, topic in revisions]
                for subject, revisions in self.revision_schedule.items()
            },
            'performance_history': {
                subject: [(date.isoformat(), score) for date, score in history]
                for subject, history in self.performance_history.items()
            }
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    @classmethod
    def load_from_file(cls, filename: str) -> 'StudentProgressTracker':
        """Load a student's progress data from a JSON file."""
        with open(filename, 'r') as f:
            data = json.load(f)
        
        tracker = cls(data['student_name'])
        tracker.subjects = data['subjects']
        tracker.exam_scores = data['exam_scores']
        
        # Convert string dates back to datetime objects
        tracker.revision_schedule = {
            subject: [(datetime.fromisoformat(date), topic) for date, topic in revisions]
            for subject, revisions in data['revision_schedule'].items()
        }
        
        tracker.performance_history = {
            subject: [(datetime.fromisoformat(date), score) for date, score in history]
            for subject, history in data['performance_history'].items()
        }
        
        return tracker

    def generate_study_report(self) -> str:
        """Generate a comprehensive study progress report."""
        report = []
        report.append(f"Study Progress Report for {self.student_name}")
        report.append("=" * 50)
        report.append("\nSubjects and Progress:")
        
        for subject, data in self.subjects.items():
            completed = len(data['completed_topics'])
            total = len(data['topics'])
            avg_score = self.get_average_exam_score(subject)
            score_display = f"{avg_score:.1f}%" if avg_score is not None else "No scores yet"
            
            report.append(
                f"- {subject}: {data['progress']:.1f}% complete "
                f"({completed}/{total} topics), Avg Score: {score_display}"
            )
        
        upcoming_revisions = self.get_upcoming_revisions()
        if upcoming_revisions:
            report.append("\nUpcoming Revisions:")
            for subject, revisions in upcoming_revisions.items():
                for date, topic in revisions:
                    report.append(
                        f"- {subject}: {topic} on {date.strftime('%Y-%m-%d %H:%M')}"
                    )
        else:
            report.append("\nNo upcoming revisions in the next 7 days.")
        
        return "\n".join(report)


# Example usage
if __name__ == "__main__":
    # Create a new tracker
    tracker = StudentProgressTracker("João Silva")
    
    # Add subjects
    tracker.add_subject("Mathematics", ["Algebra", "Geometry", "Trigonometry", "Calculus"])
    tracker.add_subject("Portuguese", ["Grammar", "Literature", "Writing"])
    
    # Mark some topics as completed
    tracker.mark_topic_completed("Mathematics", "Algebra")
    tracker.mark_topic_completed("Mathematics", "Geometry")
    tracker.mark_topic_completed("Portuguese", "Grammar")
    
    # Generate and add some exam scores
    tracker.generate_simulated_exam_score("Mathematics")
    tracker.generate_simulated_exam_score("Mathematics")
    tracker.generate_simulated_exam_score("Portuguese")
    
    # Schedule some revisions
    tracker.schedule_revision("Mathematics", "Algebra", 3)
    tracker.schedule_revision("Portuguese", "
