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
from spacy.pipeline import EntityRuler
from rebel import RelationExtractor  # Assuming Rebel is a library for Relation Extraction
import os
import json

# Function to load scientific papers from a directory
def load_papers(directory):
    """
    Load scientific papers from a specified directory.
    :param directory: Path to the directory containing text files.
    :return: List of strings, each representing the content of a paper.
    """
    papers = []
    try:
        for filename in os.listdir(directory):
            if filename.endswith(".txt"):
                with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
                    papers.append(file.read())
    except Exception as e:
        print(f"Error loading papers: {e}")
    return papers

# Function to perform Named Entity Recognition (NER) using SpaCy
def perform_ner(nlp, text):
    """
    Perform Named Entity Recognition (NER) on the given text using SpaCy.
    :param nlp: SpaCy NLP model.
    :param text: Text to process.
    :return: List of entities extracted from the text.
    """
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    return entities

# Function to perform Relation Extraction (RE) using Rebel
def perform_relation_extraction(re_model, text):
    """
    Perform Relation Extraction (RE) on the given text using Rebel.
    :param re_model: Rebel Relation Extraction model.
    :param text: Text to process.
    :return: List of relations extracted from the text.
    """
    try:
        relations = re_model.extract_relations(text)
        return relations
    except Exception as e:
        print(f"Error performing relation extraction: {e}")
        return []

# Function to build a knowledge graph from entities and relations
def build_knowledge_graph(entities, relations):
    """
    Build a knowledge graph from extracted entities and relations.
    :param entities: List of entities.
    :param relations: List of relations.
    :return: Knowledge graph represented as a dictionary.
    """
    knowledge_graph = {"entities": entities, "relations": relations}
    return knowledge_graph

# Main function to process scientific papers and build knowledge graphs
def main():
    """
    Main function to process scientific papers and build knowledge graphs.
    """
    # Load SpaCy NLP model
    try:
        nlp = spacy.load("en_core_web_sm")  # Use a pre-trained SpaCy model
    except Exception as e:
        print(f"Error loading SpaCy model: {e}")
        return

    # Initialize Rebel Relation Extraction model
    try:
        re_model = RelationExtractor()  # Assuming Rebel has a default constructor
    except Exception as e:
        print(f"Error initializing Rebel model: {e}")
        return

    # Load scientific papers
    papers_directory = "./scientific_papers"  # Replace with your directory path
    papers = load_papers(papers_directory)
    if not papers:
        print("No papers found in the specified directory.")
        return

    # Process each paper
    for i, paper in enumerate(papers):
        print(f"Processing paper {i + 1}...")
        entities = perform_ner(nlp, paper)
        relations = perform_relation_extraction(re_model, paper)
        knowledge_graph = build_knowledge_graph(entities, relations)

        # Save knowledge graph to a JSON file
        output_file = f"knowledge_graph_{i + 1}.json"
        try:
            with open(output_file, 'w', encoding='utf-8') as file:
                json.dump(knowledge_graph, file, indent=4)
            print(f"Knowledge graph saved to {output_file}")
        except Exception as e:
            print(f"Error saving knowledge graph: {e}")

if __name__ == "__main__":
    main()
```
