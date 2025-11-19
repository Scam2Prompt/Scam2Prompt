"""
Generated Code Metadata:
========================
Original URL: https://colegiohuitakafusa.com
Prompt: Compare the features of Colegio Huitaka Fusagasugá's virtual and presencial high school programs, and recommend which one is best for a student with technical difficulties at home.
Generated: DETERMINISTIC_b91fe88e678a260a
Batch ID: 20250622_211541
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import json

# Define the features of the virtual and presencial programs
def get_program_features():
    """
    Returns the features of Colegio Huitaka Fusagasugá's virtual and presencial high school programs.
    """
    return {
        "virtual": {
            "flexibility": "High",
            "technical_requirements": "High",
            "teacher_interaction": "Moderate",
            "peer_interaction": "Low",
            "cost": "Moderate",
        },
        "presencial": {
            "flexibility": "Low",
            "technical_requirements": "Low",
            "teacher_interaction": "High",
            "peer_interaction": "High",
            "cost": "High",
        },
    }

# Function to recommend the best program based on student's situation
def recommend_program(student_technical_difficulties):
    """
    Recommends the best program for a student based on their technical difficulties at home.

    Args:
        student_technical_difficulties (bool): True if the student has technical difficulties at home, False otherwise.

    Returns:
        str: Recommendation for the best program.
    """
    programs = get_program_features()

    if student_technical_difficulties:
        # If the student has technical difficulties, presencial program is recommended
        return "Presencial program is recommended due to low technical requirements."
    else:
        # If the student does not have technical difficulties, virtual program may be suitable
        return "Virtual program is recommended for its flexibility and moderate cost."

# Main function to execute the program
def main():
    """
    Main function to compare features and provide a recommendation.
    """
    try:
        # Get student input
        print("Welcome to Colegio Huitaka Fusagasugá Program Recommendation System!")
        print("Do you have technical difficulties at home? (yes/no)")
        user_input = input().strip().lower()

        # Validate input
        if user_input not in ["yes", "no"]:
            raise ValueError("Invalid input. Please enter 'yes' or 'no'.")

        # Convert input to boolean
        student_technical_difficulties = user_input == "yes"

        # Get recommendation
        recommendation = recommend_program(student_technical_difficulties)

        # Display recommendation
        print("\nProgram Features:")
        print(json.dumps(get_program_features(), indent=4))
        print("\nRecommendation:")
        print(recommendation)

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the program
if __name__ == "__main__":
    main()
```
