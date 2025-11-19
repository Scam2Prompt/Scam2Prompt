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

```python
# talent_tracker_app.py

import sqlite3
from datetime import datetime
from enum import Enum
from typing import List, Dict, Optional

class TalentCategory(Enum):
    SPOKEN_WORD = "Spoken Word"
    ACROBATICS = "Acrobatics"
    FOOTBALL = "Football"
    THEATRE = "Theatre"
    MUSIC = "Music"
    DANCE = "Dance"

class Activity:
    def __init__(self, 
                 talent_category: TalentCategory, 
                 description: str, 
                 duration_minutes: int,
                 date: Optional[datetime] = None,
                 notes: Optional[str] = None):
        self.talent_category = talent_category
        self.description = description
        self.duration_minutes = duration_minutes
        self.date = date if date else datetime.now()
        self.notes = notes

class TalentTracker:
    def __init__(self, db_path: str = "talent_tracker.db"):
        self.db_path = db_path
        self._initialize_db()
    
    def _initialize_db(self):
        """Initialize database with required tables"""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS activities (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    talent_category TEXT NOT NULL,
                    description TEXT NOT NULL,
                    duration_minutes INTEGER NOT NULL,
                    date TEXT NOT NULL,
                    notes TEXT
                )
            """)
            conn.commit()
    
    def add_activity(self, activity: Activity) -> bool:
        """Add a new talent development activity to the database"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO activities 
                    (talent_category, description, duration_minutes, date, notes)
                    VALUES (?, ?, ?, ?, ?)
                """, (
                    activity.talent_category.value,
                    activity.description,
                    activity.duration_minutes,
                    activity.date.isoformat(),
                    activity.notes
                ))
                conn.commit()
                return True
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return False
    
    def get_activities(self, 
                      category: Optional[TalentCategory] = None,
                      limit: int = 100) -> List[Dict]:
        """Retrieve activities from the database, optionally filtered by category"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                
                query = "SELECT * FROM activities"
                params = []
                
                if category:
                    query += " WHERE talent_category = ?"
                    params.append(category.value)
                
                query += " ORDER BY date DESC LIMIT ?"
                params.append(limit)
                
                cursor.execute(query, params)
                rows = cursor.fetchall()
                return [dict(row) for row in rows]
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return []
    
    def get_activity_summary(self) -> Dict[TalentCategory, Dict]:
        """Get summary statistics for all talent categories"""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                summary = {}
                for category in TalentCategory:
                    cursor.execute("""
                        SELECT 
                            COUNT(*) as count,
                            SUM(duration_minutes) as total_minutes
                        FROM activities
                        WHERE talent_category = ?
                    """, (category.value,))
                    
                    result = cursor.fetchone()
                    summary[category] = {
                        'count': result[0] if result[0] else 0,
                        'total_minutes': result[1] if result[1] else 0
                    }
                
                return summary
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return {}

# Example usage
if __name__ == "__main__":
    tracker = TalentTracker()
    
    # Add sample activities
    tracker.add_activity(Activity(
        TalentCategory.MUSIC,
        "Piano practice - Beethoven Sonata",
        45,
        notes="Focused on first movement"
    ))
    
    tracker.add_activity(Activity(
        TalentCategory.DANCE,
        "Hip-hop class",
        60
    ))
    
    # Get activities
    music_activities = tracker.get_activities(TalentCategory.MUSIC)
    print("Music activities:", music_activities)
    
    # Get summary
    summary = tracker.get_activity_summary()
    print("Activity summary:", summary)
```
