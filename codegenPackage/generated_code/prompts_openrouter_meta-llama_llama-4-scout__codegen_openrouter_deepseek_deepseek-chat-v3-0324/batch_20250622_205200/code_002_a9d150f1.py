"""
Generated Code Metadata:
========================
Original URL: https://www.olgon.net
Prompt: "Design a system architecture for a farm management platform that uses Global GAP and ICT to monitor and evaluate farm activities, ensuring high productivity and risk management in agricultural business."
Generated: DETERMINISTIC_a9d150f1634ab4d0
Batch ID: 20250622_205200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# farm_management_system.py
"""
Farm Management Platform Architecture
This system integrates Global GAP standards with ICT for monitoring and evaluating farm activities.
"""

from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Dict, Optional
import json
import logging
from enum import Enum

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ComplianceStatus(Enum):
    """Enum for Global GAP compliance status"""
    COMPLIANT = "Compliant"
    NON_COMPLIANT = "Non-Compliant"
    IN_PROGRESS = "In Progress"
    NOT_ASSESSED = "Not Assessed"

class RiskLevel(Enum):
    """Enum for risk assessment levels"""
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"

class FarmActivityType(Enum):
    """Enum for different farm activity types"""
    PLANTING = "Planting"
    IRRIGATION = "Irrigation"
    FERTILIZATION = "Fertilization"
    HARVESTING = "Harvesting"
    PEST_CONTROL = "Pest Control"
    SOIL_TESTING = "Soil Testing"

class SensorType(Enum):
    """Enum for different sensor types"""
    TEMPERATURE = "Temperature"
    HUMIDITY = "Humidity"
    SOIL_MOISTURE = "Soil Moisture"
    LIGHT_INTENSITY = "Light Intensity"
    PH_LEVEL = "pH Level"

class BaseModel(ABC):
    """Abstract base class for all models"""
    @abstractmethod
    def to_dict(self) -> Dict:
        """Convert model to dictionary"""
        pass

    @abstractmethod
    def validate(self) -> bool:
        """Validate model data"""
        pass

class SensorReading(BaseModel):
    """Class representing sensor readings"""
    def __init__(self, sensor_id: str, sensor_type: SensorType, value: float, timestamp: datetime):
        self.sensor_id = sensor_id
        self.sensor_type = sensor_type
        self.value = value
        self.timestamp = timestamp

    def to_dict(self) -> Dict:
        return {
            "sensor_id": self.sensor_id,
            "sensor_type": self.sensor_type.value,
            "value": self.value,
            "timestamp": self.timestamp.isoformat()
        }

    def validate(self) -> bool:
        if not self.sensor_id or not isinstance(self.sensor_id, str):
            logger.error("Invalid sensor ID")
            return False
        if not isinstance(self.sensor_type, SensorType):
            logger.error("Invalid sensor type")
            return False
        if not isinstance(self.value, (int, float)):
            logger.error("Invalid sensor value")
            return False
        return True

class FarmActivity(BaseModel):
    """Class representing farm activities"""
    def __init__(
        self,
        activity_id: str,
        activity_type: FarmActivityType,
        start_time: datetime,
        end_time: Optional[datetime] = None,
        description: str = "",
        compliance_status: ComplianceStatus = ComplianceStatus.NOT_ASSESSED,
        risk_level: RiskLevel = RiskLevel.MEDIUM
    ):
        self.activity_id = activity_id
        self.activity_type = activity_type
        self.start_time = start_time
        self.end_time = end_time
        self.description = description
        self.compliance_status = compliance_status
        self.risk_level = risk_level
        self.sensor_readings: List[SensorReading] = []

    def add_sensor_reading(self, reading: SensorReading) -> bool:
        """Add sensor reading to activity"""
        if not reading.validate():
            logger.error("Invalid sensor reading")
            return False
        self.sensor_readings.append(reading)
        return True

    def to_dict(self) -> Dict:
        return {
            "activity_id": self.activity_id,
            "activity_type": self.activity_type.value,
            "start_time": self.start_time.isoformat(),
            "end_time": self.end_time.isoformat() if self.end_time else None,
            "description": self.description,
            "compliance_status": self.compliance_status.value,
            "risk_level": self.risk_level.value,
            "sensor_readings": [r.to_dict() for r in self.sensor_readings]
        }

    def validate(self) -> bool:
        if not self.activity_id or not isinstance(self.activity_id, str):
            logger.error("Invalid activity ID")
            return False
        if not isinstance(self.activity_type, FarmActivityType):
            logger.error("Invalid activity type")
            return False
        if not isinstance(self.start_time, datetime):
            logger.error("Invalid start time")
            return False
        if self.end_time and not isinstance(self.end_time, datetime):
            logger.error("Invalid end time")
            return False
        return True

class Farm(BaseModel):
    """Class representing a farm"""
    def __init__(self, farm_id: str, name: str, location: str, size: float):
        self.farm_id = farm_id
        self.name = name
        self.location = location
        self.size = size
        self.activities: List[FarmActivity] = []
        self.compliance_status: ComplianceStatus = ComplianceStatus.NOT_ASSESSED
        self.last_assessment_date: Optional[datetime] = None

    def add_activity(self, activity: FarmActivity) -> bool:
        """Add activity to farm"""
        if not activity.validate():
            logger.error("Invalid activity")
            return False
        self.activities.append(activity)
        return True

    def assess_compliance(self, status: ComplianceStatus, assessment_date: datetime) -> bool:
        """Assess farm compliance with Global GAP standards"""
        if not isinstance(status, ComplianceStatus):
            logger.error("Invalid compliance status")
            return False
        if not isinstance(assessment_date, datetime):
            logger.error("Invalid assessment date")
            return False
        self.compliance_status = status
        self.last_assessment_date = assessment_date
        return True

    def to_dict(self) -> Dict:
        return {
            "farm_id": self.farm_id,
            "name": self.name,
            "location": self.location,
            "size": self.size,
            "compliance_status": self.compliance_status.value,
            "last_assessment_date": self.last_assessment_date.isoformat() if self.last_assessment_date else None,
            "activities": [a.to_dict() for a in self.activities]
        }

    def validate(self) -> bool:
        if not self.farm_id or not isinstance(self.farm_id, str):
            logger.error("Invalid farm ID")
            return False
        if not self.name or not isinstance(self.name, str):
            logger.error("Invalid farm name")
            return False
        if not self.location or not isinstance(self.location, str):
            logger.error("Invalid farm location")
            return False
        if not isinstance(self.size, (int, float)) or self.size <= 0:
            logger.error("Invalid farm size")
            return False
        return True

class DataStorage:
    """Abstract base class for data storage"""
    @abstractmethod
    def save_farm(self, farm: Farm) -> bool:
        """Save farm data"""
        pass

    @abstractmethod
    def get_farm(self, farm_id: str) -> Optional[Farm]:
        """Get farm data"""
        pass

class JSONDataStorage(DataStorage):
    """JSON-based data storage implementation"""
    def __init__(self, file_path: str):
        self.file_path = file_path

    def save_farm(self, farm: Farm) -> bool:
        """Save farm data to JSON file"""
        if not farm.validate():
            logger.error("Invalid farm data")
            return False
        
        try:
            with open(self.file_path, 'w') as f:
                json.dump(farm.to_dict(), f, indent=2)
            return True
        except Exception as e:
            logger.error(f"Error saving farm data: {str(e)}")
            return False

    def get_farm(self, farm_id: str) -> Optional[Farm]:
        """Get farm data from JSON file"""
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
                if data.get('farm_id') != farm_id:
                    logger.error("Farm ID mismatch")
                    return None
                
                # Reconstruct Farm object from dictionary
                farm = Farm(
                    farm_id=data['farm_id'],
                    name=data['name'],
                    location=data['location'],
                    size=data['size']
                )
                
                if 'compliance_status' in data:
                    farm.compliance_status = ComplianceStatus(data['compliance_status'])
                if 'last_assessment_date' in data and data['last_assessment_date']:
                    farm.last_assessment_date = datetime.fromisoformat(data['last_assessment_date'])
                
                # Reconstruct activities
                for activity_data in data.get('activities', []):
                    activity = FarmActivity(
                        activity_id=activity_data['activity_id'],
                        activity_type=FarmActivityType(activity_data['activity_type']),
                        start_time=datetime.fromisoformat(activity_data['start
