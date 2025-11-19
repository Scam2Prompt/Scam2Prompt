"""
Generated Code Metadata:
========================
Original URL: https://learnenglishsimply.com
Prompt: Create a sentence making exercise using the "Dare to Sentence Making" section from Learn English Simply, and provide a Python function to generate random sentences.
Generated: DETERMINISTIC_4c112e96ad3d8a49
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class SentenceMaker:
    def __init__(self):
        # Initialize the lists of subjects, verbs, and objects
        self.subjects = [
            "The cat", "A dog", "My friend", "The teacher", 
            "The car", "A child", "The sun", "The computer"
        ]
        self.verbs = [
            "jumps", "runs", "sings", "drives", 
            "teaches", "plays", "writes", "reads"
        ]
        self.objects = [
            "a ball", "the book", "the road", "a song", 
            "the lesson", "a game", "the story", "the code"
        ]

    def generate_sentence(self):
        """
        Generate a random sentence using the subject, verb, and object lists.
        
        Returns:
            str: A randomly generated sentence.
        """
        try:
            # Randomly select a subject, verb, and object
            subject = random.choice(self.subjects)
            verb = random.choice(self.verbs)
            obj = random.choice(self.objects)
            
            # Construct the sentence
            sentence = f"{subject} {verb} {obj}."
            return sentence
        except Exception as e:
            # Handle any unexpected errors
            return f"An error occurred while generating the sentence: {e}"

def main():
    # Create an instance of the SentenceMaker
    sentence_maker = SentenceMaker()
    
    # Generate and print 5 random sentences
    for _ in range(5):
        print(sentence_maker.generate_sentence())

if __name__ == "__main__":
    main()
```
