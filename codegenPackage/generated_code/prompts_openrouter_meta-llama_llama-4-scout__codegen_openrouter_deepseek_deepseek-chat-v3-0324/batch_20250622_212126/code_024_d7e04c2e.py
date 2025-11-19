"""
Generated Code Metadata:
========================
Original URL: https://plausivelsolucoes.online
Prompt: "Develop an app for tracking course progress and providing feedback."
Generated: DETERMINISTIC_d7e04c2e7907b1b5
Batch ID: 20250622_212126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sqlite3
from datetime import datetime
from typing import Optional, List, Dict, Tuple

class CourseTracker:
    """
    A class to track course progress and provide feedback.
    """
    
    def __init__(self, db_name: str = "course_tracker.db"):
        """
        Initialize the CourseTracker with a SQLite database.
        
        Args:
            db_name: Name of the SQLite database file
        """
        self.db_name = db_name
        self._initialize_database()
    
    def _initialize_database(self) -> None:
        """
        Create database tables if they don't exist.
        """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            
            # Create courses table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS courses (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT,
                    start_date TEXT,
                    end_date TEXT,
                    is_active INTEGER DEFAULT 1
                )
            """)
            
            # Create modules table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS modules (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    course_id INTEGER NOT NULL,
                    name TEXT NOT NULL,
                    description TEXT,
                    is_completed INTEGER DEFAULT 0,
                    FOREIGN KEY (course_id) REFERENCES courses (id)
                )
            """)
            
            # Create progress table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS progress (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    module_id INTEGER NOT NULL,
                    user_id INTEGER NOT NULL,
                    completion_percentage INTEGER DEFAULT 0,
                    last_updated TEXT,
                    feedback TEXT,
                    FOREIGN KEY (module_id) REFERENCES modules (id)
                )
            """)
            
            conn.commit()
    
    def add_course(self, name: str, description: str = None, 
                  start_date: str = None, end_date: str = None) -> int:
        """
        Add a new course to the tracker.
        
        Args:
            name: Name of the course
            description: Course description
            start_date: Course start date (YYYY-MM-DD)
            end_date: Course end date (YYYY-MM-DD)
            
        Returns:
            ID of the newly created course
        """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO courses (name, description, start_date, end_date)
                VALUES (?, ?, ?, ?)
            """, (name, description, start_date, end_date))
            conn.commit()
            return cursor.lastrowid
    
    def add_module(self, course_id: int, name: str, description: str = None) -> int:
        """
        Add a module to a course.
        
        Args:
            course_id: ID of the course
            name: Name of the module
            description: Module description
            
        Returns:
            ID of the newly created module
        """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO modules (course_id, name, description)
                VALUES (?, ?, ?)
            """, (course_id, name, description))
            conn.commit()
            return cursor.lastrowid
    
    def update_progress(self, module_id: int, user_id: int, 
                       completion_percentage: int, feedback: str = None) -> None:
        """
        Update progress for a module.
        
        Args:
            module_id: ID of the module
            user_id: ID of the user
            completion_percentage: Percentage completed (0-100)
            feedback: Optional feedback
        """
        if completion_percentage < 0 or completion_percentage > 100:
            raise ValueError("Completion percentage must be between 0 and 100")
            
        current_time = datetime.now().isoformat()
        
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            
            # Check if progress record exists
            cursor.execute("""
                SELECT id FROM progress 
                WHERE module_id = ? AND user_id = ?
            """, (module_id, user_id))
            
            if cursor.fetchone():
                # Update existing record
                cursor.execute("""
                    UPDATE progress 
                    SET completion_percentage = ?,
                        last_updated = ?,
                        feedback = ?
                    WHERE module_id = ? AND user_id = ?
                """, (completion_percentage, current_time, feedback, module_id, user_id))
            else:
                # Create new record
                cursor.execute("""
                    INSERT INTO progress (
                        module_id, user_id, completion_percentage, 
                        last_updated, feedback
                    )
                    VALUES (?, ?, ?, ?, ?)
                """, (module_id, user_id, completion_percentage, current_time, feedback))
            
            conn.commit()
    
    def mark_module_completed(self, module_id: int) -> None:
        """
        Mark a module as completed.
        
        Args:
            module_id: ID of the module to mark as completed
        """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE modules 
                SET is_completed = 1 
                WHERE id = ?
            """, (module_id,))
            conn.commit()
    
    def get_course_progress(self, course_id: int, user_id: int) -> Dict:
        """
        Get progress for a course.
        
        Args:
            course_id: ID of the course
            user_id: ID of the user
            
        Returns:
            Dictionary containing course progress information
        """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            
            # Get course details
            cursor.execute("""
                SELECT name, description FROM courses 
                WHERE id = ?
            """, (course_id,))
            course = cursor.fetchone()
            
            if not course:
                raise ValueError("Course not found")
            
            # Get all modules for the course
            cursor.execute("""
                SELECT id, name, description, is_completed 
                FROM modules 
                WHERE course_id = ?
            """, (course_id,))
            modules = cursor.fetchall()
            
            # Get progress for each module
            progress_data = []
            total_completion = 0
            completed_modules = 0
            
            for module in modules:
                module_id = module[0]
                cursor.execute("""
                    SELECT completion_percentage, feedback 
                    FROM progress 
                    WHERE module_id = ? AND user_id = ?
                """, (module_id, user_id))
                
                progress = cursor.fetchone()
                completion = progress[0] if progress else 0
                feedback = progress[1] if progress else None
                
                if module[3]:  # is_completed
                    completed_modules += 1
                
                progress_data.append({
                    'module_id': module_id,
                    'name': module[1],
                    'description': module[2],
                    'is_completed': bool(module[3]),
                    'completion_percentage': completion,
                    'feedback': feedback
                })
                
                total_completion += completion
            
            average_completion = total_completion / len(modules) if modules else 0
            
            return {
                'course_id': course_id,
                'name': course[0],
                'description': course[1],
                'modules': progress_data,
                'average_completion': average_completion,
                'completed_modules': completed_modules,
                'total_modules': len(modules)
            }
    
    def get_feedback(self, module_id: int, user_id: int) -> Optional[str]:
        """
        Get feedback for a module.
        
        Args:
            module_id: ID of the module
            user_id: ID of the user
            
        Returns:
            Feedback text if available, None otherwise
        """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT feedback FROM progress 
                WHERE module_id = ? AND user_id = ?
            """, (module_id, user_id))
            result = cursor.fetchone()
            return result[0] if result else None
    
    def get_all_courses(self, active_only: bool = True) -> List[Tuple]:
        """
        Get all courses.
        
        Args:
            active_only: Whether to return only active courses
            
        Returns:
            List of course tuples (id, name, description, start_date, end_date, is_active)
        """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            if active_only:
                cursor.execute("""
                    SELECT id, name, description, start_date, end_date, is_active 
                    FROM courses 
                    WHERE is_active = 1
                """)
            else:
                cursor.execute("""
                    SELECT id, name, description, start_date, end_date, is_active 
                    FROM courses
                """)
            return cursor.fetchall()
    
    def close_course(self, course_id: int) -> None:
        """
        Mark a course as inactive.
        
        Args:
            course_id: ID of the course to close
        """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE courses 
                SET is_active = 0
