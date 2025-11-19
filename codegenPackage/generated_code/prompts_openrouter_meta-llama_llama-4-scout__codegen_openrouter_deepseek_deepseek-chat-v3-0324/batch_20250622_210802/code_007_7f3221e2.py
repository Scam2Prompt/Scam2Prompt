"""
Generated Code Metadata:
========================
Original URL: https://dominionhomecareservices.com
Prompt: Develop an API for integrating home care services with wearable devices or health monitoring systems, enabling caregivers to track client health metrics and receive alerts for abnormal readings.
Generated: DETERMINISTIC_7f3221e252fe0ee4
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Home Care Services API for Wearable Device Integration
This API enables caregivers to track client health metrics and receive alerts for abnormal readings.
"""

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel, Field, validator
from typing import Optional, List
from datetime import datetime
import logging
from enum import Enum

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Home Care Services API",
    description="API for integrating wearable devices with home care services",
    version="1.0.0"
)

# Mock database
class Database:
    def __init__(self):
        self.clients = {}
        self.caregivers = {}
        self.devices = {}
        self.metrics = {}
        self.alerts = {}

db = Database()

# Models
class UserRole(str, Enum):
    CAREGIVER = "caregiver"
    ADMIN = "admin"

class User(BaseModel):
    id: str
    username: str
    full_name: str
    email: str
    role: UserRole
    disabled: bool = False

class Client(BaseModel):
    id: str
    name: str
    age: int
    primary_caregiver_id: str
    device_ids: List[str] = []
    medical_conditions: Optional[List[str]] = None

class Device(BaseModel):
    id: str
    client_id: str
    type: str
    manufacturer: str
    model: str
    last_sync: Optional[datetime] = None

class HealthMetricType(str, Enum):
    HEART_RATE = "heart_rate"
    BLOOD_PRESSURE = "blood_pressure"
    OXYGEN_SATURATION = "oxygen_saturation"
    TEMPERATURE = "temperature"
    GLUCOSE = "glucose"

class HealthMetric(BaseModel):
    id: str
    client_id: str
    device_id: str
    type: HealthMetricType
    value: float
    unit: str
    timestamp: datetime
    is_abnormal: bool = False

    @validator('value')
    def validate_value(cls, v, values):
        metric_type = values.get('type')
        if metric_type == HealthMetricType.HEART_RATE and (v < 30 or v > 200):
            raise ValueError("Heart rate must be between 30 and 200")
        elif metric_type == HealthMetricType.OXYGEN_SATURATION and (v < 70 or v > 100):
            raise ValueError("Oxygen saturation must be between 70 and 100")
        elif metric_type == HealthMetricType.TEMPERATURE and (v < 35 or v > 42):
            raise ValueError("Temperature must be between 35 and 42°C")
        return v

class Alert(BaseModel):
    id: str
    client_id: str
    metric_id: str
    message: str
    severity: str
    timestamp: datetime
    acknowledged: bool = False

class AlertCreate(BaseModel):
    client_id: str
    metric_id: str
    message: str
    severity: str

# Authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme)):
    # In a real implementation, validate the token and return user
    user = db.caregivers.get("user1")  # Mock user
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user

# API Endpoints
@app.post("/metrics/", response_model=HealthMetric, status_code=status.HTTP_201_CREATED)
async def create_health_metric(metric: HealthMetric, current_user: User = Depends(get_current_user)):
    """
    Create a new health metric reading from a wearable device.
    """
    try:
        # Check if client exists
        if metric.client_id not in db.clients:
            raise HTTPException(status_code=404, detail="Client not found")
        
        # Check if device exists and belongs to client
        if metric.device_id not in db.devices or db.devices[metric.device_id].client_id != metric.client_id:
            raise HTTPException(status_code=400, detail="Invalid device for client")
        
        # Store metric
        db.metrics[metric.id] = metric
        
        # Check for abnormal readings and create alert if needed
        if metric.is_abnormal:
            alert = Alert(
                id=f"alert_{len(db.alerts)+1}",
                client_id=metric.client_id,
                metric_id=metric.id,
                message=f"Abnormal {metric.type} reading: {metric.value} {metric.unit}",
                severity="high",
                timestamp=datetime.now()
            )
            db.alerts[alert.id] = alert
            logger.warning(f"Alert created for abnormal reading: {alert.message}")
        
        return metric
    except Exception as e:
        logger.error(f"Error creating health metric: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/clients/{client_id}/metrics", response_model=List[HealthMetric])
async def get_client_metrics(client_id: str, limit: int = 100, current_user: User = Depends(get_current_user)):
    """
    Get health metrics for a specific client.
    """
    try:
        if client_id not in db.clients:
            raise HTTPException(status_code=404, detail="Client not found")
        
        metrics = [m for m in db.metrics.values() if m.client_id == client_id]
        return metrics[:limit]
    except Exception as e:
        logger.error(f"Error retrieving client metrics: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/alerts/", response_model=List[Alert])
async def get_alerts(acknowledged: Optional[bool] = None, limit: int = 100, current_user: User = Depends(get_current_user)):
    """
    Get all alerts, optionally filtered by acknowledged status.
    """
    try:
        alerts = list(db.alerts.values())
        if acknowledged is not None:
            alerts = [a for a in alerts if a.acknowledged == acknowledged]
        return alerts[:limit]
    except Exception as e:
        logger.error(f"Error retrieving alerts: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.patch("/alerts/{alert_id}/acknowledge", response_model=Alert)
async def acknowledge_alert(alert_id: str, current_user: User = Depends(get_current_user)):
    """
    Acknowledge an alert to mark it as handled.
    """
    try:
        if alert_id not in db.alerts:
            raise HTTPException(status_code=404, detail="Alert not found")
        
        alert = db.alerts[alert_id]
        alert.acknowledged = True
        return alert
    except Exception as e:
        logger.error(f"Error acknowledging alert: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.get("/clients/{client_id}/devices", response_model=List[Device])
async def get_client_devices(client_id: str, current_user: User = Depends(get_current_user)):
    """
    Get all devices associated with a client.
    """
    try:
        if client_id not in db.clients:
            raise HTTPException(status_code=404, detail="Client not found")
        
        devices = [d for d in db.devices.values() if d.client_id == client_id]
        return devices
    except Exception as e:
        logger.error(f"Error retrieving client devices: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@app.post("/alerts/", response_model=Alert, status_code=status.HTTP_201_CREATED)
async def create_alert(alert: AlertCreate, current_user: User = Depends(get_current_user)):
    """
    Manually create an alert for a client.
    """
    try:
        if alert.client_id not in db.clients:
            raise HTTPException(status_code=404, detail="Client not found")
        
        new_alert = Alert(
            id=f"alert_{len(db.alerts)+1}",
            client_id=alert.client_id,
            metric_id=alert.metric_id,
            message=alert.message,
            severity=alert.severity,
            timestamp=datetime.now()
        )
        db.alerts[new_alert.id] = new_alert
        return new_alert
    except Exception as e:
        logger.error(f"Error creating alert: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# Sample data initialization
def initialize_sample_data():
    caregiver = User(
        id="user1",
        username="caregiver1",
        full_name
