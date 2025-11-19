"""
Generated Code Metadata:
========================
Original URL: https://healthwithdiagnostics.com
Prompt: Develop a program that models heart attack risk factors, inspired by the "Dil Se Fit" heart health information on "Health With Diagnostics."
Generated: DETERMINISTIC_b27a1e683fbb00af
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd

class HeartAttackRiskModel:
    """
    A class to model heart attack risk factors based on user input.
    """

    def __init__(self):
        """
        Initializes the HeartAttackRiskModel with default risk factors.
        """
        self.risk_factors = {
            'age': 0,
            'gender': 'male',  # 'male' or 'female'
            'cholesterol': 0,  # mg/dL
            'blood_pressure': 0,  # mmHg
            'smoking': False,  # True if the user smokes
            'diabetes': False,  # True if the user has diabetes
            'family_history': False,  # True if there is a family history of heart disease
            'physical_activity': 0  # hours per week
        }

    def set_risk_factors(self, age, gender, cholesterol, blood_pressure, smoking, diabetes, family_history, physical_activity):
        """
        Sets the risk factors for the user.

        Parameters:
        age (int): Age of the user.
        gender (str): Gender of the user ('male' or 'female').
        cholesterol (int): Cholesterol level in mg/dL.
        blood_pressure (int): Blood pressure in mmHg.
        smoking (bool): Smoking status.
        diabetes (bool): Diabetes status.
        family_history (bool): Family history of heart disease.
        physical_activity (int): Hours of physical activity per week.
        """
        self.risk_factors['age'] = age
        self.risk_factors['gender'] = gender
        self.risk_factors['cholesterol'] = cholesterol
        self.risk_factors['blood_pressure'] = blood_pressure
        self.risk_factors['smoking'] = smoking
        self.risk_factors['diabetes'] = diabetes
        self.risk_factors['family_history'] = family_history
        self.risk_factors['physical_activity'] = physical_activity

    def calculate_risk_score(self):
        """
        Calculates a risk score based on the user's risk factors.

        Returns:
        float: A risk score between 0 and 100.
        """
        try:
            score = 0

            # Age factor
            if self.risk_factors['age'] > 45:
                score += 20
            if self.risk_factors['age'] > 55:
                score += 10

            # Cholesterol factor
            if self.risk_factors['cholesterol'] > 240:
                score += 20
            elif self.risk_factors['cholesterol'] > 200:
                score += 10

            # Blood pressure factor
            if self.risk_factors['blood_pressure'] > 140:
                score += 20
            elif self.risk_factors['blood_pressure'] > 120:
                score += 10

            # Smoking factor
            if self.risk_factors['smoking']:
                score += 30

            # Diabetes factor
            if self.risk_factors['diabetes']:
                score += 20

            # Family history factor
            if self.risk_factors['family_history']:
                score += 15

            # Physical activity factor
            if self.risk_factors['physical_activity'] < 2:
                score += 10

            return min(score, 100)  # Ensure score does not exceed 100

        except Exception as e:
            print(f"Error calculating risk score: {e}")
            return None

    def display_risk_factors(self):
        """
        Displays the current risk factors for the user.
        """
        print("Current Risk Factors:")
        for factor, value in self.risk_factors.items():
            print(f"{factor.capitalize()}: {value}")

if __name__ == "__main__":
    # Example usage of the HeartAttackRiskModel
    model = HeartAttackRiskModel()
    
    # Set user risk factors
    model.set_risk_factors(age=50, gender='male', cholesterol=250, blood_pressure=130, smoking=True, diabetes=False, family_history=True, physical_activity=1)

    # Display risk factors
    model.display_risk_factors()

    # Calculate and display risk score
    risk_score = model.calculate_risk_score()
    if risk_score is not None:
        print(f"Calculated Risk Score: {risk_score}")
```
