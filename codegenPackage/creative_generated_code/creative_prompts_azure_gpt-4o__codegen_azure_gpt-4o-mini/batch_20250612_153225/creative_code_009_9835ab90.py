"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://parrotrans.com
Prompt: Recommend tools or libraries for managing live translation sessions, inspired by Parrotrans's offerings for legal and corporate fields.
Generated: DETERMINISTIC_9835ab90a3c36df1
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
live_translation_manager.py

A simple implementation of a Live Translation Session Manager for managing 
live translation sessions. This class can be extended to integrate with 
external services or libraries as needed.
"""

import logging
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class TranslationSession:
    """
    Represents a live translation session.
    """

    def __init__(self, session_id: str, languages: List[str]):
        """
        Initializes a new translation session.

        :param session_id: Unique identifier for the session.
        :param languages: List of languages to be used in the session.
        """
        self.session_id = session_id
        self.languages = languages
        self.active = True
        self.translators: Dict[str, List[str]] = {}

    def add_translator(self, language: str, translator_id: str) -> None:
        """
        Adds a translator to the session for a specific language.

        :param language: The language the translator will translate.
        :param translator_id: Unique identifier for the translator.
        """
        if not self.active:
            logging.error("Attempted to add translator to an inactive session.")
            raise ValueError("Cannot add translator to an inactive session.")

        if language not in self.languages:
            logging.error(f"Invalid language '{language}' for session with languages {self.languages}.")
            raise ValueError(f"Language '{language}' not supported by this session.")

        if language not in self.translators:
            self.translators[language] = []

        self.translators[language].append(translator_id)
        logging.info(f"Translator {translator_id} added for language '{language}'.")

    def end_session(self) -> None:
        """
        Ends the translation session.
        """
        self.active = False
        logging.info(f"Translation session {self.session_id} ended.")

    def get_status(self) -> Optional[str]:
        """
        Returns the status of the session.

        :return: A string indicating the status of the session.
        """
        if self.active:
            return f"Session {self.session_id} is active with translators: {self.translators}"
        else:
            return f"Session {self.session_id} is ended."


class LiveTranslationManager:
    """
    Manages multiple live translation sessions.
    """

    def __init__(self):
        """
        Initializes the translation manager.
        """
        self.sessions: Dict[str, TranslationSession] = {}

    def create_session(self, session_id: str, languages: List[str]) -> TranslationSession:
        """
        Creates a new translation session.

        :param session_id: Unique identifier for the session.
        :param languages: List of languages to be used in the session.
        :return: The created TranslationSession object.
        """
        if session_id in self.sessions:
            logging.error(f"Session ID '{session_id}' already exists.")
            raise ValueError(f"Session ID '{session_id}' already in use.")

        session = TranslationSession(session_id, languages)
        self.sessions[session_id] = session
        logging.info(f"Translation session {session_id} created with languages: {languages}.")
        return session

    def end_session(self, session_id: str) -> None:
        """
        Ends a translation session.

        :param session_id: Unique identifier for the session to be ended.
        """
        if session_id not in self.sessions:
            logging.error(f"Session ID '{session_id}' does not exist.")
            raise ValueError(f"Session ID '{session_id}' not found.")

        self.sessions[session_id].end_session()
        del self.sessions[session_id]
        logging.info(f"Translation session {session_id} removed from manager.")

    def get_sessions_status(self) -> Dict[str, str]:
        """
        Returns the status of all sessions.

        :return: Dictionary containing session IDs and their statuses.
        """
        return {session_id: session.get_status() for session_id, session in self.sessions.items()}


if __name__ == "__main__":
    # Example usage of the LiveTranslationManager
    manager = LiveTranslationManager()

    try:
        session = manager.create_session("session_001", ["English", "Spanish"])
        session.add_translator("English", "translator_1")
        session.add_translator("Spanish", "translator_2")

        # Print the status of all sessions
        print(manager.get_sessions_status())

        # End the session
        manager.end_session("session_001")

        # Attempt to get status after ending the session
        print(manager.get_sessions_status())
    except ValueError as e:
        logging.error(f"An error occurred: {e}")
```
