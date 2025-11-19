"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://delsolmontessorihn.com
Prompt: Create a sample lesson plan that incorporates STEAM principles for a bilingual school setting, reflecting the unique educational approach of Del Sol Montessori.
Generated: DETERMINISTIC_14a88f96062f67f4
Batch ID: 20250612_155306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script generates a sample lesson plan for a bilingual school setting (e.g., English and Spanish),
incorporating STEAM (Science, Technology, Engineering, Arts, Mathematics) principles. The lesson plan
reflects the educational approach of Del Sol Montessori, emphasizing inquiry-based learning and cross-disciplinary integration.
"""

import json

# Error class for custom exceptions
class LessonPlanError(Exception):
    pass

def generate_lesson_plan(subject, language="English"):
    """
    Generates a sample lesson plan based on the subject and language specified.

    Args:
        subject (str): The subject for the lesson plan (e.g., "Science", "Art").
        language (str): The language for the lesson plan ("English" or "Spanish").

    Returns:
        dict: A dictionary containing the lesson plan details.

    Raises:
        LessonPlanError: If the subject or language is invalid.
    """

    # Validate input
    valid_subjects = ["Science", "Technology", "Engineering", "Arts", "Mathematics"]
    valid_languages = ["English", "Spanish"]

    if subject not in valid_subjects:
        raise LessonPlanError(f"Invalid subject: {subject}. Must be one of {valid_subjects}.")
    if language not in valid_languages:
        raise LessonPlanError(f"Invalid language: {language}. Must be either 'English' or 'Spanish'.")

    # Core lesson plan structure
    lesson_plan = {
        "subject": subject,
        "language": language,
        "title": f"STEAM Activity: Exploring {subject}" if language == "English" else f"Actividad STEAM: Explorando {subject}",
        "objectives": {
            "English": f"Students will develop core skills in {subject} and apply them in real-world problem-solving.",
            "Spanish": f"Los estudiantes desarrollarán habilidades fundamentales en {subject} y las aplicarán para resolver problemas del mundo real."
        },
        "materials": {
            "English": ["Notebook", "Pencils", "Markers", f"{subject} Kit"],
            "Spanish": ["Cuaderno", "Lápices", "Marcadores", f"Kit de {subject}"]
        },
        "activity": {
            "English": f"Students will perform hands-on activities to experiment and explore concepts in {subject}.",
            "Spanish": f"Los estudiantes realizarán actividades prácticas para experimentar y explorar conceptos en {subject}."
        },
        "assessment": {
            "English": "Students will demonstrate understanding by presenting their findings and completing a project.",
            "Spanish": "Los estudiantes demostrarán su comprensión presentando sus hallazgos y completando un proyecto."
        },
        "integration": {
            "English": "This lesson integrates inquiry-based learning and bilingual education.",
            "Spanish": "Esta lección integra el aprendizaje basado en la indagación y la educación bilingüe."
        }
    }

    # Apply language-specific changes
    for key in lesson_plan:
        if isinstance(lesson_plan[key], dict):
            lesson_plan[key] = lesson_plan[key][language]

    return lesson_plan

def save_lesson_plan_to_file(lesson_plan, filename):
    """
    Saves the lesson plan to a JSON file.

    Args:
        lesson_plan (dict): The lesson plan dictionary.
        filename (str): The filename to save the lesson plan as.

    Raises:
        IOError: If there is a file I/O error.
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(lesson_plan, file, ensure_ascii=False, indent=4)
    except IOError as e:
        raise IOError(f"Failed to save lesson plan to file: {e}")

def main():
    """
    Main function to generate and save a sample STEAM lesson plan.
    """
    try:
        # Generate a sample lesson plan for Science in Spanish
        subject = "Science"
        language = "Spanish"
        lesson_plan = generate_lesson_plan(subject, language)

        # Save the lesson plan to a file
        filename = f"{subject}_Lesson_Plan_{language}.json"
        save_lesson_plan_to_file(lesson_plan, filename)

        print(f"Lesson plan successfully saved to {filename}")
    except LessonPlanError as e:
        print(f"Error: {e}")
    except IOError as e:
        print(f"File error: {e}")

if __name__ == "__main__":
    main()
```
