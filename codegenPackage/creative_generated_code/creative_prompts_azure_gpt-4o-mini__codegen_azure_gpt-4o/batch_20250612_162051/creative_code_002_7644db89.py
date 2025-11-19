"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magicbear.com.br
Prompt: Write a Python script that utilizes an API to create interactive language exercises for students in a bilingual program.
Generated: DETERMINISTIC_7644db89ad6bfa93
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.dictionaryapi.dev/api/v2/entries/en/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import json
import random
import sys

# Constants
API_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"  # Free dictionary API for English words
LANGUAGE_PAIR = ("en", "es")  # English (source) to Spanish (target)

def fetch_translation(word):
    """
    Fetch translation of a word from the API.
    Args:
        word (str): The English word to translate.
    Returns:
        dict: A dictionary containing the word, meaning, and examples, or None in case of failure.
    """
    try:
        response = requests.get(f"{API_URL}{word}")
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        data = response.json()

        # Extract meaning and example sentences
        meanings = data[0].get('meanings', [])
        definitions = []
        examples = []

        for meaning in meanings:
            for definition in meaning.get('definitions', []):
                definitions.append(definition.get('definition', ''))
                example = definition.get('example', '')
                if example:
                    examples.append(example)

        return {
            "word": word,
            "definitions": definitions,
            "examples": examples
        }
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from the API: {e}")
        return None
    except (IndexError, KeyError) as e:
        print(f"Error parsing API response: {e}")
        return None

def create_exercise(word_data):
    """
    Create a language exercise based on the fetched word data.
    Args:
        word_data (dict): The word data containing definitions and examples.
    Returns:
        dict: An interactive exercise dictionary.
    """
    if not word_data:
        return None

    # Randomly select a definition and example (if available)
    definition = random.choice(word_data['definitions']) if word_data['definitions'] else "No definition available."
    example = random.choice(word_data['examples']) if word_data['examples'] else "No example available."

    # Create a basic exercise
    exercise = {
        "word": word_data['word'],
        "definition": definition,
        "example": example,
        "question": f"What is the meaning of '{word_data['word']}'? Can you use it in a sentence?",
    }
    return exercise

def main():
    """
    Main function to run the script.
    Prompts the user for an English word and creates an interactive exercise.
    """
    print("Welcome to the Interactive Language Exercise Generator!")
    word = input(f"Enter an English word to generate an exercise ({LANGUAGE_PAIR[0]} to {LANGUAGE_PAIR[1]}): ").strip()

    if not word:
        print("No word entered. Exiting.")
        sys.exit(1)

    word_data = fetch_translation(word)

    if not word_data:
        print("Failed to generate exercise. Please try again.")
        sys.exit(1)

    exercise = create_exercise(word_data)

    if exercise:
        print("\n--- Interactive Language Exercise ---")
        print(f"Word: {exercise['word']}")
        print(f"Definition: {exercise['definition']}")
        print(f"Example Usage: {exercise['example']}")
        print(f"Question: {exercise['question']}")
    else:
        print("Failed to create an exercise. Please try again.")

if __name__ == "__main__":
    main()
```
