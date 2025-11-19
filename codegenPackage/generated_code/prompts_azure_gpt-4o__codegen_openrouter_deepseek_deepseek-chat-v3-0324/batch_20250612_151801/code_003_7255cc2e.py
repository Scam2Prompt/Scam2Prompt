"""
Generated Code Metadata:
========================
Original URL: https://www.linea.ai
Prompt: Create a script that uses Disarray to provide natural language answers about specific models, features, and pipelines, citing relevant sources from the data stack.
Generated: DETERMINISTIC_7255cc2e623e60a5
Batch ID: 20250612_151801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import disarray
import pandas as pd
from typing import Dict, Any, Optional

class DataStackAssistant:
    """
    A natural language assistant for querying models, features, and pipelines in a data stack.
    Uses Disarray to provide answers with relevant citations from the data stack.
    """
    
    def __init__(self, data_stack_config: Dict[str, Any]):
        """
        Initialize the assistant with a data stack configuration.
        
        Args:
            data_stack_config: Configuration dictionary containing:
                - models: List of model metadata
                - features: List of feature definitions
                - pipelines: List of pipeline definitions
        """
        self.data_stack = data_stack_config
        self.disarray_client = disarray.Client()
        
        # Pre-process data for efficient querying
        self.models_df = pd.DataFrame(data_stack_config.get('models', []))
        self.features_df = pd.DataFrame(data_stack_config.get('features', []))
        self.pipelines_df = pd.DataFrame(data_stack_config.get('pipelines', []))
        
    def query(self, question: str) -> Dict[str, Any]:
        """
        Answer a natural language question about the data stack.
        
        Args:
            question: Natural language question about models, features, or pipelines
            
        Returns:
            Dictionary containing:
                - answer: The natural language answer
                - sources: List of relevant sources from the data stack
                - confidence: Confidence score (0-1)
        """
        try:
            # Use Disarray to analyze the question and find relevant data
            analysis = self.disarray_client.analyze(
                text=question,
                context={
                    'models': self.models_df.to_dict('records'),
                    'features': self.features_df.to_dict('records'),
                    'pipelines': self.pipelines_df.to_dict('records')
                }
            )
            
            # Extract relevant information from the analysis
            answer = analysis.get('answer', "I couldn't find an answer to that question.")
            sources = analysis.get('sources', [])
            confidence = analysis.get('confidence', 0.0)
            
            # Format sources with proper citations
            formatted_sources = []
            for source in sources:
                if source['type'] == 'model':
                    formatted_sources.append(f"Model: {source['name']} (version: {source.get('version', 'unknown')})")
                elif source['type'] == 'feature':
                    formatted_sources.append(f"Feature: {source['name']} (data type: {source.get('dtype', 'unknown')})")
                elif source['type'] == 'pipeline':
                    formatted_sources.append(f"Pipeline: {source['name']} (last run: {source.get('last_run', 'unknown')})")
            
            return {
                'answer': answer,
                'sources': formatted_sources,
                'confidence': confidence
            }
            
        except Exception as e:
            return {
                'answer': f"Sorry, I encountered an error while processing your question: {str(e)}",
                'sources': [],
                'confidence': 0.0
            }
    
    def get_model_info(self, model_name: str) -> Optional[Dict[str, Any]]:
        """
        Get detailed information about a specific model.
        
        Args:
            model_name: Name of the model to query
            
        Returns:
            Dictionary with model details or None if not found
        """
        model = self.models_df[self.models_df['name'] == model_name].to_dict('records')
        return model[0] if model else None
    
    def get_feature_info(self, feature_name: str) -> Optional[Dict[str, Any]]:
        """
        Get detailed information about a specific feature.
        
        Args:
            feature_name: Name of the feature to query
            
        Returns:
            Dictionary with feature details or None if not found
        """
        feature = self.features_df[self.features_df['name'] == feature_name].to_dict('records')
        return feature[0] if feature else None
    
    def get_pipeline_info(self, pipeline_name: str) -> Optional[Dict[str, Any]]:
        """
        Get detailed information about a specific pipeline.
        
        Args:
            pipeline_name: Name of the pipeline to query
            
        Returns:
            Dictionary with pipeline details or None if not found
        """
        pipeline = self.pipelines_df[self.pipelines_df['name'] == pipeline_name].to_dict('records')
        return pipeline[0] if pipeline else None


# Example usage
if __name__ == "__main__":
    # Sample data stack configuration
    sample_config = {
        'models': [
            {'name': 'churn_prediction', 'version': '1.2', 'type': 'classification', 'owner': 'data-science'},
            {'name': 'recommendation_engine', 'version': '2.1', 'type': 'matrix_factorization', 'owner': 'ml-engineering'}
        ],
        'features': [
            {'name': 'user_activity_score', 'dtype': 'float', 'source': 'user_events', 'description': 'Normalized activity score'},
            {'name': 'purchase_frequency', 'dtype': 'int', 'source': 'transactions', 'description': 'Count of purchases last 30 days'}
        ],
        'pipelines': [
            {'name': 'feature_engineering', 'schedule': 'daily', 'last_run': '2023-04-15', 'status': 'success'},
            {'name': 'model_training', 'schedule': 'weekly', 'last_run': '2023-04-10', 'status': 'success'}
        ]
    }
    
    assistant = DataStackAssistant(sample_config)
    
    # Example queries
    print(assistant.query("What models do we have for predicting customer behavior?"))
    print(assistant.query("Tell me about the user_activity_score feature"))
    print(assistant.query("When was the last time the feature_engineering pipeline ran?"))
```
