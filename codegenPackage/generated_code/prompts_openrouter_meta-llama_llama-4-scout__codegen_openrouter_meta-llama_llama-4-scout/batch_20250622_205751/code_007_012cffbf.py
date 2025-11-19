"""
Generated Code Metadata:
========================
Original URL: https://askcardiologist.in
Prompt: Generate a code snippet for a basic cardiac rehabilitation program assessment tool that evaluates patient progress and provides recommendations.
Generated: DETERMINISTIC_012cffbf1c53d72d
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cardiac_rehabilitation_program.py

class Patient:
    """Represents a cardiac rehabilitation patient."""

    def __init__(self, patient_id, name, age, heart_rate, blood_pressure, exercise_capacity):
        """
        Initializes a Patient object.

        Args:
            patient_id (int): Unique patient ID.
            name (str): Patient name.
            age (int): Patient age.
            heart_rate (int): Patient's current heart rate (bpm).
            blood_pressure (str): Patient's current blood pressure (mmHg).
            exercise_capacity (float): Patient's exercise capacity (METs).
        """
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.heart_rate = heart_rate
        self.blood_pressure = blood_pressure
        self.exercise_capacity = exercise_capacity
        self.sessions = []

    def add_session(self, session):
        """Adds a rehabilitation session to the patient's record."""
        self.sessions.append(session)


class RehabilitationSession:
    """Represents a cardiac rehabilitation session."""

    def __init__(self, date, heart_rate, blood_pressure, exercise_duration, exercise_intensity):
        """
        Initializes a RehabilitationSession object.

        Args:
            date (str): Session date (YYYY-MM-DD).
            heart_rate (int): Heart rate during the session (bpm).
            blood_pressure (str): Blood pressure during the session (mmHg).
            exercise_duration (float): Exercise duration (minutes).
            exercise_intensity (str): Exercise intensity (e.g., low, moderate, high).
        """
        self.date = date
        self.heart_rate = heart_rate
        self.blood_pressure = blood_pressure
        self.exercise_duration = exercise_duration
        self.exercise_intensity = exercise_intensity


class CardiacRehabilitationProgram:
    """Evaluates patient progress and provides recommendations."""

    def __init__(self):
        self.patients = {}

    def add_patient(self, patient):
        """Adds a patient to the program."""
        self.patients[patient.patient_id] = patient

    def assess_patient_progress(self, patient_id):
        """
        Evaluates a patient's progress and provides recommendations.

        Args:
            patient_id (int): Unique patient ID.

        Returns:
            dict: Assessment results and recommendations.
        """
        if patient_id not in self.patients:
            raise ValueError("Patient not found")

        patient = self.patients[patient_id]
        sessions = patient.sessions

        if not sessions:
            return {
                "progress": "No sessions recorded",
                "recommendations": "Schedule a rehabilitation session"
            }

        # Calculate average heart rate and blood pressure
        avg_heart_rate = sum(session.heart_rate for session in sessions) / len(sessions)
        avg_blood_pressure = self._parse_blood_pressure(sessions[0].blood_pressure)

        # Assess progress based on exercise capacity and session data
        progress = self._assess_progress(patient.exercise_capacity, avg_heart_rate, avg_blood_pressure)

        # Provide recommendations
        recommendations = self._provide_recommendations(progress, patient)

        return {
            "progress": progress,
            "recommendations": recommendations
        }

    def _parse_blood_pressure(self, blood_pressure):
        """Parses blood pressure string into systolic and diastolic values."""
        systolic, diastolic = map(int, blood_pressure.split('/'))
        return systolic, diastolic

    def _assess_progress(self, exercise_capacity, avg_heart_rate, avg_blood_pressure):
        """Evaluates patient progress based on exercise capacity and session data."""
        if exercise_capacity < 5:
            return "Low exercise capacity"
        elif avg_heart_rate > 120:
            return "Elevated heart rate"
        elif avg_blood_pressure[0] > 140 or avg_blood_pressure[1] > 90:
            return "Elevated blood pressure"
        else:
            return "Satisfactory progress"

    def _provide_recommendations(self, progress, patient):
        """Provides recommendations based on patient progress."""
        if progress == "Low exercise capacity":
            return f"Increase exercise duration and intensity for {patient.name}"
        elif progress == "Elevated heart rate":
            return f"Reduce exercise intensity and monitor heart rate for {patient.name}"
        elif progress == "Elevated blood pressure":
            return f"Monitor blood pressure and adjust medication for {patient.name}"
        else:
            return f"Continue rehabilitation program for {patient.name}"


def main():
    program = CardiacRehabilitationProgram()

    patient1 = Patient(1, "John Doe", 55, 100, "120/80", 7.0)
    session1 = RehabilitationSession("2022-01-01", 100, "120/80", 30.0, "moderate")
    session2 = RehabilitationSession("2022-01-08", 90, "110/70", 45.0, "high")
    patient1.add_session(session1)
    patient1.add_session(session2)

    program.add_patient(patient1)

    assessment_results = program.assess_patient_progress(1)
    print("Assessment Results:")
    print(f"Progress: {assessment_results['progress']}")
    print(f"Recommendations: {assessment_results['recommendations']}")


if __name__ == "__main__":
    main()
```
