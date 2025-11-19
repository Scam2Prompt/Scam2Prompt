"""
Generated Code Metadata:
========================
Original URL: https://daoprivateai.pages.dev
Prompt: Develop a Natural Language Processing (NLP) model using SpaCy and Rebel to perform Named Entity Recognition (NER) and Relation Extraction (RE) for building comprehensive knowledge graphs from scientific papers.
Generated: DETERMINISTIC_14f7fecb6240cf7a
Batch ID: 20250622_211405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import spacy
from spacy.util import minibatch, compounding
import rebel
from rebel import Rebel
import pandas as pd
import numpy as np

# Load the SpaCy English model
nlp = spacy.load("en_core_web_lg")

# Load the Rebel model
rebel_model = Rebel.load("rebel-ontonotes")

def perform_ner(text):
    """
    Perform Named Entity Recognition (NER) using SpaCy.

    Args:
    text (str): The input text.

    Returns:
    entities (list): A list of entities in the text.
    """
    # Process the text using SpaCy
    doc = nlp(text)

    # Extract entities
    entities = [(entity.text, entity.label_) for entity in doc.ents]

    return entities

def perform_re(text):
    """
    Perform Relation Extraction (RE) using Rebel.

    Args:
    text (str): The input text.

    Returns:
    relations (list): A list of relations in the text.
    """
    try:
        # Process the text using Rebel
        output = rebel_model.generate(text)

        # Extract relations
        relations = []
        for triple in output:
            subject = triple["subject"]
            predicate = triple["predicate"]
            object = triple["object"]
            relations.append((subject, predicate, object))

        return relations
    except Exception as e:
        print(f"Error performing RE: {str(e)}")
        return []

def build_knowledge_graph(text):
    """
    Build a comprehensive knowledge graph from scientific papers.

    Args:
    text (str): The input text.

    Returns:
    graph (dict): A dictionary representing the knowledge graph.
    """
    # Perform NER
    entities = perform_ner(text)

    # Perform RE
    relations = perform_re(text)

    # Build the knowledge graph
    graph = {"entities": entities, "relations": relations}

    return graph

def main():
    # Example usage
    text = "The protein p53 is a tumor suppressor that regulates cell growth and division. It is often mutated in cancer cells."

    # Build the knowledge graph
    graph = build_knowledge_graph(text)

    # Print the knowledge graph
    print("Entities:")
    for entity in graph["entities"]:
        print(entity)

    print("\nRelations:")
    for relation in graph["relations"]:
        print(relation)

if __name__ == "__main__":
    main()
```
