"""
Generated Code Metadata:
========================
Original URL: https://stellar-limited.com
Prompt: Generate code to handle legal requests for personal information disclosure, ensuring compliance with the scenarios listed in STELLAR TECHNOLOGY LIMITED's privacy policy (e.g., national security or criminal investigations).
Generated: DETERMINISTIC_6a63313d6bc3b68f
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from enum import Enum
from typing import Optional, Dict, List, Union
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class RequestType(Enum):
    """Enum representing types of legal requests."""
    NATIONAL_SECURITY = "national_security"
    CRIMINAL_INVESTIGATION = "criminal_investigation"
    SUBPOENA = "subpoena"
    COURT_ORDER = "court_order"
    OTHER = "other"

class LegalRequest:
    """Class to handle legal requests for personal information disclosure."""
    
    def __init__(
        self,
        request_id: str,
        request_type: RequestType,
        requesting_authority: str,
        description: str,
        user_ids: List[str],
        required_data: List[str],
        expiration_date: Optional[datetime] = None
    ):
        """
        Initialize a legal request.
        
        Args:
            request_id: Unique identifier for the request
            request_type: Type of legal request (RequestType enum)
            requesting_authority: Name of the authority making the request
            description: Description of the request
            user_ids: List of user IDs affected by this request
            required_data: List of data fields being requested
            expiration_date: Optional expiration date for the request
        """
        self.request_id = request_id
        self.request_type = request_type
        self.requesting_authority = requesting_authority
        self.description = description
        self.user_ids = user_ids
        self.required_data = required_data
        self.expiration_date = expiration_date
        self.timestamp = datetime.utcnow()
        self.is_fulfilled = False
        self.fulfillment_date = None
        
    def validate_request(self) -> bool:
        """Validate the legal request meets compliance requirements."""
        if not self.request_id:
            logger.error("Request validation failed: Missing request ID")
            return False
            
        if not isinstance(self.request_type, RequestType):
            logger.error("Request validation failed: Invalid request type")
            return False
            
        if not self.requesting_authority:
            logger.error("Request validation failed: Missing requesting authority")
            return False
            
        if not self.user_ids:
            logger.error("Request validation failed: No user IDs specified")
            return False
            
        if not self.required_data:
            logger.error("Request validation failed: No data fields specified")
            return False
            
        if self.expiration_date and self.expiration_date < datetime.utcnow():
            logger.error("Request validation failed: Expired request")
            return False
            
        return True
    
    def fulfill_request(self, user_data: Dict[str, Dict]) -> Dict[str, Union[bool, str, Dict]]:
        """
        Fulfill the legal request by providing the requested user data.
        
        Args:
            user_data: Dictionary containing user data (key: user_id, value: user data dict)
            
        Returns:
            Dictionary containing:
                - success: Boolean indicating if fulfillment was successful
                - message: Status message
                - data: The provided data if successful
        """
        if not self.validate_request():
            return {
                "success": False,
                "message": "Request validation failed",
                "data": None
            }
            
        if self.is_fulfilled:
            return {
                "success": False,
                "message": "Request has already been fulfilled",
                "data": None
            }
            
        response_data = {}
        missing_users = []
        
        for user_id in self.user_ids:
            if user_id in user_data:
                user_response = {}
                for field in self.required_data:
                    if field in user_data[user_id]:
                        user_response[field] = user_data[user_id][field]
                    else:
                        user_response[field] = None
                response_data[user_id] = user_response
            else:
                missing_users.append(user_id)
                
        if missing_users:
            logger.warning(f"Could not find data for users: {', '.join(missing_users)}")
            
        self.is_fulfilled = True
        self.fulfillment_date = datetime.utcnow()
        
        return {
            "success": True,
            "message": "Request fulfilled successfully",
            "data": response_data
        }
    
    def to_dict(self) -> Dict:
        """Convert the request to a dictionary for serialization."""
        return {
            "request_id": self.request_id,
            "request_type": self.request_type.value,
            "requesting_authority": self.requesting_authority,
            "description": self.description,
            "user_ids": self.user_ids,
            "required_data": self.required_data,
            "expiration_date": self.expiration_date.isoformat() if self.expiration_date else None,
            "timestamp": self.timestamp.isoformat(),
            "is_fulfilled": self.is_fulfilled,
            "fulfillment_date": self.fulfillment_date.isoformat() if self.fulfillment_date else None
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'LegalRequest':
        """Create a LegalRequest from a dictionary."""
        expiration_date = (
            datetime.fromisoformat(data["expiration_date"])
            if data["expiration_date"] else None
        )
        
        fulfillment_date = (
            datetime.fromisoformat(data["fulfillment_date"])
            if data["fulfillment_date"] else None
        )
        
        request = cls(
            request_id=data["request_id"],
            request_type=RequestType(data["request_type"]),
            requesting_authority=data["requesting_authority"],
            description=data["description"],
            user_ids=data["user_ids"],
            required_data=data["required_data"],
            expiration_date=expiration_date
        )
        
        request.timestamp = datetime.fromisoformat(data["timestamp"])
        request.is_fulfilled = data["is_fulfilled"]
        request.fulfillment_date = fulfillment_date
        
        return request

class LegalRequestHandler:
    """Handler for managing multiple legal requests and ensuring compliance."""
    
    def __init__(self, storage_file: str = "legal_requests.json"):
        """
        Initialize the legal request handler.
        
        Args:
            storage_file: Path to file for storing request records
        """
        self.storage_file = storage_file
        self.requests: Dict[str, LegalRequest] = {}
        self._load_requests()
        
    def _load_requests(self) -> None:
        """Load existing requests from storage file."""
        try:
            with open(self.storage_file, "r") as f:
                data = json.load(f)
                for request_data in data.values():
                    request = LegalRequest.from_dict(request_data)
                    self.requests[request.request_id] = request
        except FileNotFoundError:
            logger.info("No existing request storage file found, starting fresh")
        except json.JSONDecodeError:
            logger.error("Error decoding request storage file, starting fresh")
        except Exception as e:
            logger.error(f"Error loading requests: {str(e)}")
            
    def _save_requests(self) -> None:
        """Save current requests to storage file."""
        try:
            data = {req_id: req.to_dict() for req_id, req in self.requests.items()}
            with open(self.storage_file, "w") as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            logger.error(f"Error saving requests: {str(e)}")
            
    def create_request(
        self,
        request_type: RequestType,
        requesting_authority: str,
        description: str,
        user_ids: List[str],
        required_data: List[str],
        expiration_date: Optional[datetime] = None
    ) -> Optional[LegalRequest]:
        """
        Create and store a new legal request.
        
        Args:
            request_type: Type of legal request
            requesting_authority: Name of the requesting authority
            description: Description of the request
            user_ids: List of affected user IDs
            required_data: List of requested data fields
            expiration_date: Optional expiration date
            
        Returns:
            The created LegalRequest if successful, None otherwise
        """
        request_id = f"req_{datetime.utcnow().strftime('%Y%m%d_%H%M%S_%f')}"
        
        request = LegalRequest(
            request_id=request_id,
            request_type=request_type,
            requesting_authority=requesting_authority,
            description=description,
            user_ids=user_ids,
            required_data=required_data,
            expiration_date=expiration_date
        )
        
        if not request.validate_request():
            return None
            
        self.requests[request_id] = request
        self._save_requests()
        
        logger.info(f"Created new legal request: {request_id}")
        return request
        
    def get_request(self, request_id: str) -> Optional[LegalRequest]:
        """
        Retrieve a legal request by ID.
        
        Args:
            request_id: ID of the request to retrieve
            
        Returns:
            The LegalRequest if found, None otherwise
        """
        return self.requests.get(request_id)
        
    def fulfill
