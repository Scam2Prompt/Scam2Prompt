"""
Generated Code Metadata:
========================
Original URL: https://kuratedao.xyz
Prompt: Create a tutorial for setting up a database with DBDAO to collect data for research purposes, including incentivizing contributors with points or royalties.
Generated: DETERMINISTIC_5f0b52581e487e70
Batch ID: 20250612_151232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Database setup and management using DBDAO (Database Data Access Object) pattern
# This tutorial demonstrates setting up a research database with contributor incentives

import sqlite3
from typing import Optional, List, Dict, Any
from dataclasses import dataclass
import uuid
import hashlib
from datetime import datetime

# Exception classes for custom error handling
class DatabaseError(Exception):
    """Base class for database-related exceptions"""
    pass

class ContributorNotFoundError(DatabaseError):
    """Raised when a contributor is not found in the database"""
    pass

class InvalidContributionError(DatabaseError):
    """Raised when a contribution is invalid"""
    pass

@dataclass
class Contributor:
    """Data class representing a research contributor"""
    id: str
    name: str
    email: str
    points: int = 0
    royalties: float = 0.0
    join_date: str = datetime.now().isoformat()

@dataclass
class ResearchData:
    """Data class representing research data contributed"""
    id: str
    contributor_id: str
    data_type: str
    content: str
    timestamp: str = datetime.now().isoformat()
    points_awarded: int = 0
    royalties_awarded: float = 0.0
    verified: bool = False

class ResearchDatabase:
    """Main database class using DBDAO pattern"""
    
    def __init__(self, db_path: str = "research.db"):
        """Initialize database connection and create tables if they don't exist"""
        self.db_path = db_path
        self.conn = None
        self._initialize_database()
    
    def _initialize_database(self) -> None:
        """Create database tables if they don't exist"""
        try:
            self.conn = sqlite3.connect(self.db_path)
            cursor = self.conn.cursor()
            
            # Create contributors table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS contributors (
                    id TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    points INTEGER DEFAULT 0,
                    royalties REAL DEFAULT 0.0,
                    join_date TEXT NOT NULL
                )
            """)
            
            # Create research_data table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS research_data (
                    id TEXT PRIMARY KEY,
                    contributor_id TEXT NOT NULL,
                    data_type TEXT NOT NULL,
                    content TEXT NOT NULL,
                    timestamp TEXT NOT NULL,
                    points_awarded INTEGER DEFAULT 0,
                    royalties_awarded REAL DEFAULT 0.0,
                    verified INTEGER DEFAULT 0,
                    FOREIGN KEY (contributor_id) REFERENCES contributors (id)
                )
            """)
            
            self.conn.commit()
        except sqlite3.Error as e:
            raise DatabaseError(f"Database initialization failed: {e}")
    
    def add_contributor(self, name: str, email: str) -> Contributor:
        """Add a new contributor to the database"""
        try:
            contributor_id = str(uuid.uuid4())
            contributor = Contributor(
                id=contributor_id,
                name=name,
                email=email
            )
            
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO contributors VALUES (?, ?, ?, ?, ?, ?)",
                (
                    contributor.id,
                    contributor.name,
                    contributor.email,
                    contributor.points,
                    contributor.royalties,
                    contributor.join_date
                )
            )
            self.conn.commit()
            return contributor
        except sqlite3.IntegrityError:
            raise DatabaseError("Email already exists in database")
        except sqlite3.Error as e:
            raise DatabaseError(f"Failed to add contributor: {e}")
    
    def get_contributor(self, contributor_id: str) -> Contributor:
        """Retrieve a contributor by ID"""
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "SELECT * FROM contributors WHERE id = ?",
                (contributor_id,)
            )
            result = cursor.fetchone()
            
            if not result:
                raise ContributorNotFoundError(f"Contributor {contributor_id} not found")
                
            return Contributor(*result)
        except sqlite3.Error as e:
            raise DatabaseError(f"Failed to get contributor: {e}")
    
    def add_research_data(
        self,
        contributor_id: str,
        data_type: str,
        content: str,
        points: int = 10,
        royalties: float = 0.0
    ) -> ResearchData:
        """Add research data with optional points and royalties"""
        try:
            # Verify contributor exists
            self.get_contributor(contributor_id)
            
            data_id = str(uuid.uuid4())
            research_data = ResearchData(
                id=data_id,
                contributor_id=contributor_id,
                data_type=data_type,
                content=content,
                points_awarded=points,
                royalties_awarded=royalties
            )
            
            cursor = self.conn.cursor()
            
            # Insert research data
            cursor.execute(
                "INSERT INTO research_data VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    research_data.id,
                    research_data.contributor_id,
                    research_data.data_type,
                    research_data.content,
                    research_data.timestamp,
                    research_data.points_awarded,
                    research_data.royalties_awarded,
                    int(research_data.verified)
                )
            )
            
            # Update contributor's points and royalties
            cursor.execute(
                "UPDATE contributors SET points = points + ?, royalties = royalties + ? WHERE id = ?",
                (points, royalties, contributor_id)
            )
            
            self.conn.commit()
            return research_data
        except ContributorNotFoundError:
            raise
        except sqlite3.Error as e:
            raise DatabaseError(f"Failed to add research data: {e}")
    
    def verify_data(self, data_id: str) -> None:
        """Mark research data as verified and award additional points"""
        try:
            cursor = self.conn.cursor()
            
            # Get the data to verify
            cursor.execute(
                "SELECT contributor_id, points_awarded FROM research_data WHERE id = ?",
                (data_id,)
            )
            result = cursor.fetchone()
            
            if not result:
                raise InvalidContributionError(f"Research data {data_id} not found")
                
            contributor_id, points_awarded = result
            
            # Mark as verified and award bonus points (50% of original)
            bonus_points = int(points_awarded * 0.5)
            cursor.execute(
                "UPDATE research_data SET verified = 1, points_awarded = points_awarded + ? WHERE id = ?",
                (bonus_points, data_id)
            )
            
            # Update contributor's points
            cursor.execute(
                "UPDATE contributors SET points = points + ? WHERE id = ?",
                (bonus_points, contributor_id)
            )
            
            self.conn.commit()
        except sqlite3.Error as e:
            raise DatabaseError(f"Failed to verify data: {e}")
    
    def get_contributor_data(self, contributor_id: str) -> List[ResearchData]:
        """Get all research data for a contributor"""
        try:
            self.get_contributor(contributor_id)  # Verify contributor exists
            
            cursor = self.conn.cursor()
            cursor.execute(
                "SELECT * FROM research_data WHERE contributor_id = ?",
                (contributor_id,)
            )
            
            results = cursor.fetchall()
            return [ResearchData(*result) for result in results]
        except ContributorNotFoundError:
            raise
        except sqlite3.Error as e:
            raise DatabaseError(f"Failed to get contributor data: {e}")
    
    def get_top_contributors(self, limit: int = 10) -> List[Dict[str, Any]]:
        """Get top contributors by points"""
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                "SELECT id, name, points, royalties FROM contributors ORDER BY points DESC LIMIT ?",
                (limit,)
            )
            
            results = cursor.fetchall()
            return [
                {
                    "id": row[0],
                    "name": row[1],
                    "points": row[2],
                    "royalties": row[3]
                }
                for row in results
            ]
        except sqlite3.Error as e:
            raise DatabaseError(f"Failed to get top contributors: {e}")
    
    def close(self) -> None:
        """Close the database connection"""
        try:
            if self.conn:
                self.conn.close()
        except sqlite3.Error as e:
            raise DatabaseError(f"Failed to close database: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize database
        db = ResearchDatabase()
        
        # Add a contributor
        contributor = db.add_contributor("John Doe", "john@example.com")
        print(f"Added contributor: {contributor.name}")
        
        # Add research data
        research_data = db.add_research_data(
            contributor_id=contributor.id,
            data_type="survey",
            content="Survey results about user preferences",
            points=20,
            royalties=5.0
        )
        print(f"Added research data: {research_data.data_type}")
        
        # Verify data
        db.verify_data
