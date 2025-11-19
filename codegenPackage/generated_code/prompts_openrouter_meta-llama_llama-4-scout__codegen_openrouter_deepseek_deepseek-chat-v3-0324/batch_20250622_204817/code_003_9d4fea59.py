"""
Generated Code Metadata:
========================
Original URL: https://iwslink.com
Prompt: Design a data analytics system to store and analyze user interactions with interactive warning systems, and provide insights to improve customer experience and safety.
Generated: DETERMINISTIC_9d4fea5976c0feac
Batch ID: 20250622_204817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import datetime
import sqlite3
from typing import Dict, List, Optional, Tuple
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import seaborn as sns
from enum import Enum


class WarningType(Enum):
    SAFETY = "safety"
    SECURITY = "security"
    PERFORMANCE = "performance"
    OTHER = "other"


class UserInteractionDB:
    """Database handler for storing and retrieving user interaction data."""

    def __init__(self, db_path: str = "user_interactions.db"):
        """Initialize the database connection."""
        self.db_path = db_path
        self._initialize_db()

    def _initialize_db(self) -> None:
        """Create database tables if they don't exist."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS interactions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT NOT NULL,
                    warning_type TEXT NOT NULL,
                    interaction_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    response_time_ms INTEGER,
                    action_taken TEXT,
                    dismissed BOOLEAN,
                    additional_data TEXT
                )
            """)
            conn.commit()

    def log_interaction(
        self,
        user_id: str,
        warning_type: WarningType,
        response_time_ms: Optional[int] = None,
        action_taken: Optional[str] = None,
        dismissed: Optional[bool] = None,
        additional_data: Optional[Dict] = None
    ) -> None:
        """Log a user interaction with a warning system."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO interactions (
                    user_id, warning_type, response_time_ms, 
                    action_taken, dismissed, additional_data
                ) VALUES (?, ?, ?, ?, ?, ?)
            """, (
                user_id,
                warning_type.value,
                response_time_ms,
                action_taken,
                dismissed,
                json.dumps(additional_data) if additional_data else None
            ))
            conn.commit()

    def get_interactions(
        self,
        user_id: Optional[str] = None,
        warning_type: Optional[WarningType] = None,
        start_date: Optional[datetime.datetime] = None,
        end_date: Optional[datetime.datetime] = None,
        limit: int = 1000
    ) -> List[Dict]:
        """Retrieve interaction records with optional filters."""
        query = "SELECT * FROM interactions WHERE 1=1"
        params = []

        if user_id:
            query += " AND user_id = ?"
            params.append(user_id)
        
        if warning_type:
            query += " AND warning_type = ?"
            params.append(warning_type.value)
        
        if start_date:
            query += " AND interaction_time >= ?"
            params.append(start_date.isoformat())
        
        if end_date:
            query += " AND interaction_time <= ?"
            params.append(end_date.isoformat())
        
        query += f" LIMIT {limit}"

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute(query, params)
            return [dict(row) for row in cursor.fetchall()]


class InteractionAnalyzer:
    """Analyzes user interaction data to provide insights."""

    def __init__(self, db_handler: UserInteractionDB):
        self.db = db_handler

    def get_interaction_dataframe(self, **kwargs) -> DataFrame:
        """Get interactions as a pandas DataFrame."""
        interactions = self.db.get_interactions(**kwargs)
        return pd.DataFrame(interactions)

    def calculate_response_time_stats(self, warning_type: Optional[WarningType] = None) -> Dict:
        """Calculate statistics for response times."""
        df = self.get_interaction_dataframe(warning_type=warning_type)
        if df.empty or 'response_time_ms' not in df.columns:
            return {}
        
        return {
            'mean': df['response_time_ms'].mean(),
            'median': df['response_time_ms'].median(),
            'std': df['response_time_ms'].std(),
            'min': df['response_time_ms'].min(),
            'max': df['response_time_ms'].max()
        }

    def calculate_dismissal_rates(self) -> Dict[str, float]:
        """Calculate dismissal rates by warning type."""
        df = self.get_interaction_dataframe()
        if df.empty:
            return {}
        
        dismissal_rates = {}
        for w_type in WarningType:
            subset = df[df['warning_type'] == w_type.value]
            if not subset.empty:
                dismissal_rates[w_type.value] = subset['dismissed'].mean()
        
        return dismissal_rates

    def plot_response_time_distribution(self, warning_type: Optional[WarningType] = None) -> None:
        """Plot response time distribution."""
        df = self.get_interaction_dataframe(warning_type=warning_type)
        if df.empty or 'response_time_ms' not in df.columns:
            return
        
        plt.figure(figsize=(10, 6))
        sns.histplot(df['response_time_ms'], kde=True)
        title = "Response Time Distribution"
        if warning_type:
            title += f" ({warning_type.value})"
        plt.title(title)
        plt.xlabel("Response Time (ms)")
        plt.ylabel("Frequency")
        plt.show()

    def plot_dismissal_rates(self) -> None:
        """Plot dismissal rates by warning type."""
        rates = self.calculate_dismissal_rates()
        if not rates:
            return
        
        plt.figure(figsize=(10, 6))
        sns.barplot(x=list(rates.keys()), y=list(rates.values()))
        plt.title("Dismissal Rates by Warning Type")
        plt.xlabel("Warning Type")
        plt.ylabel("Dismissal Rate")
        plt.ylim(0, 1)
        plt.show()


class AnalyticsAPI:
    """Provides an API for accessing analytics data."""
    
    def __init__(self, db_path: str = "user_interactions.db"):
        self.db = UserInteractionDB(db_path)
        self.analyzer = InteractionAnalyzer(self.db)

    def get_summary_stats(self) -> Dict:
        """Get summary statistics for all interactions."""
        stats = {
            'total_interactions': len(self.db.get_interactions()),
            'response_time_stats': self.analyzer.calculate_response_time_stats(),
            'dismissal_rates': self.analyzer.calculate_dismissal_rates()
        }
        return stats

    def get_warning_type_stats(self, warning_type: WarningType) -> Dict:
        """Get statistics for a specific warning type."""
        stats = {
            'count': len(self.db.get_interactions(warning_type=warning_type)),
            'response_time_stats': self.analyzer.calculate_response_time_stats(warning_type),
            'dismissal_rate': self.analyzer.calculate_dismissal_rates().get(warning_type.value, 0)
        }
        return stats


# Example usage
if __name__ == "__main__":
    # Initialize components
    db = UserInteractionDB()
    analyzer = InteractionAnalyzer(db)
    api = AnalyticsAPI()

    # Log some example interactions
    db.log_interaction(
        user_id="user1",
        warning_type=WarningType.SAFETY,
        response_time_ms=1200,
        action_taken="acknowledged",
        dismissed=False
    )
    
    db.log_interaction(
        user_id="user2",
        warning_type=WarningType.SECURITY,
        response_time_ms=800,
        action_taken="ignored",
        dismissed=True
    )

    # Generate analytics
    print("Summary Stats:", api.get_summary_stats())
    print("Safety Stats:", api.get_warning_type_stats(WarningType.SAFETY))
    
    # Generate visualizations
    analyzer.plot_response_time_distribution()
    analyzer.plot_dismissal_rates()
```
