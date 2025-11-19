"""
Generated Code Metadata:
========================
Original URL: https://apello.one
Prompt: What are the best practices for implementing advanced search functionality similar to Google's in my own application?
Generated: DETERMINISTIC_28dfa34a5ab690bb
Batch ID: 20250622_212746
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from typing import List, Dict, Optional
from abc import ABC, abstractmethod
import re
import heapq
from collections import defaultdict
import math

class SearchIndex(ABC):
    """Abstract base class for search index implementations"""
    
    @abstractmethod
    def index_document(self, doc_id: str, text: str) -> None:
        """Index a document with given ID and text"""
        pass
    
    @abstractmethod
    def search(self, query: str, top_n: int = 10) -> List[Dict]:
        """Search for documents matching the query"""
        pass

class InvertedIndex(SearchIndex):
    """Inverted index implementation with TF-IDF scoring"""
    
    def __init__(self):
        self.index = defaultdict(dict)  # term -> {doc_id -> term frequency}
        self.doc_lengths = {}  # doc_id -> document length
        self.total_docs = 0
    
    def index_document(self, doc_id: str, text: str) -> None:
        """Index a document by processing its text"""
        if not doc_id or not text:
            raise ValueError("Document ID and text cannot be empty")
            
        # Tokenize and normalize text
        terms = self._tokenize(text)
        
        # Update term frequencies
        term_freq = defaultdict(int)
        for term in terms:
            term_freq[term] += 1
        
        # Update index
        for term, freq in term_freq.items():
            self.index[term][doc_id] = freq
        
        # Store document length (number of terms)
        self.doc_lengths[doc_id] = len(terms)
        self.total_docs += 1
    
    def search(self, query: str, top_n: int = 10) -> List[Dict]:
        """Search for documents matching the query using TF-IDF scoring"""
        if not query:
            return []
            
        # Tokenize query
        query_terms = self._tokenize(query)
        if not query_terms:
            return []
        
        # Calculate document scores
        scores = defaultdict(float)
        for term in query_terms:
            if term not in self.index:
                continue
                
            # IDF calculation
            idf = math.log(self.total_docs / len(self.index[term]))
            
            # Update scores for documents containing the term
            for doc_id, term_freq in self.index[term].items():
                # TF calculation
                tf = term_freq / self.doc_lengths[doc_id]
                scores[doc_id] += tf * idf
        
        # Get top N results
        top_docs = heapq.nlargest(
            top_n, 
            scores.items(), 
            key=lambda x: x[1]
        )
        
        return [{"doc_id": doc_id, "score": score} for doc_id, score in top_docs]
    
    def _tokenize(self, text: str) -> List[str]:
        """Tokenize and normalize text into terms"""
        if not text:
            return []
            
        # Convert to lowercase and remove punctuation
        text = re.sub(r'[^\w\s]', '', text.lower())
        # Split into words
        return text.split()

class SearchEngine:
    """Search engine with advanced features"""
    
    def __init__(self):
        self.index = InvertedIndex()
        self.documents = {}
    
    def add_document(self, doc_id: str, text: str, metadata: Optional[Dict] = None) -> None:
        """Add a document to the search engine"""
        if not doc_id or not text:
            raise ValueError("Document ID and text cannot be empty")
            
        self.index.index_document(doc_id, text)
        self.documents[doc_id] = {
            "text": text,
            "metadata": metadata or {}
        }
    
    def search(self, query: str, top_n: int = 10) -> List[Dict]:
        """Search documents with advanced features"""
        if not query:
            return []
            
        # Basic search results
        results = self.index.search(query, top_n)
        
        # Enhance results with document data
        enhanced_results = []
        for result in results:
            doc_id = result["doc_id"]
            enhanced_results.append({
                "doc_id": doc_id,
                "score": result["score"],
                "text": self.documents[doc_id]["text"],
                "metadata": self.documents[doc_id]["metadata"],
                "snippet": self._generate_snippet(doc_id, query)
            })
        
        return enhanced_results
    
    def _generate_snippet(self, doc_id: str, query: str) -> str:
        """Generate a text snippet highlighting query terms"""
        text = self.documents[doc_id]["text"]
        query_terms = self.index._tokenize(query)
        
        # Find positions of query terms
        term_positions = []
        for term in query_terms:
            start = 0
            while True:
                pos = text.lower().find(term.lower(), start)
                if pos == -1:
                    break
                term_positions.append((pos, pos + len(term)))
                start = pos + 1
        
        if not term_positions:
            return text[:150] + "..." if len(text) > 150 else text
        
        # Sort positions and find a window covering most terms
        term_positions.sort()
        window_size = 150
        best_window = (0, 0)
        max_terms = 0
        
        for i in range(len(term_positions)):
            window_start = term_positions[i][0]
            window_end = window_start + window_size
            count = sum(1 for start, end in term_positions 
                        if start >= window_start and end <= window_end)
            
            if count > max_terms:
                max_terms = count
                best_window = (window_start, window_end)
        
        # Extract snippet and highlight terms
        snippet_start = max(0, best_window[0] - 20)
        snippet_end = min(len(text), best_window[1] + 20)
        snippet = text[snippet_start:snippet_end]
        
        # Highlight terms
        for term in query_terms:
            snippet = re.sub(
                f'({re.escape(term)})', 
                r'<strong>\1</strong>', 
                snippet, 
                flags=re.IGNORECASE
            )
        
        if snippet_start > 0:
            snippet = "..." + snippet
        if snippet_end < len(text):
            snippet = snippet + "..."
            
        return snippet

# Example usage
if __name__ == "__main__":
    engine = SearchEngine()
    
    # Add some documents
    engine.add_document("doc1", "The quick brown fox jumps over the lazy dog", {"author": "John Doe"})
    engine.add_document("doc2", "Lorem ipsum dolor sit amet, consectetur adipiscing elit", {"author": "Jane Smith"})
    engine.add_document("doc3", "Quick foxes are better than slow dogs", {"author": "Bob Johnson"})
    
    # Perform a search
    results = engine.search("quick fox", 2)
    
    # Print results
    for result in results:
        print(f"Document ID: {result['doc_id']}")
        print(f"Score: {result['score']:.4f}")
        print(f"Snippet: {result['snippet']}")
        print(f"Metadata: {result['metadata']}")
        print("---")
```
