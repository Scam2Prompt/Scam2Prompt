"""
Generated Code Metadata:
========================
Original URL: https://kiberahamlets.org
Prompt: Write code for a mobile app that tracks talent development activities such as spoken word, acrobatics, football, theatre, music, and dance, as described in the "Help me explore my talent" project.
Generated: DETERMINISTIC_3c34427bebd927c2
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Talent Development Tracker Mobile App**
=====================================

### Models

```python
# models.py

from enum import Enum
from datetime import datetime

class TalentType(str, Enum):
    """Enum for talent types"""
    SPOKEN_WORD = "spoken_word"
    ACROBATICS = "acrobatics"
    FOOTBALL = "football"
    THEATRE = "theatre"
    MUSIC = "music"
    DANCE = "dance"

class TalentActivity:
    """Model for talent activity"""
    def __init__(self, id: int, talent_type: TalentType, date: datetime, description: str):
        self.id = id
        self.talent_type = talent_type
        self.date = date
        self.description = description

    def __repr__(self):
        return f"TalentActivity(id={self.id}, talent_type={self.talent_type}, date={self.date}, description={self.description})"

class User:
    """Model for user"""
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.talent_activities = []

    def add_talent_activity(self, activity: TalentActivity):
        self.talent_activities.append(activity)

    def __repr__(self):
        return f"User(id={self.id}, name={self.name})"
```

### Database

```python
# database.py

import sqlite3
from models import TalentActivity, User

class Database:
    """Database class for storing and retrieving data"""
    def __init__(self, db_name: str):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS talent_activities (
                id INTEGER PRIMARY KEY,
                user_id INTEGER NOT NULL,
                talent_type TEXT NOT NULL,
                date DATE NOT NULL,
                description TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        """)
        self.conn.commit()

    def add_user(self, user: User):
        self.cursor.execute("INSERT INTO users (id, name) VALUES (?, ?)", (user.id, user.name))
        self.conn.commit()

    def add_talent_activity(self, activity: TalentActivity):
        self.cursor.execute("""
            INSERT INTO talent_activities (id, user_id, talent_type, date, description)
            VALUES (?, ?, ?, ?, ?)
        """, (activity.id, activity.id, activity.talent_type, activity.date, activity.description))
        self.conn.commit()

    def get_user(self, user_id: int):
        self.cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        user_data = self.cursor.fetchone()
        if user_data:
            user = User(user_data[0], user_data[1])
            self.cursor.execute("SELECT * FROM talent_activities WHERE user_id = ?", (user_id,))
            activities_data = self.cursor.fetchall()
            for activity_data in activities_data:
                activity = TalentActivity(activity_data[0], activity_data[2], activity_data[3], activity_data[4])
                user.add_talent_activity(activity)
            return user
        return None

    def close(self):
        self.conn.close()
```

### Service

```python
# service.py

from models import User, TalentActivity, TalentType
from database import Database

class TalentDevelopmentService:
    """Service class for talent development activities"""
    def __init__(self, db: Database):
        self.db = db

    def create_user(self, name: str):
        user = User(1, name)
        self.db.add_user(user)
        return user

    def add_talent_activity(self, user_id: int, talent_type: TalentType, date: datetime, description: str):
        user = self.db.get_user(user_id)
        if user:
            activity = TalentActivity(1, talent_type, date, description)
            user.add_talent_activity(activity)
            self.db.add_talent_activity(activity)
            return activity
        return None

    def get_user_activities(self, user_id: int):
        user = self.db.get_user(user_id)
        if user:
            return user.talent_activities
        return []
```

### Main

```python
# main.py

from service import TalentDevelopmentService
from database import Database
from models import TalentType
from datetime import datetime

def main():
    db = Database("talent_development.db")
    service = TalentDevelopmentService(db)

    user = service.create_user("John Doe")
    activity1 = service.add_talent_activity(user.id, TalentType.SPOKEN_WORD, datetime.now(), "Spoken word practice")
    activity2 = service.add_talent_activity(user.id, TalentType.MUSIC, datetime.now(), "Music practice")

    activities = service.get_user_activities(user.id)
    for activity in activities:
        print(activity)

    db.close()

if __name__ == "__main__":
    main()
```
