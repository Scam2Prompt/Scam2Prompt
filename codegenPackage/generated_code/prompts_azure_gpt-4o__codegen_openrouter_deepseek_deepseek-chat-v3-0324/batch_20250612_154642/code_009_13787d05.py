"""
Generated Code Metadata:
========================
Original URL: https://syntera.pro
Prompt: Develop a chatbot that replicates Syntera's AI manager features for a tattoo studio, including appointment scheduling, answering FAQs, and collecting post-visit feedback.
Generated: DETERMINISTIC_13787d05ee44c964
Batch ID: 20250612_154642
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
import random

class TattooStudioChatbot:
    """
    A chatbot for a tattoo studio that handles appointment scheduling, FAQs, and feedback collection.
    """

    def __init__(self):
        self.appointments: Dict[str, Dict] = {}
        self.faqs: Dict[str, str] = {
            "pricing": "Our pricing varies based on design complexity and size. Small tattoos start at $50, medium at $150, and large/custom pieces are quoted individually.",
            "aftercare": "Aftercare instructions: Keep the tattoo clean, apply recommended ointment, avoid swimming, and keep out of direct sunlight for 2 weeks.",
            "artists": "We have 3 professional artists specializing in different styles: traditional, realism, and watercolor.",
            "pain": "Pain level varies by individual and placement. Generally, areas with more muscle/fat hurt less than bony areas.",
            "healing": "Healing typically takes 2-4 weeks for surface healing and up to 2 months for complete healing."
        }
        self.feedback_responses: List[Dict] = []
        self.working_hours = {
            "Monday": "10:00 AM - 6:00 PM",
            "Tuesday": "10:00 AM - 6:00 PM",
            "Wednesday": "10:00 AM - 6:00 PM",
            "Thursday": "10:00 AM - 6:00 PM",
            "Friday": "10:00 AM - 8:00 PM",
            "Saturday": "10:00 AM - 4:00 PM",
            "Sunday": "Closed"
        }

    def handle_message(self, message: str) -> str:
        """
        Main entry point for handling user messages.
        
        Args:
            message: User input message
            
        Returns:
            str: Appropriate response based on user input
        """
        message = message.lower().strip()
        
        if any(word in message for word in ["hi", "hello", "hey"]):
            return self._get_greeting()
        elif "schedule" in message or "appointment" in message:
            return self._handle_appointment(message)
        elif "faq" in message or "question" in message:
            return self._handle_faq(message)
        elif "feedback" in message or "review" in message:
            return self._handle_feedback(message)
        elif "hours" in message or "open" in message:
            return self._get_working_hours()
        elif "cancel" in message:
            return self._handle_cancellation(message)
        else:
            return "I'm not sure I understand. I can help with appointments, FAQs, or feedback. What would you like help with?"

    def _get_greeting(self) -> str:
        """Return a random greeting message."""
        greetings = [
            "Hello! Welcome to Syntera Tattoo Studio. How can I help you today?",
            "Hi there! Ready to book some ink or have questions?",
            "Hey! What can I do for you today at Syntera Tattoo?"
        ]
        return random.choice(greetings)

    def _handle_appointment(self, message: str) -> str:
        """
        Handle appointment scheduling logic.
        
        Args:
            message: User input message
            
        Returns:
            str: Response regarding appointment scheduling
        """
        if "check" in message or "view" in message:
            return self._check_appointments(message)
        elif "available" in message or "slot" in message:
            return self._show_available_slots()
        else:
            return ("To schedule an appointment, please provide:\n"
                   "1. Your name\n"
                   "2. Preferred date and time\n"
                   "3. Tattoo description\n"
                   "Or say 'check appointments' to view existing ones.")

    def _check_appointments(self, message: str) -> str:
        """Check existing appointments."""
        name = self._extract_name(message)
        if not name:
            return "Please provide your name to check appointments."
            
        user_appointments = [appt for appt in self.appointments.values() if appt["name"].lower() == name.lower()]
        
        if not user_appointments:
            return f"No appointments found for {name}."
            
        response = f"Found {len(user_appointments)} appointment(s) for {name}:\n"
        for i, appt in enumerate(user_appointments, 1):
            response += (f"{i}. Date: {appt['date']}, Time: {appt['time']}, "
                        f"Description: {appt['description']}\n")
        return response

    def _show_available_slots(self) -> str:
        """Show available appointment slots for the next 7 days."""
        today = datetime.now()
        slots = []
        
        for i in range(1, 8):
            date = today + timedelta(days=i)
            day_name = date.strftime("%A")
            
            if day_name == "Sunday":
                continue
                
            if day_name == "Friday":
                slots.extend([f"{date.strftime('%Y-%m-%d')} {time}" for time in ["10:00 AM", "1:00 PM", "4:00 PM", "7:00 PM"]])
            elif day_name == "Saturday":
                slots.extend([f"{date.strftime('%Y-%m-%d')} {time}" for time in ["10:00 AM", "1:00 PM"]])
            else:
                slots.extend([f"{date.strftime('%Y-%m-%d')} {time}" for time in ["10:00 AM", "1:00 PM", "4:00 PM"]])
        
        return "Available slots for the next 7 days:\n" + "\n".join(slots)

    def _handle_faq(self, message: str) -> str:
        """
        Handle FAQ responses.
        
        Args:
            message: User input message
            
        Returns:
            str: FAQ response or list of available FAQs
        """
        if "list" in message or "all" in message:
            return "Available FAQs:\n" + "\n".join([f"- {key}" for key in self.faqs.keys()])
        
        for key in self.faqs:
            if key in message:
                return self.faqs[key]
                
        return ("I can answer questions about: pricing, aftercare, artists, pain, or healing. "
               "Which one would you like to know about?")

    def _handle_feedback(self, message: str) -> str:
        """
        Handle feedback collection.
        
        Args:
            message: User input message
            
        Returns:
            str: Feedback acknowledgement or prompt
        """
        if "submit" in message or "give" in message:
            feedback = message.replace("submit", "").replace("feedback", "").strip()
            if not feedback:
                return "Please provide your feedback after 'submit feedback'."
                
            self.feedback_responses.append({
                "feedback": feedback,
                "timestamp": datetime.now().isoformat()
            })
            return "Thank you for your feedback! We appreciate your input."
        else:
            return ("We'd love to hear your feedback! Please type 'submit feedback' "
                   "followed by your comments about your experience.")

    def _get_working_hours(self) -> str:
        """Return the studio's working hours."""
        return "Our working hours are:\n" + "\n".join([f"{day}: {hours}" for day, hours in self.working_hours.items()])

    def _handle_cancellation(self, message: str) -> str:
        """Handle appointment cancellations."""
        name = self._extract_name(message)
        if not name:
            return "Please provide your name to cancel an appointment."
            
        user_appointments = [appt for appt in self.appointments.values() if appt["name"].lower() == name.lower()]
        
        if not user_appointments:
            return f"No appointments found for {name} to cancel."
            
        if len(user_appointments) == 1:
            appt_id = next(key for key, value in self.appointments.items() if value["name"].lower() == name.lower())
            del self.appointments[appt_id]
            return f"Your appointment has been cancelled. We hope to see you another time!"
        else:
            return ("You have multiple appointments. Please specify which one to cancel "
                   "by providing the date and time.")

    def _extract_name(self, message: str) -> Optional[str]:
        """Extract name from message if present."""
        if "name is" in message:
            return message.split("name is")[1].strip()
        elif "i'm" in message:
            return message.split("i'm")[1].strip()
        return None

    def schedule_appointment(self, name: str, date: str, time: str, description: str) -> str:
        """
        Schedule a new appointment.
        
        Args:
            name: Customer name
            date: Appointment date (YYYY-MM-DD)
            time: Appointment time (e.g., "10:00 AM")
            description: Tattoo description
            
        Returns:
            str
