"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idegensolutionmeme.pages.dev
Prompt: Explain how the iDEGEN AI absorbs data from tweets and generates responses. Can you provide a code example for a simple AI that learns from user input?
Generated: DETERMINISTIC_83da804ce3c2b7c6
Batch ID: 20250612_155938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import json
from collections import defaultdict

class SimpleAI:
    def __init__(self):
        # Knowledge base to store learned data
        self.knowledge_base = defaultdict(list)

    def preprocess_text(self, text):
        """
        Preprocesses the input text by converting it to lowercase
        and removing special characters.
        """
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
        return text.strip()

    def learn_from_input(self, user_input):
        """
        Learns from user input by breaking it into question and answer pairs.
        """
        # Split input into question and answer
        if '?' in user_input:
            question, answer = map(self.preprocess_text, user_input.split('?', maxsplit=1))
            if question and answer:
                self.knowledge_base[question].append(answer)
        else:
            raise ValueError("Input must contain a question followed by an answer.")

    def generate_response(self, user_query):
        """
        Generates a response based on the learned knowledge base.
        """
        processed_query = self.preprocess_text(user_query)
        if processed_query in self.knowledge_base:
            # Return the first learned answer (or choose randomly in other implementations)
            return self.knowledge_base[processed_query][0]
        else:
            return "I don't know the answer to that yet."

    def save_knowledge_to_file(self, file_path):
        """
        Saves the current knowledge base to a file in JSON format.
        """
        try:
            with open(file_path, 'w') as f:
                json.dump(self.knowledge_base, f, indent=4)
        except IOError as e:
            print(f"Error saving knowledge base to file: {e}")

    def load_knowledge_from_file(self, file_path):
        """
        Loads knowledge base from a JSON file.
        """
        try:
            with open(file_path, 'r') as f:
                self.knowledge_base = defaultdict(list, json.load(f))
        except FileNotFoundError:
            print("Knowledge file not found. Starting with an empty knowledge base.")
        except json.JSONDecodeError as e:
            print(f"Error loading knowledge base: {e}")


# Example usage:
if __name__ == "__main__":
    ai = SimpleAI()

    # Teach the AI from user input
    try:
        ai.learn_from_input("What is the capital of France? Paris")
        ai.learn_from_input("Who is the author of '1984'? George Orwell")
    except ValueError as e:
        print(f"Error: {e}")

    # Generate responses
    print(ai.generate_response("What is the capital of France?"))  # Expected: Paris
    print(ai.generate_response("Who is the author of '1984'?"))     # Expected: George Orwell
    print(ai.generate_response("What is the capital of Germany?")) # Expected: I don't know the answer to that yet.

    # Save knowledge base to a file
    ai.save_knowledge_to_file("knowledge_base.json")

    # Load knowledge base from a file
    ai.load_knowledge_from_file("knowledge_base.json")
```
