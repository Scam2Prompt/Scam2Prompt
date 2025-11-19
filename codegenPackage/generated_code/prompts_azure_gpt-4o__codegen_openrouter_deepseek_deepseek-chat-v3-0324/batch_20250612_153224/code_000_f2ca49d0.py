"""
Generated Code Metadata:
========================
Original URL: https://neshagroup.ir
Prompt: "Write Python code to implement a virtual assessment center for evaluating behavioral competencies, as described by Nesha Group's services."
Generated: DETERMINISTIC_f2ca49d0be10a1c8
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional
from enum import Enum
from datetime import datetime
import uuid
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class CompetencyType(Enum):
    """Enum for different types of behavioral competencies"""
    LEADERSHIP = "Leadership"
    COMMUNICATION = "Communication"
    PROBLEM_SOLVING = "Problem Solving"
    TEAMWORK = "Teamwork"
    ADAPTABILITY = "Adaptability"

class AssessmentMethod(Enum):
    """Enum for different assessment methods"""
    CASE_STUDY = "Case Study"
    ROLE_PLAY = "Role Play"
    GROUP_DISCUSSION = "Group Discussion"
    PRESENTATION = "Presentation"
    INTERVIEW = "Interview"

class Participant:
    """Class representing a participant in the assessment center"""
    def __init__(self, participant_id: str, name: str, email: str):
        self.participant_id = participant_id
        self.name = name
        self.email = email
        self.assessments: Dict[str, 'Assessment'] = {}

    def add_assessment(self, assessment: 'Assessment') -> None:
        """Add an assessment to the participant"""
        if assessment.assessment_id in self.assessments:
            raise ValueError("Assessment already exists for this participant")
        self.assessments[assessment.assessment_id] = assessment

    def get_assessment_results(self) -> Dict[str, Dict]:
        """Get all assessment results for the participant"""
        return {
            assessment_id: assessment.get_results()
            for assessment_id, assessment in self.assessments.items()
        }

class Assessor:
    """Class representing an assessor in the assessment center"""
    def __init__(self, assessor_id: str, name: str, email: str):
        self.assessor_id = assessor_id
        self.name = name
        self.email = email
        self.assigned_assessments: List['Assessment'] = []

    def assign_assessment(self, assessment: 'Assessment') -> None:
        """Assign an assessment to the assessor"""
        self.assigned_assessments.append(assessment)

    def evaluate_participant(
        self,
        assessment: 'Assessment',
        participant: Participant,
        scores: Dict[CompetencyType, int],
        feedback: str
    ) -> None:
        """Evaluate a participant's performance in an assessment"""
        if assessment not in self.assigned_assessments:
            raise ValueError("Assessor not assigned to this assessment")
        
        if participant.participant_id not in assessment.participants:
            raise ValueError("Participant not in this assessment")
        
        assessment.record_evaluation(
            participant.participant_id,
            self.assessor_id,
            scores,
            feedback
        )

