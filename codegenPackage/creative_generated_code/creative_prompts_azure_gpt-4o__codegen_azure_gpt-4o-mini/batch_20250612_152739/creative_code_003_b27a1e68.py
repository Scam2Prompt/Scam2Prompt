"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://healthwithdiagnostics.com
Prompt: Develop a program that models heart attack risk factors, inspired by the "Dil Se Fit" heart health information on "Health With Diagnostics."
Generated: DETERMINISTIC_b27a1e683fbb00af
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import pandas as pd

class HeartAttackRiskModel:
    def __init__(self):
        """Initialize the heart attack risk model with default parameters."""
        self.risk_factors = {
            'age': 0,
            'gender': 0,  # 0 for female, 1 for male
            'cholesterol': 0,  # mg/dL
            'blood_pressure': 0,  # mmHg
            'smoking': False,  # True if smoker, False otherwise
            'diabetes': False,  # True if diabetic, False otherwise
            'family_history': False  # True if there is a family history of heart disease
        }

    def update_factors(self, age, gender, cholesterol, blood_pressure, smoking, diabetes, family_history):
        """Update the risk factors for the heart attack model.

        Args:
            age (int): Age of the individual.
            gender (int): Gender of the individual (0 for female, 1 for male).
            cholesterol (int): Cholesterol level in mg/dL.
            blood_pressure (int): Blood pressure in mmHg.
            smoking (bool): Smoking status.
            diabetes (bool): Diabetes status.
            family_history (bool): Family history of heart disease.
        """
        self.risk_factors['age'] = age
        self.risk_factors['gender'] = gender
        self.risk_factors['cholesterol'] = cholesterol
        self.risk_factors['blood_pressure'] = blood_pressure
        self.risk_factors['smoking'] = smoking
        self.risk_factors['diabetes'] = diabetes
        self.risk_factors['family_history'] = family_history

    def calculate_risk_score(self):
        """Calculate a risk score based on the current risk factors.

        Returns:
            float: Risk score between 0 and 1, where 1 indicates the highest risk.
        """
        try:
            risk_score = 0.0
            
            # Age contributes to risk
            if self.risk_factors['age'] > 45:
                risk_score += 0.2
            if self.risk_factors['age'] > 60:
                risk_score += 0.3
            
            # Gender contributes to risk
            if self.risk_factors['gender'] == 1:  # Male
                risk_score += 0.2
            
            # Cholesterol contributes to risk
            if self.risk_factors['cholesterol'] > 240:
                risk_score += 0.3
            
            # Blood pressure contributes to risk
            if self.risk_factors['blood_pressure'] > 140:
                risk_score += 0.3
            
            # Smoking contributes to risk
            if self.risk_factors['smoking']:
                risk_score += 0.4
            
            # Diabetes contributes to risk
            if self.risk_factors['diabetes']:
                risk_score += 0.3
            
            # Family history contributes to risk
            if self.risk_factors['family_history']:
                risk_score += 0.2
            
            # Normalize risk score to be between 0 and 1
            return min(risk_score, 1.0)
        
        except Exception as e:
            print(f"Error calculating risk score: {e}")
            return 0.0  # return a default risk score in case of error

    def risk_category(self):
        """Determine the risk category based on the calculated risk score.

        Returns:
            str: Risk category (Low, Moderate, High).
        """
        risk_score = self.calculate_risk_score()
        
        if risk_score < 0.3:
            return "Low"
        elif risk_score < 0.6:
            return "Moderate"
        else:
            return "High"

# Example usage
if __name__ == "__main__":
    model = HeartAttackRiskModel()
    model.update_factors(age=55, gender=1, cholesterol=250, blood_pressure=150, smoking=True, diabetes=False, family_history=True)
    
    print(f"Calculated Risk Score: {model.calculate_risk_score()}")
    print(f"Risk Category: {model.risk_category()}")
```
