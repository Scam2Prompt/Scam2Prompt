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
import json

class Patient:
    """Class to represent a patient in the cardiac rehabilitation program."""
    
    def __init__(self, name, age, weight, height, heart_rate, blood_pressure):
        self.name = name
        self.age = age
        self.weight = weight  # in kg
        self.height = height  # in cm
        self.heart_rate = heart_rate  # in bpm
        self.blood_pressure = blood_pressure  # in mmHg (systolic, diastolic)

    def calculate_bmi(self):
        """Calculate Body Mass Index (BMI) of the patient."""
        height_m = self.height / 100  # convert cm to m
        bmi = self.weight / (height_m ** 2)
        return round(bmi, 2)

    def assess_progress(self):
        """Assess the patient's progress based on heart rate and blood pressure."""
        recommendations = []
        
        # Heart rate assessment
        if self.heart_rate < 60:
            recommendations.append("Heart rate is below normal. Consult a physician.")
        elif 60 <= self.heart_rate <= 100:
            recommendations.append("Heart rate is within normal range.")
        else:
            recommendations.append("Heart rate is above normal. Consult a physician.")
        
        # Blood pressure assessment
        systolic, diastolic = self.blood_pressure
        if systolic < 90 or diastolic < 60:
            recommendations.append("Blood pressure is too low. Consult a physician.")
        elif 90 <= systolic <= 120 and 60 <= diastolic <= 80:
            recommendations.append("Blood pressure is within normal range.")
        else:
            recommendations.append("Blood pressure is elevated. Consult a physician.")
        
        return recommendations

def save_patient_data(patient, filename='patient_data.json'):
    """Save patient data to a JSON file."""
    try:
        with open(filename, 'w') as file:
            json.dump(patient.__dict__, file)
        print(f"Patient data for {patient.name} saved successfully.")
    except IOError as e:
        print(f"Error saving patient data: {e}")

def load_patient_data(filename='patient_data.json'):
    """Load patient data from a JSON file."""
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            return Patient(**data)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error loading patient data: {e}")
        return None

def main():
    """Main function to run the cardiac rehabilitation assessment tool."""
    # Example patient data
    patient = Patient(name="John Doe", age=65, weight=80, height=175, heart_rate=75, blood_pressure=(120, 80))
    
    # Assess patient progress
    progress_report = patient.assess_progress()
    print(f"Assessment for {patient.name}:")
    for recommendation in progress_report:
        print(f"- {recommendation}")
    
    # Save patient data
    save_patient_data(patient)

if __name__ == "__main__":
    main()
```
