"""
Generated Code Metadata:
========================
Original URL: https://goldenapp.online
Prompt: "Design a basic AI system that can be used for identifying and providing results in an educational context."
Generated: DETERMINISTIC_0369c5063feea305
Batch ID: 20250622_211614
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json

class EducationalAI:
    """
    A basic AI system for identifying and providing results in an educational context.
    """

    def __init__(self, knowledge_base_file):
        """
        Initializes the AI system with a knowledge base.

        :param knowledge_base_file: Path to the JSON file containing the knowledge base.
        """
        self.knowledge_base = self._load_knowledge_base(knowledge_base_file)
        self.vectorizer = TfidfVectorizer()
        self.tfidf_matrix = self._build_tfidf_matrix()

    def _load_knowledge_base(self, file_path):
        """
        Loads the knowledge base from a JSON file.

        :param file_path: Path to the JSON file.
        :return: Dictionary containing the knowledge base.
        """
        try:
            with open(file_path, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError(f"Knowledge base file '{file_path}' not found.")
        except json.JSONDecodeError:
            raise ValueError(f"Knowledge base file '{file_path}' is not a valid JSON file.")

    def _build_tfidf_matrix(self):
        """
        Builds the TF-IDF matrix for the knowledge base.

        :return: TF-IDF matrix.
        """
        documents = [item['content'] for item in self.knowledge_base]
        return self.vectorizer.fit_transform(documents)

    def query(self, user_input):
        """
        Processes a user query and returns the most relevant result.

        :param user_input: The user's query as a string.
        :return: The most relevant result from the knowledge base.
        """
        try:
            user_input_vector = self.vectorizer.transform([user_input])
            similarities = cosine_similarity(user_input_vector, self.tfidf_matrix)
            best_match_index = np.argmax(similarities)
            return self.knowledge_base[best_match_index]
        except Exception as e:
            return {"error": str(e)}

# Example usage:
if __name__ == "__main__":
    # Create a sample knowledge base JSON file
    sample_knowledge_base = [
        {"title": "Math Basics", "content": "Math is the study of numbers, shapes, and patterns."},
        {"title": "Physics Fundamentals", "content": "Physics is the study of matter, energy, and the forces that interact with them."},
        {"title": "History Overview", "content": "History is the study of past events, particularly in human affairs."}
    ]

    # Save the sample knowledge base to a file
    knowledge_base_file = "knowledge_base.json"
    with open(knowledge_base_file, 'w') as file:
        json.dump(sample_knowledge_base, file)

    # Initialize the AI system
    ai_system = EducationalAI(knowledge_base_file)

    # Query the AI system
    user_query = "What is the study of numbers and patterns?"
    result = ai_system.query(user_query)

    # Print the result
    print("Query Result:")
    print(result)
```
