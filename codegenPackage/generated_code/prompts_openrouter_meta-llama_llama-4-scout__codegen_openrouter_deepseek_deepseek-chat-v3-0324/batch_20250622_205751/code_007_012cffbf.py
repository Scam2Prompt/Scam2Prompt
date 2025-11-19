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
"""
Cardiac Rehabilitation Assessment Tool
Evaluates patient progress and provides recommendations based on input parameters.
"""

class CardiacRehabAssessment:
    """
    A class to assess cardiac rehabilitation progress and provide recommendations.
    """

    def __init__(self):
        """
        Initialize assessment parameters with default values.
        """
        self.parameters = {
            'exercise_capacity': None,  # METs (Metabolic Equivalents)
            'blood_pressure': None,     # mmHg (systolic/diastolic)
            'resting_heart_rate': None, # bpm
            'cholesterol_levels': None, # mg/dL (total cholesterol)
            'patient_weight': None,     # kg
            'medication_adherence': None # percentage (0-100)
        }
        self.recommendations = []

    def input_parameters(self, exercise_capacity, blood_pressure, resting_heart_rate,
                        cholesterol_levels, patient_weight, medication_adherence):
        """
        Set patient parameters for assessment.
        
        Args:
            exercise_capacity (float): Patient's exercise capacity in METs
            blood_pressure (tuple): Systolic and diastolic blood pressure (mmHg)
            resting_heart_rate (int): Resting heart rate (bpm)
            cholesterol_levels (float): Total cholesterol level (mg/dL)
            patient_weight (float): Patient weight in kg
            medication_adherence (float): Percentage of medication adherence (0-100)
        """
        self.parameters['exercise_capacity'] = exercise_capacity
        self.parameters['blood_pressure'] = blood_pressure
        self.parameters['resting_heart_rate'] = resting_heart_rate
        self.parameters['cholesterol_levels'] = cholesterol_levels
        self.parameters['patient_weight'] = patient_weight
        self.parameters['medication_adherence'] = medication_adherence

    def assess_progress(self):
        """
        Evaluate patient progress based on input parameters and generate recommendations.
        """
        self.recommendations = []
        
        # Exercise capacity assessment
        if self.parameters['exercise_capacity'] < 5:
            self.recommendations.append("Increase aerobic exercise gradually under supervision")
        elif 5 <= self.parameters['exercise_capacity'] < 8:
            self.recommendations.append("Maintain current exercise program with gradual progression")
        else:
            self.recommendations.append("Excellent exercise capacity - continue current regimen")

        # Blood pressure assessment
        systolic, diastolic = self.parameters['blood_pressure']
        if systolic >= 140 or diastolic >= 90:
            self.recommendations.append("Blood pressure elevated - consult physician for possible medication adjustment")
        elif systolic >= 130 or diastolic >= 85:
            self.recommendations.append("Monitor blood pressure closely - consider dietary sodium reduction")
        else:
            self.recommendations.append("Blood pressure within normal range - maintain current management")

        # Resting heart rate assessment
        if self.parameters['resting_heart_rate'] > 100:
            self.recommendations.append("Elevated resting heart rate - consult physician")
        elif self.parameters['resting_heart_rate'] > 80:
            self.recommendations.append("Moderate resting heart rate - consider increasing aerobic exercise")
        else:
            self.recommendations.append("Normal resting heart rate - good cardiovascular fitness")

        # Cholesterol assessment
        if self.parameters['cholesterol_levels'] >= 240:
            self.recommendations.append("High cholesterol - consult physician for possible medication adjustment")
        elif self.parameters['cholesterol_levels'] >= 200:
            self.recommendations.append("Borderline high cholesterol - focus on dietary improvements")
        else:
            self.recommendations.append("Cholesterol within desirable range - maintain current diet")

        # Weight assessment
        bmi = self.parameters['patient_weight'] / ((1.7) ** 2)  # Simplified BMI calculation
        if bmi >= 30:
            self.recommendations.append("Obese - implement weight loss program with nutritionist")
        elif bmi >= 25:
            self.recommendations.append("Overweight - focus on gradual weight reduction")
        else:
            self.recommendations.append("Normal weight - maintain healthy diet")

        # Medication adherence assessment
        if self.parameters['medication_adherence'] < 80:
            self.recommendations.append("Low medication adherence - discuss barriers with healthcare team")
        elif self.parameters['medication_adherence'] < 95:
            self.recommendations.append("Moderate medication adherence - consider reminder strategies")
        else:
            self.recommendations.append("Excellent medication adherence - continue current regimen")

    def get_recommendations(self):
        """
        Return the generated recommendations.
        
        Returns:
            list: List of recommendations for the patient
        """
        return self.recommendations

    def print_assessment(self):
        """
        Print a formatted assessment report with recommendations.
        """
        print("\nCardiac Rehabilitation Progress Assessment")
        print("----------------------------------------")
        print(f"Exercise Capacity: {self.parameters['exercise_capacity']} METs")
        print(f"Blood Pressure: {self.parameters['blood_pressure'][0]}/{self.parameters['blood_pressure'][1]} mmHg")
        print(f"Resting Heart Rate: {self.parameters['resting_heart_rate']} bpm")
        print(f"Total Cholesterol: {self.parameters['cholesterol_levels']} mg/dL")
        print(f"Weight: {self.parameters['patient_weight']} kg")
        print(f"Medication Adherence: {self.parameters['medication_adherence']}%")
        
        print("\nRecommendations:")
        for i, recommendation in enumerate(self.recommendations, 1):
            print(f"{i}. {recommendation}")


# Example usage
if __name__ == "__main__":
    try:
        assessment = CardiacRehabAssessment()
        assessment.input_parameters(
            exercise_capacity=6.5,
            blood_pressure=(135, 88),
            resting_heart_rate=78,
            cholesterol_levels=210,
            patient_weight=82,
            medication_adherence=92
        )
        assessment.assess_progress()
        assessment.print_assessment()
    except Exception as e:
        print(f"An error occurred during assessment: {str(e)}")
```
