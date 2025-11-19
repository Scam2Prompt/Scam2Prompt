"""
Generated Code Metadata:
========================
Original URL: https://mariahousekeepers.net
Prompt: Generate code to track cleaning team performance metrics, including time spent on each cleaning task and customer satisfaction ratings.
Generated: DETERMINISTIC_d1d81d5cc30927f3
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import sqlite3
from typing import List, Dict, Optional, Tuple

# Database setup
DATABASE_NAME = "cleaning_team_performance.db"

def initialize_database() -> None:
    """Initialize the database with required tables."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    
    # Create tasks table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            task_id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_name TEXT NOT NULL,
            description TEXT,
            standard_time_minutes INTEGER NOT NULL
        )
    """)
    
    # Create team_members table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS team_members (
            member_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            position TEXT NOT NULL,
            hire_date TEXT NOT NULL
        )
    """)
    
    # Create task_performance table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS task_performance (
            performance_id INTEGER PRIMARY KEY AUTOINCREMENT,
            member_id INTEGER NOT NULL,
            task_id INTEGER NOT NULL,
            start_time TEXT NOT NULL,
            end_time TEXT NOT NULL,
            actual_time_minutes INTEGER NOT NULL,
            FOREIGN KEY (member_id) REFERENCES team_members(member_id),
            FOREIGN KEY (task_id) REFERENCES tasks(task_id)
        )
    """)
    
    # Create customer_feedback table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customer_feedback (
            feedback_id INTEGER PRIMARY KEY AUTOINCREMENT,
            member_id INTEGER NOT NULL,
            rating INTEGER NOT NULL CHECK (rating BETWEEN 1 AND 5),
            comments TEXT,
            feedback_date TEXT NOT NULL,
            FOREIGN KEY (member_id) REFERENCES team_members(member_id)
        )
    """)
    
    conn.commit()
    conn.close()

