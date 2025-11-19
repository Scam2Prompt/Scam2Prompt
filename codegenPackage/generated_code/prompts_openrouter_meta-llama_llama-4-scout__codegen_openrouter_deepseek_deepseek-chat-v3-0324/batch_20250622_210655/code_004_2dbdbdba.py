"""
Generated Code Metadata:
========================
Original URL: https://thehashtagconsultants.com
Prompt: "Design a data management system to track and analyze call center metrics, such as customer satisfaction and first-call resolution rates, for a BPO provider like The Hashtag Consultants."
Generated: DETERMINISTIC_2dbdbdba4a7521f7
Batch ID: 20250622_210655
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
from typing import List, Dict, Optional, Tuple
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('call_center_metrics.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class CallCenterMetricsDB:
    """Database handler for call center metrics tracking."""
    
    def __init__(self, db_name: str = 'call_center_metrics.db'):
        """Initialize database connection and create tables if they don't exist."""
        self.db_name = db_name
        self.conn = None
        self._initialize_db()

    def _initialize_db(self) -> None:
        """Create database tables if they don't exist."""
        try:
            self.conn = sqlite3.connect(self.db_name)
            cursor = self.conn.cursor()
            
            # Create agents table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS agents (
                    agent_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL,
                    hire_date TEXT NOT NULL,
                    department TEXT NOT NULL
                )
            ''')
            
            # Create calls table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS calls (
                    call_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    agent_id INTEGER NOT NULL,
                    customer_id TEXT NOT NULL,
                    start_time TEXT NOT NULL,
                    end_time TEXT NOT NULL,
                    duration INTEGER NOT NULL,
                    resolution_status TEXT NOT NULL CHECK(resolution_status IN ('resolved', 'unresolved', 'escalated')),
                    satisfaction_score INTEGER CHECK(satisfaction_score BETWEEN 1 AND 5),
                    FOREIGN KEY (agent_id) REFERENCES agents (agent_id)
                )
            ''')
            
            # Create metrics table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS metrics (
                    metric_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    agent_id INTEGER NOT NULL,
                    date TEXT NOT NULL,
                    calls_handled INTEGER NOT NULL DEFAULT 0,
                    avg_duration REAL NOT NULL DEFAULT 0,
                    first_call_resolution_rate REAL NOT NULL DEFAULT 0,
                    avg_satisfaction_score REAL NOT NULL DEFAULT 0,
                    FOREIGN KEY (agent_id) REFERENCES agents (agent_id),
                    UNIQUE(agent_id, date)
                )
            ''')
            
            self.conn.commit()
            logger.info("Database initialized successfully")
            
        except sqlite3.Error as e:
            logger.error(f"Database initialization failed: {e}")
            raise
            
    def close(self) -> None:
        """Close database connection."""
        if self.conn:
            self.conn.close()
            logger.info("Database connection closed")

    def add_agent(self, name: str, email: str, hire_date: str, department: str) -> int:
        """Add a new agent to the database."""
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT INTO agents (name, email, hire_date, department)
                VALUES (?, ?, ?, ?)
            ''', (name, email, hire_date, department))
            self.conn.commit()
            agent_id = cursor.lastrowid
            logger.info(f"Added new agent: {name} (ID: {agent_id})")
            return agent_id
        except sqlite3.Error as e:
            logger.error(f"Failed to add agent: {e}")
            self.conn.rollback()
            raise

    def log_call(
        self,
        agent_id: int,
        customer_id: str,
        start_time: str,
        end_time: str,
        resolution_status: str,
        satisfaction_score: Optional[int] = None
    ) -> int:
        """Log a new call in the database."""
        try:
            # Calculate duration in seconds
            start = datetime.fromisoformat(start_time)
            end = datetime.fromisoformat(end_time)
            duration = int((end - start).total_seconds())
            
            cursor = self.conn.cursor()
            cursor.execute('''
                INSERT INTO calls (
                    agent_id, customer_id, start_time, end_time, duration,
                    resolution_status, satisfaction_score
                )
                VALUES (?, ?, ?, ?, ?, ?, ?)
            ''', (
                agent_id, customer_id, start_time, end_time, duration,
                resolution_status, satisfaction_score
            ))
            self.conn.commit()
            call_id = cursor.lastrowid
            logger.info(f"Logged new call (ID: {call_id}) for agent ID: {agent_id}")
            return call_id
        except (sqlite3.Error, ValueError) as e:
            logger.error(f"Failed to log call: {e}")
            self.conn.rollback()
            raise

    def calculate_daily_metrics(self, date: str = None) -> None:
        """Calculate and store daily metrics for all agents."""
        if not date:
            date = datetime.now().strftime('%Y-%m-%d')
            
        try:
            cursor = self.conn.cursor()
            
            # Get all agents
            cursor.execute('SELECT agent_id FROM agents')
            agents = cursor.fetchall()
            
            for (agent_id,) in agents:
                # Calculate calls handled
                cursor.execute('''
                    SELECT COUNT(*) FROM calls
                    WHERE agent_id = ? AND date(start_time) = ?
                ''', (agent_id, date))
                calls_handled = cursor.fetchone()[0]
                
                if calls_handled == 0:
                    continue
                
                # Calculate average duration
                cursor.execute('''
                    SELECT AVG(duration) FROM calls
                    WHERE agent_id = ? AND date(start_time) = ?
                ''', (agent_id, date))
                avg_duration = cursor.fetchone()[0]
                
                # Calculate first call resolution rate
                cursor.execute('''
                    SELECT COUNT(*) FROM calls
                    WHERE agent_id = ? AND date(start_time) = ? AND resolution_status = 'resolved'
                ''', (agent_id, date))
                resolved_calls = cursor.fetchone()[0]
                fcr_rate = (resolved_calls / calls_handled) * 100
                
                # Calculate average satisfaction score
                cursor.execute('''
                    SELECT AVG(satisfaction_score) FROM calls
                    WHERE agent_id = ? AND date(start_time) = ? AND satisfaction_score IS NOT NULL
                ''', (agent_id, date))
                avg_satisfaction = cursor.fetchone()[0] or 0
                
                # Insert or update metrics
                cursor.execute('''
                    INSERT OR REPLACE INTO metrics (
                        agent_id, date, calls_handled, avg_duration,
                        first_call_resolution_rate, avg_satisfaction_score
                    )
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (
                    agent_id, date, calls_handled, avg_duration,
                    fcr_rate, avg_satisfaction
                ))
            
            self.conn.commit()
            logger.info(f"Calculated daily metrics for {date}")
            
        except sqlite3.Error as e:
            logger.error(f"Failed to calculate daily metrics: {e}")
            self.conn.rollback()
            raise

    def get_agent_metrics(
        self,
        agent_id: int,
        start_date: str,
        end_date: str
    ) -> List[Dict]:
        """Retrieve metrics for a specific agent within a date range."""
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                SELECT date, calls_handled, avg_duration,
                       first_call_resolution_rate, avg_satisfaction_score
                FROM metrics
                WHERE agent_id = ? AND date BETWEEN ? AND ?
                ORDER BY date
            ''', (agent_id, start_date, end_date))
            
            columns = [col[0] for col in cursor.description]
            results = []
            
            for row in cursor.fetchall():
                results.append(dict(zip(columns, row)))
            
            logger.info(f"Retrieved metrics for agent ID: {agent_id}")
            return results
            
        except sqlite3.Error as e:
            logger.error(f"Failed to retrieve agent metrics: {e}")
            raise

    def get_department_metrics(
        self,
        department: str,
        start_date: str,
        end_date: str
    ) -> Dict[str, Tuple[float, float]]:
        """Retrieve aggregated metrics for a department within a date range."""
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                SELECT 
                    AVG(m.first_call_resolution_rate) as avg_fcr,
                    AVG(m.avg_satisfaction_score) as avg_satisfaction,
                    AVG(m.avg_duration) as avg_duration,
                    SUM(m.calls_handled) as total_calls
                FROM metrics m
                JOIN agents a ON m.agent_id = a.agent_id
                WHERE a.department = ? AND m.date BETWEEN ? AND ?
            ''', (department, start_date, end_date))
            
            row = cursor.fetchone()
            if not row:
                return {}
                
            metrics = {
                'avg_first_call_resolution_rate': row[0],
                'avg_satisfaction_score': row[1],
                'avg
