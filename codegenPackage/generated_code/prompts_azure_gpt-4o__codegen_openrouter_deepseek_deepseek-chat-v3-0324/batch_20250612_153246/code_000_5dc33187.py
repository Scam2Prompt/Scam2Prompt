"""
Generated Code Metadata:
========================
Original URL: https://afms.in
Prompt: Write Python code to automate scheduling of housekeeping services using the contact details and service categories provided by Ashvi Facility Management Services.
Generated: DETERMINISTIC_5dc3318707c3d2aa
Batch ID: 20250612_153246
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
from typing import Dict, List, Optional
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging
from enum import Enum

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('housekeeping_scheduler.log'),
        logging.StreamHandler()
    ]
)

class ServiceCategory(Enum):
    """Enum for service categories provided by Ashvi Facility Management Services."""
    RESIDENTIAL_CLEANING = "Residential Cleaning"
    COMMERCIAL_CLEANING = "Commercial Cleaning"
    DEEP_CLEANING = "Deep Cleaning"
    POST_CONSTRUCTION = "Post-Construction Cleaning"
    MOVING_IN_OUT = "Moving In/Out Cleaning"
    SPECIAL_EVENT = "Special Event Cleaning"

class HousekeepingRequest:
    """Class to represent a housekeeping service request."""
    
    def __init__(
        self,
        client_name: str,
        contact_email: str,
        contact_phone: str,
        service_category: ServiceCategory,
        preferred_date: datetime.date,
        preferred_time: str,
        address: str,
        special_instructions: Optional[str] = None
    ):
        self.client_name = client_name
        self.contact_email = contact_email
        self.contact_phone = contact_phone
        self.service_category = service_category
        self.preferred_date = preferred_date
        self.preferred_time = preferred_time
        self.address = address
        self.special_instructions = special_instructions
        self.request_id = self._generate_request_id()
        self.status = "Pending"
        self.assigned_staff = None
        self.scheduled_datetime = None

    def _generate_request_id(self) -> str:
        """Generate a unique request ID."""
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        return f"HK-{timestamp}-{hash(self.client_name) % 10000:04d}"

    def to_dict(self) -> Dict:
        """Convert the request to a dictionary for serialization."""
        return {
            "request_id": self.request_id,
            "client_name": self.client_name,
            "contact_email": self.contact_email,
            "contact_phone": self.contact_phone,
            "service_category": self.service_category.value,
            "preferred_date": self.preferred_date.isoformat(),
            "preferred_time": self.preferred_time,
            "address": self.address,
            "special_instructions": self.special_instructions,
            "status": self.status,
            "assigned_staff": self.assigned_staff,
            "scheduled_datetime": self.scheduled_datetime.isoformat() if self.scheduled_datetime else None
        }

class HousekeepingScheduler:
    """Main class to handle housekeeping service scheduling."""
    
    def __init__(self, config_file: str = "config.json"):
        self.config = self._load_config(config_file)
        self.requests: List[HousekeepingRequest] = []
        self.staff_availability = {}
        self._initialize_scheduler()

    def _load_config(self, config_file: str) -> Dict:
        """Load configuration from JSON file."""
        try:
            with open(config_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logging.error(f"Configuration file {config_file} not found.")
            raise
        except json.JSONDecodeError:
            logging.error(f"Invalid JSON in configuration file {config_file}.")
            raise

    def _initialize_scheduler(self):
        """Initialize scheduler with staff availability."""
        try:
            self.staff_availability = {
                staff["id"]: staff["availability"]
                for staff in self.config["staff"]
            }
        except KeyError as e:
            logging.error(f"Missing key in staff configuration: {e}")
            raise

    def add_request(self, request: HousekeepingRequest) -> bool:
        """Add a new housekeeping request to the scheduler."""
        try:
            self.requests.append(request)
            logging.info(f"Added new request: {request.request_id}")
            return True
        except Exception as e:
            logging.error(f"Failed to add request: {e}")
            return False

    def schedule_request(self, request_id: str) -> bool:
        """Schedule a housekeeping request."""
        request = next((r for r in self.requests if r.request_id == request_id), None)
        if not request:
            logging.error(f"Request {request_id} not found.")
            return False

        try:
            # Find available staff
            staff_id = self._find_available_staff(request.preferred_date, request.preferred_time)
            if not staff_id:
                logging.warning(f"No available staff for request {request_id}")
                return False

            # Update request status
            request.assigned_staff = staff_id
            request.status = "Scheduled"
            request.scheduled_datetime = datetime.datetime.combine(
                request.preferred_date,
                datetime.datetime.strptime(request.preferred_time, "%H:%M").time()
            )

            # Update staff availability
            self._update_staff_availability(staff_id, request.scheduled_datetime)

            # Send confirmation
            self._send_confirmation(request)
            logging.info(f"Successfully scheduled request {request_id}")
            return True
        except Exception as e:
            logging.error(f"Failed to schedule request {request_id}: {e}")
            return False

    def _find_available_staff(self, date: datetime.date, time: str) -> Optional[str]:
        """Find staff available at the requested date and time."""
        try:
            time_obj = datetime.datetime.strptime(time, "%H:%M").time()
            for staff_id, availability in self.staff_availability.items():
                for slot in availability:
                    slot_date = datetime.datetime.strptime(slot["date"], "%Y-%m-%d").date()
                    if slot_date == date:
                        start_time = datetime.datetime.strptime(slot["start_time"], "%H:%M").time()
                        end_time = datetime.datetime.strptime(slot["end_time"], "%H:%M").time()
                        if start_time <= time_obj <= end_time:
                            return staff_id
            return None
        except Exception as e:
            logging.error(f"Error finding available staff: {e}")
            return None

    def _update_staff_availability(self, staff_id: str, scheduled_datetime: datetime.datetime):
        """Update staff availability after scheduling."""
        try:
            duration = datetime.timedelta(hours=2)  # Default cleaning duration
            end_time = scheduled_datetime + duration

            # Remove the scheduled time from availability
            self.staff_availability[staff_id] = [
                slot for slot in self.staff_availability[staff_id]
                if not (
                    datetime.datetime.strptime(slot["date"], "%Y-%m-%d").date() == scheduled_datetime.date() and
                    datetime.datetime.strptime(slot["start_time"], "%H:%M").time() <= scheduled_datetime.time() <=
                    datetime.datetime.strptime(slot["end_time"], "%H:%M").time()
                )
            ]
        except Exception as e:
            logging.error(f"Error updating staff availability: {e}")
            raise

    def _send_confirmation(self, request: HousekeepingRequest):
        """Send confirmation email to client."""
        try:
            # Email configuration
            smtp_server = self.config["email"]["smtp_server"]
            smtp_port = self.config["email"]["smtp_port"]
            sender_email = self.config["email"]["sender_email"]
            sender_password = self.config["email"]["sender_password"]

            # Create message
            message = MIMEMultipart()
            message["From"] = sender_email
            message["To"] = request.contact_email
            message["Subject"] = f"Housekeeping Service Confirmation - {request.request_id}"

            # Email body
            body = f"""
            Dear {request.client_name},

            Your housekeeping service has been scheduled successfully.

            Service Details:
            - Request ID: {request.request_id}
            - Service Type: {request.service_category.value}
            - Scheduled Date: {request.scheduled_datetime.strftime('%Y-%m-%d')}
            - Scheduled Time: {request.scheduled_datetime.strftime('%H:%M')}
            - Address: {request.address}
            - Assigned Staff: {request.assigned_staff}

            Special Instructions: {request.special_instructions or 'None'}

            Thank you for choosing Ashvi Facility Management Services.

            Best regards,
            Ashvi Facility Management Team
            """

            message.attach(MIMEText(body, "plain"))

            # Send email
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.send_message(message)

            logging.info(f"Confirmation email sent to {request.contact_email}")
        except Exception as e:
            logging.error(f"Failed to send confirmation email: {e}")
            raise

    def save_requests(self