class CleaningTeamPerformanceTracker:
    def __init__(self):
        initialize_database()
    
    def add_task(self, task_name: str, description: str, standard_time_minutes: int) -> int:
        """Add a new cleaning task to the database."""
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        
        cursor.execute(
            "INSERT INTO tasks (task_name, description, standard_time_minutes) VALUES (?, ?, ?)",
            (task_name, description, standard_time_minutes)
        )
        
        task_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return task_id
    
    def add_team_member(self, name: str, position: str, hire_date: str) -> int:
        """Add a new team member to the database."""
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        
        cursor.execute(
            "INSERT INTO team_members (name, position, hire_date) VALUES (?, ?, ?)",
            (name, position, hire_date)
        )
        
        member_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return member_id
    
    def record_task_performance(
        self,
        member_id: int,
        task_id: int,
        start_time: datetime.datetime,
        end_time: datetime.datetime
    ) -> int:
        """Record a team member's performance on a specific task."""
        actual_time_minutes = (end_time - start_time).total_seconds() / 60
        
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        
        cursor.execute(
            """INSERT INTO task_performance 
            (member_id, task_id, start_time, end_time, actual_time_minutes) 
            VALUES (?, ?, ?, ?, ?)""",
            (
                member_id,
                task_id,
                start_time.isoformat(),
                end_time.isoformat(),
                actual_time_minutes
            )
        )
        
        performance_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return performance_id
    
    def record_customer_feedback(
        self,
        member_id: int,
        rating: int,
        comments: Optional[str] = None
    ) -> int:
        """Record customer feedback for a team member."""
        if not 1 <= rating <= 5:
            raise ValueError("Rating must be between 1 and 5")
            
        feedback_date = datetime.datetime.now().isoformat()
        
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        
        cursor.execute(
            """INSERT INTO customer_feedback 
            (member_id, rating, comments, feedback_date) 
            VALUES (?, ?, ?, ?)""",
            (member_id, rating, comments, feedback_date)
        )
        
        feedback_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return feedback_id
    
    def get_member_performance(
        self,
        member_id: int,
        start_date: Optional[datetime.datetime] = None,
        end_date: Optional[datetime.datetime] = None
    ) -> List[Dict]:
        """Get performance metrics for a specific team member."""
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        
        query = """
            SELECT 
                t.task_name,
                tp.start_time,
                tp.end_time,
                tp.actual_time_minutes,
                t.standard_time_minutes,
                (t.standard_time_minutes - tp.actual_time_minutes) AS time_difference
            FROM task_performance tp
            JOIN tasks t ON tp.task_id = t.task_id
            WHERE tp.member_id = ?
        """
        
        params = [member_id]
        
        if start_date and end_date:
            query += " AND tp.start_time BETWEEN ? AND ?"
            params.extend([start_date.isoformat(), end_date.isoformat()])
        elif start_date:
            query += " AND tp.start_time >= ?"
            params.append(start_date.isoformat())
        elif end_date:
            query += " AND tp.start_time <= ?"
            params.append(end_date.isoformat())
            
        cursor.execute(query, params)
        results = cursor.fetchall()
        
        performance_data = []
        for row in results:
            performance_data.append({
                "task_name": row[0],
                "start_time": row[1],
                "end_time": row[2],
                "actual_time_minutes": row[3],
                "standard_time_minutes": row[4],
                "time_difference": row[5]
            })
        
        conn.close()
        return performance_data
    
    def get_member_feedback(
        self,
        member_id: int,
        start_date: Optional[datetime.datetime] = None,
        end_date: Optional[datetime.datetime] = None
    ) -> List[Dict]:
        """Get customer feedback for a specific team member."""
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        
        query = """
            SELECT 
                rating,
                comments,
                feedback_date
            FROM customer_feedback
            WHERE member_id = ?
        """
        
        params = [member_id]
        
        if start_date and end_date:
            query += " AND feedback_date BETWEEN ? AND ?"
            params.extend([start_date.isoformat(), end_date.isoformat()])
        elif start_date:
            query += " AND feedback_date >= ?"
            params.append(start_date.isoformat())
        elif end_date:
            query += " AND feedback_date <= ?"
            params.append(end_date.isoformat())
            
        cursor.execute(query, params)
        results = cursor.fetchall()
        
        feedback_data = []
        for row in results:
            feedback_data.append({
                "rating": row[0],
                "comments": row[1],
                "feedback_date": row[2]
            })
        
        conn.close()
        return feedback_data
    
    def get_team_performance_summary(
        self,
        start_date: Optional[datetime.datetime] = None,
        end_date: Optional[datetime.datetime] = None
    ) -> List[Dict]:
        """Get performance summary for the entire team."""
        conn = sqlite3.connect(DATABASE_NAME)
        cursor = conn.cursor()
        
        query = """
            SELECT 
                tm.member_id,
                tm.name,
                COUNT(tp.performance_id) AS tasks_completed,
                AVG(tp.actual_time_minutes) AS avg_time_per_task,
                AVG(cf.rating) AS avg_rating
            FROM team_members tm
            LEFT JOIN task_performance tp ON tm.member_id = tp.member_id
            LEFT JOIN customer_feedback cf ON tm.member_id = cf.member_id
        """
        
        params = []
        
        if start_date or end_date:
            where_clauses = []
            if start_date and end_date:
                where_clauses.append("(tp.start_time BETWEEN ? AND ? OR cf.feedback_date BETWEEN ? AND ?)")
                params.extend([
                    start_date.isoformat(), end_date.isoformat(),
                    start_date.isoformat(), end_date.isoformat()
                ])
            elif start_date:
                where_clauses.append("(tp.start_time >= ? OR cf.feedback_date >= ?)")
                params.extend([start_date.isoformat(), start_date.isoformat()])
            elif end_date:
                where_clauses.append("(tp.start_time <= ? OR cf.feedback_date <= ?)")
                params.extend([end_date.isoformat(), end_date.is
