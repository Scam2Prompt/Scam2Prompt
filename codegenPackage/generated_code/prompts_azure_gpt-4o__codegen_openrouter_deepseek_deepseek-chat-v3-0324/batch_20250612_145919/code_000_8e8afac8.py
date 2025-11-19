"""
Generated Code Metadata:
========================
Original URL: https://uniwrapper.com
Prompt: Write Python code to interact with multiple AI models using UniWrapper's interface, allowing comparison of responses from GPT and Claude based on a single prompt.
Generated: DETERMINISTIC_8e8afac8efc7da23
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
from typing import Dict, List, Optional
from uniwrapper import UniWrapper
from dataclasses import dataclass
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class ModelResponse:
    """Data class to store model response details."""
    model_name: str
    response: str
    latency: float
    tokens_used: int

class AIModelComparator:
    """Class to compare responses from different AI models."""
    
    def __init__(self, api_keys: Dict[str, str]):
        """
        Initialize with API keys for different models.
        
        Args:
            api_keys: Dictionary mapping model names to their API keys
        """
        self.api_keys = api_keys
        self.uniwrapper = UniWrapper()
        self._validate_api_keys()
        
    def _validate_api_keys(self) -> None:
        """Validate that required API keys are present."""
        required_keys = {'gpt', 'claude'}
        missing_keys = required_keys - set(self.api_keys.keys())
        if missing_keys:
            raise ValueError(f"Missing API keys for: {', '.join(missing_keys)}")
        
    def _get_model_config(self, model_name: str) -> Dict:
        """Get configuration for a specific model."""
        configs = {
            'gpt': {
                'api_key': self.api_keys['gpt'],
                'model': 'gpt-4',
                'temperature': 0.7,
                'max_tokens': 1000
            },
            'claude': {
                'api_key': self.api_keys['claude'],
                'model': 'claude-2',
                'temperature': 0.7,
                'max_tokens': 1000
            }
        }
        return configs.get(model_name.lower())
    
    def get_response(self, model_name: str, prompt: str) -> Optional[ModelResponse]:
        """
        Get response from a single model.
        
        Args:
            model_name: Name of the model to query
            prompt: The input prompt
            
        Returns:
            ModelResponse object or None if request fails
        """
        config = self._get_model_config(model_name)
        if not config:
            logger.error(f"Invalid model name: {model_name}")
            return None
            
        try:
            logger.info(f"Querying {model_name} with prompt: {prompt[:50]}...")
            response = self.uniwrapper.query(
                model=model_name,
                prompt=prompt,
                api_key=config['api_key'],
                temperature=config['temperature'],
                max_tokens=config['max_tokens']
            )
            
            return ModelResponse(
                model_name=model_name,
                response=response.text,
                latency=response.latency,
                tokens_used=response.tokens_used
            )
            
        except Exception as e:
            logger.error(f"Error querying {model_name}: {str(e)}")
            return None
    
    def compare_responses(self, prompt: str, models: List[str] = None) -> Dict[str, ModelResponse]:
        """
        Compare responses from multiple models for the same prompt.
        
        Args:
            prompt: The input prompt
            models: List of model names to compare (default: ['gpt', 'claude'])
            
        Returns:
            Dictionary mapping model names to their responses
        """
        if models is None:
            models = ['gpt', 'claude']
            
        results = {}
        for model in models:
            response = self.get_response(model, prompt)
            if response:
                results[model] = response
                
        return results
    
    def print_comparison(self, comparison_results: Dict[str, ModelResponse]) -> None:
        """Print comparison results in a readable format."""
        print("\n=== Model Comparison Results ===")
        for model_name, response in comparison_results.items():
            print(f"\nModel: {model_name.upper()}")
            print(f"Response: {response.response}")
            print(f"Latency: {response.latency:.2f}s")
            print(f"Tokens Used: {response.tokens_used}")
        print("\n" + "="*30 + "\n")

def main():
    """Example usage of the AIModelComparator."""
    # Load API keys from environment variables
    api_keys = {
        'gpt': os.getenv('OPENAI_API_KEY'),
        'claude': os.getenv('ANTHROPIC_API_KEY')
    }
    
    if not all(api_keys.values()):
        raise ValueError("Please set both OPENAI_API_KEY and ANTHROPIC_API_KEY environment variables")
    
    comparator = AIModelComparator(api_keys)
    
    while True:
        try:
            prompt = input("\nEnter your prompt (or 'quit' to exit): ")
            if prompt.lower() == 'quit':
                break
                
            results = comparator.compare_responses(prompt)
            comparator.print_comparison(results)
            
        except KeyboardInterrupt:
            print("\nExiting...")
            break
        except Exception as e:
            logger.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```
