"""
Generated Code Metadata:
========================
Original URL: https://cupomestudante.com.br
Prompt: "Create a sample lesson plan for teaching Biologia for the ENEM exam using the CUPOMESTUDANTE approach."
Generated: DETERMINISTIC_7f1b5bce23ed743b
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Lesson Plan Generator for Teaching Biology for the ENEM Exam
Using the CUPOMESTUDANTE Approach

This script generates a sample lesson plan based on the CUPOMESTUDANTE methodology.
CUPOMESTUDANTE is a mnemonic-based approach to help students remember key concepts.
"""

import json

# Define a custom exception for invalid input
class LessonPlanError(Exception):
    pass

def generate_lesson_plan(topic, approach):
    """
    Generates a lesson plan for a given topic using a specified approach.

    Args:
        topic (str): The subject/topic of the lesson (e.g., "Biologia").
        approach (str): The teaching methodology (e.g., "CUPOMESTUDANTE").

    Returns:
        dict: A structured lesson plan.
    """
    if not topic or not approach:
        raise LessonPlanError("Both topic and approach must be provided.")

    if approach.lower() != "cupomestudante":
        raise LessonPlanError("Unsupported approach. Only 'CUPOMESTUDANTE' is supported.")

    # Lesson plan structure
    lesson_plan = {
        "title": f"Biologia Lesson Plan for ENEM - {approach.upper()} Approach",
        "objectives": [
            "Understand key biological concepts relevant to the ENEM exam.",
            "Apply the CUPOMESTUDANTE mnemonic to retain information effectively.",
            "Develop critical thinking skills for solving biology-related questions."
        ],
        "methodology": {
            "mnemonic": "CUPOMESTUDANTE",
            "steps": [
                "C - Contextualize the topic within real-world applications.",
                "U - Understand the fundamental concepts and definitions.",
                "P - Practice with past ENEM questions and exercises.",
                "O - Organize the information into diagrams, charts, or mind maps.",
                "M - Memorize key terms and processes using repetition techniques.",
                "E - Evaluate understanding through quizzes and self-assessment.",
                "S - Summarize the topic in your own words.",
                "T - Test your knowledge with timed mock exams.",
                "U - Utilize group discussions to clarify doubts.",
                "D - Develop connections between biology and other subjects.",
                "A - Apply knowledge to solve interdisciplinary problems.",
                "N - Note down important points for quick revision.",
                "T - Track progress and adjust study strategies as needed.",
                "E - Engage in active recall to reinforce learning."
            ]
        },
        "materials": [
            "ENEM biology syllabus",
            "Textbooks and reference materials",
            "Practice exams and past ENEM questions",
            "Visual aids (diagrams, charts, videos)",
            "Notebook for summarizing and note-taking"
        ],
        "schedule": {
            "day_1": "Introduction to the CUPOMESTUDANTE approach and overview of ENEM biology topics.",
            "day_2": "Focus on cellular biology and biochemistry.",
            "day_3": "Study genetics and evolution.",
            "day_4": "Explore ecology and environmental biology.",
            "day_5": "Review and practice with mock exams."
        },
        "evaluation": [
            "Daily quizzes to assess understanding.",
            "Group discussions to clarify doubts.",
            "Mock exams to simulate ENEM conditions."
        ]
    }

    return lesson_plan

def save_lesson_plan_to_file(lesson_plan, filename="lesson_plan.json"):
    """
    Saves the lesson plan to a JSON file.

    Args:
        lesson_plan (dict): The lesson plan to save.
        filename (str): The name of the file to save the lesson plan to.
    """
    try:
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(lesson_plan, file, indent=4, ensure_ascii=False)
        print(f"Lesson plan saved successfully to {filename}")
    except Exception as e:
        print(f"Error saving lesson plan: {e}")

def main():
    """
    Main function to generate and save the lesson plan.
    """
    try:
        # Generate the lesson plan
        topic = "Biologia"
        approach = "CUPOMESTUDANTE"
        lesson_plan = generate_lesson_plan(topic, approach)

        # Save the lesson plan to a file
        save_lesson_plan_to_file(lesson_plan)

    except LessonPlanError as e:
        print(f"Lesson Plan Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point of the script
if __name__ == "__main__":
    main()
```
