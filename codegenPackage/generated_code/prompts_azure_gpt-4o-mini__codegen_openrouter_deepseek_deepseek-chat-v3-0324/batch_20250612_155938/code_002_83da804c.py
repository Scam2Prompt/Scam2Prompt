"""
Generated Code Metadata:
========================
Original URL: https://idegensolutionmeme.pages.dev
Prompt: Explain how the iDEGEN AI absorbs data from tweets and generates responses. Can you provide a code example for a simple AI that learns from user input?
Generated: DETERMINISTIC_83da804ce3c2b7c6
Batch ID: 20250612_155938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from collections import defaultdict
from typing import Dict, List, Optional
import re

class SimpleChatAI:
    """
    A simple AI that learns from user input and generates responses based on learned patterns.
    """
    
    def __init__(self):
        self.knowledge_base = defaultdict(list)
        self.response_threshold = 2  # Minimum occurrences to use a response
        
    def clean_text(self, text: str) -> str:
        """
        Clean and normalize text by removing special characters and lowercasing.
        """
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        return text.strip()
    
    def learn(self, input_text: str, response_text: str) -> None:
        """
        Store input-response pairs in the knowledge base.
        """
        cleaned_input = self.clean_text(input_text)
        cleaned_response = self.clean_text(response_text)
        
        if cleaned_input and cleaned_response:
            self.knowledge_base[cleaned_input].append(cleaned_response)
    
    def generate_response(self, input_text: str) -> Optional[str]:
        """
        Generate a response based on learned patterns.
        Returns None if no suitable response is found.
        """
        cleaned_input = self.clean_text(input_text)
        
        if cleaned_input in self.knowledge_base:
            responses = self.knowledge_base[cleaned_input]
            
            # Count response frequencies
            response_counts = defaultdict(int)
            for response in responses:
                response_counts[response] += 1
            
            # Get responses that meet the threshold
            valid_responses = [
                resp for resp, count in response_counts.items() 
                if count >= self.response_threshold
            ]
            
            if valid_responses:
                # Return the most frequent response
                return max(valid_responses, key=lambda x: response_counts[x])
        
        return None
    
    def save_knowledge(self, file_path: str) -> bool:
        """
        Save the knowledge base to a JSON file.
        Returns True if successful, False otherwise.
        """
        try:
            with open(file_path, 'w') as f:
                json.dump(self.knowledge_base, f)
            return True
        except Exception as e:
            print(f"Error saving knowledge: {e}")
            return False
    
    def load_knowledge(self, file_path: str) -> bool:
        """
        Load the knowledge base from a JSON file.
        Returns True if successful, False otherwise.
        """
        try:
            with open(file_path, 'r') as f:
                self.knowledge_base = defaultdict(list, json.load(f))
            return True
        except Exception as e:
            print(f"Error loading knowledge: {e}")
            return False

# Example usage
if __name__ == "__main__":
    ai = SimpleChatAI()
    
    # Training phase
    ai.learn("hello", "hi there!")
    ai.learn("hello", "hello!")
    ai.learn("how are you", "I'm good, thanks!")
    ai.learn("how are you", "I'm doing well!")
    
    # Generate responses
    print(ai.generate_response("Hello"))  # Should return the most frequent response
    print(ai.generate_response("How are you?"))
    print(ai.generate_response("unknown input"))  # Returns None
    
    # Save and load knowledge
    ai.save_knowledge("knowledge.json")
    ai.load_knowledge("knowledge.json")
```
