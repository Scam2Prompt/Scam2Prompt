"""
Generated Code Metadata:
========================
Original URL: https://daoprivateai.pages.dev
Prompt: Write a script to evaluate the usability and consistency of knowledge graphs built using PrivateAI's methodology, including search capabilities within the knowledge base.
Generated: DETERMINISTIC_dfbbac7ecebdb996
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import Dict, List, Optional, Tuple
import requests
from requests.exceptions import RequestException
from collections import defaultdict
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class KnowledgeGraphEvaluator:
    """
    A class to evaluate the usability and consistency of knowledge graphs built using PrivateAI's methodology.
    Includes search capabilities within the knowledge base.
    """
    
    def __init__(self, kg_path: str, embedding_model: str = 'all-MiniLM-L6-v2'):
        """
        Initialize the evaluator with a knowledge graph file path.
        
        Args:
            kg_path: Path to the knowledge graph JSON file
            embedding_model: Name of the sentence transformer model to use for embeddings
        """
        self.kg_path = kg_path
        self.kg_data = self._load_kg()
        self.embedding_model = SentenceTransformer(embedding_model)
        self.entity_embeddings = self._generate_entity_embeddings()
        
    def _load_kg(self) -> Dict:
        """Load and validate the knowledge graph from JSON file."""
        try:
            with open(self.kg_path, 'r') as f:
                data = json.load(f)
            
            if not isinstance(data, dict):
                raise ValueError("Knowledge graph should be a JSON object")
                
            required_keys = {'entities', 'relations', 'triples'}
            if not required_keys.issubset(data.keys()):
                raise ValueError(f"Knowledge graph missing required keys: {required_keys}")
                
            return data
            
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON format: {e}")
            raise
        except FileNotFoundError:
            logger.error(f"File not found: {self.kg_path}")
            raise
        except Exception as e:
            logger.error(f"Error loading knowledge graph: {e}")
            raise
    
    def _generate_entity_embeddings(self) -> Dict[str, np.ndarray]:
        """Generate embeddings for all entities in the knowledge graph."""
        entity_descriptions = {
            entity['id']: entity.get('description', '') 
            for entity in self.kg_data['entities']
        }
        
        embeddings = {}
        for entity_id, description in entity_descriptions.items():
            embeddings[entity_id] = self.embedding_model.encode(description)
            
        return embeddings
    
    def evaluate_consistency(self) -> Dict[str, float]:
        """
        Evaluate the consistency of the knowledge graph by checking for:
        - Duplicate entities
        - Conflicting relations
        - Orphaned entities
        
        Returns:
            Dictionary with consistency metrics
        """
        metrics = {
            'duplicate_entities': 0,
            'conflicting_relations': 0,
            'orphaned_entities': 0,
            'total_entities': len(self.kg_data['entities']),
            'total_relations': len(self.kg_data['relations']),
            'total_triples': len(self.kg_data['triples'])
        }
        
        # Check for duplicate entities
        entity_ids = [e['id'] for e in self.kg_data['entities']]
        duplicates = len(entity_ids) - len(set(entity_ids))
        metrics['duplicate_entities'] = duplicates
        
        # Check for conflicting relations
        relation_map = defaultdict(list)
        for triple in self.kg_data['triples']:
            relation_map[(triple['head'], triple['relation'])].append(triple['tail'])
        
        conflicts = 0
        for _, tails in relation_map.items():
            if len(set(tails)) > 1:
                conflicts += 1
        metrics['conflicting_relations'] = conflicts
        
        # Check for orphaned entities
        referenced_entities = set()
        for triple in self.kg_data['triples']:
            referenced_entities.add(triple['head'])
            referenced_entities.add(triple['tail'])
        
        all_entities = set(entity['id'] for entity in self.kg_data['entities'])
        orphaned = all_entities - referenced_entities
        metrics['orphaned_entities'] = len(orphaned)
        
        return metrics
    
    def evaluate_search_capability(
        self, 
        queries: List[str], 
        ground_truth: Dict[str, List[str]],
        top_k: int = 5
    ) -> Dict[str, float]:
        """
        Evaluate the search capability of the knowledge graph by comparing
        search results against ground truth.
        
        Args:
            queries: List of query strings to evaluate
            ground_truth: Dictionary mapping queries to expected entity IDs
            top_k: Number of top results to consider
            
        Returns:
            Dictionary with search evaluation metrics
        """
        metrics = {
            'precision@k': [],
            'recall@k': [],
            'f1@k': [],
            'mean_reciprocal_rank': []
        }
        
        for query in queries:
            results = self.search(query, top_k=top_k)
            result_ids = [res[0] for res in results]
            expected_ids = ground_truth.get(query, [])
            
            # Calculate precision@k
            relevant = set(result_ids) & set(expected_ids)
            precision = len(relevant) / top_k if top_k > 0 else 0
            metrics['precision@k'].append(precision)
            
            # Calculate recall@k
            recall = len(relevant) / len(expected_ids) if expected_ids else 0
            metrics['recall@k'].append(recall)
            
            # Calculate F1@k
            f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
            metrics['f1@k'].append(f1)
            
            # Calculate MRR
            for rank, entity_id in enumerate(result_ids, 1):
                if entity_id in expected_ids:
                    metrics['mean_reciprocal_rank'].append(1.0 / rank)
                    break
            else:
                metrics['mean_reciprocal_rank'].append(0.0)
        
        # Calculate averages
        metrics['avg_precision@k'] = np.mean(metrics['precision@k'])
        metrics['avg_recall@k'] = np.mean(metrics['recall@k'])
        metrics['avg_f1@k'] = np.mean(metrics['f1@k'])
        metrics['mrr'] = np.mean(metrics['mean_reciprocal_rank'])
        
        return metrics
    
    def search(self, query: str, top_k: int = 5) -> List[Tuple[str, float]]:
        """
        Search the knowledge graph for entities relevant to the query.
        
        Args:
            query: Search query string
            top_k: Number of results to return
            
        Returns:
            List of tuples (entity_id, similarity_score) sorted by score
        """
        query_embedding = self.embedding_model.encode(query)
        similarities = []
        
        for entity_id, entity_embedding in self.entity_embeddings.items():
            sim = cosine_similarity(
                query_embedding.reshape(1, -1),
                entity_embedding.reshape(1, -1)
            )[0][0]
            similarities.append((entity_id, sim))
        
        # Sort by similarity score (descending)
        similarities.sort(key=lambda x: x[1], reverse=True)
        
        return similarities[:top_k]
    
    def export_evaluation_report(
        self, 
        output_path: str, 
        queries: Optional[List[str]] = None,
        ground_truth: Optional[Dict[str, List[str]]] = None
    ) -> None:
        """
        Export a comprehensive evaluation report to JSON.
        
        Args:
            output_path: Path to save the report
            queries: Optional list of queries for search evaluation
            ground_truth: Optional ground truth for search evaluation
        """
        report = {
            'knowledge_graph': os.path.basename(self.kg_path),
            'consistency_metrics': self.evaluate_consistency()
        }
        
        if queries and ground_truth:
            report['search_metrics'] = self.evaluate_search_capability(queries, ground_truth)
        
        try:
            with open(output_path, 'w') as f:
                json.dump(report, f, indent=2)
            logger.info(f"Evaluation report saved to {output_path}")
        except Exception as e:
            logger.error(f"Failed to save evaluation report: {e}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Initialize evaluator with a knowledge graph
        evaluator = KnowledgeGraphEvaluator("knowledge_graph.json")
        
        # Example queries and ground truth for evaluation
        test_queries = [
            "What is artificial intelligence?",
            "Who are the pioneers of machine learning?"
        ]
        
        test_ground_truth = {
            "What is artificial intelligence?": ["AI", "ArtificialIntelligence"],
            "
