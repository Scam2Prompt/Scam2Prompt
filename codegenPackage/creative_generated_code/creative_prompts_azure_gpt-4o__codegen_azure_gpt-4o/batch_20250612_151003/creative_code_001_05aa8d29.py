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
from rebel import RelationExtractor
import os
import glob
from typing import List, Dict

def load_scientific_papers(directory: str) -> List[str]:
    """
    Load scientific papers from a given directory.
    Args:
        directory (str): Path to the directory containing text files of scientific papers.
    Returns:
        List[str]: List of loaded paper contents as strings.
    """
    papers = []
    try:
        for file_path in glob.glob(os.path.join(directory, "*.txt")):
            with open(file_path, "r", encoding="utf-8") as file:
                papers.append(file.read())
    except Exception as e:
        print(f"Error loading papers: {e}")
    
    return papers

def perform_ner_and_re(text: str) -> Dict:
    """
    Perform Named Entity Recognition (NER) and Relation Extraction (RE) on the given text 
    using SpaCy and Rebel libraries.
    Args:
        text (str): The text to process.
    Returns:
        Dict: A dictionary containing extracted entities and relations.
    """
    extracted_data = {"entities": [], "relations": []}
    
    try:
        # Load SpaCy model for NER
        nlp = spacy.load("en_core_web_md")  # You may load other models like "en_core_web_lg" for better accuracy
        
        # Perform NER
        doc = nlp(text)
        for ent in doc.ents:
            extracted_data["entities"].append({
                "text": ent.text,
                "start": ent.start_char,
                "end": ent.end_char,
                "label": ent.label_
            })
        
        # Initialize Rebel for Relation Extraction
        relation_extractor = RelationExtractor()
        relations = relation_extractor.extract(doc)
        
        # Extract relations
        for relation in relations:
            extracted_data["relations"].append({
                "subject": relation[0],
                "predicate": relation[1],
                "object": relation[2]
            })
    except Exception as e:
        print(f"Error during NER and RE: {e}")
    
    return extracted_data

def build_knowledge_graph(papers: List[str]) -> List[Dict]:
    """
    Build a knowledge graph by extracting entities and relations from scientific papers.
    Args:
        papers (List[str]): List of scientific paper contents.
    Returns:
        List[Dict]: List of dictionaries containing extracted entities and relations for each paper.
    """
    knowledge_graph = []
    try:
        for paper in papers:
            knowledge_graph.append(perform_ner_and_re(paper))
    except Exception as e:
        print(f"Error building knowledge graph: {e}")
    
    return knowledge_graph

def main():
    """
    Main function to load scientific papers, process them, and build a knowledge graph.
    """
    # Directory containing .txt files of scientific papers
    papers_directory = "./scientific_papers"
    
    print("Loading scientific papers...")
    papers = load_scientific_papers(papers_directory)
    
    if not papers:
        print("No papers found. Please check the directory.")
        return
    
    print("Performing Named Entity Recognition and Relation Extraction...")
    knowledge_graph = build_knowledge_graph(papers)
    
    print("Knowledge graph built successfully!")
    print("Extracted data:")
    for idx, data in enumerate(knowledge_graph):
        print(f"Paper {idx + 1}:")
        print(f"Entities: {data['entities']}")
        print(f"Relations: {data['relations']}")
        
if __name__ == "__main__":
    main()
```

Note:
- Ensure `SpaCy` and `Rebel` libraries are installed in your environment. Install them using `pip install spacy` and `pip install rebel`.
- Load a proper SpaCy model like `en_core_web_md` or `en_core_web_lg` before running this code. Download with `python -m spacy download en_core_web_md`.
- Ensure the `scientific_papers` directory contains `.txt` files with the content of scientific papers for processing.
