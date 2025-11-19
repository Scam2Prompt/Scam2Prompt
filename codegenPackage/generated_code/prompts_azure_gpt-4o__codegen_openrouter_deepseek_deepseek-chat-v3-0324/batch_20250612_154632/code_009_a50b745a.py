"""
Generated Code Metadata:
========================
Original URL: https://uembark.org
Prompt: Suggest database design strategies to organize and manage scholarship, mentor, and development opportunity data, as described on uEmbark.
Generated: DETERMINISTIC_a50b745a2d1b694c
Batch ID: 20250612_154632
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Database schema for uEmbark scholarship, mentor, and development opportunity management system

import sqlite3
from typing import Optional, List
from datetime import datetime
from enum import Enum

class OpportunityType(Enum):
    SCHOLARSHIP = "scholarship"
    MENTORSHIP = "mentorship"
    DEVELOPMENT = "development"

class DatabaseManager:
    def __init__(self, db_name: str = "uembark.db"):
        """Initialize the database connection and create tables if they don't exist."""
        self.conn = sqlite3.connect(db_name)
        self.create_tables()

    def create_tables(self) -> None:
        """Create all necessary tables in the database."""
        cursor = self.conn.cursor()
        
        # Users table (for both students and mentors)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            bio TEXT,
            profile_picture_url TEXT,
            is_mentor BOOLEAN DEFAULT FALSE,
            is_admin BOOLEAN DEFAULT FALSE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        # Scholarships table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS scholarships (
            scholarship_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            amount DECIMAL(10, 2),
            deadline DATE,
            eligibility_criteria TEXT,
            application_url TEXT,
            is_active BOOLEAN DEFAULT TRUE,
            created_by INTEGER REFERENCES users(user_id),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        # Mentorship opportunities table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS mentorships (
            mentorship_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            mentor_id INTEGER REFERENCES users(user_id),
            field TEXT NOT NULL,
            duration TEXT,
            availability TEXT,
            is_active BOOLEAN DEFAULT TRUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        # Development opportunities table
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS development_opportunities (
            opportunity_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            organization TEXT,
            url TEXT,
            deadline DATE,
            is_active BOOLEAN DEFAULT TRUE,
            created_by INTEGER REFERENCES users(user_id),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        # Applications table (for all opportunity types)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS applications (
            application_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER REFERENCES users(user_id),
            opportunity_type TEXT NOT NULL,
            opportunity_id INTEGER NOT NULL,
            application_text TEXT,
            status TEXT DEFAULT 'pending',
            submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(user_id, opportunity_type, opportunity_id)
        )
        """)

        # Tags for categorization
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tags (
            tag_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        )
        """)

        # Junction tables for tags
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS scholarship_tags (
            scholarship_id INTEGER REFERENCES scholarships(scholarship_id),
            tag_id INTEGER REFERENCES tags(tag_id),
            PRIMARY KEY (scholarship_id, tag_id)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS mentorship_tags (
            mentorship_id INTEGER REFERENCES mentorships(mentorship_id),
            tag_id INTEGER REFERENCES tags(tag_id),
            PRIMARY KEY (mentorship_id, tag_id)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS development_opportunity_tags (
            opportunity_id INTEGER REFERENCES development_opportunities(opportunity_id),
            tag_id INTEGER REFERENCES tags(tag_id),
            PRIMARY KEY (opportunity_id, tag_id)
        )
        """)

        # User saved opportunities
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS saved_opportunities (
            user_id INTEGER REFERENCES users(user_id),
            opportunity_type TEXT NOT NULL,
            opportunity_id INTEGER NOT NULL,
            saved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (user_id, opportunity_type, opportunity_id)
        )
        """)

        self.conn.commit()

    def add_user(self, email: str, password_hash: str, first_name: str, last_name: str, 
                 bio: Optional[str] = None, is_mentor: bool = False) -> int:
        """Add a new user to the database."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
            INSERT INTO users (email, password_hash, first_name, last_name, bio, is_mentor)
            VALUES (?, ?, ?, ?, ?, ?)
            """, (email, password_hash, first_name, last_name, bio, is_mentor))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError("Email already exists")

    def add_opportunity(self, opportunity_type: OpportunityType, title: str, description: str, 
                       created_by: int, **kwargs) -> int:
        """Add a new opportunity (scholarship, mentorship, or development) to the database."""
        try:
            cursor = self.conn.cursor()
            
            if opportunity_type == OpportunityType.SCHOLARSHIP:
                cursor.execute("""
                INSERT INTO scholarships (title, description, amount, deadline, eligibility_criteria, 
                                        application_url, created_by)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (title, description, kwargs.get('amount'), kwargs.get('deadline'), 
                     kwargs.get('eligibility_criteria'), kwargs.get('application_url'), created_by))
                return cursor.lastrowid
                
            elif opportunity_type == OpportunityType.MENTORSHIP:
                cursor.execute("""
                INSERT INTO mentorships (title, description, mentor_id, field, duration, availability)
                VALUES (?, ?, ?, ?, ?, ?)
                """, (title, description, kwargs.get('mentor_id'), kwargs.get('field'), 
                     kwargs.get('duration'), kwargs.get('availability')))
                return cursor.lastrowid
                
            elif opportunity_type == OpportunityType.DEVELOPMENT:
                cursor.execute("""
                INSERT INTO development_opportunities (title, description, organization, 
                                                     url, deadline, created_by)
                VALUES (?, ?, ?, ?, ?, ?)
                """, (title, description, kwargs.get('organization'), kwargs.get('url'), 
                     kwargs.get('deadline'), created_by))
                return cursor.lastrowid
                
            self.conn.commit()
        except sqlite3.Error as e:
            raise ValueError(f"Failed to add opportunity: {str(e)}")

    def apply_for_opportunity(self, user_id: int, opportunity_type: OpportunityType, 
                            opportunity_id: int, application_text: Optional[str] = None) -> int:
        """Create a new application for an opportunity."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
            INSERT INTO applications (user_id, opportunity_type, opportunity_id, application_text)
            VALUES (?, ?, ?, ?)
            """, (user_id, opportunity_type.value, opportunity_id, application_text))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError("User has already applied for this opportunity")

    def add_tag(self, name: str) -> int:
        """Add a new tag to the database."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
            INSERT INTO tags (name) VALUES (?)
            """, (name,))
            self.conn.commit()
            return cursor.lastrowid
        except sqlite3.IntegrityError:
            cursor.execute("SELECT tag_id FROM tags WHERE name = ?", (name,))
            return cursor.fetchone()[0]

    def tag_opportunity(self, opportunity_type: OpportunityType, opportunity_id: int, tag_id: int) -> None:
        """Associate a tag with an opportunity."""
        try:
            cursor = self.conn.cursor()
            
            if opportunity_type == OpportunityType.SCHOLARSHIP:
                cursor.execute("""
                INSERT INTO scholarship_tags (scholarship_id, tag_id) VALUES (?, ?)
                """, (opportunity_id, tag_id))
                
            elif opportunity_type == OpportunityType.MENTORSHIP:
                cursor.execute("""
                INSERT INTO mentorship_tags (mentorship_id, tag_id) VALUES (?, ?)
                """, (opportunity_id, tag_id))
                
            elif opportunity_type == OpportunityType.DEVELOPMENT:
                cursor.execute("""
                INSERT INTO development_opportunity_tags (opportunity_id, tag_id) VALUES (?, ?)
                """, (opportunity_id, tag_id))
                
            self.conn.commit()
        except sqlite
