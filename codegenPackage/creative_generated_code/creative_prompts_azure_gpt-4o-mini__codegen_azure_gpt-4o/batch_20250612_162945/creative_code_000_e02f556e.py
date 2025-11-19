"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onchain-adventures.com
Prompt: Generate a code snippet for a consultancy service management system that includes features for tracking client consultations and feedback, inspired by Dusanto Consultancy Trading OU's focus on customer satisfaction.
Generated: DETERMINISTIC_e02f556e179a14ff
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Consultancy Service Management System
# This script provides functionality to track client consultations and feedback,
# with a focus on customer satisfaction.

import datetime

class Client:
    """
    Represents a client in the system.
    """
    def __init__(self, client_id, name, email):
        self.client_id = client_id
        self.name = name
        self.email = email

    def __str__(self):
        return f"Client({self.client_id}, {self.name}, {self.email})"


class Consultation:
    """
    Represents a consultation event.
    """
    def __init__(self, consultation_id, client, date, notes):
        self.consultation_id = consultation_id
        self.client = client
        self.date = date
        self.notes = notes

    def __str__(self):
        return (f"Consultation({self.consultation_id}, Client: {self.client.name}, "
                f"Date: {self.date}, Notes: {self.notes})")


class Feedback:
    """
    Represents feedback provided by a client.
    """
    def __init__(self, feedback_id, client, consultation, rating, comments):
        self.feedback_id = feedback_id
        self.client = client
        self.consultation = consultation
        self.rating = rating  # Rating should be between 1 and 5
        self.comments = comments

    def __str__(self):
        return (f"Feedback({self.feedback_id}, Client: {self.client.name}, "
                f"Consultation: {self.consultation.consultation_id}, "
                f"Rating: {self.rating}, Comments: {self.comments})")


class ConsultancyServiceManagementSystem:
    """
    Manages client consultations and feedback.
    """
    def __init__(self):
        self.clients = {}
        self.consultations = {}
        self.feedbacks = {}

    def add_client(self, client_id, name, email):
        """
        Adds a new client to the system.
        """
        if client_id in self.clients:
            raise ValueError(f"Client with ID {client_id} already exists.")
        self.clients[client_id] = Client(client_id, name, email)
        print(f"Client {name} added successfully.")

    def schedule_consultation(self, consultation_id, client_id, date, notes):
        """
        Schedules a new consultation for a client.
        """
        if consultation_id in self.consultations:
            raise ValueError(f"Consultation with ID {consultation_id} already exists.")
        if client_id not in self.clients:
            raise ValueError(f"Client with ID {client_id} not found.")
        client = self.clients[client_id]
        consultation = Consultation(consultation_id, client, date, notes)
        self.consultations[consultation_id] = consultation
        print(f"Consultation scheduled for {client.name} on {date}.")

    def add_feedback(self, feedback_id, consultation_id, rating, comments):
        """
        Adds feedback for a consultation.
        """
        if feedback_id in self.feedbacks:
            raise ValueError(f"Feedback with ID {feedback_id} already exists.")
        if consultation_id not in self.consultations:
            raise ValueError(f"Consultation with ID {consultation_id} not found.")
        if not (1 <= rating <= 5):
            raise ValueError("Rating must be between 1 and 5.")
        consultation = self.consultations[consultation_id]
        client = consultation.client
        feedback = Feedback(feedback_id, client, consultation, rating, comments)
        self.feedbacks[feedback_id] = feedback
        print(f"Feedback added for consultation {consultation_id}.")

    def get_client_feedback(self, client_id):
        """
        Retrieves all feedback provided by a specific client.
        """
        if client_id not in self.clients:
            raise ValueError(f"Client with ID {client_id} not found.")
        client_feedbacks = [
            feedback for feedback in self.feedbacks.values()
            if feedback.client.client_id == client_id
        ]
        return client_feedbacks

    def print_summary(self):
        """
        Prints a summary of all consultations and feedback.
        """
        print("\n------ Summary ------")
        print("\nConsultations:")
        for consultation in self.consultations.values():
            print(consultation)

        print("\nFeedbacks:")
        for feedback in self.feedbacks.values():
            print(feedback)


# Example usage
if __name__ == "__main__":
    system = ConsultancyServiceManagementSystem()

    # Adding clients
    system.add_client(1, "Alice Johnson", "alice@example.com")
    system.add_client(2, "Bob Smith", "bob@example.com")

    # Scheduling consultations
    system.schedule_consultation(101, 1, datetime.date(2023, 10, 15), "Discuss project scope.")
    system.schedule_consultation(102, 2, datetime.date(2023, 10, 16), "Budget planning session.")

    # Adding feedback
    system.add_feedback(201, 101, 5, "Very helpful discussion!")
    system.add_feedback(202, 102, 4, "Good insights on budgeting.")

    # Printing summary
    system.print_summary()
```
