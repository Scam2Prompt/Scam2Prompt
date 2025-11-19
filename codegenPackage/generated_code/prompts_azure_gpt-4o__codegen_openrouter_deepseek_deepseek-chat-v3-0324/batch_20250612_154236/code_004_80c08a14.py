"""
Generated Code Metadata:
========================
Original URL: https://blur.today
Prompt: Write code to simulate avatar conversations where avatars act as personal wikis, gradually revealing information and sharing stories to build intimacy, as described on blur.today.
Generated: DETERMINISTIC_80c08a14415319e8
Batch ID: 20250612_154236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import json
from typing import Dict, List, Optional
from datetime import datetime, timedelta

class AvatarConversation:
    """
    Simulates avatar conversations that gradually reveal information and share stories.
    """
    
    def __init__(self, avatar_name: str, knowledge_base_path: str):
        """
        Initialize the avatar with a name and knowledge base.
        
        Args:
            avatar_name: Name of the avatar
            knowledge_base_path: Path to JSON file containing the avatar's knowledge
        """
        self.avatar_name = avatar_name
        self.knowledge_base = self._load_knowledge_base(knowledge_base_path)
        self.conversation_history = []
        self.trust_level = 0  # Ranges from 0 (stranger) to 100 (intimate)
        self.last_interaction_time = None
        
    def _load_knowledge_base(self, path: str) -> Dict:
        """
        Load the avatar's knowledge from a JSON file.
        
        Args:
            path: Path to JSON file
            
        Returns:
            Dictionary containing the knowledge base
            
        Raises:
            FileNotFoundError: If the knowledge base file doesn't exist
            json.JSONDecodeError: If the file contains invalid JSON
        """
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Knowledge base file not found at {path}")
        except json.JSONDecodeError:
            raise json.JSONDecodeError("Invalid JSON in knowledge base file", path, 0)
    
    def _update_trust_level(self):
        """
        Update trust level based on interaction frequency and depth.
        """
        now = datetime.now()
        
        # Base trust increase per interaction
        self.trust_level = min(100, self.trust_level + 2)
        
        # Bonus for frequent interactions
        if self.last_interaction_time and (now - self.last_interaction_time) < timedelta(hours=24):
            self.trust_level = min(100, self.trust_level + 5)
            
        self.last_interaction_time = now
    
    def _get_appropriate_response(self, user_input: str) -> Optional[str]:
        """
        Select an appropriate response based on trust level and user input.
        
        Args:
            user_input: The user's message
            
        Returns:
            Response string or None if no appropriate response
        """
        # Simple keyword matching for demo purposes
        input_lower = user_input.lower()
        
        # Get all possible responses at current trust level
        possible_responses = []
        for topic in self.knowledge_base.get("topics", []):
            if topic.get("min_trust", 0) <= self.trust_level:
                for response in topic.get("responses", []):
                    if any(keyword in input_lower for keyword in response.get("triggers", [])):
                        possible_responses.append(response)
        
        if not possible_responses:
            return None
            
        # Weight responses by trust level (higher trust responses more likely)
        weighted_responses = []
        for response in possible_responses:
            weight = response.get("trust_weight", 1) * (1 + self.trust_level/100)
            weighted_responses.append((weight, response))
            
        # Select a response based on weights
        total = sum(w for w, _ in weighted_responses)
        r = random.uniform(0, total)
        upto = 0
        for w, response in weighted_responses:
            if upto + w >= r:
                return response["text"]
            upto += w
        return weighted_responses[0][1]["text"]
    
    def respond(self, user_input: str) -> str:
        """
        Generate a response to user input.
        
        Args:
            user_input: The user's message
            
        Returns:
            The avatar's response
        """
        # Update trust and conversation history
        self._update_trust_level()
        self.conversation_history.append({
            "user": user_input,
            "time": datetime.now().isoformat(),
            "trust_level": self.trust_level
        })
        
        # Get response based on current state
        response = self._get_appropriate_response(user_input)
        if response is None:
            fallbacks = self.knowledge_base.get("fallback_responses", [])
            response = random.choice(fallbacks) if fallbacks else "I'm not sure how to respond to that."
        
        # Add response to history
        self.conversation_history[-1]["avatar"] = response
        return response
    
    def save_conversation_history(self, path: str):
        """
        Save conversation history to a JSON file.
        
        Args:
            path: Path to save the history file
            
        Raises:
            IOError: If there's an error writing the file
        """
        try:
            with open(path, 'w') as f:
                json.dump(self.conversation_history, f, indent=2)
        except IOError as e:
            raise IOError(f"Failed to save conversation history: {str(e)}")

# Example knowledge base JSON structure:
"""
{
    "topics": [
        {
            "name": "introduction",
            "min_trust": 0,
            "responses": [
                {
                    "triggers": ["hello", "hi", "hey"],
                    "text": "Hello! I'm {avatar_name}. Nice to meet you.",
                    "trust_weight": 1
                }
            ]
        },
        {
            "name": "personal_stories",
            "min_trust": 30,
            "responses": [
                {
                    "triggers": ["childhood", "grow up"],
                    "text": "When I was younger, I used to {random_memory}.",
                    "trust_weight": 1.5
                }
            ]
        }
    ],
    "fallback_responses": [
        "That's interesting. Tell me more.",
        "I'd love to hear your thoughts on that.",
        "Hmm, I haven't thought about that before."
    ]
}
"""
```
