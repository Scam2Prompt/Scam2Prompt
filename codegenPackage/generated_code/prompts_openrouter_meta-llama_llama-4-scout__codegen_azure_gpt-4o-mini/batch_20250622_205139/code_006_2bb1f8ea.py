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
from typing import List, Optional
from pydantic import BaseModel, Field, condecimal, constr, validator

class MentalHealthMetric(BaseModel):
    """Model to represent a mental health metric."""
    name: constr(min_length=1)  # Name of the metric (e.g., anxiety level)
    value: condecimal(gt=-1, lt=11)  # Value of the metric (0-10 scale)
    date_recorded: datetime  # Date when the metric was recorded

    @validator('date_recorded')
    def check_date_not_future(cls, v):
        """Ensure the recorded date is not in the future."""
        if v > datetime.now():
            raise ValueError('Date recorded cannot be in the future.')
        return v

class Treatment(BaseModel):
    """Model to represent a treatment plan."""
    treatment_type: constr(min_length=1)  # Type of treatment (e.g., therapy, medication)
    start_date: datetime  # Start date of the treatment
    end_date: Optional[datetime] = None  # End date of the treatment, if applicable
    efficacy_rating: Optional[condecimal(gt=-1, lt=11)] = None  # Efficacy rating (0-10 scale)

    @validator('start_date')
    def check_start_date(cls, v):
        """Ensure the start date is not in the future."""
        if v > datetime.now():
            raise ValueError('Start date cannot be in the future.')
        return v

    @validator('end_date', always=True)
    def check_end_date(cls, v, values):
        """Ensure the end date is after the start date, if provided."""
        if v and v < values.get('start_date'):
            raise ValueError('End date must be after the start date.')
        return v

class PatientOutcome(BaseModel):
    """Model to represent a patient's outcome and progress."""
    patient_id: constr(min_length=1)  # Unique identifier for the patient
    metrics: List[MentalHealthMetric]  # List of mental health metrics
    treatments: List[Treatment]  # List of treatments the patient has undergone
    last_updated: datetime = Field(default_factory=datetime.now)  # Last updated timestamp

    @validator('metrics', each_item=True)
    def check_metrics_not_empty(cls, v):
        """Ensure that each metric has a valid value."""
        if v.value is None:
            raise ValueError('Metric value cannot be None.')
        return v

    @validator('treatments', each_item=True)
    def check_treatments_not_empty(cls, v):
        """Ensure that each treatment has a valid treatment type."""
        if not v.treatment_type:
            raise ValueError('Treatment type cannot be empty.')
        return v

# Example usage
if __name__ == "__main__":
    try:
        # Create a sample patient outcome
        patient_outcome = PatientOutcome(
            patient_id="12345",
            metrics=[
                MentalHealthMetric(name="Anxiety Level", value=5.0, date_recorded=datetime.now()),
                MentalHealthMetric(name="Depression Level", value=3.0, date_recorded=datetime.now())
            ],
            treatments=[
                Treatment(treatment_type="Cognitive Behavioral Therapy", start_date=datetime.now())
            ]
        )
        print(patient_outcome.json(indent=4))
    except ValueError as e:
        print(f"Error creating patient outcome: {e}")
```
