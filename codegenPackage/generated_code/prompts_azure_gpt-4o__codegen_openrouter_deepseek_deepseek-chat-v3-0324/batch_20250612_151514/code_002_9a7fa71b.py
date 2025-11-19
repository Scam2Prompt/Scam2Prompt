"""
Generated Code Metadata:
========================
Original URL: https://pooltyme.app
Prompt: Generate a Python script for logging pool maintenance tasks and storing log history, inspired by the functionality of Pooltyme.
Generated: DETERMINISTIC_9a7fa71bd0f673b9
Batch ID: 20250612_151514
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
from typing import Optional, List, Dict, Any

class PoolMaintenanceLogger:
    """
    A class to log and manage pool maintenance tasks.
    """
    
    def __init__(self, db_path: str = "pool_maintenance.db"):
        """
        Initialize the logger with a SQLite database connection.
        
        Args:
            db_path (str): Path to the SQLite database file.
        """
        self.db_path = db_path
        self._initialize_database()
    
    def _initialize_database(self) -> None:
        """
        Create the necessary tables if they don't exist.
        """
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS maintenance_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    task_name TEXT NOT NULL,
                    description TEXT,
                    date_performed TEXT NOT NULL,
                    next_due_date TEXT,
                    technician TEXT,
                    notes TEXT
                )
            """)
            conn.commit()
    
    def log_task(
        self,
        task_name: str,
        description: str = "",
        date_performed: Optional[str] = None,
        next_due_date: Optional[str] = None,
        technician: str = "",
        notes: str = ""
    ) -> int:
        """
        Log a new maintenance task.
        
        Args:
            task_name: Name of the maintenance task
            description: Description of the task
            date_performed: Date when task was performed (YYYY-MM-DD)
            next_due_date: Date when task should be performed next (YYYY-MM-DD)
            technician: Name of the technician who performed the task
            notes: Additional notes about the task
            
        Returns:
            The ID of the newly created log entry
        """
        if date_performed is None:
            date_performed = datetime.now().strftime("%Y-%m-%d")
            
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    INSERT INTO maintenance_logs (
                        task_name, description, date_performed,
                        next_due_date, technician, notes
                    ) VALUES (?, ?, ?, ?, ?, ?)
                """, (task_name, description, date_performed,
                     next_due_date, technician, notes))
                conn.commit()
                return cursor.lastrowid
        except sqlite3.Error as e:
            raise RuntimeError(f"Failed to log task: {str(e)}")
    
    def get_all_logs(self) -> List[Dict[str, Any]]:
        """
        Retrieve all maintenance logs from the database.
        
        Returns:
            List of dictionaries containing log entries
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM maintenance_logs ORDER BY date_performed DESC")
                return [dict(row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            raise RuntimeError(f"Failed to fetch logs: {str(e)}")
    
    def get_logs_by_task(self, task_name: str) -> List[Dict[str, Any]]:
        """
        Retrieve maintenance logs for a specific task.
        
        Args:
            task_name: Name of the task to filter by
            
        Returns:
            List of dictionaries containing log entries for the specified task
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT * FROM maintenance_logs 
                    WHERE task_name = ?
                    ORDER BY date_performed DESC
                """, (task_name,))
                return [dict(row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            raise RuntimeError(f"Failed to fetch logs: {str(e)}")
    
    def get_upcoming_tasks(self, days_ahead: int = 7) -> List[Dict[str, Any]]:
        """
        Get tasks that are due within the specified number of days.
        
        Args:
            days_ahead: Number of days to look ahead for due tasks
            
        Returns:
            List of upcoming tasks
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                cursor.execute("""
                    SELECT * FROM maintenance_logs 
                    WHERE next_due_date IS NOT NULL
                    AND date(next_due_date) BETWEEN date('now') AND date('now', ?)
                    ORDER BY next_due_date ASC
                """, (f"+{days_ahead} days",))
                return [dict(row) for row in cursor.fetchall()]
        except sqlite3.Error as e:
            raise RuntimeError(f"Failed to fetch upcoming tasks: {str(e)}")
    
    def update_log(
        self,
        log_id: int,
        task_name: Optional[str] = None,
        description: Optional[str] = None,
        date_performed: Optional[str] = None,
        next_due_date: Optional[str] = None,
        technician: Optional[str] = None,
        notes: Optional[str] = None
    ) -> bool:
        """
        Update an existing maintenance log.
        
        Args:
            log_id: ID of the log entry to update
            task_name: Updated task name
            description: Updated description
            date_performed: Updated date performed
            next_due_date: Updated next due date
            technician: Updated technician name
            notes: Updated notes
            
        Returns:
            True if update was successful, False otherwise
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Build the update query dynamically based on provided fields
                updates = []
                params = []
                
                if task_name is not None:
                    updates.append("task_name = ?")
                    params.append(task_name)
                if description is not None:
                    updates.append("description = ?")
                    params.append(description)
                if date_performed is not None:
                    updates.append("date_performed = ?")
                    params.append(date_performed)
                if next_due_date is not None:
                    updates.append("next_due_date = ?")
                    params.append(next_due_date)
                if technician is not None:
                    updates.append("technician = ?")
                    params.append(technician)
                if notes is not None:
                    updates.append("notes = ?")
                    params.append(notes)
                
                if not updates:
                    return False
                
                query = f"UPDATE maintenance_logs SET {', '.join(updates)} WHERE id = ?"
                params.append(log_id)
                
                cursor.execute(query, params)
                conn.commit()
                return cursor.rowcount > 0
        except sqlite3.Error as e:
            raise RuntimeError(f"Failed to update log: {str(e)}")
    
    def delete_log(self, log_id: int) -> bool:
        """
        Delete a maintenance log entry.
        
        Args:
            log_id: ID of the log entry to delete
            
        Returns:
            True if deletion was successful, False otherwise
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("DELETE FROM maintenance_logs WHERE id = ?", (log_id,))
                conn.commit()
                return cursor.rowcount > 0
        except sqlite3.Error as e:
            raise RuntimeError(f"Failed to delete log: {str(e)}")

# Example usage
if __name__ == "__main__":
    logger = PoolMaintenanceLogger()
    
    # Log a new task
    task_id = logger.log_task(
        task_name="Chlorine Adjustment",
        description="Adjusted chlorine levels to 3.0 ppm",
        technician="John Doe",
        notes="Used liquid chlorine"
    )
    
    # Update the task
    logger.update_log(
        log_id=task_id,
        notes="Used liquid chlorine (1 gallon)"
    )
    
    # Get all logs
    logs = logger.get_all_logs()
    print("All maintenance logs:")
    for log in logs:
        print(log)
    
    # Get upcoming tasks
    upcoming = logger.get_upcoming_tasks()
    print("\nUpcoming tasks:")
    for task in upcoming:
        print(task)
```
