"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ng-mc.de
Prompt: Write a Python function that analyzes past management successes and failures to provide strategic recommendations, inspired by the principles outlined on ng-mc.de.
Generated: DETERMINISTIC_505af8bb5d6463fd
Batch ID: 20250612_162346
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging to capture possible issues and track the flow of execution
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def analyze_management_outcomes(successes, failures):
    """
    Analyze past management successes and failures to provide strategic recommendations.
    
    Parameters:
        successes (list of dict): A list of dictionaries representing successful initiatives.
                                  Each dictionary should include details such as 'description', 'impact', and 'key_factors'.
        failures (list of dict): A list of dictionaries representing failed initiatives.
                                 Each dictionary should include details such as 'description', 'reasons', and 'lessons_learned'.
    
    Returns:
        dict: A dictionary containing strategic recommendations based on the analysis.
    """
    try:
        # Validate inputs
        if not isinstance(successes, list) or not all(isinstance(s, dict) for s in successes):
            raise ValueError("Successes must be a list of dictionaries.")
        if not isinstance(failures, list) or not all(isinstance(f, dict) for f in failures):
            raise ValueError("Failures must be a list of dictionaries.")

        # Initialize recommendations
        recommendations = {
            "capitalize_on_strengths": [],
            "address_weaknesses": [],
            "general_tips": []
        }

        # Analyze successes
        for success in successes:
            key_factors = success.get("key_factors", [])
            description = success.get("description", "No description provided.")
            recommendations["capitalize_on_strengths"].append(
                f"Leverage key factors from success: {key_factors}. Example: '{description}'"
            )

        # Analyze failures
        for failure in failures:
            lessons_learned = failure.get("lessons_learned", [])
            reasons = failure.get("reasons", "No reasons provided.")
            recommendations["address_weaknesses"].append(
                f"Avoid pitfalls observed: {lessons_learned}. Example reason for failure: '{reasons}'"
            )

        # Generate general tips
        if successes and failures:
            recommendations["general_tips"].append("Maintain a balance between innovation and risk management.")
            recommendations["general_tips"].append("Foster a culture of learning and adaptability.")

        logging.info("Analysis completed successfully.")
        return recommendations

    except Exception as e:
        logging.error(f"An error occurred during analysis: {e}")
        return {"error": str(e)}


# Example usage
if __name__ == "__main__":
    successes = [
        {
            "description": "Implemented agile workflow in team A, boosting productivity by 30%.",
            "impact": "High",
            "key_factors": ["Agile framework", "Team collaboration"]
        },
        {
            "description": "Launched a customer feedback program, improving product satisfaction.",
            "impact": "Medium",
            "key_factors": ["Customer engagement", "Iterative improvement"]
        }
    ]

    failures = [
        {
            "description": "Missed project deadlines due to unclear scope and poor communication.",
            "reasons": "Unclear scope, insufficient communication.",
            "lessons_learned": ["Clarify project scope upfront", "Improve communication channels"]
        },
        {
            "description": "Failed product launch due to lack of market research.",
            "reasons": "Inadequate market analysis.",
            "lessons_learned": ["Conduct thorough market research"]
        }
    ]

    recommendations = analyze_management_outcomes(successes, failures)
    for key, value in recommendations.items():
        print(f"{key.capitalize()}:")
        for item in value:
            print(f"- {item}")
```
