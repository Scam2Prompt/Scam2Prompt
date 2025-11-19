"""
Generated Code Metadata:
========================
Original URL: https://www.projectortechnology.gr
Prompt: Create a program to track and log the usage of interactive kits in an educational setting, referencing the interactive education products offered by Projector Technology.
Generated: DETERMINISTIC_1b4da32dd5c136c7
Batch ID: 20250612_153246
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
import logging
from typing import Optional, Dict, List

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('kit_usage.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger('KitTracker')

class KitTracker:
    """
    A class to track and log the usage of interactive educational kits.
    """
    
    def __init__(self, db_path: str = 'kit_usage.db'):
        """
        Initialize the KitTracker with a SQLite database connection.
        
        Args:
            db_path (str): Path to the SQLite database file.
        """
        self.db_path = db_path
        self._initialize_database()
        
    def _initialize_database(self) -> None:
        """
        Create the database tables if they don't exist.
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Create kits table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS kits (
                        kit_id TEXT PRIMARY KEY,
                        name TEXT NOT NULL,
                        description TEXT,
                        category TEXT,
                        date_added TEXT NOT NULL
                    )
                ''')
                
                # Create usage_log table
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS usage_log (
                        log_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        kit_id TEXT NOT NULL,
                        user_id TEXT NOT NULL,
                        start_time TEXT NOT NULL,
                        end_time TEXT,
                        duration_minutes INTEGER,
                        notes TEXT,
                        FOREIGN KEY (kit_id) REFERENCES kits (kit_id)
                    )
                ''')
                
                conn.commit()
                logger.info("Database initialized successfully")
                
        except sqlite3.Error as e:
            logger.error(f"Error initializing database: {e}")
            raise
    
    def add_kit(self, kit_id: str, name: str, description: str = None, category: str = None) -> bool:
        """
        Add a new interactive kit to the database.
        
        Args:
            kit_id (str): Unique identifier for the kit
            name (str): Name of the kit
            description (str, optional): Description of the kit
            category (str, optional): Category of the kit
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO kits (kit_id, name, description, category, date_added)
                    VALUES (?, ?, ?, ?, ?)
                ''', (kit_id, name, description, category, datetime.now().isoformat()))
                conn.commit()
                logger.info(f"Added new kit: {kit_id} - {name}")
                return True
        except sqlite3.Error as e:
            logger.error(f"Error adding kit {kit_id}: {e}")
            return False
    
    def log_usage(self, kit_id: str, user_id: str, notes: str = None) -> bool:
        """
        Log the start of kit usage.
        
        Args:
            kit_id (str): ID of the kit being used
            user_id (str): ID of the user
            notes (str, optional): Additional notes
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO usage_log (kit_id, user_id, start_time, notes)
                    VALUES (?, ?, ?, ?)
                ''', (kit_id, user_id, datetime.now().isoformat(), notes))
                conn.commit()
                logger.info(f"Logged usage start for kit {kit_id} by user {user_id}")
                return True
        except sqlite3.Error as e:
            logger.error(f"Error logging usage for kit {kit_id}: {e}")
            return False
    
    def end_usage(self, kit_id: str, user_id: str) -> bool:
        """
        Log the end of kit usage and calculate duration.
        
        Args:
            kit_id (str): ID of the kit
            user_id (str): ID of the user
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                
                # Get the most recent usage for this kit and user
                cursor.execute('''
                    SELECT log_id, start_time FROM usage_log
                    WHERE kit_id = ? AND user_id = ? AND end_time IS NULL
                    ORDER BY start_time DESC
                    LIMIT 1
                ''', (kit_id, user_id))
                
                result = cursor.fetchone()
                if not result:
                    logger.warning(f"No active usage found for kit {kit_id} and user {user_id}")
                    return False
                
                log_id, start_time = result
                start_datetime = datetime.fromisoformat(start_time)
                end_datetime = datetime.now()
                duration = int((end_datetime - start_datetime).total_seconds() / 60)
                
                cursor.execute('''
                    UPDATE usage_log
                    SET end_time = ?, duration_minutes = ?
                    WHERE log_id = ?
                ''', (end_datetime.isoformat(), duration, log_id))
                
                conn.commit()
                logger.info(f"Logged usage end for kit {kit_id} by user {user_id}. Duration: {duration} minutes")
                return True
                
        except sqlite3.Error as e:
            logger.error(f"Error ending usage for kit {kit_id}: {e}")
            return False
    
    def get_kit_usage(self, kit_id: str) -> List[Dict]:
        """
        Get usage history for a specific kit.
        
        Args:
            kit_id (str): ID of the kit
            
        Returns:
            List[Dict]: List of usage records as dictionaries
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                
                cursor.execute('''
                    SELECT * FROM usage_log
                    WHERE kit_id = ?
                    ORDER BY start_time DESC
                ''', (kit_id,))
                
                results = cursor.fetchall()
                return [dict(row) for row in results]
                
        except sqlite3.Error as e:
            logger.error(f"Error getting usage for kit {kit_id}: {e}")
            return []
    
    def get_all_kits(self) -> List[Dict]:
        """
        Get all registered kits.
        
        Returns:
            List[Dict]: List of all kits as dictionaries
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                
                cursor.execute('SELECT * FROM kits ORDER BY name')
                results = cursor.fetchall()
                return [dict(row) for row in results]
                
        except sqlite3.Error as e:
            logger.error(f"Error getting all kits: {e}")
            return []
    
    def generate_usage_report(self, start_date: str = None, end_date: str = None) -> List[Dict]:
        """
        Generate a usage report for all kits within a date range.
        
        Args:
            start_date (str, optional): Start date in ISO format
            end_date (str, optional): End date in ISO format
            
        Returns:
            List[Dict]: List of usage records as dictionaries
        """
        try:
            with sqlite3.connect(self.db_path) as conn:
                conn.row_factory = sqlite3.Row
                cursor = conn.cursor()
                
                query = '''
                    SELECT k.kit_id, k.name, 
                           COUNT(u.log_id) as usage_count,
                           SUM(u.duration_minutes) as total_minutes
                    FROM kits k
                    LEFT JOIN usage_log u ON k.kit_id = u.kit_id
                '''
                
                params = []
                
                if start_date or end_date:
                    query += ' WHERE '
                    conditions = []
                    
                    if start_date:
                        conditions.append('u.start_time >= ?')
                        params.append(start_date)
                    
                    if end_date:
                        conditions.append('u.start_time <= ?')
                        params.append(end_date)
                    
                    query += ' AND '.join(conditions)
                
                query += ' GROUP BY k.kit_id, k.name ORDER BY k.name'
                
                cursor.execute(query, params)
                results = cursor.fetchall()
                return [dict(row) for row in results]
                
        except sqlite3.Error as e:
            logger.error(f"Error generating usage report: {e}")
            return []

# Example usage
if __name__ == "__main__":
    tracker = KitTracker()
    
    # Add some example kits
    tracker.add_kit("kit001", "Interactive Math Kit", "Math learning tools", "Mathematics")
    tracker.add_kit("kit002", "Science Exploration Kit", "Hands-on science experiments", "Science")
    
    # Log usage
    tracker.log_usage("kit001", "user123", "Classroom activity")
    tracker.log_usage("kit002", "
