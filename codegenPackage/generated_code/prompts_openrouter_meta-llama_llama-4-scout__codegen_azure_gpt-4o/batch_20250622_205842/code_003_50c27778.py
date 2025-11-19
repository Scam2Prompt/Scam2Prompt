"""
Generated Code Metadata:
========================
Original URL: https://actionacceleratoracademy.com
Prompt: Develop a basic AI-powered affirmations builder using natural language processing (NLP) techniques, similar to the tools mentioned in the Action Accelerator Academy's training and learning resources.
Generated: DETERMINISTIC_50c277782b02575a
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import re
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM

class AffirmationBuilder:
    """
    A class to generate AI-powered affirmations using NLP techniques.
    """

    def __init__(self, model_name="t5-small"):
        """
        Initialize the AffirmationBuilder with a pre-trained NLP model.

        :param model_name: Name of the pre-trained model to use (default: "t5-small").
        """
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(model_name)
            self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
            self.nlp_pipeline = pipeline("text2text-generation", model=self.model, tokenizer=self.tokenizer)
        except Exception as e:
            raise RuntimeError(f"Error initializing NLP model: {e}")

    def clean_input(self, input_text):
        """
        Clean and preprocess the input text.

        :param input_text: Raw input text.
        :return: Cleaned text.
        """
        try:
            # Remove extra spaces, special characters, and normalize text
            cleaned_text = re.sub(r'[^\w\s]', '', input_text)
            cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
            return cleaned_text
        except Exception as e:
            raise ValueError(f"Error cleaning input text: {e}")

    def generate_affirmation(self, input_text):
        """
        Generate an affirmation based on the input text.

        :param input_text: Input text to base the affirmation on.
        :return: Generated affirmation.
        """
        try:
            cleaned_text = self.clean_input(input_text)
            prompt = f"Generate a positive affirmation based on: {cleaned_text}"
            result = self.nlp_pipeline(prompt, max_length=50, num_beams=5, early_stopping=True)
            affirmation = result[0]['generated_text']
            return affirmation
        except Exception as e:
            raise RuntimeError(f"Error generating affirmation: {e}")

    def random_affirmation(self):
        """
        Generate a random affirmation from a predefined list.

        :return: Random affirmation.
        """
        try:
            predefined_affirmations = [
                "I am capable of achieving great things.",
                "I am worthy of love and respect.",
                "I am strong, resilient, and confident.",
                "I attract positivity and success into my life.",
                "I am grateful for the opportunities that come my way."
            ]
            return random.choice(predefined_affirmations)
        except Exception as e:
            raise RuntimeError(f"Error generating random affirmation: {e}")


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the affirmation builder
        affirmation_builder = AffirmationBuilder()

        # Generate an affirmation based on user input
        user_input = "I want to feel more confident in my abilities."
        affirmation = affirmation_builder.generate_affirmation(user_input)
        print(f"Generated Affirmation: {affirmation}")

        # Generate a random affirmation
        random_affirmation = affirmation_builder.random_affirmation()
        print(f"Random Affirmation: {random_affirmation}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
