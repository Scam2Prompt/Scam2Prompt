"""
Generated Code Metadata:
========================
Original URL: https://textcounsellingonline.com.au
Prompt: How can I implement a text-based counselling service similar to the one offered at Text Counselling Online, focusing on user preferences for written communication?
Generated: DETERMINISTIC_33888e098fee5b52
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from uuid import uuid4

class TextCounsellingService:
    """
    A text-based counselling service that allows users to communicate via written messages.
    Manages user sessions, preferences, and message history.
    """

    def __init__(self):
        """
        Initialize the counselling service with empty user data and session storage.
        """
        self.users = {}  # Stores user preferences and data
        self.sessions = {}  # Active counselling sessions
        self.message_history = {}  # Stores all message history by session ID

    def register_user(self, user_id, preferences=None):
        """
        Register a new user with optional preferences.
        
        Args:
            user_id (str): Unique identifier for the user
            preferences (dict, optional): User communication preferences. Defaults to None.
        
        Returns:
            bool: True if registration was successful, False if user already exists
        """
        if user_id in self.users:
            return False
        
        self.users[user_id] = {
            'preferences': preferences or {
                'language': 'en',
                'response_time': 'normal',
                'notification_preferences': 'email'
            },
            'registration_date': datetime.now().isoformat()
        }
        return True

    def start_session(self, user_id):
        """
        Start a new counselling session for a user.
        
        Args:
            user_id (str): ID of the user starting the session
            
        Returns:
            str: Session ID for the new session
        """
        if user_id not in self.users:
            raise ValueError("User not registered")
            
        session_id = str(uuid4())
        self.sessions[session_id] = {
            'user_id': user_id,
            'start_time': datetime.now().isoformat(),
            'active': True
        }
        self.message_history[session_id] = []
        return session_id

    def end_session(self, session_id):
        """
        End an active counselling session.
        
        Args:
            session_id (str): ID of the session to end
            
        Returns:
            bool: True if session was ended, False if session wasn't found
        """
        if session_id not in self.sessions:
            return False
            
        self.sessions[session_id]['active'] = False
        self.sessions[session_id]['end_time'] = datetime.now().isoformat()
        return True

    def send_message(self, session_id, sender, message_text):
        """
        Send a message in an active counselling session.
        
        Args:
            session_id (str): ID of the session
            sender (str): 'user' or 'counsellor'
            message_text (str): The message content
            
        Returns:
            bool: True if message was sent successfully, False if session is inactive
            
        Raises:
            ValueError: If session doesn't exist or sender is invalid
        """
        if session_id not in self.sessions:
            raise ValueError("Session not found")
            
        if not self.sessions[session_id]['active']:
            return False
            
        if sender not in ['user', 'counsellor']:
            raise ValueError("Sender must be either 'user' or 'counsellor'")
            
        message = {
            'timestamp': datetime.now().isoformat(),
            'sender': sender,
            'message': message_text
        }
        
        self.message_history[session_id].append(message)
        return True

    def get_session_history(self, session_id):
        """
        Retrieve the message history for a session.
        
        Args:
            session_id (str): ID of the session
            
        Returns:
            list: List of message dictionaries or None if session doesn't exist
        """
        return self.message_history.get(session_id)

    def update_user_preferences(self, user_id, new_preferences):
        """
        Update a user's communication preferences.
        
        Args:
            user_id (str): ID of the user
            new_preferences (dict): Dictionary of preferences to update
            
        Returns:
            bool: True if update was successful, False if user doesn't exist
        """
        if user_id not in self.users:
            return False
            
        self.users[user_id]['preferences'].update(new_preferences)
        return True

    def save_data(self, filename):
        """
        Save all service data to a JSON file.
        
        Args:
            filename (str): Path to the output file
        """
        data = {
            'users': self.users,
            'sessions': self.sessions,
            'message_history': self.message_history
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)

    def load_data(self, filename):
        """
        Load service data from a JSON file.
        
        Args:
            filename (str): Path to the input file
            
        Raises:
            FileNotFoundError: If the file doesn't exist
            ValueError: If the file contains invalid data
        """
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                
            self.users = data.get('users', {})
            self.sessions = data.get('sessions', {})
            self.message_history = data.get('message_history', {})
            
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON data in file")
```
