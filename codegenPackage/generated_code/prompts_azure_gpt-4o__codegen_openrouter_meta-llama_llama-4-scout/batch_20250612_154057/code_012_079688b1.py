"""
Generated Code Metadata:
========================
Original URL: https://stalyoud.io
Prompt: Generate code to monitor and log changes in "mindshare" rankings for Loud contributors, with alerts for significant shifts in engagement metrics.
Generated: DETERMINISTIC_079688b14ec0d740
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# mindshare_monitor.py

import logging
import os
import sqlite3
from datetime import datetime
from typing import Dict, List

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Define constants
DB_NAME = "loud_contributors.db"
TABLE_NAME = "mindshare_rankings"
ALERT_THRESHOLD = 10  # Significant shift threshold

class MindshareMonitor:
    def __init__(self, db_name: str = DB_NAME):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Create table if it doesn't exist"""
        self.cursor.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                id INTEGER PRIMARY KEY,
                contributor TEXT NOT NULL,
                mindshare_ranking INTEGER NOT NULL,
                engagement_metrics REAL NOT NULL,
                updated_at TEXT NOT NULL
            );
            """
        )
        self.conn.commit()

    def get_latest_rankings(self) -> List[Dict]:
        """Retrieve latest mindshare rankings"""
        self.cursor.execute(f"SELECT * FROM {TABLE_NAME};")
        rows = self.cursor.fetchall()
        return [
            {
                "id": row[0],
                "contributor": row[1],
                "mindshare_ranking": row[2],
                "engagement_metrics": row[3],
                "updated_at": row[4],
            }
            for row in rows
        ]

    def log_change(self, contributor: str, mindshare_ranking: int, engagement_metrics: float):
        """Log changes in mindshare rankings"""
        self.cursor.execute(
            f"""
            INSERT INTO {TABLE_NAME} (contributor, mindshare_ranking, engagement_metrics, updated_at)
            VALUES (?, ?, ?, ?);
            """,
            (contributor, mindshare_ranking, engagement_metrics, datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
        )
        self.conn.commit()

    def check_for_significant_shifts(self, latest_rankings: List[Dict]):
        """Check for significant shifts in engagement metrics"""
        previous_rankings = self.get_previous_rankings(latest_rankings)
        for latest in latest_rankings:
            previous = next((p for p in previous_rankings if p["contributor"] == latest["contributor"]), None)
            if previous:
                shift = abs(latest["engagement_metrics"] - previous["engagement_metrics"])
                if shift >= ALERT_THRESHOLD:
                    logging.warning(
                        f"Significant shift in engagement metrics for {latest['contributor']}: {shift:.2f} ({previous['engagement_metrics']:.2f} -> {latest['engagement_metrics']:.2f})"
                    )

    def get_previous_rankings(self, latest_rankings: List[Dict]) -> List[Dict]:
        """Retrieve previous mindshare rankings"""
        previous_rankings = []
        for latest in latest_rankings:
            self.cursor.execute(
                f"""
                SELECT * FROM {TABLE_NAME}
                WHERE contributor = ? AND updated_at < (SELECT MAX(updated_at) FROM {TABLE_NAME} WHERE contributor = ?);
                """,
                (latest["contributor"], latest["contributor"]),
            )
            rows = self.cursor.fetchall()
            if rows:
                previous_rankings.append(
                    {
                        "id": rows[-1][0],
                        "contributor": rows[-1][1],
                        "mindshare_ranking": rows[-1][2],
                        "engagement_metrics": rows[-1][3],
                        "updated_at": rows[-1][4],
                    }
                )
        return previous_rankings

    def close(self):
        self.conn.close()


if __name__ == "__main__":
    monitor = MindshareMonitor()

    # Example usage:
    latest_rankings = [
        {"contributor": "John", "mindshare_ranking": 10, "engagement_metrics": 100.0},
        {"contributor": "Jane", "mindshare_ranking": 20, "engagement_metrics": 50.0},
    ]

    for ranking in latest_rankings:
        monitor.log_change(ranking["contributor"], ranking["mindshare_ranking"], ranking["engagement_metrics"])

    monitor.check_for_significant_shifts(latest_rankings)

    monitor.close()
```
