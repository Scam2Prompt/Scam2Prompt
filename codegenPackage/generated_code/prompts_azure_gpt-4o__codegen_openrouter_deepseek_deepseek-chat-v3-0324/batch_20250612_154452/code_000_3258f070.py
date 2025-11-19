"""
Generated Code Metadata:
========================
Original URL: https://retinabd.org
Prompt: Write Python code to simulate a standard exam preparation schedule for medical admission coaching, incorporating Retina's updated preparation strategies and class effectiveness metrics.
Generated: DETERMINISTIC_3258f070ffee55f1
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import List, Dict, Optional
import random
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class Subject(Enum):
    """Enum representing different subjects in medical admission coaching."""
    BIOLOGY = "Biology"
    CHEMISTRY = "Chemistry"
    PHYSICS = "Physics"
    MATHEMATICS = "Mathematics"
    ENGLISH = "English"

class StudyMethod(Enum):
    """Enum representing different study methods."""
    LECTURE = "Lecture"
    PRACTICE = "Practice"
    REVISION = "Revision"
    MOCK_TEST = "Mock Test"

class ClassEffectiveness:
    """Class to represent effectiveness metrics for a coaching class."""
    
    def __init__(self, subject: Subject, method: StudyMethod, effectiveness: float):
        """
        Initialize ClassEffectiveness.
        
        Args:
            subject: Subject being taught
            method: Study method used
            effectiveness: Effectiveness score (0.0 to 1.0)
        """
        if not 0.0 <= effectiveness <= 1.0:
            raise ValueError("Effectiveness must be between 0.0 and 1.0")
        
        self.subject = subject
        self.method = method
        self.effectiveness = effectiveness
    
    def __repr__(self):
        return f"ClassEffectiveness(subject={self.subject}, method={self.method}, effectiveness={self.effectiveness})"

class StudySession:
    """Class to represent a single study session."""
    
    def __init__(self, subject: Subject, method: StudyMethod, duration: int, effectiveness: float):
        """
        Initialize StudySession.
        
        Args:
            subject: Subject being studied
            method: Study method used
            duration: Duration in minutes
            effectiveness: Effectiveness score (0.0 to 1.0)
        """
        if duration <= 0:
            raise ValueError("Duration must be positive")
        if not 0.0 <= effectiveness <= 1.0:
            raise ValueError("Effectiveness must be between 0.0 and 1.0")
        
        self.subject = subject
        self.method = method
        self.duration = duration
        self.effectiveness = effectiveness
    
    def calculate_productivity(self) -> float:
        """Calculate the productivity score for this session."""
        return self.duration * self.effectiveness
    
    def __repr__(self):
        return f"StudySession(subject={self.subject}, method={self.method}, duration={self.duration}, effectiveness={self.effectiveness})"

class ExamPreparationSchedule:
    """Class to simulate an exam preparation schedule for medical admission coaching."""
    
    def __init__(self, start_date: datetime.date, end_date: datetime.date, 
                 class_effectiveness: List[ClassEffectiveness], daily_study_hours: int = 8):
        """
        Initialize ExamPreparationSchedule.
        
        Args:
            start_date: Start date of preparation
            end_date: End date of preparation
            class_effectiveness: List of ClassEffectiveness objects
            daily_study_hours: Hours available for study each day (default: 8)
        """
        if start_date >= end_date:
            raise ValueError("Start date must be before end date")
        if daily_study_hours <= 0 or daily_study_hours > 24:
            raise ValueError("Daily study hours must be between 1 and 24")
        
        self.start_date = start_date
        self.end_date = end_date
        self.class_effectiveness = class_effectiveness
        self.daily_study_minutes = daily_study_hours * 60
        self.schedule: Dict[datetime.date, List[StudySession]] = {}
        
        # Initialize empty schedule
        current_date = start_date
        while current_date <= end_date:
            self.schedule[current_date] = []
            current_date += datetime.timedelta(days=1)
    
    def _get_effectiveness(self, subject: Subject, method: StudyMethod) -> float:
        """Get effectiveness score for a subject and method combination."""
        for ce in self.class_effectiveness:
            if ce.subject == subject and ce.method == method:
                return ce.effectiveness
        return 0.5  # Default effectiveness if not specified
    
    def generate_schedule(self, subject_weights: Optional[Dict[Subject, float]] = None):
        """
        Generate a study schedule based on subject weights and class effectiveness.
        
        Args:
            subject_weights: Dictionary mapping subjects to their relative weights
                           (default: equal weights for all subjects)
        """
        if subject_weights is None:
            subject_weights = {s: 1.0 for s in Subject}
        
        # Normalize weights
        total_weight = sum(subject_weights.values())
        normalized_weights = {s: w/total_weight for s, w in subject_weights.items()}
        
        current_date = self.start_date
        while current_date <= self.end_date:
            # Skip weekends (optional)
            if current_date.weekday() >= 5:  # 5 and 6 are Saturday and Sunday
                current_date += datetime.timedelta(days=1)
                continue
            
            remaining_minutes = self.daily_study_minutes
            daily_sessions = []
            
            # Distribute study time according to weights
            while remaining_minutes > 0:
                # Choose subject based on weights
                subject = random.choices(
                    list(normalized_weights.keys()),
                    weights=list(normalized_weights.values()),
                    k=1
                )[0]
                
                # Choose method (weighted towards more effective methods)
                available_methods = [m for m in StudyMethod]
                method_weights = [
                    self._get_effectiveness(subject, m) for m in available_methods
                ]
                method = random.choices(available_methods, weights=method_weights, k=1)[0]
                
                # Determine session duration (30-120 minutes)
                duration = min(random.randint(30, 120), remaining_minutes)
                if duration <= 0:
                    break
                
                effectiveness = self._get_effectiveness(subject, method)
                session = StudySession(subject, method, duration, effectiveness)
                daily_sessions.append(session)
                remaining_minutes -= duration
            
            self.schedule[current_date] = daily_sessions
            current_date += datetime.timedelta(days=1)
    
    def get_daily_schedule(self, date: datetime.date) -> List[StudySession]:
        """Get study sessions for a specific date."""
        return self.schedule.get(date, [])
    
    def get_total_productivity(self) -> Dict[Subject, float]:
        """Calculate total productivity per subject across the entire schedule."""
        productivity = {s: 0.0 for s in Subject}
        
        for date, sessions in self.schedule.items():
            for session in sessions:
                productivity[session.subject] += session.calculate_productivity()
        
        return productivity
    
    def print_schedule(self):
        """Print the entire study schedule in a human-readable format."""
        current_date = self.start_date
        while current_date <= self.end_date:
            sessions = self.schedule[current_date]
            if not sessions:
                current_date += datetime.timedelta(days=1)
                continue
                
            print(f"\n{current_date.strftime('%A, %B %d, %Y')}:")
            for i, session in enumerate(sessions, 1):
                print(f"  {i}. {session.subject.value} - {session.method.value}: "
                      f"{session.duration} mins (Effectiveness: {session.effectiveness:.2f})")
            
            current_date += datetime.timedelta(days=1)

# Example usage
if __name__ == "__main__":
    try:
        # Define class effectiveness metrics (Retina's updated strategies)
        class_effectiveness = [
            ClassEffectiveness(Subject.BIOLOGY, StudyMethod.LECTURE, 0.8),
            ClassEffectiveness(Subject.BIOLOGY, StudyMethod.PRACTICE, 0.9),
            ClassEffectiveness(Subject.BIOLOGY, StudyMethod.REVISION, 0.7),
            ClassEffectiveness(Subject.BIOLOGY, StudyMethod.MOCK_TEST, 0.95),
            ClassEffectiveness(Subject.CHEMISTRY, StudyMethod.LECTURE, 0.75),
            ClassEffectiveness(Subject.CHEMISTRY, StudyMethod.PRACTICE, 0.85),
            ClassEffectiveness(Subject.CHEMISTRY, StudyMethod.REVISION, 0.8),
            ClassEffectiveness(Subject.CHEMISTRY, StudyMethod.MOCK_TEST, 0.9),
            ClassEffectiveness(Subject.PHYSICS, StudyMethod.LECTURE, 0.7),
            ClassEffectiveness(Subject.PHYSICS, StudyMethod.PRACTICE, 0.8),
            ClassEffectiveness(Subject.PHYSICS, StudyMethod.REVISION, 0.75),
            ClassEffectiveness(Subject.PHYSICS, StudyMethod.MOCK_TEST, 0.85),
            ClassEffectiveness(Subject.MATHEMATICS, StudyMethod.LECT