class Assessment:
    """Class representing an assessment in the center"""
    def __init__(
        self,
        assessment_id: str,
        name: str,
        method: AssessmentMethod,
        competencies: List[CompetencyType],
        max_score: int = 10
    ):
        self.assessment_id = assessment_id
        self.name = name
        self.method = method
        self.competencies = competencies
        self.max_score = max_score
        self.participants: Dict[str, Participant] = {}
        self.evaluations: Dict[str, Dict] = {}  # participant_id -> evaluations
        self.start_time: Optional[datetime] = None
        self.end_time: Optional[datetime] = None

    def add_participant(self, participant: Participant) -> None:
        """Add a participant to the assessment"""
        if participant.participant_id in self.participants:
            raise ValueError("Participant already in this assessment")
        self.participants[participant.participant_id] = participant
        participant.add_assessment(self)

    def start_assessment(self) -> None:
        """Mark the assessment as started"""
        if self.start_time is not None:
            raise ValueError("Assessment already started")
        self.start_time = datetime.now()

    def end_assessment(self) -> None:
        """Mark the assessment as ended"""
        if self.start_time is None:
            raise ValueError("Assessment not started")
        if self.end_time is not None:
            raise ValueError("Assessment already ended")
        self.end_time = datetime.now()

    def record_evaluation(
        self,
        participant_id: str,
        assessor_id: str,
        scores: Dict[CompetencyType, int],
        feedback: str
    ) -> None:
        """Record an evaluation for a participant"""
        if participant_id not in self.participants:
            raise ValueError("Participant not in this assessment")
        
        for score in scores.values():
            if not 0 <= score <= self.max_score:
                raise ValueError(f"Score must be between 0 and {self.max_score}")
        
        if participant_id not in self.evaluations:
            self.evaluations[participant_id] = []
        
        evaluation = {
            "assessor_id": assessor_id,
            "scores": {comp.value: score for comp, score in scores.items()},
            "feedback": feedback,
            "timestamp": datetime.now().isoformat()
        }
        
        self.evaluations[participant_id].append(evaluation)

    def get_results(self) -> Dict:
        """Get results for all participants in this assessment"""
        return {
            "assessment_id": self.assessment_id,
            "name": self.name,
            "method": self.method.value,
            "participants": {
                pid: {
                    "evaluations": evals,
                    "average_scores": self._calculate_average_scores(pid)
                }
                for pid, evals in self.evaluations.items()
            }
        }

    def _calculate_average_scores(self, participant_id: str) -> Dict[str, float]:
        """Calculate average scores for a participant"""
        if participant_id not in self.evaluations:
            return {}
        
        scores = {comp.value: [] for comp in self.competencies}
        
        for evaluation in self.evaluations[participant_id]:
            for comp, score in evaluation["scores"].items():
                scores[comp].append(score)
        
        return {
            comp: sum(score_list) / len(score_list)
            for comp, score_list in scores.items() if score_list
        }

class VirtualAssessmentCenter:
    """Main class representing the virtual assessment center"""
    def __init__(self):
        self.participants: Dict[str, Participant] = {}
        self.assessors: Dict[str, Assessor] = {}
        self.assessments: Dict[str, Assessment] = {}

    def add_participant(self, name: str, email: str) -> str:
        """Add a new participant to the center"""
        participant_id = str(uuid.uuid4())
        participant = Participant(participant_id, name, email)
        self.participants[participant_id] = participant
        logger.info(f"Added participant: {name} ({participant_id})")
        return participant_id

    def add_assessor(self, name: str, email: str) -> str:
        """Add a new assessor to the center"""
        assessor_id = str(uuid.uuid4())
        assessor = Assessor(assessor_id, name, email)
        self.assessors[assessor_id] = assessor
        logger.info(f"Added assessor: {name} ({assessor_id})")
        return assessor_id

    def create_assessment(
        self,
        name: str,
        method: AssessmentMethod,
        competencies: List[CompetencyType],
        max_score: int = 10
    ) -> str:
        """Create a new assessment"""
        assessment_id = str(uuid.uuid4())
        assessment = Assessment(assessment_id, name, method, competencies, max_score)
        self.assessments[assessment_id] = assessment
        logger.info(f"Created assessment: {name} ({assessment_id})")
        return assessment_id

    def assign_assessor(self, assessment_id: str, assessor_id: str) -> None:
        """Assign an assessor to an assessment"""
        if assessment_id not in self.assessments:
            raise ValueError("Assessment not found")
        if assessor_id not in self.assessors:
            raise ValueError("Assessor not found")
        
        assessment = self.assessments[assessment_id]
        assessor = self.assessors[assessor_id]
        
        assessor.assign_assessment(assessment)
        logger.info(f"Assigned assessor {assessor_id} to assessment {assessment_id}")

    def enroll_participant(self, assessment_id: str, participant_id: str) -> None:
        """Enroll a participant in an assessment"""
        if assessment_id not in self.assessments:
            raise ValueError("Assessment not found")
        if participant_id not in self.participants:
            raise ValueError("Participant not found")
        
        assessment = self.assessments[assessment_id]
        participant = self.participants[participant_id]
