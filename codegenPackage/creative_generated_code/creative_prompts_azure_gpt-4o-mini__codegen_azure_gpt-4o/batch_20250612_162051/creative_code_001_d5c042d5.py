"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://velemeny.moriczdental.hu
Prompt: Write a Python script that collects user feedback on dental treatments, including fields for "doctor's communication" and "treatment effectiveness," similar to the evaluation criteria on the Móricz Dental feedback page.
Generated: DETERMINISTIC_d5c042d5f551524d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

def ask_feedback():
    """
    Prompt the user for feedback on dental treatments. Collects data for:
    - Doctor's communication
    - Treatment effectiveness

    Returns:
        dict: A dictionary containing the user's feedback.
    """
    print("Welcome to the Dental Treatment Feedback Form!")
    print("Please rate the following on a scale from 1 (Poor) to 5 (Excellent):")

    feedback = {}

    # Collect feedback for doctor's communication
    while True:
        try:
            communication_rating = int(input("Doctor's communication (1-5): "))
            if communication_rating < 1 or communication_rating > 5:
                raise ValueError("Rating must be between 1 and 5.")
            feedback['doctor_communication'] = communication_rating
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

    # Collect feedback for treatment effectiveness
    while True:
        try:
            effectiveness_rating = int(input("Treatment effectiveness (1-5): "))
            if effectiveness_rating < 1 or effectiveness_rating > 5:
                raise ValueError("Rating must be between 1 and 5.")
            feedback['treatment_effectiveness'] = effectiveness_rating
            break
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")

    # Optional: Collect additional comments
    additional_comments = input("Any additional comments? (Press Enter to skip): ")
    feedback['additional_comments'] = additional_comments.strip()

    return feedback


def save_feedback(feedback, filename="feedback.json"):
    """
    Save the user feedback to a JSON file.

    Args:
        feedback (dict): The feedback data to save.
        filename (str): The name of the file where feedback will be saved.
    """
    try:
        # Load existing feedback if the file exists
        try:
            with open(filename, 'r') as file:
                existing_feedback = json.load(file)
        except FileNotFoundError:
            existing_feedback = []

        # Add the new feedback
        existing_feedback.append(feedback)

        # Write all feedback back to the file
        with open(filename, 'w') as file:
            json.dump(existing_feedback, file, indent=4)
        
        print("Thank you for your feedback! It has been saved successfully.")
    except Exception as e:
        print(f"An error occurred while saving feedback: {e}")


def main():
    """
    Main function to handle the feedback collection and saving process.
    """
    feedback = ask_feedback()
    save_feedback(feedback)


if __name__ == "__main__":
    main()
```
