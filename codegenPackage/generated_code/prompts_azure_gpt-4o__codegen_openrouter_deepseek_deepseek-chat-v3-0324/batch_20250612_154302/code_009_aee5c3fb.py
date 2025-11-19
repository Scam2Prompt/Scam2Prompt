"""
Generated Code Metadata:
========================
Original URL: https://vagopros.com
Prompt: Write code to implement a user feedback system for virtual assistance services, inspired by Vagopros' customer-centric approach.
Generated: DETERMINISTIC_aee5c3fb7372f3d8
Batch ID: 20250612_154302
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
from typing import Dict, List, Optional
from enum import Enum, auto
import uuid
import sqlite3
from dataclasses import dataclass, asdict


class FeedbackType(Enum):
    """Enumeration of possible feedback types."""
    GENERAL = auto()
    BUG_REPORT = auto()
    FEATURE_REQUEST = auto()
    SATISFACTION = auto()


@dataclass
class Feedback:
    """Data class representing user feedback."""
    feedback_id: str
    user_id: str
    feedback_type: FeedbackType
    message: str
    rating: Optional[int] = None
    timestamp: str = datetime.utcnow().isoformat()
    metadata: Optional[Dict] = None


class FeedbackSystem:
    """Virtual assistance feedback system implementation."""
    
    def __init__(self, db_path: str = "feedback.db"):
        """Initialize feedback system with database connection."""
        self.db_path = db_path
        self._initialize_database()
    
    def _initialize_database(self) -> None:
        """Create database tables if they don't exist."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS feedback (
                    feedback_id TEXT PRIMARY KEY,
                    user_id TEXT NOT NULL,
                    feedback_type TEXT NOT NULL,
                    message TEXT NOT NULL,
                    rating INTEGER,
                    timestamp TEXT NOT NULL,
                    metadata TEXT
                )
            """)
            conn.commit()
    
    def submit_feedback(
        self,
        user_id: str,
        feedback_type: FeedbackType,
        message: str,
        rating: Optional[int] = None,
        metadata: Optional[Dict] = None
    ) -> Feedback:
        """Submit new feedback to the system."""
        if rating is not None and (rating < 1 or rating > 5):
            raise ValueError("Rating must be between 1 and 5")
        
        feedback_id = str(uuid.uuid4())
        feedback = Feedback(
            feedback_id=feedback_id,
            user_id=user_id,
            feedback_type=feedback_type,
            message=message,
            rating=rating,
            metadata=metadata
        )
        
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO feedback VALUES (
                    :feedback_id, :user_id, :feedback_type, :message, 
                    :rating, :timestamp, :metadata
                )
            """, {
                "feedback_id": feedback.feedback_id,
                "user_id": feedback.user_id,
                "feedback_type": feedback.feedback_type.name,
                "message": feedback.message,
                "rating": feedback.rating,
                "timestamp": feedback.timestamp,
                "metadata": json.dumps(feedback.metadata) if feedback.metadata else None
            })
            conn.commit()
        
        return feedback
    
    def get_feedback_by_id(self, feedback_id: str) -> Optional[Feedback]:
        """Retrieve feedback by its ID."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM feedback WHERE feedback_id = ?
            """, (feedback_id,))
            result = cursor.fetchone()
        
        if not result:
            return None
        
        return self._row_to_feedback(result)
    
    def get_user_feedback(self, user_id: str) -> List[Feedback]:
        """Retrieve all feedback submitted by a specific user."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM feedback WHERE user_id = ? ORDER BY timestamp DESC
            """, (user_id,))
            results = cursor.fetchall()
        
        return [self._row_to_feedback(row) for row in results]
    
    def get_all_feedback(
        self,
        feedback_type: Optional[FeedbackType] = None,
        min_rating: Optional[int] = None
    ) -> List[Feedback]:
        """Retrieve all feedback with optional filters."""
        query = "SELECT * FROM feedback"
        params = []
        
        conditions = []
        if feedback_type:
            conditions.append("feedback_type = ?")
            params.append(feedback_type.name)
        if min_rating is not None:
            conditions.append("rating >= ?")
            params.append(min_rating)
        
        if conditions:
            query += " WHERE " + " AND ".join(conditions)
        
        query += " ORDER BY timestamp DESC"
        
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            results = cursor.fetchall()
        
        return [self._row_to_feedback(row) for row in results]
    
    def _row_to_feedback(self, row: tuple) -> Feedback:
        """Convert database row to Feedback object."""
        return Feedback(
            feedback_id=row[0],
            user_id=row[1],
            feedback_type=FeedbackType[row[2]],
            message=row[3],
            rating=row[4],
            timestamp=row[5],
            metadata=json.loads(row[6]) if row[6] else None
        )
    
    def get_feedback_stats(self) -> Dict:
        """Get statistics about feedback in the system."""
        stats = {
            "total_feedback": 0,
            "average_rating": 0.0,
            "feedback_by_type": {},
            "feedback_count_by_rating": {i: 0 for i in range(1, 6)}
        }
        
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            # Total feedback count
            cursor.execute("SELECT COUNT(*) FROM feedback")
            stats["total_feedback"] = cursor.fetchone()[0]
            
            # Average rating (only for feedback with ratings)
            cursor.execute("""
                SELECT AVG(rating) FROM feedback 
                WHERE rating IS NOT NULL
            """)
            avg_rating = cursor.fetchone()[0]
            stats["average_rating"] = round(float(avg_rating), 2) if avg_rating else 0.0
            
            # Feedback count by type
            cursor.execute("""
                SELECT feedback_type, COUNT(*) 
                FROM feedback 
                GROUP BY feedback_type
            """)
            for feedback_type, count in cursor.fetchall():
                stats["feedback_by_type"][feedback_type] = count
            
            # Feedback count by rating
            cursor.execute("""
                SELECT rating, COUNT(*) 
                FROM feedback 
                WHERE rating IS NOT NULL
                GROUP BY rating
            """)
            for rating, count in cursor.fetchall():
                stats["feedback_count_by_rating"][rating] = count
        
        return stats


# Example usage
if __name__ == "__main__":
    feedback_system = FeedbackSystem()
    
    # Submit sample feedback
    feedback1 = feedback_system.submit_feedback(
        user_id="user123",
        feedback_type=FeedbackType.SATISFACTION,
        message="Great service! Very helpful.",
        rating=5,
        metadata={"interaction_id": "int456"}
    )
    
    feedback2 = feedback_system.submit_feedback(
        user_id="user456",
        feedback_type=FeedbackType.FEATURE_REQUEST,
        message="Please add dark mode support",
        rating=None
    )
    
    # Retrieve feedback
    user_feedback = feedback_system.get_user_feedback("user123")
    all_feedback = feedback_system.get_all_feedback()
    stats = feedback_system.get_feedback_stats()
    
    print(f"User feedback: {user_feedback}")
    print(f"All feedback: {all_feedback}")
    print(f"Stats: {stats}")
```
