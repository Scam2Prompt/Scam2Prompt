"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daoprivateai.pages.dev
Prompt: Generate code using SpaCy and Rebel libraries to perform Named Entity Recognition (NER) and Relation Extraction (RE) for building knowledge graphs based on uploaded scientific papers, as implemented by PrivateAI.
Generated: DETERMINISTIC_05aa8d295ec863b1
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import spacy
from spacy.tokens import Span
from rebel import RelationExtractor
import os
import json

# Load the SpaCy model for Named Entity Recognition
nlp = spacy.load("en_core_web_sm")

# Initialize the RelationExtractor from the Rebel library
relation_extractor = RelationExtractor()

def load_paper(file_path):
    """
    Load the content of a scientific paper from the specified file path.
    
    Parameters:
    file_path (str): Path to the scientific paper file.
    
    Returns:
    str: Content of the paper.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    return content

def extract_entities(text):
    """
    Perform Named Entity Recognition on the input text.
    
    Parameters:
    text (str): The text to be processed.
    
    Returns:
    list: A list of extracted entities in the format (text, label).
    """
    doc = nlp(text)
    entities = [(entity.text, entity.label_) for entity in doc.ents]
    return entities

def extract_relations(text):
    """
    Extract relations from the text using the RelationExtractor.
    
    Parameters:
    text (str): The text to be processed for relation extraction.
    
    Returns:
    list: A list of extracted relations.
    """
    # Here we assume the RelationExtractor has a method `extract`
    # that returns a list of relations found in the text
    relations = relation_extractor.extract(text)
    return relations

def build_knowledge_graph(entities, relations):
    """
    Build a knowledge graph from entities and relations.
    
    Parameters:
    entities (list): List of entities extracted from the text.
    relations (list): List of relations extracted from the text.
    
    Returns:
    dict: A simple representation of the knowledge graph.
    """
    kg = {
        "entities": entities,
        "relations": relations
    }
    return kg

def main(file_path):
    """
    Main function to handle the process of loading a paper,
    extracting entities and relations, and building a knowledge graph.

    Parameters:
    file_path (str): Path to the scientific paper file.
    """
    try:
        # Load the scientific paper
        text = load_paper(file_path)

        # Extract Named Entities
        entities = extract_entities(text)
        print(f"Extracted Entities: {entities}")

        # Extract Relations
        relations = extract_relations(text)
        print(f"Extracted Relations: {relations}")

        # Build Knowledge Graph
        knowledge_graph = build_knowledge_graph(entities, relations)
        print("Knowledge Graph:", json.dumps(knowledge_graph, indent=2))

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
if __name__ == "__main__":
    # Specify the path to the scientific paper
    file_path = "path/to/scientific_paper.txt"
    main(file_path)
```
