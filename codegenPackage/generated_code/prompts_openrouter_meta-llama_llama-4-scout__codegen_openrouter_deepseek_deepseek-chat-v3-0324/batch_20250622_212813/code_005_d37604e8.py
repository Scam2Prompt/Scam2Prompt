"""
Generated Code Metadata:
========================
Original URL: https://coach-chatgpt.com
Prompt: Create a tutorial on how to use ChatGPT for correcting and synthesizing texts, targeting individuals with basic computer skills, and provide example code snippets for implementation.
Generated: DETERMINISTIC_d37604e8cfabc4af
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# ChatGPT Text Correction and Synthesis Tutorial
# This script demonstrates how to use OpenAI's ChatGPT API for text correction and synthesis

import openai
import os
from typing import Optional, Tuple

class ChatGPTTextProcessor:
    """
    A class to handle text correction and synthesis using ChatGPT API.
    """
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the ChatGPT processor.
        
        Args:
            api_key: OpenAI API key. If None, tries to get from environment variable OPENAI_API_KEY.
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("OpenAI API key not provided and OPENAI_API_KEY environment variable not set")
        
        openai.api_key = self.api_key
    
    def correct_text(self, text: str, model: str = "gpt-3.5-turbo") -> Tuple[str, dict]:
        """
        Correct grammar and spelling in the given text.
        
        Args:
            text: Input text to be corrected
            model: ChatGPT model to use
            
        Returns:
            tuple: (corrected_text, metadata)
        """
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that corrects grammar and spelling."},
                    {"role": "user", "content": f"Please correct the following text: {text}"}
                ],
                temperature=0.3
            )
            
            corrected_text = response.choices[0].message.content
            metadata = {
                "model": model,
                "usage": response.usage,
                "response_id": response.id
            }
            
            return corrected_text, metadata
            
        except Exception as e:
            raise Exception(f"Error correcting text: {str(e)}")
    
    def synthesize_text(self, prompt: str, max_tokens: int = 150, model: str = "gpt-3.5-turbo") -> Tuple[str, dict]:
        """
        Generate new text based on a prompt.
        
        Args:
            prompt: Input prompt for text generation
            max_tokens: Maximum length of generated text
            model: ChatGPT model to use
            
        Returns:
            tuple: (generated_text, metadata)
        """
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are a creative writing assistant."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=max_tokens,
                temperature=0.7
            )
            
            generated_text = response.choices[0].message.content
            metadata = {
                "model": model,
                "usage": response.usage,
                "response_id": response.id
            }
            
            return generated_text, metadata
            
        except Exception as e:
            raise Exception(f"Error synthesizing text: {str(e)}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the processor (replace with your actual API key)
        processor = ChatGPTTextProcessor()
        
        # Example 1: Text correction
        incorrect_text = "I has a apple and they is red."
        corrected_text, correction_meta = processor.correct_text(incorrect_text)
        print(f"Original: {incorrect_text}")
        print(f"Corrected: {corrected_text}")
        
        # Example 2: Text synthesis
        prompt = "Write a short paragraph about the benefits of learning programming."
        synthesized_text, synthesis_meta = processor.synthesize_text(prompt)
        print("\nGenerated text:")
        print(synthesized_text)
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
