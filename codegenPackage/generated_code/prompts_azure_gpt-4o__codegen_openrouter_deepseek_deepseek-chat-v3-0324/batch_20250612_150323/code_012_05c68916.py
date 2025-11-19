"""
Generated Code Metadata:
========================
Original URL: https://opensea.institute
Prompt: Create a chatbot using natural language processing to assist clients in scheduling OSI-type coaching sessions and answering questions about proprietary methods.
Generated: DETERMINISTIC_05c68916fe4df0c4
Batch ID: 20250612_150323
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
import random
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens import Doc, Span
import pytz

# Load NLP model
nlp = spacy.load("en_core_web_md")

# Define coaching session types and durations
SESSION_TYPES = {
    "discovery": {"duration": 30, "description": "Introductory session to assess needs"},
    "strategy": {"duration": 60, "description": "Strategic planning session"},
    "implementation": {"duration": 90, "description": "Practical implementation guidance"},
    "followup": {"duration": 45, "description": "Progress review and adjustment"}
}

# Define proprietary methods and their descriptions
PROPRIETARY_METHODS = {
    "osi framework": "Our core methodology for organizational transformation",
    "behavioral mapping": "Technique for identifying key behavioral patterns",
    "resonance analysis": "Method for assessing organizational alignment",
    "transformation matrix": "Tool for tracking change progress"
}

# Define available time slots (in production, this would come from a calendar system)
AVAILABLE_SLOTS = [
    {"date": "2023-11-15", "times": ["09:00", "11:00", "14:00"]},
    {"date": "2023-11-16", "times": ["10:00", "13:00", "15:00"]},
    {"date": "2023-11-17", "times": ["09:30", "12:00", "16:00"]}
]

class CoachingChatbot:
    def __init__(self):
        self.nlp = nlp
        self.session_types = SESSION_TYPES
        self.methods = PROPRIETARY_METHODS
        self.available_slots = AVAILABLE_SLOTS
        self._initialize_matchers()
        self.user_context = {}
        
    def _initialize_matchers(self):
        """Initialize phrase matchers for session types and methods."""
        # Session type matcher
        self.session_matcher = PhraseMatcher(self.nlp.vocab)
        session_patterns = [self.nlp(text) for text in self.session_types.keys()]
        self.session_matcher.add("SESSION_TYPES", session_patterns)
        
        # Method matcher
        self.method_matcher = PhraseMatcher(self.nlp.vocab)
        method_patterns = [self.nlp(text) for text in self.methods.keys()]
        self.method_matcher.add("METHODS", method_patterns)
        
    def process_input(self, user_input: str) -> str:
        """Process user input and generate appropriate response."""
        try:
            doc = self.nlp(user_input.lower())
            
            # Check for greetings
            if self._is_greeting(doc):
                return self._generate_greeting_response()
                
            # Check for session scheduling
            if self._is_scheduling_request(doc):
                session_type = self._extract_session_type(doc)
                if session_type:
                    self.user_context["session_type"] = session_type
                    return self._handle_scheduling(session_type)
                return "Which type of session would you like to schedule? We offer: " + ", ".join(self.session_types.keys())
            
            # Check for method inquiries
            if self._is_method_inquiry(doc):
                method = self._extract_method(doc)
                if method:
                    return self._describe_method(method)
                return "Which method would you like to know about? We have: " + ", ".join(self.methods.keys())
            
            # Default response
            return "I can help you schedule coaching sessions or explain our proprietary methods. What would you like to do?"
            
        except Exception as e:
            return f"Sorry, I encountered an error: {str(e)}. Please try again."
    
    def _is_greeting(self, doc: Doc) -> bool:
        """Check if the input is a greeting."""
        greetings = ["hello", "hi", "hey", "greetings"]
        return any(token.text in greetings for token in doc)
    
    def _generate_greeting_response(self) -> str:
        """Generate a greeting response."""
        greetings = [
            "Hello! How can I assist you today?",
            "Hi there! What can I help you with?",
            "Greetings! How may I help you with your coaching needs?"
        ]
        return random.choice(greetings)
    
    def _is_scheduling_request(self, doc: Doc) -> bool:
        """Check if the input is about scheduling."""
        scheduling_keywords = ["schedule", "book", "appointment", "session", "meeting"]
        return any(token.text in scheduling_keywords for token in doc)
    
    def _extract_session_type(self, doc: Doc) -> Optional[str]:
        """Extract session type from user input."""
        matches = self.session_matcher(doc)
        for match_id, start, end in matches:
            span = doc[start:end]
            return span.text
        return None
    
    def _handle_scheduling(self, session_type: str) -> str:
        """Handle the scheduling process."""
        session_info = self.session_types.get(session_type)
        if not session_info:
            return "Sorry, I don't recognize that session type."
            
        response = [
            f"Great! {session_info['description']}. ",
            f"The session duration is {session_info['duration']} minutes. ",
            "Here are available time slots:"
        ]
        
        for slot in self.available_slots:
            response.append(f"\n- {slot['date']}: {', '.join(slot['times'])}")
            
        response.append("\nPlease specify your preferred date and time.")
        return "".join(response)
    
    def _is_method_inquiry(self, doc: Doc) -> bool:
        """Check if the input is about proprietary methods."""
        inquiry_keywords = ["method", "approach", "technique", "what is", "explain", "tell me about"]
        return any(token.text in inquiry_keywords for token in doc)
    
    def _extract_method(self, doc: Doc) -> Optional[str]:
        """Extract method name from user input."""
        matches = self.method_matcher(doc)
        for match_id, start, end in matches:
            span = doc[start:end]
            return span.text
        return None
    
    def _describe_method(self, method: str) -> str:
        """Provide description of a proprietary method."""
        description = self.methods.get(method)
        if description:
            return f"Our {method} is {description}."
        return f"Sorry, I don't have information about {method}."
    
    def confirm_booking(self, date: str, time: str) -> str:
        """Confirm a booking with the provided date and time."""
        try:
            # In a real implementation, this would interface with a calendar system
            datetime.strptime(date, "%Y-%m-%d")
            datetime.strptime(time, "%H:%M")
            
            session_type = self.user_context.get("session_type", "coaching")
            duration = self.session_types.get(session_type, {}).get("duration", 60)
            
            return (
                f"Your {session_type} session is confirmed for {date} at {time}. "
                f"The session will last {duration} minutes. "
                "You'll receive a confirmation email with details."
            )
        except ValueError:
            return "Invalid date or time format. Please use YYYY-MM-DD for date and HH:MM for time."

# Example usage
if __name__ == "__main__":
    chatbot = CoachingChatbot()
    print("Chatbot: Hello! I'm your OSI coaching assistant. How can I help you today?")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Chatbot: Goodbye! Have a great day.")
            break
            
        response = chatbot.process_input(user_input)
        print(f"Chatbot: {response}")
        
        # Simulate booking confirmation if user provides date and time
        if "preferred date and time" in response.lower():
            print("Chatbot: (For demo purposes, enter a date and time to confirm booking)")
            date_time_input = input("You (date time): ")
            try:
                date, time = date_time_input.split()
                confirmation = chatbot.confirm_booking(date, time)
                print(f"Chatbot: {confirmation}")
            except:
                print("Chatbot: I didn't understand that. Please provide date and time separated by space.")
```
