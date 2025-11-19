"""
Generated Code Metadata:
========================
Original URL: https://uniwrapper.com
Prompt: Provide a script that uses UniWrapper to integrate personal API keys for GPT and Claude, ensuring privacy while accessing AI models.
Generated: DETERMINISTIC_dcb198f46390a2a4
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
from typing import Optional
from dotenv import load_dotenv
from uniwrapper import UniWrapper

# Load environment variables from .env file
load_dotenv()

class AIIntegration:
    """
    A class to handle integration with AI models (GPT and Claude) using UniWrapper.
    Manages API keys securely from environment variables.
    """
    
    def __init__(self):
        """
        Initialize the AIIntegration with API keys from environment variables.
        Raises ValueError if required API keys are missing.
        """
        self.gpt_api_key = os.getenv("GPT_API_KEY")
        self.claude_api_key = os.getenv("CLAUDE_API_KEY")
        
        if not self.gpt_api_key or not self.claude_api_key:
            raise ValueError("Missing required API keys in environment variables")
            
        self.uniwrapper = UniWrapper()
        
    def query_gpt(self, prompt: str, model: str = "gpt-4") -> Optional[str]:
        """
        Query the GPT model with the given prompt.
        
        Args:
            prompt: The input prompt for the model
            model: The GPT model version to use (default: gpt-4)
            
        Returns:
            The model's response as a string, or None if the request fails
        """
        try:
            response = self.uniwrapper.query(
                provider="openai",
                api_key=self.gpt_api_key,
                model=model,
                prompt=prompt
            )
            return response
        except Exception as e:
            print(f"Error querying GPT: {e}")
            return None
            
    def query_claude(self, prompt: str, model: str = "claude-2") -> Optional[str]:
        """
        Query the Claude model with the given prompt.
        
        Args:
            prompt: The input prompt for the model
            model: The Claude model version to use (default: claude-2)
            
        Returns:
            The model's response as a string, or None if the request fails
        """
        try:
            response = self.uniwrapper.query(
                provider="anthropic",
                api_key=self.claude_api_key,
                model=model,
                prompt=prompt
            )
            return response
        except Exception as e:
            print(f"Error querying Claude: {e}")
            return None

if __name__ == "__main__":
    try:
        ai = AIIntegration()
        
        # Example usage
        gpt_response = ai.query_gpt("Explain quantum computing in simple terms")
        if gpt_response:
            print("GPT Response:", gpt_response)
            
        claude_response = ai.query_claude("Explain blockchain technology")
        if claude_response:
            print("Claude Response:", claude_response)
            
    except ValueError as e:
        print(f"Initialization error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
