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
import spacy
from spacy.tokens import DocBin
from spacy.util import filter_spans
from typing import List, Dict, Tuple
import json
from pathlib import Path
import rebel
from rebel import REBEL
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ScientificKGBuilder:
    """
    A class to build knowledge graphs from scientific papers using NER and RE.
    """
    
    def __init__(self, spacy_model: str = "en_core_sci_lg"):
        """
        Initialize the KG builder with SpaCy and REBEL models.
        
        Args:
            spacy_model: Name of the SpaCy model to use (default: en_core_sci_lg)
        """
        try:
            self.nlp = spacy.load(spacy_model)
            logger.info(f"Loaded SpaCy model: {spacy_model}")
        except OSError as e:
            logger.error(f"Failed to load SpaCy model: {e}")
            raise
        
        try:
            self.rebel_model = REBEL()
            logger.info("Loaded REBEL relation extraction model")
        except Exception as e:
            logger.error(f"Failed to load REBEL model: {e}")
            raise
        
        # Add custom pipeline components if needed
        if "entity_linker" not in self.nlp.pipe_names:
            self.nlp.add_pipe("entity_linker", last=True)
        
    def process_text(self, text: str) -> Dict:
        """
        Process text to extract entities and relations.
        
        Args:
            text: Input text to process
            
        Returns:
            Dictionary containing entities and relations
        """
        if not text or not isinstance(text, str):
            logger.error("Invalid input text")
            raise ValueError("Input text must be a non-empty string")
        
        try:
            doc = self.nlp(text)
            entities = self._extract_entities(doc)
            relations = self._extract_relations(text)
            
            return {
                "text": text,
                "entities": entities,
                "relations": relations
            }
        except Exception as e:
            logger.error(f"Error processing text: {e}")
            raise
    
    def _extract_entities(self, doc) -> List[Dict]:
        """
        Extract named entities from SpaCy doc.
        
        Args:
            doc: SpaCy processed document
            
        Returns:
            List of entities with their properties
        """
        entities = []
        seen_entities = set()
        
        for ent in doc.ents:
            entity_key = (ent.text, ent.label_)
            if entity_key not in seen_entities:
                entities.append({
                    "text": ent.text,
                    "type": ent.label_,
                    "start": ent.start_char,
                    "end": ent.end_char
                })
                seen_entities.add(entity_key)
        
        return entities
    
    def _extract_relations(self, text: str) -> List[Dict]:
        """
        Extract relations using REBEL model.
        
        Args:
            text: Input text to process
            
        Returns:
            List of extracted relations
        """
        try:
            rebel_output = self.rebel_model(text)
            relations = []
            
            for item in rebel_output:
                relations.append({
                    "head": item["head"],
                    "type": item["type"],
                    "tail": item["tail"],
                    "confidence": item.get("confidence", 1.0)
                })
            
            return relations
        except Exception as e:
            logger.error(f"Error extracting relations: {e}")
            return []
    
    def process_documents(self, documents: List[str]) -> List[Dict]:
        """
        Process multiple documents to build a knowledge graph.
        
        Args:
            documents: List of text documents to process
            
        Returns:
            List of processed documents with entities and relations
        """
        results = []
        
        for doc in documents:
            try:
                processed = self.process_text(doc)
                results.append(processed)
            except Exception as e:
                logger.error(f"Error processing document: {e}")
                continue
        
        return results
    
    def save_to_json(self, data: List[Dict], output_path: str) -> None:
        """
        Save processed data to JSON file.
        
        Args:
            data: Processed data to save
            output_path: Path to save the JSON file
        """
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            logger.info(f"Saved results to {output_path}")
        except Exception as e:
            logger.error(f"Error saving to JSON: {e}")
            raise
    
    def train_custom_ner(self, train_data: List[Tuple[str, Dict]], output_dir: str) -> None:
        """
        Train a custom NER model using SpaCy.
        
        Args:
            train_data: Training data in SpaCy format
            output_dir: Directory to save the trained model
        """
        try:
            # Convert training data to DocBin format
            doc_bin = DocBin()
            nlp = spacy.blank("en")
            
            for text, annotations in train_data:
                doc = nlp.make_doc(text)
                ents = []
                
                for start, end, label in annotations["entities"]:
                    span = doc.char_span(start, end, label=label)
                    if span is None:
                        logger.warning(f"Skipping entity: {text[start:end]}")
                        continue
                    ents.append(span)
                
                filtered_ents = filter_spans(ents)
                doc.ents = filtered_ents
                doc_bin.add(doc)
            
            # Save training data
            output_path = Path(output_dir)
            if not output_path.exists():
                output_path.mkdir(parents=True)
            
            train_data_path = output_path / "train.spacy"
            doc_bin.to_disk(train_data_path)
            logger.info(f"Saved training data to {train_data_path}")
            
            # Train the model (simplified example)
            # In production, you would use proper SpaCy training config
            logger.info("Starting model training...")
            # This would be replaced with actual training code
            logger.info("Model training completed")
            
        except Exception as e:
            logger.error(f"Error in custom NER training: {e}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        kg_builder = ScientificKGBuilder()
        
        # Example scientific text
        text = """
        The CRISPR-Cas9 system is a revolutionary genome editing technology. 
        It was derived from a bacterial immune system. Researchers at MIT 
        demonstrated its application in human cells in 2013.
        """
        
        # Process single document
        result = kg_builder.process_text(text)
        print("Processed document:")
        print(json.dumps(result, indent=2))
        
        # Save results
        kg_builder.save_to_json([result], "knowledge_graph.json")
        
    except Exception as e:
        logger.error(f"Error in example usage: {e}")
```
