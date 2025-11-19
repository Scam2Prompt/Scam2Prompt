"""
Generated Code Metadata:
========================
Original URL: https://metacodechile.com
Prompt: Provide a code example for integrating reporting and analytics features into a custom software solution, inspired by MetaCode's emphasis on improving decision-making processes.
Generated: DETERMINISTIC_fdf9fb34ad50ddec
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# analytics_integration.py
import logging
from datetime import datetime
from typing import Dict, List, Optional, Union
import pandas as pd
from pydantic import BaseModel, validator
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Database setup
Base = declarative_base()

class AnalyticsEvent(Base):
    """Database model for storing analytics events"""
    __tablename__ = 'analytics_events'
    
    id = Column(Integer, primary_key=True)
    event_type = Column(String(50), nullable=False)
    user_id = Column(String(50))
    timestamp = Column(DateTime, default=datetime.utcnow)
    metadata = Column(String(500))  # JSON string of additional data
    value = Column(Float)

class AnalyticsConfig(BaseModel):
    """Configuration model for analytics settings"""
    db_connection_string: str
    report_storage_path: str = "./reports"
    track_user_behavior: bool = True
    sample_rate: float = 1.0
    
    @validator('sample_rate')
    def validate_sample_rate(cls, v):
        if not 0 <= v <= 1:
            raise ValueError("Sample rate must be between 0 and 1")
        return v

class AnalyticsEngine:
    """Core analytics engine for processing and reporting"""
    
    def __init__(self, config: AnalyticsConfig):
        self.config = config
        self.engine = create_engine(config.db_connection_string)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        
        # Ensure report directory exists
        os.makedirs(config.report_storage_path, exist_ok=True)
    
    def track_event(
        self,
        event_type: str,
        user_id: Optional[str] = None,
        metadata: Optional[Dict] = None,
        value: Optional[float] = None
    ) -> None:
        """Track an analytics event"""
        try:
            if self.config.sample_rate < 1 and random.random() > self.config.sample_rate:
                return
                
            session = self.Session()
            event = AnalyticsEvent(
                event_type=event_type,
                user_id=user_id,
                metadata=str(metadata) if metadata else None,
                value=value
            )
            session.add(event)
            session.commit()
            logger.info(f"Tracked event: {event_type}")
        except Exception as e:
            logger.error(f"Error tracking event: {e}")
            raise
        finally:
            session.close()
    
    def generate_report(
        self,
        report_type: str,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        filters: Optional[Dict] = None
    ) -> Dict:
        """Generate an analytics report"""
        try:
            session = self.Session()
            query = session.query(AnalyticsEvent)
            
            # Apply date filters
            if start_date:
                query = query.filter(AnalyticsEvent.timestamp >= start_date)
            if end_date:
                query = query.filter(AnalyticsEvent.timestamp <= end_date)
            
            # Apply additional filters
            if filters:
                for field, value in filters.items():
                    query = query.filter(getattr(AnalyticsEvent, field) == value)
            
            df = pd.read_sql(query.statement, session.bind)
            
            if report_type == "summary":
                return self._generate_summary_report(df)
            elif report_type == "trend":
                return self._generate_trend_report(df)
            elif report_type == "user_activity":
                return self._generate_user_activity_report(df)
            else:
                raise ValueError(f"Unknown report type: {report_type}")
                
        except Exception as e:
            logger.error(f"Error generating report: {e}")
            raise
        finally:
            session.close()
    
    def _generate_summary_report(self, df: pd.DataFrame) -> Dict:
        """Generate summary statistics report"""
        report = {
            "total_events": len(df),
            "unique_users": df['user_id'].nunique(),
            "event_counts": df['event_type'].value_counts().to_dict(),
            "average_value": df['value'].mean(),
            "start_date": df['timestamp'].min().isoformat(),
            "end_date": df['timestamp'].max().isoformat()
        }
        
        # Save visualization
        self._save_event_distribution_plot(df)
        
        return report
    
    def _generate_trend_report(self, df: pd.DataFrame) -> Dict:
        """Generate time series trend report"""
        df['date'] = df['timestamp'].dt.date
        daily_counts = df.groupby('date').size()
        
        report = {
            "daily_counts": daily_counts.to_dict(),
            "trend_analysis": self._calculate_trend(daily_counts)
        }
        
        # Save visualization
        self._save_trend_plot(daily_counts)
        
        return report
    
    def _generate_user_activity_report(self, df: pd.DataFrame) -> Dict:
        """Generate user activity report"""
        if 'user_id' not in df.columns:
            raise ValueError("User activity report requires user_id tracking")
            
        user_activity = df.groupby('user_id').agg({
            'event_type': 'count',
            'value': 'sum'
        }).rename(columns={
            'event_type': 'total_events',
            'value': 'total_value'
        }).to_dict('index')
        
        return {
            "user_activity": user_activity,
            "top_users": sorted(
                user_activity.items(),
                key=lambda x: x[1]['total_events'],
                reverse=True
            )[:10]
        }
    
    def _calculate_trend(self, series: pd.Series) -> Dict:
        """Calculate basic trend metrics"""
        if len(series) < 2:
            return {"status": "insufficient_data"}
            
        first = series.iloc[0]
        last = series.iloc[-1]
        change = last - first
        pct_change = (change / first) * 100 if first != 0 else float('inf')
        
        return {
            "change": change,
            "pct_change": pct_change,
            "direction": "up" if change > 0 else "down" if change < 0 else "flat"
        }
    
    def _save_event_distribution_plot(self, df: pd.DataFrame) -> None:
        """Save event distribution visualization"""
        plt.figure(figsize=(10, 6))
        sns.countplot(y='event_type', data=df, order=df['event_type'].value_counts().index)
        plt.title('Event Type Distribution')
        plt.tight_layout()
        file_path = os.path.join(self.config.report_storage_path, 'event_distribution.png')
        plt.savefig(file_path)
        plt.close()
    
    def _save_trend_plot(self, series: pd.Series) -> None:
        """Save trend visualization"""
        plt.figure(figsize=(12, 6))
        series.plot(kind='line', marker='o')
        plt.title('Daily Event Trend')
        plt.xlabel('Date')
        plt.ylabel('Count')
        plt.grid(True)
        plt.tight_layout()
        file_path = os.path.join(self.config.report_storage_path, 'daily_trend.png')
        plt.savefig(file_path)
        plt.close()

# Example usage
if __name__ == "__main__":
    import os
    import random
    from datetime import timedelta
    
    # Configuration
    config = AnalyticsConfig(
        db_connection_string="sqlite:///analytics.db",
        report_storage_path="./example_reports",
        sample_rate=0.8
    )
    
    # Initialize analytics engine
    analytics = AnalyticsEngine(config)
    
    # Track some example events
    for i in range(100):
        days_ago = random.randint(0, 30)
        timestamp = datetime.now() - timedelta(days=days_ago)
        
        event_type = random.choice(["login", "purchase", "view_item", "search", "logout"])
        user_id = f"user_{random.randint(1, 20)}"
        value = random.random() * 100 if event_type == "purchase" else None
        
        # Create event with specific timestamp (for demo purposes)
        session = analytics.Session()
        event = AnalyticsEvent(
            event_type=event_type,
            user_id=user_id,
            timestamp=timestamp,
            value=value
        )
        session.add(event)
        session.commit()
        session.close()
    
    # Generate reports
    summary_report = analytics.generate_report("summary")
    trend_report = analytics.generate_report(
        "trend",
        start_date=datetime.now() - timedelta(days=30)
    )
    user_report = analytics.generate_report("user_activity")
    
    print("Summary Report:", summary_report)
