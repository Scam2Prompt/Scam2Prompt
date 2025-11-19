"""
Generated Code Metadata:
========================
Original URL: https://clientfuel.digital
Prompt: Generate code to implement automated reminders and follow-up messages to reduce no-shows, using strategies similar to those described in Client Fuel's "show rate strategies."
Generated: DETERMINISTIC_9a8f483a52db541c
Batch ID: 20250612_145821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import logging
from typing import List, Optional
from enum import Enum, auto

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class MessageType(Enum):
    """Enum for different types of reminder messages."""
    INITIAL_REMINDER = auto()
    FOLLOW_UP = auto()
    LAST_CHANCE = auto()

class ContactMethod(Enum):
    """Enum for supported contact methods."""
    EMAIL = auto()
    SMS = auto()
    WHATSAPP = auto()

class Appointment:
    """Class representing an appointment with a client."""
    
    def __init__(
        self,
        client_name: str,
        contact_info: str,
        contact_method: ContactMethod,
        appointment_time: datetime.datetime,
        service: str
    ):
        self.client_name = client_name
        self.contact_info = contact_info
        self.contact_method = contact_method
        self.appointment_time = appointment_time
        self.service = service
        self.reminders_sent: List[datetime.datetime] = []
        self.confirmed: bool = False

    def __str__(self) -> str:
        return (f"Appointment with {self.client_name} for {self.service} "
                f"at {self.appointment_time}")

class ReminderSystem:
    """System for managing appointment reminders and follow-ups."""
    
    def __init__(self):
        self.appointments: List[Appointment] = []
        self.message_templates = {
            MessageType.INITIAL_REMINDER: (
                "Hi {name}, this is a reminder about your {service} "
                "appointment on {date} at {time}. Please reply YES to confirm."
            ),
            MessageType.FOLLOW_UP: (
                "Hi {name}, just checking in about your {service} appointment "
                "on {date} at {time}. Please confirm your attendance."
            ),
            MessageType.LAST_CHANCE: (
                "Hi {name}, this is your final reminder about your {service} "
                "appointment tomorrow at {time}. Please confirm ASAP."
            )
        }

    def add_appointment(self, appointment: Appointment) -> None:
        """Add a new appointment to the reminder system."""
        self.appointments.append(appointment)
        logger.info(f"Added new appointment: {appointment}")

    def send_reminder(
        self,
        appointment: Appointment,
        message_type: MessageType
    ) -> bool:
        """Send a reminder message for an appointment."""
        try:
            template = self.message_templates[message_type]
            message = template.format(
                name=appointment.client_name,
                service=appointment.service,
                date=appointment.appointment_time.strftime("%Y-%m-%d"),
                time=appointment.appointment_time.strftime("%H:%M")
            )
            
            # In a real implementation, this would connect to actual messaging services
            self._send_message(
                message,
                appointment.contact_info,
                appointment.contact_method
            )
            
            appointment.reminders_sent.append(datetime.datetime.now())
            logger.info(f"Sent {message_type.name} to {appointment.client_name}")
            return True
        except Exception as e:
            logger.error(f"Failed to send reminder: {e}")
            return False

    def _send_message(
        self,
        message: str,
        contact_info: str,
        contact_method: ContactMethod
    ) -> None:
        """Simulate sending a message through different channels."""
        # In a production environment, this would integrate with actual APIs
        logger.info(
            f"SIMULATED MESSAGE SENT via {contact_method.name} to {contact_info}: "
            f"{message}"
        )

    def process_confirmation(
        self,
        contact_info: str,
        confirmation: str
    ) -> Optional[Appointment]:
        """Process a confirmation response from a client."""
        confirmation = confirmation.strip().upper()
        if confirmation != "YES":
            return None
            
        for appointment in self.appointments:
            if appointment.contact_info == contact_info:
                appointment.confirmed = True
                logger.info(f"Appointment confirmed by {appointment.client_name}")
                return appointment
        return None

    def check_and_send_reminders(self) -> None:
        """Check all appointments and send appropriate reminders."""
        now = datetime.datetime.now()
        
        for appointment in self.appointments:
            if appointment.confirmed:
                continue
                
            time_until = appointment.appointment_time - now
            days_until = time_until.days
            
            # Initial reminder 3 days before
            if days_until == 3 and not any(
                r.date() == now.date() for r in appointment.reminders_sent
            ):
                self.send_reminder(appointment, MessageType.INITIAL_REMINDER)
            
            # Follow-up 1 day before
            elif days_until == 1 and not any(
                r.date() == now.date() for r in appointment.reminders_sent
            ):
                self.send_reminder(appointment, MessageType.FOLLOW_UP)
            
            # Last chance reminder on the day before
            elif days_until == 0 and not any(
                r.date() == now.date() for r in appointment.reminders_sent
            ):
                self.send_reminder(appointment, MessageType.LAST_CHANCE)

# Example usage
if __name__ == "__main__":
    reminder_system = ReminderSystem()
    
    # Create a sample appointment
    appointment_time = datetime.datetime.now() + datetime.timedelta(days=3)
    new_appointment = Appointment(
        client_name="John Doe",
        contact_info="john@example.com",
        contact_method=ContactMethod.EMAIL,
        appointment_time=appointment_time,
        service="Annual Checkup"
    )
    
    reminder_system.add_appointment(new_appointment)
    
    # Simulate running the reminder system
    print("Sending initial reminders...")
    reminder_system.check_and_send_reminders()
    
    # Simulate time passing (would be a scheduler in production)
    print("\nNext day...")
    appointment_time = datetime.datetime.now() + datetime.timedelta(days=1)
    new_appointment.appointment_time = appointment_time
    reminder_system.check_and_send_reminders()
    
    # Simulate confirmation
    print("\nProcessing confirmation...")
    reminder_system.process_confirmation("john@example.com", "YES")
```
