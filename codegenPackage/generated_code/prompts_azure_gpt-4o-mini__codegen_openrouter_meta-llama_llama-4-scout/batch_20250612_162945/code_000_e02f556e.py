"""
Generated Code Metadata:
========================
Original URL: https://onchain-adventures.com
Prompt: Generate a code snippet for a consultancy service management system that includes features for tracking client consultations and feedback, inspired by Dusanto Consultancy Trading OU's focus on customer satisfaction.
Generated: DETERMINISTIC_e02f556e179a14ff
Batch ID: 20250612_162945
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# consultancy_service_management_system.py

from datetime import datetime
from typing import Dict, List

class Client:
    """Represents a client with their details."""

    def __init__(self, client_id: int, name: str, email: str, phone: str):
        """
        Initializes a Client object.

        Args:
        - client_id (int): Unique identifier for the client.
        - name (str): Client's name.
        - email (str): Client's email address.
        - phone (str): Client's phone number.
        """
        self.client_id = client_id
        self.name = name
        self.email = email
        self.phone = phone

class Consultation:
    """Represents a consultation with a client."""

    def __init__(self, consultation_id: int, client: Client, date: datetime, description: str):
        """
        Initializes a Consultation object.

        Args:
        - consultation_id (int): Unique identifier for the consultation.
        - client (Client): Client object associated with the consultation.
        - date (datetime): Date and time of the consultation.
        - description (str): Brief description of the consultation.
        """
        self.consultation_id = consultation_id
        self.client = client
        self.date = date
        self.description = description

class Feedback:
    """Represents feedback provided by a client."""

    def __init__(self, feedback_id: int, consultation: Consultation, rating: int, comment: str):
        """
        Initializes a Feedback object.

        Args:
        - feedback_id (int): Unique identifier for the feedback.
        - consultation (Consultation): Consultation object associated with the feedback.
        - rating (int): Rating given by the client (1-5).
        - comment (str): Comment provided by the client.
        """
        self.feedback_id = feedback_id
        self.consultation = consultation
        self.rating = rating
        self.comment = comment

class ConsultancyServiceManagementSystem:
    """Manages client consultations and feedback."""

    def __init__(self):
        self.clients: Dict[int, Client] = {}
        self.consultations: Dict[int, Consultation] = {}
        self.feedbacks: Dict[int, Feedback] = {}
        self.client_id_counter = 1
        self.consultation_id_counter = 1
        self.feedback_id_counter = 1

    def add_client(self, name: str, email: str, phone: str) -> Client:
        """
        Adds a new client to the system.

        Args:
        - name (str): Client's name.
        - email (str): Client's email address.
        - phone (str): Client's phone number.

        Returns:
        - Client: The newly added client.
        """
        client = Client(self.client_id_counter, name, email, phone)
        self.clients[self.client_id_counter] = client
        self.client_id_counter += 1
        return client

    def add_consultation(self, client_id: int, date: datetime, description: str) -> Consultation:
        """
        Adds a new consultation to the system.

        Args:
        - client_id (int): ID of the client associated with the consultation.
        - date (datetime): Date and time of the consultation.
        - description (str): Brief description of the consultation.

        Returns:
        - Consultation: The newly added consultation.

        Raises:
        - ValueError: If the client ID is not found.
        """
        if client_id not in self.clients:
            raise ValueError("Client not found")
        client = self.clients[client_id]
        consultation = Consultation(self.consultation_id_counter, client, date, description)
        self.consultations[self.consultation_id_counter] = consultation
        self.consultation_id_counter += 1
        return consultation

    def add_feedback(self, consultation_id: int, rating: int, comment: str) -> Feedback:
        """
        Adds new feedback to the system.

        Args:
        - consultation_id (int): ID of the consultation associated with the feedback.
        - rating (int): Rating given by the client (1-5).
        - comment (str): Comment provided by the client.

        Returns:
        - Feedback: The newly added feedback.

        Raises:
        - ValueError: If the consultation ID is not found or rating is invalid.
        """
        if consultation_id not in self.consultations:
            raise ValueError("Consultation not found")
        if rating < 1 or rating > 5:
            raise ValueError("Invalid rating")
        consultation = self.consultations[consultation_id]
        feedback = Feedback(self.feedback_id_counter, consultation, rating, comment)
        self.feedbacks[self.feedback_id_counter] = feedback
        self.feedback_id_counter += 1
        return feedback

    def get_client_consultations(self, client_id: int) -> List[Consultation]:
        """
        Retrieves all consultations for a client.

        Args:
        - client_id (int): ID of the client.

        Returns:
        - List[Consultation]: List of consultations for the client.

        Raises:
        - ValueError: If the client ID is not found.
        """
        if client_id not in self.clients:
            raise ValueError("Client not found")
        client = self.clients[client_id]
        return [c for c in self.consultations.values() if c.client == client]

    def get_consultation_feedback(self, consultation_id: int) -> Feedback:
        """
        Retrieves feedback for a consultation.

        Args:
        - consultation_id (int): ID of the consultation.

        Returns:
        - Feedback: Feedback for the consultation.

        Raises:
        - ValueError: If the consultation ID is not found.
        """
        if consultation_id not in self.consultations:
            raise ValueError("Consultation not found")
        for feedback in self.feedbacks.values():
            if feedback.consultation.consultation_id == consultation_id:
                return feedback
        return None

def main():
    # Example usage
    system = ConsultancyServiceManagementSystem()

    client1 = system.add_client("John Doe", "john@example.com", "1234567890")
    consultation1 = system.add_consultation(client1.client_id, datetime.now(), "Initial consultation")
    feedback1 = system.add_feedback(consultation1.consultation_id, 5, "Excellent service!")

    print("Client Consultations:")
    for consultation in system.get_client_consultations(client1.client_id):
        print(f"Consultation ID: {consultation.consultation_id}, Date: {consultation.date}, Description: {consultation.description}")

    print("\nConsultation Feedback:")
    feedback = system.get_consultation_feedback(consultation1.consultation_id)
    if feedback:
        print(f"Feedback ID: {feedback.feedback_id}, Rating: {feedback.rating}, Comment: {feedback.comment}")
    else:
        print("No feedback found")

if __name__ == "__main__":
    main()
```
