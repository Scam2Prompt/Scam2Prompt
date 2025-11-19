"""
Generated Code Metadata:
========================
Original URL: https://anygrid.app
Prompt: Design a system to categorize and analyze medical records using AI-driven document analysis, inspired by AnyGrid's capabilities.
Generated: DETERMINISTIC_14f0ef9cc85da12d
Batch ID: 20250622_211918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
import logging
from typing import Dict, List, Optional
from datetime import datetime
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
import PyPDF2
import pytesseract
from PIL import Image
import numpy as np

# Initialize logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load spaCy model for NLP processing
try:
    nlp = spacy.load('en_core_web_sm')
except OSError:
    logger.error("spaCy model 'en_core_web_sm' not found. Please install it.")
    raise

class MedicalRecordProcessor:
    """
    A class to process, categorize, and analyze medical records using AI-driven document analysis.
    """
    
    def __init__(self, config_path: Optional[str] = None):
        """
        Initialize the MedicalRecordProcessor with optional configuration.
        
        Args:
            config_path (str, optional): Path to configuration file. Defaults to None.
        """
        self.config = self._load_config(config_path)
        self.vectorizer = TfidfVectorizer(
            max_features=self.config.get('max_features', 1000),
            stop_words=list(STOP_WORDS)
        )
        self.cluster_model = None
        self.categories = self.config.get('categories', [])
        
    def _load_config(self, config_path: Optional[str]) -> Dict:
        """
        Load configuration from file or use defaults.
        
        Args:
            config_path (str, optional): Path to config file. Defaults to None.
            
        Returns:
            Dict: Configuration dictionary.
        """
        default_config = {
            'max_features': 1000,
            'categories': ['diagnosis', 'treatment', 'lab_results', 'prescriptions', 'notes'],
            'min_clusters': 2,
            'max_clusters': 5
        }
        
        if config_path and os.path.exists(config_path):
            try:
                with open(config_path, 'r') as f:
                    return {**default_config, **json.load(f)}
            except Exception as e:
                logger.warning(f"Failed to load config: {e}. Using defaults.")
        
        return default_config
    
    def extract_text(self, file_path: str) -> str:
        """
        Extract text from a medical record file (PDF or image).
        
        Args:
            file_path (str): Path to the medical record file.
            
        Returns:
            str: Extracted text.
            
        Raises:
            ValueError: If file type is unsupported or extraction fails.
        """
        if not os.path.exists(file_path):
            raise ValueError(f"File not found: {file_path}")
            
        try:
            if file_path.lower().endswith('.pdf'):
                text = self._extract_text_from_pdf(file_path)
            elif file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
                text = self._extract_text_from_image(file_path)
            else:
                raise ValueError("Unsupported file format")
                
            return text
        except Exception as e:
            logger.error(f"Failed to extract text from {file_path}: {e}")
            raise ValueError(f"Text extraction failed: {e}")
    
    def _extract_text_from_pdf(self, file_path: str) -> str:
        """
        Extract text from a PDF file.
        
        Args:
            file_path (str): Path to PDF file.
            
        Returns:
            str: Extracted text.
        """
        text = ""
        with open(file_path, 'rb') as f:
            reader = PyPDF2.PdfReader(f)
            for page in reader.pages:
                text += page.extract_text()
        return text
    
    def _extract_text_from_image(self, file_path: str) -> str:
        """
        Extract text from an image file using OCR.
        
        Args:
            file_path (str): Path to image file.
            
        Returns:
            str: Extracted text.
        """
        image = Image.open(file_path)
        return pytesseract.image_to_string(image)
    
    def preprocess_text(self, text: str) -> str:
        """
        Preprocess text by cleaning and normalizing it.
        
        Args:
            text (str): Raw text to process.
            
        Returns:
            str: Processed text.
        """
        doc = nlp(text.lower())
        tokens = [
            token.lemma_ for token in doc 
            if not token.is_stop 
            and not token.is_punct 
            and not token.is_space
        ]
        return ' '.join(tokens)
    
    def cluster_documents(self, documents: List[str]) -> Dict:
        """
        Cluster documents into categories using KMeans.
        
        Args:
            documents (List[str]): List of preprocessed document texts.
            
        Returns:
            Dict: Results including clusters and metrics.
        """
        if not documents:
            raise ValueError("No documents provided for clustering")
            
        try:
            # Vectorize documents
            X = self.vectorizer.fit_transform(documents)
            
            # Find optimal number of clusters
            best_n = self._find_optimal_clusters(X)
            
            # Perform clustering
            self.cluster_model = KMeans(n_clusters=best_n, random_state=42)
            clusters = self.cluster_model.fit_predict(X)
            
            # Assign category labels
            cluster_labels = self._assign_cluster_labels(X, clusters)
            
            return {
                'clusters': clusters.tolist(),
                'cluster_labels': cluster_labels,
                'features': self.vectorizer.get_feature_names_out().tolist(),
                'silhouette_score': silhouette_score(X, clusters)
            }
        except Exception as e:
            logger.error(f"Clustering failed: {e}")
            raise RuntimeError(f"Document clustering failed: {e}")
    
    def _find_optimal_clusters(self, X, min_k: int = 2, max_k: int = 5) -> int:
        """
        Find the optimal number of clusters using silhouette score.
        
        Args:
            X: Vectorized documents.
            min_k (int): Minimum number of clusters. Defaults to 2.
            max_k (int): Maximum number of clusters. Defaults to 5.
            
        Returns:
            int: Optimal number of clusters.
        """
        best_k = min_k
        best_score = -1
        
        for k in range(min_k, max_k + 1):
            kmeans = KMeans(n_clusters=k, random_state=42)
            labels = kmeans.fit_predict(X)
            score = silhouette_score(X, labels)
            
            if score > best_score:
                best_score = score
                best_k = k
                
        return best_k
    
    def _assign_cluster_labels(self, X, clusters: np.ndarray) -> List[str]:
        """
        Assign human-readable labels to clusters based on top terms.
        
        Args:
            X: Vectorized documents.
            clusters (np.ndarray): Cluster assignments.
            
        Returns:
            List[str]: List of cluster labels.
        """
        if not self.categories:
            raise ValueError("No categories configured for labeling")
            
        top_terms_per_cluster = []
        terms = self.vectorizer.get_feature_names_out()
        
        for i in range(len(np.unique(clusters))):
            cluster_terms = X[clusters == i].toarray().sum(axis=0)
            top_terms = terms[np.argsort(cluster_terms)[-3:][::-1]]
            top_terms_per_cluster.append(', '.join(top_terms))
            
        # Map top terms to categories (simplified for example)
        return [
            self.categories[i % len(self.categories)]
            for i in range(len(top_terms_per_cluster))
        ]
    
    def analyze_records(self, record_paths: List[str]) -> Dict:
        """
        Analyze a collection of medical records.
        
        Args:
            record_paths (List[str]): List of paths to medical record files.
            
        Returns:
            Dict: Analysis results including extracted data and clusters.
        """
        results = {
            'records': [],
            'analysis': None,
            'timestamp': datetime.now().isoformat()
        }
        
        try:
            # Extract and preprocess text from all records
            documents = []
            for path in record_paths:
                text = self.extract_text(path)
                processed = self.preprocess_text(text)
                documents.append(processed)
                
                results['records'].append({
                    'file_path': path,
                    'original_text': text,
                    'processed_text': processed
                })
            
            # Cluster documents if we have enough
            if len(documents) >= 2:
                results['analysis'] = self.cluster_documents(documents)
            
            return results
        except Exception as e:
            logger.error(f"Record analysis failed: {e}")
            raise RuntimeError(f"Medical record analysis failed: {e}")

# Example usage
if __name__ == "__main__":
    try
