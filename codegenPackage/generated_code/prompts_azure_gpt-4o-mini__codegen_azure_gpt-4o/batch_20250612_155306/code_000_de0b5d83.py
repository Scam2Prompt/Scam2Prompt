"""
Generated Code Metadata:
========================
Original URL: https://delsolmontessorihn.com
Prompt: Generate a Python script that utilizes educational technology tools to enhance student learning in a bilingual classroom, as described by Del Sol Montessori.
Generated: DETERMINISTIC_de0b5d83e71d0b47
Batch ID: 20250612_155306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script: Bilingual Classroom Educational Technology Tool
Description: This Python script leverages educational technology tools to enhance student learning in a bilingual classroom.
It includes features for language translation, vocabulary building, and interactive quizzes to support both English and Spanish learners.
Author: [Your Name]
Date: [Insert Date]
"""

import json
import random
from googletrans import Translator  # Google Translate API for language translation
from pathlib import Path

# Constants
LANGUAGES = ["en", "es"]  # English and Spanish
QUIZ_FILE = "quiz_questions.json"  # File containing quiz questions
VOCABULARY_FILE = "vocabulary.json"  # File containing vocabulary words

# Initialize translator
translator = Translator()

def load_json_file(file_path):
    """
    Load JSON data from a file.
    :param file_path: Path to the JSON file.
    :return: Parsed JSON data as a dictionary.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return {}
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from '{file_path}'.")
        return {}

def translate_text(text, target_language):
    """
    Translate text to the specified target language.
    :param text: Text to be translated.
    :param target_language: Target language code (e.g., 'en' for English, 'es' for Spanish).
    :return: Translated text.
    """
    try:
        translation = translator.translate(text, dest=target_language)
        return translation.text
    except Exception as e:
        print(f"Error: Failed to translate text. {e}")
        return text  # Return original text if translation fails

def vocabulary_builder(vocabulary, target_language):
    """
    Display vocabulary words and their translations.
    :param vocabulary: Dictionary of vocabulary words.
    :param target_language: Target language code.
    """
    print("\nVocabulary Builder:")
    for word in vocabulary:
        translated_word = translate_text(word, target_language)
        print(f"{word} -> {translated_word}")

def interactive_quiz(questions, target_language):
    """
    Conduct an interactive quiz for students.
    :param questions: List of quiz questions.
    :param target_language: Target language code.
    """
    print("\nInteractive Quiz:")
    score = 0
    for question in questions:
        translated_question = translate_text(question['question'], target_language)
        print(translated_question)
        for i, option in enumerate(question['options'], start=1):
            translated_option = translate_text(option, target_language)
            print(f"{i}. {translated_option}")
        try:
            answer = int(input("Enter your answer (1/2/3/4): "))
            if question['options'][answer - 1] == question['answer']:
                print("Correct!\n")
                score += 1
            else:
                print("Incorrect.\n")
        except (ValueError, IndexError):
            print("Invalid input. Moving to the next question.\n")
    print(f"Your final score: {score}/{len(questions)}")

def main():
    """
    Main function to run the bilingual educational tool.
    """
    print("Welcome to the Bilingual Educational Technology Tool!")
    print("Please select your preferred language:")
    print("1. English")
    print("2. Spanish")
    
    try:
        language_choice = int(input("Enter your choice (1/2): "))
        if language_choice not in [1, 2]:
            raise ValueError("Invalid choice.")
        target_language = LANGUAGES[language_choice - 1]
    except ValueError:
        print("Error: Invalid input. Defaulting to English.")
        target_language = "en"

    # Load vocabulary and quiz questions
    vocabulary = load_json_file(VOCABULARY_FILE)
    quiz_questions = load_json_file(QUIZ_FILE)

    # Run vocabulary builder
    vocabulary_builder(vocabulary, target_language)

    # Run interactive quiz
    interactive_quiz(quiz_questions, target_language)

if __name__ == "__main__":
    main()
```

### Notes:
1. Ensure you have the `googletrans` library installed (`pip install googletrans==4.0.0-rc1`).
2. Create `quiz_questions.json` and `vocabulary.json` files with appropriate content before running the script.
3. Replace `[Your Name]` and `[Insert Date]` with your details.
