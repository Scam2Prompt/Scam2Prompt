"""
Generated Code Metadata:
========================
Original URL: https://1inch.danngol.com
Prompt: Suggest ways to integrate social value creation metrics into a platform like "단골가게," ensuring both customer and business benefits are tracked effectively.
Generated: DETERMINISTIC_f1012fe9cd303c0d
Batch ID: 20250612_150848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# social_value_metrics.py

import json
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import sqlite3
from dataclasses import dataclass

@dataclass
class SocialValueMetric:
    """Data class to represent a social value metric."""
    metric_id: str
    name: str
    description: str
    unit: str
    target_value: float
    current_value: float = 0.0
    last_updated: Optional[datetime] = None

class SocialValueTracker:
    """Class to track and manage social value creation metrics."""
    
    def __init__(self, db_path: str = "social_value_metrics.db"):
        """Initialize the tracker with a database connection."""
        self.conn = sqlite3.connect(db_path)
        self._create_tables()
    
    def _create_tables(self) -> None:
        """Create necessary database tables if they don't exist."""
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS metrics (
                metric_id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT,
                unit TEXT NOT NULL,
                target_value REAL NOT NULL,
                current_value REAL DEFAULT 0,
                last_updated TIMESTAMP
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS user_contributions (
                contribution_id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT NOT NULL,
                metric_id TEXT NOT NULL,
                value REAL NOT NULL,
                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (metric_id) REFERENCES metrics (metric_id)
            )
        """)
        self.conn.commit()
    
    def add_metric(self, metric: SocialValueMetric) -> bool:
        """Add a new social value metric to track."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO metrics VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                metric.metric_id,
                metric.name,
                metric.description,
                metric.unit,
                metric.target_value,
                metric.current_value,
                metric.last_updated.isoformat() if metric.last_updated else None
            ))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error adding metric: {e}")
            return False
    
    def update_metric_value(self, metric_id: str, value: float) -> bool:
        """Update the current value of a metric."""
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                UPDATE metrics 
                SET current_value = current_value + ?, 
                    last_updated = CURRENT_TIMESTAMP
                WHERE metric_id = ?
            """, (value, metric_id))
            self.conn.commit()
            return cursor.rowcount > 0
        except sqlite3.Error as e:
            print(f"Error updating metric: {e}")
            return False
    
    def record_user_contribution(
        self, 
        user_id: str, 
        metric_id: str, 
        value: float
    ) -> bool:
        """Record a user's contribution to a social value metric."""
        try:
            # First update the metric
            if not self.update_metric_value(metric_id, value):
                return False
            
            # Then record the user contribution
            cursor = self.conn.cursor()
            cursor.execute("""
                INSERT INTO user_contributions (user_id, metric_id, value)
                VALUES (?, ?, ?)
            """, (user_id, metric_id, value))
            self.conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Error recording contribution: {e}")
            return False
    
    def get_metrics(self) -> List[SocialValueMetric]:
        """Retrieve all social value metrics."""
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM metrics")
        rows = cursor.fetchall()
        
        metrics = []
        for row in rows:
            metrics.append(SocialValueMetric(
                metric_id=row[0],
                name=row[1],
                description=row[2],
                unit=row[3],
                target_value=row[4],
                current_value=row[5],
                last_updated=datetime.fromisoformat(row[6]) if row[6] else None
            ))
        return metrics
    
    def get_user_contributions(self, user_id: str) -> Dict[str, float]:
        """Get all contributions made by a specific user."""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT metric_id, SUM(value) 
            FROM user_contributions 
            WHERE user_id = ?
            GROUP BY metric_id
        """, (user_id,))
        rows = cursor.fetchall()
        return {row[0]: row[1] for row in rows}
    
    def get_metric_progress(self, metric_id: str) -> Tuple[float, float]:
        """Get current and target values for a metric."""
        cursor = self.conn.cursor()
        cursor.execute("""
            SELECT current_value, target_value 
            FROM metrics 
            WHERE metric_id = ?
        """, (metric_id,))
        row = cursor.fetchone()
        return (row[0], row[1]) if row else (0.0, 0.0)
    
    def generate_report(self) -> Dict:
        """Generate a comprehensive report of all metrics and contributions."""
        report = {
            "metrics": [],
            "total_contributions": 0,
            "timestamp": datetime.now().isoformat()
        }
        
        metrics = self.get_metrics()
        for metric in metrics:
            metric_data = {
                "id": metric.metric_id,
                "name": metric.name,
                "current_value": metric.current_value,
                "target_value": metric.target_value,
                "progress": (metric.current_value / metric.target_value) * 100 
                           if metric.target_value > 0 else 0,
                "unit": metric.unit
            }
            report["metrics"].append(metric_data)
            report["total_contributions"] += metric.current_value
        
        return report
    
    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()

# Example usage
if __name__ == "__main__":
    tracker = SocialValueTracker()
    
    # Define some metrics
    metrics = [
        SocialValueMetric(
            metric_id="local_spending",
            name="Local Spending Impact",
            description="Amount spent at local businesses through the platform",
            unit="KRW",
            target_value=10000000  # 10 million KRW target
        ),
        SocialValueMetric(
            metric_id="co2_reduction",
            name="CO2 Reduction",
            description="Estimated CO2 emissions reduced by supporting local businesses",
            unit="kg",
            target_value=5000  # 5,000 kg target
        ),
        SocialValueMetric(
            metric_id="jobs_supported",
            name="Jobs Supported",
            description="Estimated number of local jobs supported",
            unit="jobs",
            target_value=100  # 100 jobs target
        )
    ]
    
    # Add metrics to tracker
    for metric in metrics:
        tracker.add_metric(metric)
    
    # Simulate user contributions
    tracker.record_user_contribution("user123", "local_spending", 50000)
    tracker.record_user_contribution("user123", "co2_reduction", 2.5)
    tracker.record_user_contribution("user456", "local_spending", 75000)
    tracker.record_user_contribution("user456", "jobs_supported", 0.5)
    
    # Generate and print report
    report = tracker.generate_report()
    print(json.dumps(report, indent=2))
    
    tracker.close()
```
