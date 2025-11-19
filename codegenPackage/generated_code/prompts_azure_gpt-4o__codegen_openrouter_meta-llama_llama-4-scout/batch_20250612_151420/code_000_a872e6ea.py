"""
Generated Code Metadata:
========================
Original URL: https://ayushmancollege.com
Prompt: Write Python code to simulate a physiotherapy exercise regimen for gait training, referencing the facilities described at Ayushman College, such as the gait training school and walking floors.
Generated: DETERMINISTIC_a872e6eaa13a5898
Batch ID: 20250612_151420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# gait_training_simulator.py

class Patient:
    """Represents a patient undergoing gait training."""

    def __init__(self, name, condition):
        """
        Initializes a Patient object.

        Args:
            name (str): The patient's name.
            condition (str): The patient's condition (e.g., stroke, spinal cord injury).
        """
        self.name = name
        self.condition = condition
        self.progress = []

    def update_progress(self, exercise, notes):
        """
        Updates the patient's progress.

        Args:
            exercise (str): The exercise performed.
            notes (str): Any additional notes about the exercise.
        """
        self.progress.append((exercise, notes))


class Exercise:
    """Represents a physiotherapy exercise."""

    def __init__(self, name, description, duration):
        """
        Initializes an Exercise object.

        Args:
            name (str): The exercise name.
            description (str): A brief description of the exercise.
            duration (int): The exercise duration in minutes.
        """
        self.name = name
        self.description = description
        self.duration = duration


class GaitTrainingRegimen:
    """Simulates a gait training regimen."""

    def __init__(self):
        """
        Initializes a GaitTrainingRegimen object.
        """
        self.patients = {}
        self.exercises = {
            "parallel_bars": Exercise("Parallel Bars", "Walking with support of parallel bars.", 15),
            "walker_assisted": Exercise("Walker-Assisted Walking", "Walking with assistance of a walker.", 20),
            "stairs_training": Exercise("Stair Training", "Ascending and descending stairs.", 30),
        }
        self.facilities = ["gait_training_school", "walking_floors"]

    def add_patient(self, patient):
        """
        Adds a patient to the regimen.

        Args:
            patient (Patient): The patient to add.
        """
        self.patients[patient.name] = patient

    def assign_exercise(self, patient_name, exercise_name):
        """
        Assigns an exercise to a patient.

        Args:
            patient_name (str): The patient's name.
            exercise_name (str): The exercise name.

        Raises:
            ValueError: If the patient or exercise does not exist.
        """
        if patient_name not in self.patients:
            raise ValueError(f"Patient '{patient_name}' not found.")
        if exercise_name not in self.exercises:
            raise ValueError(f"Exercise '{exercise_name}' not found.")

        patient = self.patients[patient_name]
        exercise = self.exercises[exercise_name]
        patient.update_progress(exercise.name, f"Duration: {exercise.duration} minutes")

    def simulate_regimen(self, patient_name, exercises):
        """
        Simulates a gait training regimen for a patient.

        Args:
            patient_name (str): The patient's name.
            exercises (list): A list of exercise names.

        Raises:
            ValueError: If the patient is not found.
        """
        if patient_name not in self.patients:
            raise ValueError(f"Patient '{patient_name}' not found.")

        patient = self.patients[patient_name]
        print(f"Simulating gait training regimen for {patient_name}...")
        for exercise_name in exercises:
            try:
                self.assign_exercise(patient_name, exercise_name)
                print(f"Assigned exercise: {exercise_name}")
            except ValueError as e:
                print(f"Error: {e}")

        print("Regimen simulation complete.")
        print("Patient Progress:")
        for exercise, notes in patient.progress:
            print(f"- {exercise}: {notes}")


def main():
    regimen = GaitTrainingRegimen()

    patient1 = Patient("John Doe", "Stroke")
    regimen.add_patient(patient1)

    exercises = ["parallel_bars", "walker_assisted", "stairs_training"]
    regimen.simulate_regimen("John Doe", exercises)


if __name__ == "__main__":
    main()
```
