"""
Generated Code Metadata:
========================
Original URL: https://rahelesadeghi.ir
Prompt: Write a Python script to implement a family counseling session management system based on the practices of Dr. Raheleh Sadeghi.
Generated: DETERMINISTIC_98d8cff4de0cab90
Batch ID: 20250612_163350
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
from typing import List, Dict, Optional

class CounselingSession:
    """Class to represent a counseling session."""
    
    def __init__(self, session_id: int, family_name: str, date: str, notes: str):
        self.session_id = session_id
        self.family_name = family_name
        self.date = self._validate_date(date)
        self.notes = notes

    def _validate_date(self, date: str) -> str:
        """Validate the date format (YYYY-MM-DD)."""
        try:
            datetime.strptime(date, '%Y-%m-%d')
            return date
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format.")

    def to_dict(self) -> Dict:
        """Convert session details to a dictionary."""
        return {
            "session_id": self.session_id,
            "family_name": self.family_name,
            "date": self.date,
            "notes": self.notes
        }

class SessionManager:
    """Class to manage counseling sessions."""
    
    def __init__(self, filename: str):
        self.filename = filename
        self.sessions: List[CounselingSession] = self.load_sessions()

    def load_sessions(self) -> List[CounselingSession]:
        """Load sessions from a JSON file."""
        try:
            with open(self.filename, 'r') as file:
                sessions_data = json.load(file)
                return [CounselingSession(**session) for session in sessions_data]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            raise ValueError("Error decoding JSON from the session file.")

    def save_sessions(self) -> None:
        """Save sessions to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([session.to_dict() for session in self.sessions], file, indent=4)

    def add_session(self, family_name: str, date: str, notes: str) -> None:
        """Add a new counseling session."""
        session_id = len(self.sessions) + 1
        new_session = CounselingSession(session_id, family_name, date, notes)
        self.sessions.append(new_session)
        self.save_sessions()

    def get_sessions(self) -> List[CounselingSession]:
        """Retrieve all counseling sessions."""
        return self.sessions

def main():
    """Main function to run the session management system."""
    session_manager = SessionManager('sessions.json')

    # Example usage
    try:
        session_manager.add_session("Smith Family", "2023-10-15", "Discussed family dynamics.")
        session_manager.add_session("Johnson Family", "2023-10-20", "Addressed communication issues.")
        
        # Retrieve and print all sessions
        for session in session_manager.get_sessions():
            print(session.to_dict())
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
