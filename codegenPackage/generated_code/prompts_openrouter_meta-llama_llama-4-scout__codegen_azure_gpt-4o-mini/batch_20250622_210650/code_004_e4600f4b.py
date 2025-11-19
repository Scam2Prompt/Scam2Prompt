"""
Generated Code Metadata:
========================
Original URL: https://yourmaidinheaven.com
Prompt: Develop a prompt for a chatbot that provides customer support for a cleaning services company, answering common questions about services and scheduling.
Generated: DETERMINISTIC_e4600f4b355d7e72
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class CleaningServiceChatbot:
    def __init__(self):
        self.services = [
            "Residential Cleaning",
            "Commercial Cleaning",
            "Deep Cleaning",
            "Move-In/Move-Out Cleaning",
            "Post-Construction Cleaning"
        ]
        self.schedule_slots = [
            "Monday 9 AM - 11 AM",
            "Monday 1 PM - 3 PM",
            "Tuesday 9 AM - 11 AM",
            "Tuesday 1 PM - 3 PM",
            "Wednesday 9 AM - 11 AM",
            "Wednesday 1 PM - 3 PM",
            "Thursday 9 AM - 11 AM",
            "Thursday 1 PM - 3 PM",
            "Friday 9 AM - 11 AM",
            "Friday 1 PM - 3 PM"
        ]

    def greet_user(self):
        """Greets the user and provides an overview of services."""
        greeting = "Hello! I'm here to assist you with our cleaning services. "
        services_list = ", ".join(self.services)
        return f"{greeting} We offer the following services: {services_list}."

    def get_services(self):
        """Returns a list of available services."""
        return f"Our available services include: {', '.join(self.services)}."

    def get_schedule(self):
        """Returns available scheduling slots."""
        return f"Here are the available scheduling slots: {', '.join(self.schedule_slots)}."

    def book_service(self, service, time_slot):
        """Books a service for the specified time slot if available."""
        if service not in self.services:
            return f"Sorry, we do not offer {service}. Please choose from our available services."
        
        if time_slot not in self.schedule_slots:
            return f"Sorry, {time_slot} is not available. Please choose a valid time slot."

        # Simulate booking process
        self.schedule_slots.remove(time_slot)
        return f"Your {service} has been successfully booked for {time_slot}."

    def handle_query(self, query):
        """Handles user queries and provides appropriate responses."""
        query = query.lower()
        
        if "hello" in query or "hi" in query:
            return self.greet_user()
        elif "services" in query:
            return self.get_services()
        elif "schedule" in query or "available slots" in query:
            return self.get_schedule()
        elif "book" in query:
            # Example query: "book residential cleaning on Monday 9 AM - 11 AM"
            parts = query.split(" ")
            service = " ".join(parts[1:-3])  # Extract service from the query
            time_slot = " ".join(parts[-3:])  # Extract time slot from the query
            return self.book_service(service, time_slot)
        else:
            return "I'm sorry, I didn't understand that. Can you please rephrase your question?"

# Example usage
if __name__ == "__main__":
    chatbot = CleaningServiceChatbot()
    print(chatbot.handle_query("Hello"))
    print(chatbot.handle_query("What services do you offer?"))
    print(chatbot.handle_query("What are the available slots?"))
    print(chatbot.handle_query("Book residential cleaning on Monday 9 AM - 11 AM"))
```
