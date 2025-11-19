"""
Generated Code Metadata:
========================
Original URL: https://opensea.institute
Prompt: Create a data model for tracking patient outcomes and progress in a psychiatry and coaching setting, considering factors like mental health metrics and treatment efficacy.
Generated: DETERMINISTIC_2bb1f8ea57b71f59
Batch ID: 20250622_205139
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
from enum import Enum
from typing import List

class MentalHealthMetric(Enum):
    """ Enum for different mental health metrics """
    ANXIETY = "anxiety"
    DEPRESSION = "depression"
    STRESS = "stress"
    MOOD = "mood"
    SLEEP_QUALITY = "sleep_quality"

class PatientOutcome:
    """ Data model for tracking patient outcomes and progress """

    def __init__(self, patient_id: int, metric: MentalHealthMetric, score: float, timestamp: datetime = None):
        """
        Initialize a patient outcome

        Args:
        - patient_id (int): Unique identifier for the patient
        - metric (MentalHealthMetric): The mental health metric being tracked
        - score (float): The patient's score for the given metric
        - timestamp (datetime): The timestamp for when the outcome was recorded (default: current time)
        """
        self.patient_id = patient_id
        self.metric = metric
        self.score = score
        self.timestamp = timestamp if timestamp else datetime.now()

class Treatment:
    """ Data model for a treatment or intervention """

    def __init__(self, treatment_id: int, name: str, description: str):
        """
        Initialize a treatment

        Args:
        - treatment_id (int): Unique identifier for the treatment
        - name (str): The name of the treatment
        - description (str): A brief description of the treatment
        """
        self.treatment_id = treatment_id
        self.name = name
        self.description = description

class PatientProgress:
    """ Data model for tracking patient progress """

    def __init__(self, patient_id: int):
        """
        Initialize a patient's progress

        Args:
        - patient_id (int): Unique identifier for the patient
        """
        self.patient_id = patient_id
        self.outcomes: List[PatientOutcome] = []
        self.treatments: List[Treatment] = []

    def add_outcome(self, outcome: PatientOutcome):
        """ Add a patient outcome to the patient's progress """
        self.outcomes.append(outcome)

    def add_treatment(self, treatment: Treatment):
        """ Add a treatment to the patient's progress """
        self.treatments.append(treatment)

    def get_outcomes(self, metric: MentalHealthMetric = None):
        """
        Get the patient's outcomes

        Args:
        - metric (MentalHealthMetric): Optional filter by metric

        Returns:
        - List[PatientOutcome]: The patient's outcomes
        """
        if metric:
            return [o for o in self.outcomes if o.metric == metric]
        return self.outcomes

    def get_treatments(self):
        """ Get the patient's treatments """
        return self.treatments

def calculate_treatment_efficacy(progress: PatientProgress, treatment: Treatment):
    """
    Calculate the efficacy of a treatment

    Args:
    - progress (PatientProgress): The patient's progress
    - treatment (Treatment): The treatment to evaluate

    Returns:
    - float: The efficacy of the treatment (as a percentage)
    """
    # For simplicity, this example assumes efficacy is the average improvement in a specific metric
    # In a real-world application, this would be a more complex calculation
    outcomes = progress.get_outcomes()
    treatment_outcomes = [o for o in outcomes if o.metric == MentalHealthMetric.MOOD]
    if not treatment_outcomes:
        return 0.0

    initial_score = treatment_outcomes[0].score
    final_score = treatment_outcomes[-1].score
    improvement = (final_score - initial_score) / initial_score * 100
    return improvement

# Example usage
if __name__ == "__main__":
    patient_progress = PatientProgress(1)

    treatment = Treatment(1, "Cognitive Behavioral Therapy", "A type of talk therapy")
    patient_progress.add_treatment(treatment)

    outcome1 = PatientOutcome(1, MentalHealthMetric.MOOD, 50.0)
    outcome2 = PatientOutcome(1, MentalHealthMetric.MOOD, 70.0, datetime(2024, 9, 16))
    patient_progress.add_outcome(outcome1)
    patient_progress.add_outcome(outcome2)

    efficacy = calculate_treatment_efficacy(patient_progress, treatment)
    print(f"Treatment efficacy: {efficacy}%")

    print("Patient outcomes:")
    for outcome in patient_progress.get_outcomes():
        print(f"Metric: {outcome.metric.value}, Score: {outcome.score}, Timestamp: {outcome.timestamp}")
```
