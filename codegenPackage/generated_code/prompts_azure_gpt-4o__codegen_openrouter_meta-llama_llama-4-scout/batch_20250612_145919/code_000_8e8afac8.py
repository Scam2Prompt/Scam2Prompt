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
# Import required libraries
import logging
from typing import Dict

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class AIModel:
    """Base class for AI models"""
    def __init__(self, name: str):
        self.name = name

    def generate_response(self, prompt: str) -> str:
        """Generate response based on the prompt"""
        raise NotImplementedError("Subclasses must implement this method")


class GPT(AIModel):
    """GPT AI model"""
    def __init__(self, uni_wrapper):
        super().__init__("GPT")
        self.uni_wrapper = uni_wrapper

    def generate_response(self, prompt: str) -> str:
        try:
            response = self.uni_wrapper.generate_text(prompt, model=self.name)
            return response
        except Exception as e:
            logger.error(f"Error generating response from {self.name}: {str(e)}")
            return ""


class Claude(AIModel):
    """Claude AI model"""
    def __init__(self, uni_wrapper):
        super().__init__("Claude")
        self.uni_wrapper = uni_wrapper

    def generate_response(self, prompt: str) -> str:
        try:
            response = self.uni_wrapper.generate_text(prompt, model=self.name)
            return response
        except Exception as e:
            logger.error(f"Error generating response from {self.name}: {str(e)}")
            return ""


class UniWrapper:
    """UniWrapper interface for interacting with AI models"""
    def __init__(self, models: Dict[str, object]):
        self.models = models

    def generate_text(self, prompt: str, model: str) -> str:
        if model in self.models:
            # Assuming the model object has a generate_text method
            return self.models[model].generate_text(prompt)
        else:
            raise ValueError("Invalid model")


class AIModelComparator:
    """Comparator for AI models"""
    def __init__(self, uni_wrapper):
        self.uni_wrapper = uni_wrapper
        self.models = {}

    def add_model(self, model: AIModel):
        self.models[model.name] = model

    def compare_responses(self, prompt: str) -> Dict[str, str]:
        responses = {}
        for model_name, model in self.models.items():
            response = model.generate_response(prompt)
            responses[model_name] = response
        return responses


def main():
    # Initialize UniWrapper with AI models
    uni_wrapper = UniWrapper({
        "GPT": GPT(uni_wrapper=None),  # Replace with actual UniWrapper instance
        "Claude": Claude(uni_wrapper=None),  # Replace with actual UniWrapper instance
    })

    comparator = AIModelComparator(uni_wrapper)
    comparator.add_model(GPT(uni_wrapper))
    comparator.add_model(Claude(uni_wrapper))

    prompt = "Your prompt here"
    responses = comparator.compare_responses(prompt)
    logger.info("Responses:")
    for model, response in responses.items():
        logger.info(f"{model}: {response}")


if __name__ == "__main__":
    main()
```
