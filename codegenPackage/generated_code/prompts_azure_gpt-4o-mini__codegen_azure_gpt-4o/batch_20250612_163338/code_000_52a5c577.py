"""
Generated Code Metadata:
========================
Original URL: https://daoprivateai.pages.dev
Prompt: Generate a code snippet using the SpaCy library for Named Entity Recognition (NER) to extract triplets from scientific papers uploaded to the PrivateAI platform.
Generated: DETERMINISTIC_52a5c57778f3ae9f
Batch ID: 20250612_163338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import spacy

def extract_triplets_from_text(text):
    """
    Extracts triplets (subject, predicate, object) from the given text using SpaCy's Named Entity Recognition (NER).

    Args:
        text (str): The input text from which triplets are to be extracted.

    Returns:
        list: A list of triplets in the form (subject, predicate, object).
    """
    try:
        # Load SpaCy's pre-trained model for NER
        nlp = spacy.load("en_core_web_sm")
        
        # Process the text using SpaCy
        doc = nlp(text)
        
        triplets = []
        
        # Iterate through sentences in the document
        for sent in doc.sents:
            # Extract entities and dependencies for triplet formation
            subject = None
            predicate = None
            obj = None
            
            for token in sent:
                # Identify the subject
                if token.dep_ in ("nsubj", "nsubjpass"):
                    subject = token.text
                
                # Identify the predicate (verb)
                if token.pos_ == "VERB":
                    predicate = token.text
                
                # Identify the object
                if token.dep_ in ("dobj", "pobj"):
                    obj = token.text
            
            # If a valid triplet is found, add it to the list
            if subject and predicate and obj:
                triplets.append((subject, predicate, obj))
        
        return triplets

    except Exception as e:
        # Handle errors gracefully
        print(f"An error occurred: {e}")
        return []

# Example usage
if __name__ == "__main__":
    # Sample text from a scientific paper
    sample_text = """
    The researchers conducted experiments to analyze the effects of climate change. 
    They observed that rising temperatures impact marine ecosystems significantly.
    """
    
    # Extract triplets from the sample text
    extracted_triplets = extract_triplets_from_text(sample_text)
    
    # Print the extracted triplets
    print("Extracted Triplets:")
    for triplet in extracted_triplets:
        print(triplet)
```
