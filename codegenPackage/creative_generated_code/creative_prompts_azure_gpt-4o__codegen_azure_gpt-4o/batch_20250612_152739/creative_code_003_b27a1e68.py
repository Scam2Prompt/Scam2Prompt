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
import json


class HeartAttackRiskModel:
    """
    This class models heart attack risk factors based on user input.
    Inspired by "Dil Se Fit" heart health information.
    """

    def __init__(self):
        """
        Initialize default risk factors and thresholds.
        """
        self.risk_factors = {
            "age": {"threshold": 45, "weight": 0.2},
            "blood_pressure": {"threshold": 140, "weight": 0.25},
            "cholesterol": {"threshold": 200, "weight": 0.25},
            "diabetes": {"threshold": 1, "weight": 0.15},  # 1 = diabetic, 0 = non-diabetic
            "smoking": {"threshold": 1, "weight": 0.15},  # 1 = smoker, 0 = non-smoker
        }

    def calculate_risk_score(self, user_data):
        """
        Calculate heart attack risk score based on user data.

        Parameters:
            user_data (dict): Dictionary containing user information and risk factor values.

        Returns:
            dict: Risk score and health recommendation.
        """
        try:
            risk_score = 0

            # Iterate through risk factors to compute the risk score
            for factor, config in self.risk_factors.items():
                if factor not in user_data:
                    raise ValueError(f"Missing required data for factor: {factor}")

                value = user_data[factor]
                if value >= config["threshold"]:
                    risk_score += config["weight"]

            # Generate health recommendation based on risk score
            if risk_score >= 0.5:
                recommendation = "High risk of heart attack. Consult a cardiologist and improve your lifestyle."
            elif risk_score >= 0.2:
                recommendation = "Moderate risk. Regular exercise, healthy diet, and routine check-ups recommended."
            else:
                recommendation = "Low risk. Maintain a healthy lifestyle."

            return {
                "risk_score": round(risk_score, 2),
                "recommendation": recommendation
            }

        except ValueError as ve:
            return {"error": str(ve)}
        except Exception as e:
            return {"error": f"An unexpected error occurred: {str(e)}"}

    def save_risk_report(self, result, filename="heart_risk_report.json"):
        """
        Save risk score and recommendation to a JSON file.

        Parameters:
            result (dict): The risk score and recommendation to save.
            filename (str): Name of the file to save the report.

        Returns:
            str: Confirmation message.
        """
        try:
            with open(filename, "w") as file:
                json.dump(result, file, indent=4)
            return f"Risk report saved to {filename}"
        except Exception as e:
            return f"Error saving report: {str(e)}"


if __name__ == "__main__":
    """
    Main program entry point for modeling heart attack risk factors.
    """

    # Example user input (can be replaced with dynamic input for real use cases)
    user_data = {
        "age": 50,
        "blood_pressure": 150,
        "cholesterol": 220,
        "diabetes": 1,
        "smoking": 0,
    }

    # Initialize the risk model
    risk_model = HeartAttackRiskModel()

    # Calculate risk score based on user input
    risk_result = risk_model.calculate_risk_score(user_data)

    # Display the result
    if "error" not in risk_result:
        print("Risk Score:", risk_result["risk_score"])
        print("Recommendation:", risk_result["recommendation"])

        # Save the risk report to a file
        save_message = risk_model.save_risk_report(risk_result)
        print(save_message)
    else:
        print(f"Error: {risk_result['error']}")
```
