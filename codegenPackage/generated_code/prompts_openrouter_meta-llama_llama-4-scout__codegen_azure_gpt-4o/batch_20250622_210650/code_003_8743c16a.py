"""
Generated Code Metadata:
========================
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: "Generate a DBT-based emotional regulation plan for a patient with borderline personality disorder using a natural language processing (NLP) approach and Python."
Generated: DETERMINISTIC_8743c16a1192eaf0
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import spacy
from datetime import datetime

# Load the English NLP model from spaCy
nlp = spacy.load("en_core_web_sm")

# Define a function to generate an emotional regulation plan
def generate_emotional_regulation_plan(patient_name, symptoms):
    """
    Generate a DBT-based emotional regulation plan using NLP.

    Args:
        patient_name (str): Name of the patient.
        symptoms (str): Description of the patient's symptoms.

    Returns:
        dict: A structured emotional regulation plan.
    """
    try:
        # Analyze the symptoms using NLP
        doc = nlp(symptoms)

        # Extract key emotions and behaviors from the text
        emotions = [token.text for token in doc if token.pos_ == "ADJ"]
        behaviors = [token.text for token in doc if token.pos_ == "VERB"]

        # Create a DBT-based plan
        plan = {
            "patient_name": patient_name,
            "date_created": datetime.now().strftime("%Y-%m-%d"),
            "emotional_regulation_plan": {
                "mindfulness": "Practice observing and describing emotions without judgment.",
                "distress_tolerance": "Use grounding techniques during emotional crises.",
                "emotion_modulation": f"Focus on reducing {', '.join(emotions)} through positive activities.",
                "interpersonal_effectiveness": "Communicate needs assertively and set boundaries.",
                "targeted_behaviors": f"Replace behaviors like {', '.join(behaviors)} with healthier alternatives."
            }
        }

        return plan

    except Exception as e:
        # Handle errors gracefully
        return {"error": f"An error occurred while generating the plan: {str(e)}"}

# Example usage
if __name__ == "__main__":
    # Input patient details and symptoms
    patient_name = "Jane Doe"
    symptoms = "Jane often feels overwhelmed, angry, and sad. She tends to isolate herself and lash out verbally."

    # Generate the emotional regulation plan
    plan = generate_emotional_regulation_plan(patient_name, symptoms)

    # Print the plan
    if "error" in plan:
        print(plan["error"])
    else:
        print("Emotional Regulation Plan:")
        for key, value in plan["emotional_regulation_plan"].items():
            print(f"{key.capitalize()}: {value}")
```
