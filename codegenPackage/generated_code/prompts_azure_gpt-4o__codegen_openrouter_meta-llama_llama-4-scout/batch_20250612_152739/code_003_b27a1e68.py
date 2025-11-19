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
# heart_attack_risk.py

class HeartAttackRiskCalculator:
    """
    Calculates heart attack risk based on various factors.
    """

    def __init__(self, age, sex, smoker, diabetes, cholesterol, blood_pressure):
        """
        Initializes the calculator with patient data.

        Args:
            age (int): Patient's age in years.
            sex (str): Patient's sex ('male' or 'female').
            smoker (bool): Whether the patient is a smoker.
            diabetes (bool): Whether the patient has diabetes.
            cholesterol (float): Patient's cholesterol level in mmol/L.
            blood_pressure (float): Patient's blood pressure in mmHg.
        """
        self.age = age
        self.sex = sex.lower()
        self.smoker = smoker
        self.diabetes = diabetes
        self.cholesterol = cholesterol
        self.blood_pressure = blood_pressure

    def calculate_risk(self):
        """
        Calculates the heart attack risk score.

        Returns:
            float: Risk score between 0 and 1.
        """
        risk_score = 0.0

        # Age factor (based on Framingham Heart Study)
        if self.age >= 20 and self.age <= 39:
            risk_score += 0.05
        elif self.age >= 40 and self.age <= 49:
            risk_score += 0.10
        elif self.age >= 50 and self.age <= 59:
            risk_score += 0.20
        elif self.age >= 60 and self.age <= 69:
            risk_score += 0.30
        elif self.age >= 70:
            risk_score += 0.40

        # Sex factor
        if self.sex == 'male':
            risk_score += 0.05

        # Smoking factor
        if self.smoker:
            risk_score += 0.10

        # Diabetes factor
        if self.diabetes:
            risk_score += 0.15

        # Cholesterol factor (based on LDL levels)
        if self.cholesterol >= 4.14:
            risk_score += 0.20
        elif self.cholesterol >= 2.59 and self.cholesterol < 4.14:
            risk_score += 0.10

        # Blood pressure factor
        if self.blood_pressure >= 140:
            risk_score += 0.20
        elif self.blood_pressure >= 120 and self.blood_pressure < 140:
            risk_score += 0.10

        # Ensure risk score is within bounds
        risk_score = max(0.0, min(risk_score, 1.0))

        return risk_score

    def get_risk_category(self, risk_score):
        """
        Maps the risk score to a categorical risk level.

        Args:
            risk_score (float): Risk score between 0 and 1.

        Returns:
            str: Risk category ('low', 'moderate', or 'high').
        """
        if risk_score < 0.3:
            return 'low'
        elif risk_score < 0.7:
            return 'moderate'
        else:
            return 'high'


def main():
    try:
        age = int(input("Enter your age: "))
        sex = input("Enter your sex (male/female): ")
        smoker = input("Are you a smoker? (yes/no): ").lower() == 'yes'
        diabetes = input("Do you have diabetes? (yes/no): ").lower() == 'yes'
        cholesterol = float(input("Enter your cholesterol level (mmol/L): "))
        blood_pressure = float(input("Enter your blood pressure (mmHg): "))

        calculator = HeartAttackRiskCalculator(age, sex, smoker, diabetes, cholesterol, blood_pressure)
        risk_score = calculator.calculate_risk()
        risk_category = calculator.get_risk_category(risk_score)

        print(f"Your heart attack risk score is: {risk_score:.2f}")
        print(f"Your risk category is: {risk_category}")

    except ValueError as e:
        print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()
```
