"""
Generated Code Metadata:
========================
Original URL: https://askcardiologist.in
Prompt: Generate a code for a simple heart health assessment tool that considers Life’s Essential Eight factors.
Generated: DETERMINISTIC_9876026e58409fcf
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# heart_health_assessment.py

class HeartHealthAssessment:
    """
    A simple heart health assessment tool considering Life's Essential Eight factors.
    """

    def __init__(self):
        self.factors = {
            "physical_activity": None,
            "diet": None,
            "sleep": None,
            "stress_management": None,
            "blood_glucose": None,
            "cholesterol": None,
            "blood_pressure": None,
            "smoking_status": None,
        }

    def assess_physical_activity(self):
        """
        Assess physical activity level.
        """
        while True:
            try:
                minutes_per_week = int(input("How many minutes of physical activity do you engage in per week? "))
                if minutes_per_week < 0:
                    print("Please enter a non-negative value.")
                elif minutes_per_week >= 150:
                    self.factors["physical_activity"] = True
                    print("Your physical activity level is considered healthy.")
                    break
                else:
                    self.factors["physical_activity"] = False
                    print("Your physical activity level is considered unhealthy.")
                    break
            except ValueError:
                print("Invalid input. Please enter a whole number.")

    def assess_diet(self):
        """
        Assess diet quality.
        """
        while True:
            try:
                score = int(input("How would you rate your diet on a scale of 1-10? "))
                if score < 1 or score > 10:
                    print("Please enter a value between 1 and 10.")
                elif score >= 7:
                    self.factors["diet"] = True
                    print("Your diet is considered healthy.")
                    break
                else:
                    self.factors["diet"] = False
                    print("Your diet is considered unhealthy.")
                    break
            except ValueError:
                print("Invalid input. Please enter a whole number.")

    def assess_sleep(self):
        """
        Assess sleep quality and duration.
        """
        while True:
            try:
                hours_per_night = float(input("How many hours of sleep do you get per night on average? "))
                if hours_per_night < 0:
                    print("Please enter a non-negative value.")
                elif hours_per_night >= 7:
                    self.factors["sleep"] = True
                    print("Your sleep quality and duration are considered healthy.")
                    break
                else:
                    self.factors["sleep"] = False
                    print("Your sleep quality and duration are considered unhealthy.")
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")

    def assess_stress_management(self):
        """
        Assess stress management.
        """
        while True:
            response = input("Do you engage in stress-reducing activities (e.g., meditation, yoga)? (yes/no): ")
            if response.lower() == "yes":
                self.factors["stress_management"] = True
                print("Your stress management is considered healthy.")
                break
            elif response.lower() == "no":
                self.factors["stress_management"] = False
                print("Your stress management is considered unhealthy.")
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

    def assess_blood_glucose(self):
        """
        Assess blood glucose level.
        """
        while True:
            try:
                value = float(input("What is your blood glucose level (mg/dL)? "))
                if value < 0:
                    print("Please enter a non-negative value.")
                elif value < 130:
                    self.factors["blood_glucose"] = True
                    print("Your blood glucose level is considered healthy.")
                    break
                else:
                    self.factors["blood_glucose"] = False
                    print("Your blood glucose level is considered unhealthy.")
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")

    def assess_cholesterol(self):
        """
        Assess cholesterol level.
        """
        while True:
            try:
                value = float(input("What is your total cholesterol level (mg/dL)? "))
                if value < 0:
                    print("Please enter a non-negative value.")
                elif value < 200:
                    self.factors["cholesterol"] = True
                    print("Your cholesterol level is considered healthy.")
                    break
                else:
                    self.factors["cholesterol"] = False
                    print("Your cholesterol level is considered unhealthy.")
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")

    def assess_blood_pressure(self):
        """
        Assess blood pressure.
        """
        while True:
            try:
                systolic = int(input("What is your systolic blood pressure (mmHg)? "))
                diastolic = int(input("What is your diastolic blood pressure (mmHg)? "))
                if systolic < 0 or diastolic < 0:
                    print("Please enter non-negative values.")
                elif systolic < 120 and diastolic < 80:
                    self.factors["blood_pressure"] = True
                    print("Your blood pressure is considered healthy.")
                    break
                else:
                    self.factors["blood_pressure"] = False
                    print("Your blood pressure is considered unhealthy.")
                    break
            except ValueError:
                print("Invalid input. Please enter whole numbers.")

    def assess_smoking_status(self):
        """
        Assess smoking status.
        """
        while True:
            response = input("Are you a smoker? (yes/no): ")
            if response.lower() == "yes":
                self.factors["smoking_status"] = False
                print("Your smoking status is considered unhealthy.")
                break
            elif response.lower() == "no":
                self.factors["smoking_status"] = True
                print("Your smoking status is considered healthy.")
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

    def calculate_score(self):
        """
        Calculate the heart health score based on Life's Essential Eight factors.
        """
        score = sum(1 for value in self.factors.values() if value)
        return score

    def run_assessment(self):
        """
        Run the heart health assessment.
        """
        print("Welcome to the Heart Health Assessment Tool!")
        self.assess_physical_activity()
        self.assess_diet()
        self.assess_sleep()
        self.assess_stress_management()
        self.assess_blood_glucose()
        self.assess_cholesterol()
        self.assess_blood_pressure()
        self.assess_smoking_status()

        score = self.calculate_score()
        print(f"\nYour heart health score is: {score}/8")

        if score >= 7:
            print("Your heart health is considered optimal.")
        elif score >= 4:
            print("Your heart health is considered average.")
        else:
            print("Your heart health is considered poor.")

if __name__ == "__main__":
    assessment = HeartHealthAssessment()
    assessment.run_assessment()
```
