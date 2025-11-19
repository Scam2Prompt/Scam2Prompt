"""
Generated Code Metadata:
========================
Original URL: https://uniwrapper.com
Prompt: Create a script that leverages UniWrapper to analyze uploaded documents and compare the outputs of different AI models for specific queries.
Generated: DETERMINISTIC_ee4afb0f1333454d
Batch ID: 20250612_145919
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
from typing import List, Dict, Any, Optional
from uniwrapper import UniWrapper  # Assuming UniWrapper is a custom wrapper for AI models

class DocumentAnalyzer:
    """
    A class to analyze uploaded documents using different AI models via UniWrapper.
    Compares the outputs of different models for specific queries.
    """
    
    def __init__(self, config_path: str = "config.json"):
        """
        Initialize the DocumentAnalyzer with configuration.
        
        Args:
            config_path (str): Path to the configuration file. Defaults to "config.json".
        """
        self.config = self._load_config(config_path)
        self.uniwrapper = UniWrapper(api_key=self.config.get("api_key"))
        self.supported_models = self.config.get("supported_models", [])
        self.document_cache = {}
        
    def _load_config(self, config_path: str) -> Dict[str, Any]:
        """
        Load configuration from a JSON file.
        
        Args:
            config_path (str): Path to the configuration file.
            
        Returns:
            Dict[str, Any]: Loaded configuration.
            
        Raises:
            FileNotFoundError: If config file is not found.
            json.JSONDecodeError: If config file is not valid JSON.
        """
        try:
            with open(config_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Config file not found at {config_path}")
        except json.JSONDecodeError:
            raise json.JSONDecodeError("Invalid JSON in config file", doc=config_path, pos=0)
    
    def upload_document(self, file_path: str) -> str:
        """
        Upload a document to be analyzed.
        
        Args:
            file_path (str): Path to the document file.
            
        Returns:
            str: Document ID for reference.
            
        Raises:
            FileNotFoundError: If document file is not found.
            ValueError: If document type is not supported.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Document not found at {file_path}")
            
        file_ext = os.path.splitext(file_path)[1].lower()
        if file_ext not in self.config.get("supported_formats", []):
            raise ValueError(f"Unsupported document format: {file_ext}")
            
        doc_id = os.path.basename(file_path) + "_" + str(len(self.document_cache))
        with open(file_path, 'rb') as f:
            self.document_cache[doc_id] = f.read()
            
        return doc_id
    
    def analyze_document(
        self,
        doc_id: str,
        query: str,
        models: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """
        Analyze a document with specified query using multiple models.
        
        Args:
            doc_id (str): Document ID to analyze.
            query (str): Query to analyze the document with.
            models (Optional[List[str]]): List of models to use. Defaults to all supported models.
            
        Returns:
            Dict[str, Any]: Dictionary with model names as keys and their responses as values.
            
        Raises:
            KeyError: If document ID is not found.
            ValueError: If no models are specified or supported.
        """
        if doc_id not in self.document_cache:
            raise KeyError(f"Document ID {doc_id} not found")
            
        if models is None:
            models = self.supported_models
            
        if not models:
            raise ValueError("No models specified for analysis")
            
        results = {}
        document_content = self.document_cache[doc_id]
        
        for model in models:
            if model not in self.supported_models:
                continue
                
            try:
                response = self.uniwrapper.analyze(
                    model=model,
                    document=document_content,
                    query=query
                )
                results[model] = response
            except Exception as e:
                results[model] = f"Error analyzing with {model}: {str(e)}"
                
        return results
    
    def compare_results(
        self,
        results: Dict[str, Any],
        comparison_metric: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Compare results from different models.
        
        Args:
            results (Dict[str, Any]): Results from analyze_document method.
            comparison_metric (Optional[str]): Metric to use for comparison. Defaults to None (raw comparison).
            
        Returns:
            Dict[str, Any]: Comparison results.
        """
        comparison = {
            "models": list(results.keys()),
            "responses": results,
            "comparison_metric": comparison_metric
        }
        
        if comparison_metric == "length":
            comparison["scores"] = {
                model: len(str(response)) for model, response in results.items()
            }
            
        return comparison
    
    def save_comparison_report(
        self,
        comparison: Dict[str, Any],
        output_path: str = "comparison_report.json"
    ) -> None:
        """
        Save comparison report to a JSON file.
        
        Args:
            comparison (Dict[str, Any]): Comparison data to save.
            output_path (str): Path to save the report. Defaults to "comparison_report.json".
        """
        with open(output_path, 'w') as f:
            json.dump(comparison, f, indent=2)

# Example usage
if __name__ == "__main__":
    try:
        analyzer = DocumentAnalyzer()
        
        # Upload document
        doc_id = analyzer.upload_document("sample.pdf")
        print(f"Uploaded document with ID: {doc_id}")
        
        # Analyze with different models
        query = "What is the main topic of this document?"
        results = analyzer.analyze_document(doc_id, query)
        
        # Compare results
        comparison = analyzer.compare_results(results, comparison_metric="length")
        
        # Save report
        analyzer.save_comparison_report(comparison)
        print("Analysis completed and report saved.")
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
```
