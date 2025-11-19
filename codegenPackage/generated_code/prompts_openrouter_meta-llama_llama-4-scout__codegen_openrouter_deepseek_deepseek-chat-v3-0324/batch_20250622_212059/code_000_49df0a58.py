"""
Generated Code Metadata:
========================
Original URL: https://syntera.pro
Prompt: "Implement an AI-powered chatbot for a dental clinic to automate appointment scheduling and customer inquiries, similar to the Nowa Clinic case study."
Generated: DETERMINISTIC_49df0a58c9fda621
Batch ID: 20250622_212059
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Union
import pytz
from enum import Enum

# Database simulation (in production, replace with actual database)
class Database:
    def __init__(self):
        self.appointments = []
        self.dentists = [
            {"id": 1, "name": "Dr. Smith", "specialty": "General Dentistry", "schedule": []},
            {"id": 2, "name": "Dr. Johnson", "specialty": "Orthodontics", "schedule": []},
            {"id": 3, "name": "Dr. Williams", "specialty": "Pediatric Dentistry", "schedule": []}
        ]
        self.services = [
            {"id": 1, "name": "Teeth Cleaning", "duration": 30},
            {"id": 2, "name": "Dental Checkup", "duration": 60},
            {"id": 3, "name": "Tooth Extraction", "duration": 45},
            {"id": 4, "name": "Braces Consultation", "duration": 90}
        ]

    def get_available_slots(self, dentist_id: int, date: str) -> List[Dict]:
        dentist = next((d for d in self.dentists if d["id"] == dentist_id), None)
        if not dentist:
            return []
        
        # Generate available slots (9 AM to 5 PM with 30 min intervals)
        start_time = datetime.strptime(f"{date} 09:00", "%Y-%m-%d %H:%M")
        end_time = datetime.strptime(f"{date} 17:00", "%Y-%m-%d %H:%M")
        
        slots = []
        current_time = start_time
        while current_time < end_time:
            slot_end = current_time + timedelta(minutes=30)
            if not self._is_slot_booked(dentist_id, current_time, slot_end):
                slots.append({
                    "start": current_time.strftime("%H:%M"),
                    "end": slot_end.strftime("%H:%M")
                })
            current_time += timedelta(minutes=30)
        return slots

    def _is_slot_booked(self, dentist_id: int, start: datetime, end: datetime) -> bool:
        for appt in self.appointments:
            if appt["dentist_id"] == dentist_id:
                appt_start = datetime.strptime(f"{appt['date']} {appt['start_time']}", "%Y-%m-%d %H:%M")
                appt_end = appt_start + timedelta(minutes=appt["duration"])
                if not (end <= appt_start or start >= appt_end):
                    return True
        return False

    def book_appointment(self, patient_name: str, dentist_id: int, service_id: int, date: str, start_time: str) -> Dict:
        service = next((s for s in self.services if s["id"] == service_id), None)
        if not service:
            raise ValueError("Invalid service ID")
        
        dentist = next((d for d in self.dentists if d["id"] == dentist_id), None)
        if not dentist:
            raise ValueError("Invalid dentist ID")
        
        appointment = {
            "id": len(self.appointments) + 1,
            "patient_name": patient_name,
            "dentist_id": dentist_id,
            "dentist_name": dentist["name"],
            "service_id": service_id,
            "service_name": service["name"],
            "date": date,
            "start_time": start_time,
            "duration": service["duration"],
            "status": "Scheduled"
        }
        self.appointments.append(appointment)
        return appointment

class Intent(Enum):
    GREETING = "greeting"
    BOOK_APPOINTMENT = "book_appointment"
    CHECK_AVAILABILITY = "check_availability"
    LIST_SERVICES = "list_services"
    LIST_DENTISTS = "list_dentists"
    CANCEL_APPOINTMENT = "cancel_appointment"
    THANKS = "thanks"
    GOODBYE = "goodbye"
    UNKNOWN = "unknown"

class DentalChatbot:
    def __init__(self):
        self.db = Database()
        self.context = {}

    def process_message(self, message: str) -> Dict:
        """Process user message and return bot response"""
        intent = self._classify_intent(message)
        response = self._handle_intent(intent, message)
        return response

    def _classify_intent(self, message: str) -> Intent:
        """Classify user intent based on message content"""
        message = message.lower().strip()
        
        greetings = ["hi", "hello", "hey", "good morning", "good afternoon"]
        if any(word in message for word in greetings):
            return Intent.GREETING
        
        appointment_keywords = ["book", "schedule", "make an appointment"]
        if any(word in message for word in appointment_keywords):
            return Intent.BOOK_APPOINTMENT
            
        availability_keywords = ["available", "availability", "when can i come"]
        if any(word in message for word in availability_keywords):
            return Intent.CHECK_AVAILABILITY
            
        service_keywords = ["services", "what do you offer", "treatments"]
        if any(word in message for word in service_keywords):
            return Intent.LIST_SERVICES
            
        dentist_keywords = ["dentists", "doctors", "who are the dentists"]
        if any(word in message for word in dentist_keywords):
            return Intent.LIST_DENTISTS
            
        cancel_keywords = ["cancel", "reschedule", "change appointment"]
        if any(word in message for word in cancel_keywords):
            return Intent.CANCEL_APPOINTMENT
            
        thanks_keywords = ["thanks", "thank you", "appreciate"]
        if any(word in message for word in thanks_keywords):
            return Intent.THANKS
            
        goodbye_keywords = ["bye", "goodbye", "see you"]
        if any(word in message for word in goodbye_keywords):
            return Intent.GOODBYE
            
        return Intent.UNKNOWN

    def _handle_intent(self, intent: Intent, message: str) -> Dict:
        """Handle the classified intent and generate appropriate response"""
        if intent == Intent.GREETING:
            return {
                "response": "Hello! Welcome to Smile Dental Clinic. How can I help you today?",
                "suggestions": [
                    "Book an appointment",
                    "Check dentist availability",
                    "List services",
                    "List dentists"
                ]
            }
            
        elif intent == Intent.BOOK_APPOINTMENT:
            return self._handle_book_appointment(message)
            
        elif intent == Intent.CHECK_AVAILABILITY:
            return self._handle_check_availability(message)
            
        elif intent == Intent.LIST_SERVICES:
            services = "\n".join([f"{s['id']}. {s['name']} ({s['duration']} mins)" for s in self.db.services])
            return {
                "response": f"We offer the following services:\n{services}",
                "suggestions": ["Book an appointment", "Check availability"]
            }
            
        elif intent == Intent.LIST_DENTISTS:
            dentists = "\n".join([f"{d['id']}. {d['name']} ({d['specialty']})" for d in self.db.dentists])
            return {
                "response": f"Our dentists:\n{dentists}",
                "suggestions": ["Book an appointment", "Check availability"]
            }
            
        elif intent == Intent.CANCEL_APPOINTMENT:
            return {
                "response": "Please provide your appointment ID to cancel or reschedule.",
                "needs_follow_up": True,
                "follow_up_intent": "cancel_appointment"
            }
            
        elif intent == Intent.THANKS:
            return {
                "response": "You're welcome! Is there anything else I can help you with?",
                "suggestions": ["Book an appointment", "List services"]
            }
            
        elif intent == Intent.GOODBYE:
            return {
                "response": "Goodbye! Have a great day. Don't forget to brush twice daily!",
                "end_conversation": True
            }
            
        else:
            return {
                "response": "I'm sorry, I didn't understand that. How can I help you?",
                "suggestions": [
                    "Book an appointment",
                    "Check dentist availability",
                    "List services",
                    "List dentists"
                ]
            }

    def _handle_book_appointment(self, message: str) -> Dict:
        """Handle appointment booking process"""
        if "context" not in self.context:
            # First step: Ask for dentist
            self.context["intent"] = "book_appointment"
            return {
                "response": "Which dentist would you like to book with? Here are our dentists:",
                "dentists": [{"id": d["id"], "name": d["name"], "specialty": d["
