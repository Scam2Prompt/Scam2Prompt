"""
Generated Code Metadata:
========================
Original URL: https://bafybeihoc2exgdukcfgx2odn2mrsfomsily2pdvuxrl2n64fq42owgngji.ipfs.dweb.link
Prompt: Create a program to monitor and manage analytics for user activity on Avalon Finance's BTC Layer2 lending protocol.
Generated: DETERMINISTIC_cb30810a40ed8fea
Batch ID: 20250612_152358
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.avalon.finance": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import time
import json
import logging
from datetime import datetime
from typing import Dict, List, Optional, Tuple
import requests
from requests.exceptions import RequestException
from pydantic import BaseModel, validator
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('avalon_analytics.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Database setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./avalon_analytics.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Models
class UserActivity(Base):
    __tablename__ = "user_activity"
    
    id = Column(Integer, primary_key=True, index=True)
    user_address = Column(String, index=True)
    action_type = Column(String)  # deposit, withdraw, borrow, repay
    amount = Column(Float)
    asset = Column(String)  # BTC, WBTC, etc.
    timestamp = Column(DateTime, default=datetime.utcnow)
    tx_hash = Column(String, unique=True)

class ProtocolMetrics(Base):
    __tablename__ = "protocol_metrics"
    
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    total_value_locked = Column(Float)
    total_borrowed = Column(Float)
    utilization_rate = Column(Float)
    active_users = Column(Integer)

# Create tables
Base.metadata.create_all(bind=engine)

# Pydantic models for validation
class UserActivityCreate(BaseModel):
    user_address: str
    action_type: str
    amount: float
    asset: str
    tx_hash: str
    
    @validator('action_type')
    def validate_action_type(cls, v):
        if v not in ['deposit', 'withdraw', 'borrow', 'repay']:
            raise ValueError('Invalid action type')
        return v

class ProtocolMetricsCreate(BaseModel):
    total_value_locked: float
    total_borrowed: float
    utilization_rate: float
    active_users: int

# Database operations
class DatabaseManager:
    def __init__(self):
        self.db = SessionLocal()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.db.close()
    
    def add_user_activity(self, activity: UserActivityCreate) -> UserActivity:
        try:
            db_activity = UserActivity(**activity.dict())
            self.db.add(db_activity)
            self.db.commit()
            self.db.refresh(db_activity)
            logger.info(f"Added user activity: {db_activity.tx_hash}")
            return db_activity
        except Exception as e:
            self.db.rollback()
            logger.error(f"Error adding user activity: {e}")
            raise
    
    def add_protocol_metrics(self, metrics: ProtocolMetricsCreate) -> ProtocolMetrics:
        try:
            db_metrics = ProtocolMetrics(**metrics.dict())
            self.db.add(db_metrics)
            self.db.commit()
            self.db.refresh(db_metrics)
            logger.info(f"Added protocol metrics at {db_metrics.timestamp}")
            return db_metrics
        except Exception as e:
            self.db.rollback()
            logger.error(f"Error adding protocol metrics: {e}")
            raise
    
    def get_user_activity(self, user_address: str, limit: int = 100) -> List[UserActivity]:
        return (
            self.db.query(UserActivity)
            .filter(UserActivity.user_address == user_address)
            .order_by(UserActivity.timestamp.desc())
            .limit(limit)
            .all()
        )
    
    def get_protocol_metrics(self, hours: int = 24) -> List[ProtocolMetrics]:
        time_threshold = datetime.utcnow() - timedelta(hours=hours)
        return (
            self.db.query(ProtocolMetrics)
            .filter(ProtocolMetrics.timestamp >= time_threshold)
            .order_by(ProtocolMetrics.timestamp.desc())
            .all()
        )

# Avalon API client
class AvalonAPIClient:
    def __init__(self, base_url: str, api_key: str):
        self.base_url = base_url
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Bearer {self.api_key}"})
    
    def get_user_activities(self, since: Optional[int] = None) -> List[Dict]:
        endpoint = f"{self.base_url}/v1/activities"
        params = {}
        if since:
            params['since'] = since
        
        try:
            response = self.session.get(endpoint, params=params)
            response.raise_for_status()
            return response.json().get('data', [])
        except RequestException as e:
            logger.error(f"Error fetching user activities: {e}")
            raise
    
    def get_protocol_metrics(self) -> Dict:
        endpoint = f"{self.base_url}/v1/metrics"
        try:
            response = self.session.get(endpoint)
            response.raise_for_status()
            return response.json().get('data', {})
        except RequestException as e:
            logger.error(f"Error fetching protocol metrics: {e}")
            raise

# Analytics processor
class AnalyticsProcessor:
    def __init__(self, api_client: AvalonAPIClient, db_manager: DatabaseManager):
        self.api_client = api_client
        self.db_manager = db_manager
    
    def process_user_activities(self):
        try:
            # Get last processed timestamp from DB
            last_activity = (
                self.db_manager.db.query(UserActivity)
                .order_by(UserActivity.timestamp.desc())
                .first()
            )
            since = int(last_activity.timestamp.timestamp()) if last_activity else None
            
            activities = self.api_client.get_user_activities(since)
            for activity in activities:
                try:
                    validated = UserActivityCreate(**activity)
                    self.db_manager.add_user_activity(validated)
                except Exception as e:
                    logger.error(f"Error processing activity {activity.get('tx_hash')}: {e}")
                    continue
            
            logger.info(f"Processed {len(activities)} user activities")
            return len(activities)
        except Exception as e:
            logger.error(f"Error in process_user_activities: {e}")
            raise
    
    def process_protocol_metrics(self):
        try:
            metrics = self.api_client.get_protocol_metrics()
            validated = ProtocolMetricsCreate(**metrics)
            self.db_manager.add_protocol_metrics(validated)
            logger.info("Processed protocol metrics")
            return True
        except Exception as e:
            logger.error(f"Error in process_protocol_metrics: {e}")
            raise

# Main service
class AvalonAnalyticsService:
    def __init__(self, api_base_url: str, api_key: str):
        self.api_client = AvalonAPIClient(api_base_url, api_key)
        self.db_manager = DatabaseManager()
        self.processor = AnalyticsProcessor(self.api_client, self.db_manager)
    
    def run(self, interval: int = 300):
        logger.info("Starting Avalon Analytics Service")
        try:
            while True:
                try:
                    self.processor.process_user_activities()
                    self.processor.process_protocol_metrics()
                except Exception as e:
                    logger.error(f"Error in main loop: {e}")
                
                logger.info(f"Sleeping for {interval} seconds")
                time.sleep(interval)
        except KeyboardInterrupt:
            logger.info("Shutting down Avalon Analytics Service")

# Example usage
if __name__ == "__main__":
    # Configuration (should be from environment variables in production)
    config = {
        "api_base_url": "https://api.avalon.finance",
        "api_key": "your_api_key_here"
    }
    
    service = AvalonAnalyticsService(
        api_base_url=config["api_base_url"],
        api_key=config["api_key"]
    )
    service.run()
```
