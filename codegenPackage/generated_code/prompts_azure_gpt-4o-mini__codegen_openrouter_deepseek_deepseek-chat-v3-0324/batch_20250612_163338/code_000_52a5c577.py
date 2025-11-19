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
from typing import List, Dict, Optional, Tuple
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class NERTripletExtractor:
    """
    A class for extracting named entity recognition (NER) triplets from scientific papers using SpaCy.
    The triplets consist of (subject, relation, object) extracted from the text.
    """
    
    def __init__(self, model_name: str = "en_core_sci_sm"):
        """
        Initialize the NER Triplet Extractor with a SpaCy model.
        
        Args:
            model_name (str): Name of the SpaCy model to use. Defaults to "en_core_sci_sm".
        """
        try:
            self.nlp = spacy.load(model_name)
            logger.info(f"Successfully loaded SpaCy model: {model_name}")
        except OSError as e:
            logger.error(f"Model {model_name} not found. Please install it first.")
            raise
        except Exception as e:
            logger.error(f"Error loading SpaCy model: {e}")
            raise

    def extract_triplets(self, text: str) -> List[Dict[str, str]]:
        """
        Extract (subject, relation, object) triplets from the input text using SpaCy NER.
        
        Args:
            text (str): Input text to process.
            
        Returns:
            List[Dict[str, str]]: List of triplets as dictionaries with keys 'subject', 'relation', 'object'.
        """
        if not text or not isinstance(text, str):
            logger.warning("Input text is empty or not a string.")
            return []

        try:
            doc = self.nlp(text)
            triplets = []
            
            for sent in doc.sents:
                # Extract entities in the sentence
                entities = [ent.text for ent in sent.ents]
                
                # Simple heuristic: use verbs as relations and adjacent entities as subject/object
                verbs = [token.text for token in sent if token.pos_ == "VERB"]
                
                if len(entities) >= 2 and verbs:
                    # Create triplets by pairing entities with verbs
                    for i in range(len(entities) - 1):
                        triplet = {
                            'subject': entities[i],
                            'relation': verbs[0] if verbs else "related_to",
                            'object': entities[i + 1]
                        }
                        triplets.append(triplet)
            
            logger.info(f"Extracted {len(triplets)} triplets from text.")
            return triplets
            
        except Exception as e:
            logger.error(f"Error processing text: {e}")
            return []

    def process_paper(self, file_path: str) -> Optional[List[Dict[str, str]]]:
        """
        Process a scientific paper from a file and extract triplets.
        
        Args:
            file_path (str): Path to the file containing the paper text.
            
        Returns:
            Optional[List[Dict[str, str]]]: List of triplets or None if processing fails.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                text = file.read()
                return self.extract_triplets(text)
        except FileNotFoundError:
            logger.error(f"File not found: {file_path}")
            return None
        except Exception as e:
            logger.error(f"Error reading file {file_path}: {e}")
            return None

# Example usage
if __name__ == "__main__":
    try:
        extractor = NERTripletExtractor()
        
        # Example text (in production, this would come from a file or API)
        example_text = """
        The study found that COVID-19 vaccines significantly reduce transmission rates.
        Researchers observed that Pfizer and Moderna vaccines were 90% effective.
        """
        
        triplets = extractor.extract_triplets(example_text)
        for triplet in triplets:
            print(f"Subject: {triplet['subject']}, Relation: {triplet['relation']}, Object: {triplet['object']}")
            
    except Exception as e:
        logger.error(f"Error in example usage: {e}")
```
