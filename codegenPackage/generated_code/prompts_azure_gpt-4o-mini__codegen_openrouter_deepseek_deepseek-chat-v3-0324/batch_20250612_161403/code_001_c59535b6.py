"""
Generated Code Metadata:
========================
Original URL: https://paradigmgroup.co.ug
Prompt: Write a function that manages event media coordination and crisis management for experiential marketing events, inspired by the services offered by Paradigm Group.
Generated: DETERMINISTIC_c59535b689eb0627
Batch ID: 20250612_161403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from datetime import datetime
from typing import List, Dict, Optional, Tuple
from enum import Enum, auto

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class MediaType(Enum):
    PHOTO = auto()
    VIDEO = auto()
    LIVE_STREAM = auto()
    SOCIAL_MEDIA = auto()

class CrisisSeverity(Enum):
    LOW = auto()
    MEDIUM = auto()
    HIGH = auto()
    CRITICAL = auto()

class EventMediaCoordinator:
    """
    Manages media coordination and crisis management for experiential marketing events.
    """
    
    def __init__(self, event_name: str, event_date: datetime):
        """
        Initialize the EventMediaCoordinator with event details.
        
        Args:
            event_name: Name of the event
            event_date: Date of the event
        """
        self.event_name = event_name
        self.event_date = event_date
        self.media_assets: Dict[MediaType, List[str]] = {media_type: [] for media_type in MediaType}
        self.crisis_log: List[Dict] = []
        self.media_team: List[str] = []
        self.crisis_contacts: Dict[str, str] = {}
        
    def add_media_team_member(self, name: str, role: str) -> bool:
        """
        Add a member to the media team.
        
        Args:
            name: Name of the team member
            role: Role of the team member
            
        Returns:
            bool: True if added successfully, False if already exists
        """
        if name in self.media_team:
            logger.warning(f"Team member {name} already exists")
            return False
        self.media_team.append(f"{name} ({role})")
        logger.info(f"Added {name} to media team as {role}")
        return True
    
    def add_media_asset(self, media_type: MediaType, asset_path: str) -> bool:
        """
        Add a media asset to the event collection.
        
        Args:
            media_type: Type of media asset
            asset_path: Path or identifier for the asset
            
        Returns:
            bool: True if added successfully, False if invalid type
        """
        if not isinstance(media_type, MediaType):
            logger.error(f"Invalid media type: {media_type}")
            return False
        self.media_assets[media_type].append(asset_path)
        logger.info(f"Added {media_type.name} asset: {asset_path}")
        return True
    
    def add_crisis_contact(self, name: str, contact_info: str) -> None:
        """
        Add a crisis contact to the emergency list.
        
        Args:
            name: Name of the contact
            contact_info: Contact information (phone/email)
        """
        self.crisis_contacts[name] = contact_info
        logger.info(f"Added crisis contact: {name} - {contact_info}")
    
    def log_crisis(self, description: str, severity: CrisisSeverity) -> Dict:
        """
        Log a crisis incident with description and severity.
        
        Args:
            description: Description of the crisis
            severity: Severity level of the crisis
            
        Returns:
            Dict: The logged crisis entry
        """
        if not isinstance(severity, CrisisSeverity):
            logger.error(f"Invalid crisis severity: {severity}")
            raise ValueError("Invalid crisis severity")
            
        crisis_entry = {
            "timestamp": datetime.now(),
            "description": description,
            "severity": severity.name,
            "resolved": False
        }
        self.crisis_log.append(crisis_entry)
        logger.warning(f"Logged crisis: {severity.name} - {description}")
        return crisis_entry
    
    def resolve_crisis(self, index: int, resolution: str) -> bool:
        """
        Mark a crisis as resolved with a resolution description.
        
        Args:
            index: Index of the crisis in the log
            resolution: Description of the resolution
            
        Returns:
            bool: True if resolved successfully, False if invalid index
        """
        try:
            crisis = self.crisis_log[index]
            crisis["resolved"] = True
            crisis["resolution"] = resolution
            crisis["resolved_at"] = datetime.now()
            logger.info(f"Resolved crisis: {crisis['description']}")
            return True
        except IndexError:
            logger.error(f"Invalid crisis index: {index}")
            return False
    
    def generate_media_report(self) -> Dict:
        """
        Generate a report of all media assets.
        
        Returns:
            Dict: Report containing media assets by type
        """
        report = {
            "event_name": self.event_name,
            "event_date": self.event_date,
            "media_summary": {
                media_type.name: len(assets) 
                for media_type, assets in self.media_assets.items()
            },
            "total_assets": sum(len(assets) for assets in self.media_assets.values())
        }
        logger.info(f"Generated media report for {self.event_name}")
        return report
    
    def generate_crisis_report(self) -> Dict:
        """
        Generate a report of all crisis incidents.
        
        Returns:
            Dict: Report containing crisis incidents and status
        """
        report = {
            "event_name": self.event_name,
            "total_crises": len(self.crisis_log),
            "resolved_crises": sum(1 for crisis in self.crisis_log if crisis["resolved"]),
            "crisis_by_severity": {
                severity.name: sum(1 for crisis in self.crisis_log if crisis["severity"] == severity.name)
                for severity in CrisisSeverity
            },
            "active_crises": [
                crisis for crisis in self.crisis_log 
                if not crisis["resolved"]
            ]
        }
        logger.info(f"Generated crisis report for {self.event_name}")
        return report
    
    def get_emergency_contacts(self) -> Dict[str, str]:
        """
        Get all emergency contacts.
        
        Returns:
            Dict: Dictionary of emergency contacts
        """
        return self.crisis_contacts.copy()
    
    def validate_event_readiness(self) -> Tuple[bool, List[str]]:
        """
        Validate if the event is ready from media and crisis perspectives.
        
        Returns:
            Tuple: (is_ready, list_of_issues)
        """
        issues = []
        
        # Check media team
        if not self.media_team:
            issues.append("No media team members assigned")
        
        # Check crisis contacts
        if not self.crisis_contacts:
            issues.append("No crisis contacts configured")
        
        # Check for unresolved high severity crises
        unresolved_high = any(
            crisis["severity"] in [CrisisSeverity.HIGH.name, CrisisSeverity.CRITICAL.name] 
            and not crisis["resolved"] 
            for crisis in self.crisis_log
        )
        if unresolved_high:
            issues.append("Unresolved high/critical severity crises")
        
        return (len(issues) == 0, issues)
```
