"""
Generated Code Metadata:
========================
Original URL: https://terapia-dbt-mentesanapsicologia.cl
Prompt: How can I use the DBT approach to create a mental health app that helps users manage emotional dysregulation? Include specific features based on the DBT methodology.
Generated: DETERMINISTIC_fd29a837577bb223
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# DBT Mental Health App
# This app implements Dialectical Behavior Therapy (DBT) techniques to help users manage emotional dysregulation.

import sqlite3
from datetime import datetime
import random
import json
from typing import Optional, List, Dict

class DBTApp:
    def __init__(self, db_name: str = "dbt_app.db"):
        """Initialize the DBT app with database connection."""
        self.conn = sqlite3.connect(db_name)
        self._create_tables()
        
    def _create_tables(self) -> None:
        """Create necessary database tables if they don't exist."""
        cursor = self.conn.cursor()
        
        # Users table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
        
        # Diary Cards table (core DBT tool)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS diary_cards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            date DATE NOT NULL,
            emotions TEXT,  # JSON array of emotions
            intensity INTEGER,  # 1-10 scale
            urges TEXT,  # JSON array of urges
            skills_used TEXT,  # JSON array of skills used
            notes TEXT,
            FOREIGN KEY (user_id) REFERENCES users (id),
            UNIQUE(user_id, date)
        )
        """)
        
        # Skills table (DBT skills library)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS skills (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT NOT NULL,  # mindfulness, distress tolerance, etc.
            name TEXT NOT NULL,
            description TEXT,
            example TEXT
        )
        """)
        
        # Crisis plan table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS crisis_plan (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            warning_signs TEXT,  # JSON array
            coping_strategies TEXT,  # JSON array
            emergency_contacts TEXT,  # JSON array
            professional_help TEXT,  # JSON array
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
        """)
        
        self.conn.commit()
        
    def register_user(self, username: str, password: str) -> bool:
        """Register a new user."""
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, password)
            )
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False  # Username already exists
    
    def login_user(self, username: str, password: str) -> bool:
        """Authenticate a user."""
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT 1 FROM users WHERE username = ? AND password = ?",
            (username, password)
        )
        return cursor.fetchone() is not None
    
    def add_diary_card(
        self,
        user_id: int,
        emotions: List[str],
        intensity: int,
        urges: List[str],
        skills_used: List[str],
        notes: Optional[str] = None
    ) -> bool:
        """Add a DBT diary card entry."""
        try:
            cursor = self.conn.cursor()
            today = datetime.now().date().isoformat()
            
            cursor.execute(
                """
                INSERT INTO diary_cards (
                    user_id, date, emotions, intensity, urges, skills_used, notes
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    user_id,
                    today,
                    json.dumps(emotions),
                    intensity,
                    json.dumps(urges),
                    json.dumps(skills_used),
                    notes
                )
            )
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False  # Diary card already exists for today
    
    def get_diary_card(self, user_id: int, date: str) -> Optional[Dict]:
        """Retrieve a diary card for a specific date."""
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT * FROM diary_cards WHERE user_id = ? AND date = ?",
            (user_id, date)
        )
        row = cursor.fetchone()
        
        if row:
            return {
                "id": row[0],
                "user_id": row[1],
                "date": row[2],
                "emotions": json.loads(row[3]),
                "intensity": row[4],
                "urges": json.loads(row[5]),
                "skills_used": json.loads(row[6]),
                "notes": row[7]
            }
        return None
    
    def get_random_skill(self, category: Optional[str] = None) -> Dict:
        """Get a random DBT skill suggestion."""
        cursor = self.conn.cursor()
        
        if category:
            cursor.execute(
                "SELECT * FROM skills WHERE category = ? ORDER BY RANDOM() LIMIT 1",
                (category,)
            )
        else:
            cursor.execute("SELECT * FROM skills ORDER BY RANDOM() LIMIT 1")
            
        row = cursor.fetchone()
        
        if row:
            return {
                "id": row[0],
                "category": row[1],
                "name": row[2],
                "description": row[3],
                "example": row[4]
            }
        return {}
    
    def populate_skills(self) -> None:
        """Populate the skills table with core DBT skills."""
        skills = [
            {
                "category": "mindfulness",
                "name": "Observe",
                "description": "Notice your experience without reacting to it",
                "example": "Notice thoughts like clouds passing in the sky"
            },
            {
                "category": "mindfulness",
                "name": "Describe",
                "description": "Put words to your experience",
                "example": "Say 'I'm feeling anxious right now'"
            },
            {
                "category": "distress_tolerance",
                "name": "TIPP",
                "description": "Temperature, Intense exercise, Paced breathing, Paired muscle relaxation",
                "example": "Hold ice in your hand to change body temperature"
            },
            {
                "category": "distress_tolerance",
                "name": "ACCEPTS",
                "description": "Activities, Contributing, Comparisons, Emotions, Pushing away, Thoughts, Sensations",
                "example": "Distract with a pleasant activity"
            },
            {
                "category": "emotion_regulation",
                "name": "Check the Facts",
                "description": "Examine whether your emotional reaction fits the facts",
                "example": "Ask 'Is this threat real or perceived?'"
            },
            {
                "category": "emotion_regulation",
                "name": "Opposite Action",
                "description": "Act opposite to your emotional urge",
                "example": "If you want to isolate, reach out to someone"
            },
            {
                "category": "interpersonal_effectiveness",
                "name": "DEAR MAN",
                "description": "Describe, Express, Assert, Reinforce, Mindful, Appear confident, Negotiate",
                "example": "Use this structure to make requests effectively"
            }
        ]
        
        cursor = self.conn.cursor()
        cursor.executemany(
            "INSERT INTO skills (category, name, description, example) VALUES (:category, :name, :description, :example)",
            skills
        )
        self.conn.commit()
    
    def create_crisis_plan(
        self,
        user_id: int,
        warning_signs: List[str],
        coping_strategies: List[str],
        emergency_contacts: List[str],
        professional_help: List[str]
    ) -> bool:
        """Create or update a crisis plan for a user."""
        try:
            cursor = self.conn.cursor()
            
            # Check if plan exists
            cursor.execute(
                "SELECT id FROM crisis_plan WHERE user_id = ?",
                (user_id,)
            )
            plan_exists = cursor.fetchone()
            
            if plan_exists:
                # Update existing plan
                cursor.execute(
                    """
                    UPDATE crisis_plan SET
                        warning_signs = ?,
                        coping_strategies = ?,
                        emergency_contacts = ?,
                        professional_help = ?
                    WHERE user_id = ?
                    """,
                    (
                        json.dumps(warning_signs),
                        json.dumps(coping_strategies),
                        json.dumps(emergency_contacts),
                        json.dumps(professional_help),
                        user_id
                    )
                )
            else:
                # Create new plan
                cursor.execute(
                    """
                    INSERT INTO crisis_plan (
                        user_id, warning_signs, coping_strategies, emergency_contacts, professional_help
                    ) VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        user_id,
                        json.dumps(warning_signs),
                        json.dumps(coping_strategies),
                        json.dumps(emergency_contacts),
                        json.dumps(professional_
