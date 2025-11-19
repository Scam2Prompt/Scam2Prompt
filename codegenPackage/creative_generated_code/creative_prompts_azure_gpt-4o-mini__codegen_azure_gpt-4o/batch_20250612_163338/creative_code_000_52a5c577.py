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

def extract_triplets(text):
    """
    Function to extract triplets (Subject, Predicate, Object) from scientific text using SpaCy's Named Entity Recognition (NER).

    Parameters:
        text (str): The text content of the scientific paper.

    Returns:
        list: A list of extracted triplets in the format [(subject, predicate, object), ...].
    """
    try:
        # Load SpaCy's pre-trained NLP model
        nlp = spacy.load("en_core_web_sm")
    except OSError:
        raise ValueError("SpaCy model 'en_core_web_sm' not found. Install it using `python -m spacy download en_core_web_sm`.")
    
    # Process the text with SpaCy's NLP pipeline
    doc = nlp(text)
    
    triplets = []  # List to store extracted triplets

    # Iterate through sentences in the text
    for sent in doc.sents:
        # Extract potential entities and relations
        subject = None
        predicate = None
        object_ = None

        for token in sent:
            # Identify subject (e.g., noun phrase or entity)
            if token.dep_ == "nsubj":
                subject = token.text

            # Identify predicate (e.g., verb)
            if token.pos_ == "VERB":
                predicate = token.text

            # Identify object (e.g., direct or indirect object)
            if token.dep_ in ("dobj", "pobj"):
                object_ = token.text

        # If all parts of a triplet are found, add them to the list
        if subject and predicate and object_:
            triplets.append((subject, predicate, object_))

    return triplets


# Example usage:
if __name__ == "__main__":
    # Replace with your own scientific paper text
    sample_text = (
        "Einstein proposed the theory of relativity. "
        "The theory explains how the speed of light is constant."
    )

    try:
        extracted_triplets = extract_triplets(sample_text)
        print("Extracted Triplets:")
        for triplet in extracted_triplets:
            print(triplet)
    except Exception as e:
        print(f"An error occurred: {e}")
```
