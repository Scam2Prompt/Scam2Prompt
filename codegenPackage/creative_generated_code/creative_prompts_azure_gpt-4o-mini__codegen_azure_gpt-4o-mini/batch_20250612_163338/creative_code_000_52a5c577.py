"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daoprivateai.pages.dev
Prompt: Generate a code snippet using the SpaCy library for Named Entity Recognition (NER) to extract triplets from scientific papers uploaded to the PrivateAI platform.
Generated: DETERMINISTIC_52a5c57778f3ae9f
Batch ID: 20250612_163338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import spacy
from spacy import displacy
from typing import List, Tuple

# Load the SpaCy model for Named Entity Recognition
nlp = spacy.load("en_core_web_sm")

def extract_entities(text: str) -> List[Tuple[str, str]]:
    """
    Extract named entities from the provided text using SpaCy's NER capabilities.

    Args:
        text (str): The input text from which to extract entities.

    Returns:
        List[Tuple[str, str]]: A list of tuples containing (entity_text, entity_label).
    """
    try:
        # Process the text using the NER model
        doc = nlp(text)
        
        # Extract entities
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        
        return entities

    except Exception as e:
        # Log the exception and return an empty list
        print(f"An error occurred while extracting entities: {e}")
        return []

def extract_triplets(entities: List[Tuple[str, str]]) -> List[Tuple[str, str, str]]:
    """
    Extract triplets (subject, predicate, object) from the list of named entities.

    Args:
        entities (List[Tuple[str, str]]): List of named entities.

    Returns:
        List[Tuple[str, str, str]]: A list of triplets extracted from the entities.
    """
    triplets = []

    # Simple heuristic for extracting triplets (This part may need to be improved based on specific needs)
    for i in range(len(entities) - 1):
        subject = entities[i]
        predicate = "is related to"  # Placeholder predicate
        obj = entities[i + 1]

        triplet = (subject[0], predicate, obj[0])
        triplets.append(triplet)

    return triplets

def main():
    # Example text from a scientific paper
    example_text = """
    The research conducted by Dr. Smith at the University of Science shows that 
    the new compound significantly reduces the growth of cancer cells in vitro.
    """

    # Extract entities from the text
    entities = extract_entities(example_text)
    
    # Extract triplets from the named entities
    triplets = extract_triplets(entities)

    # Display the extracted triplets
    for triplet in triplets:
        print(triplet)

if __name__ == "__main__":
    main()
```
