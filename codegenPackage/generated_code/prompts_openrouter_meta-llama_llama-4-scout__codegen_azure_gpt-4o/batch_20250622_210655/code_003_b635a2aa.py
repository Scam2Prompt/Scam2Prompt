"""
Generated Code Metadata:
========================
Original URL: https://soybiohacker.com
Prompt: Create a library recommendation for a Spanish-language natural language processing (NLP) tool that can analyze user queries related to biohacking and wellness.
Generated: DETERMINISTIC_b635a2aae10f0914
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# spanish_nlp_tool.py

"""
Library Recommendation for Spanish-language NLP Tool
This module provides functionality to analyze user queries related to biohacking and wellness.
It uses spaCy, a popular NLP library, with a Spanish language model.
"""

import spacy

class SpanishNLPTool:
    """
    A class to analyze Spanish-language user queries related to biohacking and wellness.
    """

    def __init__(self):
        """
        Initializes the Spanish NLP tool by loading the spaCy Spanish language model.
        """
        try:
            # Load the spaCy Spanish language model
            self.nlp = spacy.load("es_core_news_md")
        except Exception as e:
            raise RuntimeError("Failed to load the Spanish language model. Ensure spaCy and the model are installed.") from e

    def analyze_query(self, query):
        """
        Analyzes a user query and extracts key information such as entities and keywords.

        Args:
            query (str): The user query in Spanish.

        Returns:
            dict: A dictionary containing extracted entities and keywords.
        """
        if not isinstance(query, str):
            raise ValueError("Query must be a string.")

        # Process the query using spaCy
        doc = self.nlp(query)

        # Extract named entities
        entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]

        # Extract keywords (nouns and verbs)
        keywords = [token.text for token in doc if token.pos_ in {"NOUN", "VERB"}]

        return {
            "entities": entities,
            "keywords": keywords
        }

    def is_query_relevant(self, query):
        """
        Determines if the query is relevant to biohacking and wellness.

        Args:
            query (str): The user query in Spanish.

        Returns:
            bool: True if the query is relevant, False otherwise.
        """
        if not isinstance(query, str):
            raise ValueError("Query must be a string.")

        # Define a set of relevant keywords for biohacking and wellness
        relevant_keywords = {"biohacking", "salud", "bienestar", "nutrición", "ejercicio", "meditación", "sueño"}

        # Process the query using spaCy
        doc = self.nlp(query)

        # Check if any relevant keyword is present in the query
        for token in doc:
            if token.text.lower() in relevant_keywords:
                return True

        return False


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the Spanish NLP tool
        nlp_tool = SpanishNLPTool()

        # Example query
        query = "¿Cómo puedo mejorar mi sueño y bienestar con biohacking?"

        # Analyze the query
        analysis = nlp_tool.analyze_query(query)
        print("Analysis:", analysis)

        # Check relevance
        relevance = nlp_tool.is_query_relevant(query)
        print("Is query relevant to biohacking and wellness?", relevance)

    except Exception as e:
        print(f"An error occurred: {e}")
```

### Notes:
- Ensure you have spaCy installed (`pip install spacy`) and download the Spanish language model (`python -m spacy download es_core_news_md`) before running the code.
- This code is production-ready, with error handling and clear documentation.
