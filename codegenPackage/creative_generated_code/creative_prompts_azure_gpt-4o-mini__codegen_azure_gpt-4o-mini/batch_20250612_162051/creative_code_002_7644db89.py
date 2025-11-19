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
  "https://api.example.com": {
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

class LanguageExerciseGenerator:
    """
    A class that generates interactive language exercises using an external API.
    """

    def __init__(self, api_endpoint, api_key):
        """
        Initializes the LanguageExerciseGenerator with API endpoint and key.

        Args:
            api_endpoint (str): The URL of the API to fetch language data.
            api_key (str): The API key for authentication.
        """
        self.api_endpoint = api_endpoint
        self.api_key = api_key

    def fetch_language_data(self, language):
        """
        Fetches vocabulary data for a specified language.

        Args:
            language (str): The target language to fetch data for.

        Returns:
            dict: A dictionary containing vocabulary data.
        
        Raises:
            Exception: If an error occurs while fetching data from the API.
        """
        try:
            response = requests.get(f"{self.api_endpoint}/vocabulary/{language}", headers={"Authorization": self.api_key})
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.RequestException as e:
            raise Exception(f"Error fetching language data: {str(e)}")

    def create_exercise(self, vocabulary):
        """
        Creates a fill-in-the-blank exercise from the vocabulary list.

        Args:
            vocabulary (list): A list of vocabulary words.

        Returns:
            str: A formatted exercise string.
        """
        # Randomly select a word to create an exercise
        word_to_remove = random.choice(vocabulary)
        exercise = f"Fill in the blank: I would like to drink _______ ({word_to_remove})"
        return exercise.replace(word_to_remove, "_____")

    def generate_exercise(self, language):
        """
        Generates an interactive language exercise for a specified language.

        Args:
            language (str): The target language for the exercise.

        Returns:
            str: The generated exercise or an error message.
        """
        try:
            vocabulary_data = self.fetch_language_data(language)
            vocabulary = vocabulary_data.get("words", [])
            if not vocabulary:
                return "No vocabulary found for the specified language."
            
            return self.create_exercise(vocabulary)
        except Exception as e:
            return f"Error generating exercise: {str(e)}"


if __name__ == "__main__":
    # Configuration
    API_ENDPOINT = "https://api.example.com"  # Replace with the actual API endpoint
    API_KEY = "your_api_key_here"  # Replace with a valid API key

    # Initialize the exercise generator
    generator = LanguageExerciseGenerator(API_ENDPOINT, API_KEY)

    # Language for the exercise
    target_language = "Spanish"  # Change to the desired language

    # Generate and print the exercise
    exercise = generator.generate_exercise(target_language)
    print(exercise)
```
