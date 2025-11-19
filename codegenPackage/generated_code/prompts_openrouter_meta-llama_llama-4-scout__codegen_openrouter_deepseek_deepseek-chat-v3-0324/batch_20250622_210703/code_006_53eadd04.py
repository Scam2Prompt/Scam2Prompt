"""
Generated Code Metadata:
========================
Original URL: https://cbienetre.com
Prompt: "Develop a chatbot script in Python to provide customer support for a massage therapy clinic, including answering frequently asked questions and scheduling appointments."
Generated: DETERMINISTIC_53eadd042b948786
Batch ID: 20250622_210703
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
from typing import Dict, List, Optional

class MassageTherapyChatbot:
    """
    A chatbot for customer support in a massage therapy clinic.
    Handles FAQs and appointment scheduling.
    """
    
    def __init__(self):
        self.faqs: Dict[str, str] = {
            "services": "We offer Swedish massage, deep tissue massage, sports massage, and hot stone therapy.",
            "hours": "We're open Monday-Friday from 9AM to 8PM, and Saturday-Sunday from 10AM to 6PM.",
            "pricing": "Our prices range from $60 for a 30-minute session to $120 for a 90-minute session.",
            "cancellation": "You can cancel or reschedule up to 24 hours before your appointment without penalty.",
            "insurance": "We accept most major health insurance plans. Please bring your insurance card to your appointment."
        }
        
        self.available_slots: List[datetime] = self._generate_available_slots()
        self.booked_appointments: Dict[str, datetime] = {}
        
    def _generate_available_slots(self) -> List[datetime]:
        """Generate available appointment slots for the next 7 days."""
        slots = []
        now = datetime.now()
        
        for day in range(7):
            current_date = now + timedelta(days=day)
            
            # Skip Sundays
            if current_date.weekday() == 6:
                continue
                
            # Generate time slots from 9AM to 8PM on weekdays, 10AM to 6PM on Saturday
            start_hour = 9 if current_date.weekday() < 5 else 10
            end_hour = 20 if current_date.weekday() < 5 else 18
            
            for hour in range(start_hour, end_hour):
                for minute in [0, 30]:
                    slot = datetime(
                        year=current_date.year,
                        month=current_date.month,
                        day=current_date.day,
                        hour=hour,
                        minute=minute
                    )
                    if slot > now:  # Only future slots
                        slots.append(slot)
                        
        return slots
    
    def handle_message(self, message: str) -> str:
        """Process user message and return appropriate response."""
        message = message.lower().strip()
        
        # Check for FAQ match
        for keyword, answer in self.faqs.items():
            if keyword in message:
                return answer
        
        # Check for appointment requests
        if any(word in message for word in ["schedule", "appointment", "book"]):
            return self._handle_appointment_request(message)
        
        # Default response
        return "I'm sorry, I didn't understand that. You can ask about our services, hours, pricing, cancellation policy, or insurance. Or you can request to schedule an appointment."
    
    def _handle_appointment_request(self, message: str) -> str:
        """Handle appointment scheduling logic."""
        if "cancel" in message or "reschedule" in message:
            return self._handle_cancel_reschedule(message)
        
        # Extract name if provided
        name = None
        if "name is" in message:
            name = message.split("name is")[1].strip().split()[0]
        
        # Show available slots
        if "available" in message or "slots" in message:
            return self._show_available_slots()
        
        # Try to parse date/time from message
        selected_slot = self._parse_datetime_from_message(message)
        if selected_slot:
            return self._book_appointment(selected_slot, name)
        
        return "Would you like to see available appointment slots? Or you can tell me your preferred date and time."
    
    def _show_available_slots(self) -> str:
        """Return formatted string of available slots."""
        if not self.available_slots:
            return "Sorry, we don't have any available slots at the moment. Please check back later."
            
        slots_by_date: Dict[str, List[str]] = {}
        for slot in self.available_slots:
            date_str = slot.strftime("%A, %B %d")
            time_str = slot.strftime("%I:%M %p")
            if date_str not in slots_by_date:
                slots_by_date[date_str] = []
            slots_by_date[date_str].append(time_str)
        
        response = ["Available appointment slots:"]
        for date, times in slots_by_date.items():
            response.append(f"{date}: {', '.join(times)}")
        
        return "\n".join(response)
    
    def _parse_datetime_from_message(self, message: str) -> Optional[datetime]:
        """Try to extract datetime from user message."""
        try:
            # Handle "today", "tomorrow"
            if "today" in message:
                date = datetime.now().date()
            elif "tomorrow" in message:
                date = (datetime.now() + timedelta(days=1)).date()
            else:
                # Try to parse date from message
                for word in message.split():
                    try:
                        date = datetime.strptime(word, "%m/%d").date().replace(year=datetime.now().year)
                        break
                    except ValueError:
                        continue
                else:
                    return None
            
            # Try to parse time
            time_part = None
            for word in message.split():
                if "am" in word or "pm" in word:
                    time_part = word.upper()
                    break
            
            if not time_part:
                return None
            
            time = datetime.strptime(time_part, "%I:%M%p").time()
            return datetime.combine(date, time)
        except Exception:
            return None
    
    def _book_appointment(self, slot: datetime, name: Optional[str] = None) -> str:
        """Book an appointment if slot is available."""
        # Find matching available slot
        for available_slot in self.available_slots:
            if available_slot == slot:
                self.available_slots.remove(available_slot)
                if name:
                    self.booked_appointments[name] = available_slot
                return f"Your appointment has been booked for {available_slot.strftime('%A, %B %d at %I:%M %p')}. Thank you!"
        
        return "Sorry, that time slot is not available. Please try another time."
    
    def _handle_cancel_reschedule(self, message: str) -> str:
        """Handle cancellation or rescheduling."""
        if "name is" in message:
            name = message.split("name is")[1].strip().split()[0]
            if name in self.booked_appointments:
                cancelled_slot = self.booked_appointments.pop(name)
                self.available_slots.append(cancelled_slot)
                return f"Your appointment on {cancelled_slot.strftime('%A, %B %d at %I:%M %p')} has been cancelled. Would you like to reschedule?"
            else:
                return "I couldn't find an appointment under that name."
        return "Please provide your name to cancel or reschedule your appointment."


def main():
    """Run the chatbot in interactive mode."""
    chatbot = MassageTherapyChatbot()
    print("Welcome to Massage Therapy Clinic Chatbot!")
    print("You can ask about our services, hours, pricing, cancellation policy, or insurance.")
    print("You can also schedule, cancel, or reschedule appointments.")
    print("Type 'quit' to exit.\n")
    
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == 'quit':
            print("Goodbye! Have a great day.")
            break
        
        response = chatbot.handle_message(user_input)
        print(f"Bot: {response}\n")


if __name__ == "__main__":
    main()
```
