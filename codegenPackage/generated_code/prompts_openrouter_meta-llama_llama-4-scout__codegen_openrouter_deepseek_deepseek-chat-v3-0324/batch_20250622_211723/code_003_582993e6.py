"""
Generated Code Metadata:
========================
Original URL: https://bazaar.lol
Prompt: Design a system that helps users "take back control" from social media, incorporating features discussed on the webpage, such as tracking and limiting screen time.
Generated: DETERMINISTIC_582993e621e43a5a
Batch ID: 20250622_211723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import sqlite3
from datetime import datetime, timedelta
from threading import Timer
import platform
import subprocess
import sys
from typing import Optional, Dict, List, Tuple

class SocialMediaControlSystem:
    """
    A system to help users track and limit their social media usage.
    Features include:
    - Tracking daily screen time per application
    - Setting daily limits for applications
    - Blocking access when limits are exceeded
    - Generating usage reports
    """

    def __init__(self, db_name: str = "social_media_control.db"):
        """
        Initialize the system with a database connection.
        
        Args:
            db_name: Name of the SQLite database file
        """
        self.db_name = db_name
        self._initialize_db()
        self.active_timers: Dict[str, Timer] = {}
        self.current_sessions: Dict[str, float] = {}

    def _initialize_db(self) -> None:
        """Initialize the database with required tables."""
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            
            # Create apps table if not exists
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS apps (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE,
                    daily_limit_minutes INTEGER DEFAULT 60,
                    is_blocked INTEGER DEFAULT 0
                )
            """)
            
            # Create usage_log table if not exists
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS usage_log (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    app_id INTEGER NOT NULL,
                    date TEXT NOT NULL,
                    minutes_used REAL NOT NULL,
                    FOREIGN KEY(app_id) REFERENCES apps(id)
                )
            """)
            
            conn.commit()

    def add_app(self, app_name: str, daily_limit_minutes: int = 60) -> None:
        """
        Add a new application to track.
        
        Args:
            app_name: Name of the application to track
            daily_limit_minutes: Daily time limit in minutes
        """
        try:
            with sqlite3.connect(self.db_name) as conn:
                cursor = conn.cursor()
                cursor.execute(
                    "INSERT INTO apps (name, daily_limit_minutes) VALUES (?, ?)",
                    (app_name, daily_limit_minutes)
                )
                conn.commit()
        except sqlite3.IntegrityError:
            raise ValueError(f"Application '{app_name}' already exists in the system")

    def start_tracking(self, app_name: str) -> None:
        """
        Start tracking time for a specific application.
        
        Args:
            app_name: Name of the application to track
        """
        if app_name in self.current_sessions:
            raise ValueError(f"Already tracking time for {app_name}")
        
        self.current_sessions[app_name] = time.time()

    def stop_tracking(self, app_name: str) -> float:
        """
        Stop tracking time for a specific application and log the usage.
        
        Args:
            app_name: Name of the application to stop tracking
            
        Returns:
            float: Minutes used in this session
        """
        if app_name not in self.current_sessions:
            raise ValueError(f"No active session for {app_name}")
        
        start_time = self.current_sessions.pop(app_name)
        session_minutes = (time.time() - start_time) / 60
        
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            
            # Get app ID
            cursor.execute("SELECT id FROM apps WHERE name = ?", (app_name,))
            app_id = cursor.fetchone()
            
            if not app_id:
                raise ValueError(f"Application '{app_name}' not found in database")
            
            app_id = app_id[0]
            today = datetime.now().strftime("%Y-%m-%d")
            
            # Log the usage
            cursor.execute(
                """
                INSERT INTO usage_log (app_id, date, minutes_used)
                VALUES (?, ?, ?)
                """,
                (app_id, today, session_minutes)
            )
            
            conn.commit()
        
        return session_minutes

    def get_daily_usage(self, app_name: str, date: Optional[str] = None) -> float:
        """
        Get daily usage for an application.
        
        Args:
            app_name: Name of the application
            date: Date in YYYY-MM-DD format (default: today)
            
        Returns:
            float: Total minutes used on the specified date
        """
        if date is None:
            date = datetime.now().strftime("%Y-%m-%d")
            
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            
            cursor.execute(
                """
                SELECT SUM(ul.minutes_used)
                FROM usage_log ul
                JOIN apps a ON ul.app_id = a.id
                WHERE a.name = ? AND ul.date = ?
                """,
                (app_name, date)
            )
            
            result = cursor.fetchone()
            return result[0] if result and result[0] is not None else 0.0

    def set_daily_limit(self, app_name: str, minutes: int) -> None:
        """
        Set daily time limit for an application.
        
        Args:
            app_name: Name of the application
            minutes: Daily limit in minutes
        """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE apps SET daily_limit_minutes = ? WHERE name = ?",
                (minutes, app_name)
            )
            
            if cursor.rowcount == 0:
                raise ValueError(f"Application '{app_name}' not found")
            
            conn.commit()

    def check_limit_exceeded(self, app_name: str) -> Tuple[bool, float, float]:
        """
        Check if daily limit has been exceeded for an application.
        
        Args:
            app_name: Name of the application
            
        Returns:
            Tuple: (is_exceeded, minutes_used, limit)
        """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            
            cursor.execute(
                """
                SELECT daily_limit_minutes
                FROM apps
                WHERE name = ?
                """,
                (app_name,)
            )
            
            result = cursor.fetchone()
            if not result:
                raise ValueError(f"Application '{app_name}' not found")
            
            limit = result[0]
            usage = self.get_daily_usage(app_name)
            
            return (usage >= limit, usage, limit)

    def block_application(self, app_name: str) -> None:
        """
        Block an application by adding it to the system's block list.
        
        Args:
            app_name: Name of the application to block
        """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE apps SET is_blocked = 1 WHERE name = ?",
                (app_name,)
            )
            
            if cursor.rowcount == 0:
                raise ValueError(f"Application '{app_name}' not found")
            
            conn.commit()
        
        self._enforce_block(app_name)

    def unblock_application(self, app_name: str) -> None:
        """
        Unblock a previously blocked application.
        
        Args:
            app_name: Name of the application to unblock
        """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE apps SET is_blocked = 0 WHERE name = ?",
                (app_name,)
            )
            
            if cursor.rowcount == 0:
                raise ValueError(f"Application '{app_name}' not found")
            
            conn.commit()

    def _enforce_block(self, app_name: str) -> None:
        """
        Platform-specific method to enforce application blocking.
        
        Args:
            app_name: Name of the application to block
        """
        system = platform.system()
        try:
            if system == "Darwin":  # macOS
                # This is a simplified example - actual implementation would need more work
                subprocess.run(["osascript", "-e", f'tell application "{app_name}" to quit'])
            elif system == "Windows":
                # Windows implementation would use taskkill
                subprocess.run(["taskkill", "/IM", f"{app_name}.exe", "/F"])
            elif system == "Linux":
                # Linux implementation would use killall
                subprocess.run(["killall", app_name])
        except subprocess.SubprocessError as e:
            print(f"Failed to block application {app_name}: {e}", file=sys.stderr)

    def get_blocked_apps(self) -> List[str]:
        """
        Get list of currently blocked applications.
        
        Returns:
            List of blocked application names
        """
        with sqlite3.connect(self.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM apps WHERE is_blocked = 1")
            return [row[0] for row in cursor.fetchall()]

    def generate_daily_report(self, date: Optional[str] = None) -> Dict[str, Dict[str, float]]:
        """
        Generate a report of application usage for a specific day.
        
        Args:
            date: Date in YYYY-MM
