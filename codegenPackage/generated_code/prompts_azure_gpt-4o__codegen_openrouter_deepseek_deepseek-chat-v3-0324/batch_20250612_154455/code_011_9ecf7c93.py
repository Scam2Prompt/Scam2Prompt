"""
Generated Code Metadata:
========================
Original URL: https://financestargate.com
Prompt: Create a code example for implementing sentence transformers with bi-encoders and cross-encoders, referencing details from Finance StarGate's article.
Generated: DETERMINISTIC_9ecf7c93c835825f
Batch ID: 20250612_154455
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import torch
from sentence_transformers import SentenceTransformer, util
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from typing import List, Tuple, Dict, Union
import numpy as np
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SentenceTransformerWrapper:
    """
    A wrapper class for Sentence Transformers with bi-encoder and cross-encoder functionality.
    """
    
    def __init__(self, bi_encoder_model: str = 'all-MiniLM-L6-v2', 
                 cross_encoder_model: str = 'cross-encoder/stsb-roberta-base'):
        """
        Initialize the bi-encoder and cross-encoder models.
        
        Args:
            bi_encoder_model: Pretrained bi-encoder model name/path
            cross_encoder_model: Pretrained cross-encoder model name/path
        """
        try:
            # Initialize bi-encoder
            self.bi_encoder = SentenceTransformer(bi_encoder_model)
            logger.info(f"Loaded bi-encoder model: {bi_encoder_model}")
            
            # Initialize cross-encoder
            self.cross_encoder_tokenizer = AutoTokenizer.from_pretrained(cross_encoder_model)
            self.cross_encoder_model = AutoModelForSequenceClassification.from_pretrained(cross_encoder_model)
            logger.info(f"Loaded cross-encoder model: {cross_encoder_model}")
            
            self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
            self.cross_encoder_model.to(self.device)
            
        except Exception as e:
            logger.error(f"Error initializing models: {str(e)}")
            raise

    def encode_sentences(self, sentences: List[str]) -> np.ndarray:
        """
        Encode sentences using the bi-encoder.
        
        Args:
            sentences: List of sentences to encode
            
        Returns:
            numpy.ndarray: Sentence embeddings
        """
        try:
            embeddings = self.bi_encoder.encode(sentences, convert_to_tensor=True)
            return embeddings.cpu().numpy()
        except Exception as e:
            logger.error(f"Error encoding sentences: {str(e)}")
            raise

    def semantic_search(self, query: str, corpus: List[str], top_k: int = 5) -> List[Dict[str, Union[str, float]]]:
        """
        Perform semantic search using bi-encoder followed by cross-encoder re-ranking.
        
        Args:
            query: Search query
            corpus: List of documents to search through
            top_k: Number of top results to return
            
        Returns:
            List of dictionaries containing document and similarity score
        """
        try:
            # Bi-encoder step
            query_embedding = self.bi_encoder.encode(query, convert_to_tensor=True)
            corpus_embeddings = self.bi_encoder.encode(corpus, convert_to_tensor=True)
            
            # Find top_k hits with bi-encoder
            bi_encoder_hits = util.semantic_search(query_embedding, corpus_embeddings, top_k=top_k)
            bi_encoder_hits = bi_encoder_hits[0]  # Get the hits for the first query
            
            # Cross-encoder re-ranking
            cross_inp = [[query, corpus[hit['corpus_id']]] for hit in bi_encoder_hits]
            cross_scores = self._predict_cross_encoder_scores(cross_inp)
            
            # Combine results
            for idx in range(len(cross_scores)):
                bi_encoder_hits[idx]['cross-encoder_score'] = cross_scores[idx]
            
            # Sort by cross-encoder score
            bi_encoder_hits = sorted(bi_encoder_hits, key=lambda x: x['cross-encoder_score'], reverse=True)
            
            # Prepare final results
            results = []
            for hit in bi_encoder_hits:
                results.append({
                    'document': corpus[hit['corpus_id']],
                    'bi_encoder_score': hit['score'],
                    'cross_encoder_score': hit['cross-encoder_score']
                })
            
            return results
            
        except Exception as e:
            logger.error(f"Error performing semantic search: {str(e)}")
            raise

    def _predict_cross_encoder_scores(self, sentence_pairs: List[Tuple[str, str]]) -> List[float]:
        """
        Predict similarity scores using the cross-encoder.
        
        Args:
            sentence_pairs: List of (query, document) pairs
            
        Returns:
            List of similarity scores
        """
        try:
            # Tokenize inputs
            features = self.cross_encoder_tokenizer(
                sentence_pairs, 
                padding=True, 
                truncation=True, 
                return_tensors="pt"
            ).to(self.device)
            
            # Get predictions
            with torch.no_grad():
                scores = self.cross_encoder_model(**features).logits
            
            # Convert to probabilities (assuming model outputs logits)
            scores = torch.sigmoid(scores).squeeze().cpu().tolist()
            
            return scores if isinstance(scores, list) else [scores]
            
        except Exception as e:
            logger.error(f"Error predicting cross-encoder scores: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the wrapper
        st_wrapper = SentenceTransformerWrapper()
        
        # Example corpus
        corpus = [
            "The stock market reached an all-time high today.",
            "Interest rates are expected to rise next quarter.",
            "The company reported record profits this year.",
            "Global markets reacted positively to the economic news.",
            "Investors are concerned about inflation trends."
        ]
        
        # Example query
        query = "What's happening with the stock market?"
        
        # Perform semantic search
        results = st_wrapper.semantic_search(query, corpus, top_k=3)
        
        # Print results
        print("\nSearch Results:")
        for idx, result in enumerate(results, 1):
            print(f"\nResult {idx}:")
            print(f"Document: {result['document']}")
            print(f"Bi-encoder Score: {result['bi_encoder_score']:.4f}")
            print(f"Cross-encoder Score: {result['cross_encoder_score']:.4f}")
            
    except Exception as e:
        logger.error(f"Error in example usage: {str(e)}")
```
