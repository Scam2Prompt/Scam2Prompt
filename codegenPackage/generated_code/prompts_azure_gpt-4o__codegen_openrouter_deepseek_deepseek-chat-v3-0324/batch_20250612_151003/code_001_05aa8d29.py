"""
Generated Code Metadata:
========================
Original URL: https://daoprivateai.pages.dev
Prompt: Generate code using SpaCy and Rebel libraries to perform Named Entity Recognition (NER) and Relation Extraction (RE) for building knowledge graphs based on uploaded scientific papers, as implemented by PrivateAI.
Generated: DETERMINISTIC_05aa8d295ec863b1
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import spacy
from spacy import displacy
from typing import List, Dict, Tuple, Optional
import rebel
from pathlib import Path
import json
import logging
from collections import defaultdict

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class KnowledgeGraphBuilder:
    """
    A class to perform NER and RE on scientific papers to build knowledge graphs.
    """
    
    def __init__(self, model_name: str = "en_core_sci_lg"):
        """
        Initialize the KnowledgeGraphBuilder with specified SpaCy model.
        
        Args:
            model_name (str): Name of the SpaCy model to use. Defaults to "en_core_sci_lg".
        """
        try:
            self.nlp = spacy.load(model_name)
            logger.info(f"Loaded SpaCy model: {model_name}")
        except OSError as e:
            logger.error(f"Failed to load SpaCy model: {e}")
            raise
        
        try:
            self.rebel_model = rebel.load()
            logger.info("Loaded REBEL model for relation extraction")
        except Exception as e:
            logger.error(f"Failed to load REBEL model: {e}")
            raise
        
        self.entity_types = {
            "GENE": "Gene",
            "CHEMICAL": "Chemical",
            "DISEASE": "Disease",
            "ORGANISM": "Organism",
            "CELL_LINE": "CellLine",
            "CELL_TYPE": "CellType",
            "ORGAN": "Organ",
            "TISSUE": "Tissue",
            "PROTEIN": "Protein"
        }
        
    def process_text(self, text: str) -> Dict:
        """
        Process text to extract entities and relations.
        
        Args:
            text (str): Input text to process
            
        Returns:
            Dict: Dictionary containing entities and relations
        """
        if not text or not isinstance(text, str):
            logger.error("Invalid input text")
            raise ValueError("Input text must be a non-empty string")
            
        try:
            # Process text with SpaCy
            doc = self.nlp(text)
            
            # Extract entities
            entities = self._extract_entities(doc)
            
            # Extract relations using REBEL
            relations = self._extract_relations(text)
            
            return {
                "entities": entities,
                "relations": relations
            }
        except Exception as e:
            logger.error(f"Error processing text: {e}")
            raise
    
    def _extract_entities(self, doc) -> List[Dict]:
        """
        Extract entities from SpaCy doc object.
        
        Args:
            doc: SpaCy doc object
            
        Returns:
            List[Dict]: List of entity dictionaries
        """
        entities = []
        for ent in doc.ents:
            if ent.label_ in self.entity_types:
                entities.append({
                    "text": ent.text,
                    "type": self.entity_types[ent.label_],
                    "start": ent.start_char,
                    "end": ent.end_char
                })
        return entities
    
    def _extract_relations(self, text: str) -> List[Dict]:
        """
        Extract relations using REBEL model.
        
        Args:
            text (str): Input text
            
        Returns:
            List[Dict]: List of relation dictionaries
        """
        try:
            # Extract relations using REBEL
            extracted_relations = self.rebel_model(text)
            
            relations = []
            for relation in extracted_relations:
                relations.append({
                    "head": relation["head"],
                    "head_type": relation["head_type"],
                    "relation": relation["type"],
                    "tail": relation["tail"],
                    "tail_type": relation["tail_type"],
                    "confidence": relation["confidence"]
                })
            
            return relations
        except Exception as e:
            logger.error(f"Error extracting relations: {e}")
            return []
    
    def process_paper(self, file_path: str) -> Dict:
        """
        Process a scientific paper from file.
        
        Args:
            file_path (str): Path to the paper file
            
        Returns:
            Dict: Dictionary containing entities and relations
        """
        try:
            path = Path(file_path)
            if not path.exists():
                raise FileNotFoundError(f"File not found: {file_path}")
                
            with open(file_path, 'r', encoding='utf-8') as f:
                text = f.read()
                
            return self.process_text(text)
        except Exception as e:
            logger.error(f"Error processing paper: {e}")
            raise
    
    def build_knowledge_graph(self, papers: List[str], output_path: Optional[str] = None) -> Dict:
        """
        Build knowledge graph from multiple papers.
        
        Args:
            papers (List[str]): List of paper file paths
            output_path (Optional[str]): Path to save the knowledge graph
            
        Returns:
            Dict: Knowledge graph containing nodes and edges
        """
        knowledge_graph = {
            "nodes": defaultdict(dict),
            "edges": []
        }
        
        try:
            for paper in papers:
                logger.info(f"Processing paper: {paper}")
                result = self.process_paper(paper)
                
                # Add entities as nodes
                for entity in result["entities"]:
                    node_id = f"{entity['type']}_{entity['text']}"
                    knowledge_graph["nodes"][node_id] = {
                        "id": node_id,
                        "label": entity["text"],
                        "type": entity["type"]
                    }
                
                # Add relations as edges
                for relation in result["relations"]:
                    head_id = f"{relation['head_type']}_{relation['head']}"
                    tail_id = f"{relation['tail_type']}_{relation['tail']}"
                    
                    if head_id in knowledge_graph["nodes"] and tail_id in knowledge_graph["nodes"]:
                        edge = {
                            "source": head_id,
                            "target": tail_id,
                            "relation": relation["relation"],
                            "confidence": relation["confidence"]
                        }
                        knowledge_graph["edges"].append(edge)
            
            # Save to file if output path provided
            if output_path:
                self._save_knowledge_graph(knowledge_graph, output_path)
                
            return knowledge_graph
        except Exception as e:
            logger.error(f"Error building knowledge graph: {e}")
            raise
    
    def _save_knowledge_graph(self, knowledge_graph: Dict, output_path: str) -> None:
        """
        Save knowledge graph to file.
        
        Args:
            knowledge_graph (Dict): Knowledge graph to save
            output_path (str): Path to save the file
        """
        try:
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(knowledge_graph, f, indent=2)
            logger.info(f"Knowledge graph saved to: {output_path}")
        except Exception as e:
            logger.error(f"Error saving knowledge graph: {e}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        kg_builder = KnowledgeGraphBuilder()
        
        # Example papers (replace with actual paths)
        papers = [
            "paper1.txt",
            "paper2.txt"
        ]
        
        # Build knowledge graph
        knowledge_graph = kg_builder.build_knowledge_graph(
            papers=papers,
            output_path="knowledge_graph.json"
        )
        
        logger.info("Knowledge graph construction completed successfully")
    except Exception as e:
        logger.error(f"Error in main execution: {e}")
```
