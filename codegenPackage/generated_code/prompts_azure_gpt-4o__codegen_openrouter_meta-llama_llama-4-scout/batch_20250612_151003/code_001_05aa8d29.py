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
# Import required libraries
import spacy
from spacy.util import minibatch, compounding
import rebel
from rebel import Rebel
import networkx as nx
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class KnowledgeGraphBuilder:
    def __init__(self, spacy_model_name, rebel_model_name):
        """
        Initialize the KnowledgeGraphBuilder with SpaCy and Rebel models.

        Args:
        - spacy_model_name (str): Name of the SpaCy model to use for NER.
        - rebel_model_name (str): Name of the Rebel model to use for RE.
        """
        self.nlp = spacy.load(spacy_model_name)
        self.rebel_model = Rebel(rebel_model_name)

    def extract_entities(self, text):
        """
        Perform Named Entity Recognition (NER) on the given text.

        Args:
        - text (str): Text to extract entities from.

        Returns:
        - entities (list): List of extracted entities.
        """
        try:
            doc = self.nlp(text)
            entities = [(ent.text, ent.label_) for ent in doc.ents]
            return entities
        except Exception as e:
            logger.error(f"Error extracting entities: {str(e)}")
            return []

    def extract_relations(self, text, entities):
        """
        Perform Relation Extraction (RE) on the given text and entities.

        Args:
        - text (str): Text to extract relations from.
        - entities (list): List of entities to extract relations between.

        Returns:
        - relations (list): List of extracted relations.
        """
        try:
            relations = self.rebel_model.extract_relations(text, entities)
            return relations
        except Exception as e:
            logger.error(f"Error extracting relations: {str(e)}")
            return []

    def build_knowledge_graph(self, text):
        """
        Build a knowledge graph from the given text.

        Args:
        - text (str): Text to build the knowledge graph from.

        Returns:
        - graph (nx.Graph): Constructed knowledge graph.
        """
        entities = self.extract_entities(text)
        relations = self.extract_relations(text, [ent[0] for ent in entities])

        graph = nx.Graph()
        graph.add_nodes_from([ent[0] for ent in entities])

        for relation in relations:
            if relation['subject'] in graph.nodes and relation['object'] in graph.nodes:
                graph.add_edge(relation['subject'], relation['object'], relation=relation['relation'])

        return graph

def main():
    # Load models
    spacy_model_name = "en_core_sci_lg"
    rebel_model_name = "rebel-contriever"

    kg_builder = KnowledgeGraphBuilder(spacy_model_name, rebel_model_name)

    # Example usage
    text = "The protein kinase Akt is involved in cell survival and is activated by PI3K."
    graph = kg_builder.build_knowledge_graph(text)

    # Print the constructed knowledge graph
    print("Nodes:")
    print(graph.nodes)
    print("Edges:")
    print(graph.edges(data=True))

if __name__ == "__main__":
    main()
```
