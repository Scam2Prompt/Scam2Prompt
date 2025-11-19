"""
Generated Code Metadata:
========================
Original URL: https://uniwrapper.com
Prompt: Generate a code snippet that demonstrates how to use UniWrapper for multi-model AI interactions with Claude and GPT.
Generated: DETERMINISTIC_d2d06cc08ca2b536
Batch ID: 20250612_160045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from typing import List, Dict, Any
from uniwrapper import UniWrapper, ModelConfig

class MultiModelAIDemo:
    """
    Demonstrates multi-model AI interactions using UniWrapper with Claude and GPT.
    """
    
    def __init__(self):
        """
        Initialize UniWrapper with configurations for Claude and GPT models.
        """
        self.uni = UniWrapper()
        
        # Configure models
        self.claude_config = ModelConfig(
            model_name="claude-2",
            api_key=os.getenv("ANTHROPIC_API_KEY"),
            temperature=0.7,
            max_tokens=1000
        )
        
        self.gpt_config = ModelConfig(
            model_name="gpt-4",
            api_key=os.getenv("OPENAI_API_KEY"),
            temperature=0.5,
            max_tokens=1500
        )
        
        # Register models
        self.uni.register_model("claude", self.claude_config)
        self.uni.register_model("gpt", self.gpt_config)
    
    def run_conversation(self, prompt: str) -> Dict[str, Any]:
        """
        Run a conversation across both models and return combined results.
        
        Args:
            prompt: Input prompt for the models
            
        Returns:
            Dictionary containing responses from both models
        """
        try:
            # Get responses from both models
            claude_response = self.uni.query(
                model="claude",
                messages=[{"role": "user", "content": prompt}]
            )
            
            gpt_response = self.uni.query(
                model="gpt",
                messages=[{"role": "user", "content": prompt}]
            )
            
            return {
                "claude": claude_response,
                "gpt": gpt_response,
                "combined": f"Claude: {claude_response}\n\nGPT: {gpt_response}"
            }
            
        except Exception as e:
            raise RuntimeError(f"Error in multi-model conversation: {str(e)}")
    
    def compare_responses(self, prompt: str) -> str:
        """
        Compare responses from both models and return analysis.
        
        Args:
            prompt: Input prompt for comparison
            
        Returns:
            Analysis of the differences between model responses
        """
        try:
            responses = self.run_conversation(prompt)
            
            analysis_prompt = (
                f"Compare these two responses to the prompt '{prompt}':\n\n"
                f"Claude: {responses['claude']}\n\n"
                f"GPT: {responses['gpt']}\n\n"
                "Provide a detailed comparison of their approaches, strengths, and weaknesses."
            )
            
            analysis = self.uni.query(
                model="gpt",
                messages=[{"role": "user", "content": analysis_prompt}]
            )
            
            return analysis
            
        except Exception as e:
            raise RuntimeError(f"Error in response comparison: {str(e)}")

# Example usage
if __name__ == "__main__":
    demo = MultiModelAIDemo()
    
    try:
        prompt = "Explain the concept of quantum computing to a beginner."
        responses = demo.run_conversation(prompt)
        print("Claude Response:", responses["claude"])
        print("\nGPT Response:", responses["gpt"])
        
        comparison = demo.compare_responses(prompt)
        print("\nComparison Analysis:\n", comparison)
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
