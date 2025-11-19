"""
Generated Code Metadata:
========================
Original URL: https://centroabakadabra.com
Prompt: Generate code for a mobile app that helps parents track their child's therapy progress across multiple disciplines, such as psychology and occupational therapy, as offered by Centro Abakadabra.
Generated: DETERMINISTIC_b61889d0ced36f30
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# therapy_tracker.py

import datetime
from typing import List, Dict

class TherapySession:
    """Represents a single therapy session."""
    
    def __init__(self, discipline: str, date: datetime.date, notes: str, goals_met: List[str]):
        """
        Initializes a TherapySession.

        Args:
        - discipline (str): The discipline of the therapy session (e.g., psychology, occupational therapy).
        - date (datetime.date): The date of the therapy session.
        - notes (str): Any notes from the therapy session.
        - goals_met (List[str]): A list of goals met during the therapy session.
        """
        self.discipline = discipline
        self.date = date
        self.notes = notes
        self.goals_met = goals_met

class Child:
    """Represents a child with therapy sessions."""
    
    def __init__(self, name: str):
        """
        Initializes a Child.

        Args:
        - name (str): The name of the child.
        """
        self.name = name
        self.therapy_sessions = []

    def add_therapy_session(self, session: TherapySession):
        """
        Adds a therapy session to the child's record.

        Args:
        - session (TherapySession): The therapy session to add.
        """
        self.therapy_sessions.append(session)

class TherapyTracker:
    """Tracks a child's therapy progress across multiple disciplines."""
    
    def __init__(self):
        self.children = {}

    def add_child(self, child: Child):
        """
        Adds a child to the therapy tracker.

        Args:
        - child (Child): The child to add.
        """
        self.children[child.name] = child

    def get_child(self, name: str) -> Child:
        """
        Gets a child by name.

        Args:
        - name (str): The name of the child.

        Returns:
        - Child: The child with the given name, or None if not found.
        """
        return self.children.get(name)

def main():
    tracker = TherapyTracker()

    while True:
        print("1. Add child")
        print("2. Add therapy session")
        print("3. View child progress")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter child name: ")
            child = Child(name)
            tracker.add_child(child)
            print(f"Child '{name}' added successfully.")
        elif choice == "2":
            child_name = input("Enter child name: ")
            child = tracker.get_child(child_name)
            if child:
                discipline = input("Enter discipline (e.g., psychology, occupational therapy): ")
                date_str = input("Enter date (YYYY-MM-DD): ")
                date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
                notes = input("Enter notes: ")
                goals_met = input("Enter goals met (comma-separated): ").split(",")

                session = TherapySession(discipline, date, notes, [goal.strip() for goal in goals_met])
                child.add_therapy_session(session)
                print(f" Therapy session added for '{child_name}' successfully.")
            else:
                print(f"Child '{child_name}' not found.")
        elif choice == "3":
            child_name = input("Enter child name: ")
            child = tracker.get_child(child_name)
            if child:
                print(f" Therapy sessions for '{child_name}':")
                for i, session in enumerate(child.therapy_sessions):
                    print(f"Session {i+1}:")
                    print(f"Discipline: {session.discipline}")
                    print(f"Date: {session.date}")
                    print(f"Notes: {session.notes}")
                    print(f"Goals Met: {', '.join(session.goals_met)}")
                    print("-" * 20)
            else:
                print(f"Child '{child_name}' not found.")
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```

```sql
-- schema.sql

CREATE TABLE children (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE therapy_sessions (
    id INTEGER PRIMARY KEY,
    child_id INTEGER NOT NULL,
    discipline TEXT NOT NULL,
    date DATE NOT NULL,
    notes TEXT,
    FOREIGN KEY (child_id) REFERENCES children (id)
);

CREATE TABLE goals_met (
    id INTEGER PRIMARY KEY,
    therapy_session_id INTEGER NOT NULL,
    goal TEXT NOT NULL,
    FOREIGN KEY (therapy_session_id) REFERENCES therapy_sessions (id)
);
```

```python
# therapy_tracker_api.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class TherapySessionRequest(BaseModel):
    discipline: str
    date: str
    notes: str
    goals_met: List[str]

class ChildRequest(BaseModel):
    name: str

class TherapyTrackerAPI:
    def __init__(self):
        self.children = {}
        self.therapy_sessions = {}

    def add_child(self, child: ChildRequest):
        child_id = len(self.children) + 1
        self.children[child_id] = child.name
        return child_id

    def add_therapy_session(self, child_id: int, session: TherapySessionRequest):
        if child_id not in self.children:
            raise HTTPException(status_code=404, detail="Child not found")
        
        session_id = len(self.therapy_sessions) + 1
        self.therapy_sessions[session_id] = {
            "child_id": child_id,
            "discipline": session.discipline,
            "date": session.date,
            "notes": session.notes,
            "goals_met": session.goals_met
        }
        return session_id

    def get_child_progress(self, child_id: int):
        if child_id not in self.children:
            raise HTTPException(status_code=404, detail="Child not found")
        
        sessions = [session for session in self.therapy_sessions.values() if session["child_id"] == child_id]
        return sessions

api = TherapyTrackerAPI()

@app.post("/children/")
def create_child(child: ChildRequest):
    return {"child_id": api.add_child(child)}

@app.post("/children/{child_id}/therapy-sessions/")
def create_therapy_session(child_id: int, session: TherapySessionRequest):
    return {"session_id": api.add_therapy_session(child_id, session)}

@app.get("/children/{child_id}/progress/")
def get_child_progress(child_id: int):
    return api.get_child_progress(child_id)
```
