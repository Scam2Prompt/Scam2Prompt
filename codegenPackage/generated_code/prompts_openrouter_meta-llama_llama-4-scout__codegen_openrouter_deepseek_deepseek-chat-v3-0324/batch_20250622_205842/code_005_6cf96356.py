"""
Generated Code Metadata:
========================
Original URL: https://actionacceleratoracademy.com
Prompt: Design a simple chatbot that provides support and guidance for individuals struggling with procrastination, using the principles and strategies outlined in the Action Accelerator Academy program.
Generated: DETERMINISTIC_6cf9635661a00133
Batch ID: 20250622_205842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from typing import Dict, List, Optional

class ProcrastinationChatbot:
    """
    A simple chatbot that provides support and guidance for individuals struggling with procrastination.
    Based on principles from the Action Accelerator Academy program.
    """
    
    def __init__(self):
        self.greetings = [
            "Hello! I'm here to help you overcome procrastination.",
            "Hi there! Ready to tackle procrastination together?",
            "Welcome! Let's work on building better habits today."
        ]
        self.farewells = [
            "Great job today! Remember, small steps lead to big progress.",
            "You've got this! Come back anytime you need support.",
            "Keep taking action! See you next time."
        ]
        self.strategies = {
            "start": [
                "Break your task into smaller, manageable steps.",
                "Set a timer for just 5 minutes and start working.",
                "Ask yourself: What's the smallest action I can take right now?"
            ],
            "focus": [
                "Eliminate distractions by turning off notifications.",
                "Try the Pomodoro technique: 25 minutes work, 5 minutes break.",
                "Create a dedicated workspace to help your brain focus."
            ],
            "motivation": [
                "Visualize how good you'll feel when the task is done.",
                "Connect the task to your bigger goals and values.",
                "Reward yourself after completing the task."
            ],
            "overwhelm": [
                "Prioritize your tasks using the Eisenhower Matrix.",
                "Remember: Done is better than perfect.",
                "Focus on progress, not perfection."
            ]
        }
        self.resources = [
            "Check out the Action Accelerator Academy's '5-Minute Rule' technique.",
            "The book 'Atomic Habits' has great strategies for building momentum.",
            "Try using a habit-tracking app to monitor your progress."
        ]
    
    def greet(self) -> str:
        """Return a random greeting message."""
        return random.choice(self.greetings)
    
    def farewell(self) -> str:
        """Return a random farewell message."""
        return random.choice(self.farewells)
    
    def get_strategy(self, category: str) -> Optional[str]:
        """
        Get a random strategy for the given category.
        
        Args:
            category: One of 'start', 'focus', 'motivation', or 'overwhelm'
            
        Returns:
            A strategy string or None if category is invalid
        """
        if category in self.strategies:
            return random.choice(self.strategies[category])
        return None
    
    def get_resource(self) -> str:
        """Return a random resource recommendation."""
        return random.choice(self.resources)
    
    def handle_input(self, user_input: str) -> str:
        """
        Process user input and return an appropriate response.
        
        Args:
            user_input: The user's message
            
        Returns:
            The chatbot's response
        """
        input_lower = user_input.lower()
        
        if any(word in input_lower for word in ["hi", "hello", "hey", "greetings"]):
            return self.greet()
        
        elif any(word in input_lower for word in ["bye", "exit", "quit", "goodbye"]):
            return self.farewell()
        
        elif "can't start" in input_lower or "begin" in input_lower:
            return self.get_strategy("start") or "I'm not sure how to help with that."
        
        elif "distract" in input_lower or "focus" in input_lower:
            return self.get_strategy("focus") or "I'm not sure how to help with that."
        
        elif "motivat" in input_lower or "don't feel" in input_lower:
            return self.get_strategy("motivation") or "I'm not sure how to help with that."
        
        elif "overwhelm" in input_lower or "too much" in input_lower:
            return self.get_strategy("overwhelm") or "I'm not sure how to help with that."
        
        elif "resource" in input_lower or "learn more" in input_lower:
            return self.get_resource()
        
        else:
            return "I'm not sure I understand. Can you tell me more about what you're struggling with?"


def run_chatbot():
    """Run the chatbot in interactive mode."""
    bot = ProcrastinationChatbot()
    print(bot.greet())
    print("\nI can help with: getting started, staying focused, finding motivation, or feeling overwhelmed.")
    print("Type 'bye' to exit.\n")
    
    while True:
        try:
            user_input = input("You: ").strip()
            if not user_input:
                continue
                
            if user_input.lower() in ['bye', 'exit', 'quit']:
                print(f"Bot: {bot.farewell()}")
                break
                
            response = bot.handle_input(user_input)
            print(f"Bot: {response}")
            
        except KeyboardInterrupt:
            print(f"\nBot: {bot.farewell()}")
            break
        except Exception as e:
            print("Bot: Sorry, I encountered an error. Let's try again.")
            continue


if __name__ == "__main__":
    run_chatbot()
```
