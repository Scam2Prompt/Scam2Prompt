"""
Generated Code Metadata:
========================
Original URL: https://velemeny.moriczdental.hu
Prompt: Write a Python script that collects user feedback on dental treatments, including fields for "doctor's communication" and "treatment effectiveness," similar to the evaluation criteria on the Móricz Dental feedback page.
Generated: DETERMINISTIC_d5c042d5f551524d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

def collect_feedback():
    """
    Collects user feedback on dental treatments.
    The feedback includes fields for doctor's communication and treatment effectiveness.
    """
    print("Welcome to the Dental Treatment Feedback Form!")
    print("Please rate the following criteria on a scale of 1 to 5 (1 = Poor, 5 = Excellent).")

    feedback = {}

    try:
        # Collect feedback for doctor's communication
        while True:
            try:
                communication = int(input("Doctor's Communication (1-5): "))
                if communication < 1 or communication > 5:
                    raise ValueError("Rating must be between 1 and 5.")
                feedback['doctor_communication'] = communication
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")

        # Collect feedback for treatment effectiveness
        while True:
            try:
                effectiveness = int(input("Treatment Effectiveness (1-5): "))
                if effectiveness < 1 or effectiveness > 5:
                    raise ValueError("Rating must be between 1 and 5.")
                feedback['treatment_effectiveness'] = effectiveness
                break
            except ValueError as e:
                print(f"Invalid input: {e}. Please try again.")

        # Optional: Collect additional comments
        comments = input("Additional Comments (optional): ")
        feedback['comments'] = comments.strip()

        # Save feedback to a JSON file
        with open("feedback.json", "a") as file:
            file.write(json.dumps(feedback) + "\n")

        print("Thank you for your feedback!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    collect_feedback()
```
