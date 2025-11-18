"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arpgroupcorp.com
Prompt: Generate a training module for IT employees, including group training sessions and one-on-one coaching, based on ARP Group Corporation's IT Training and Support services.
Generated: DETERMINISTIC_a56d5456bec6d4ac
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class ITTrainingModule:
    """
    A class to manage IT training modules, including group sessions and one-on-one coaching.
    """

    def __init__(self, company_name):
        """
        Initialize the training module with company information.
        :param company_name: Name of the company providing training services
        """
        self.company_name = company_name
        self.group_sessions = []
        self.one_on_one_sessions = []

    def schedule_group_training(self, topic, date, time, trainer, max_participants):
        """
        Schedule a group training session.
        :param topic: Topic of the training session
        :param date: Date of the training session
        :param time: Time of the training session
        :param trainer: Name of the trainer conducting the session
        :param max_participants: Maximum number of participants allowed
        """
        try:
            session = {
                "topic": topic,
                "date": date,
                "time": time,
                "trainer": trainer,
                "max_participants": max_participants,
                "registered_participants": []
            }
            self.group_sessions.append(session)
            print(f"Group training on '{topic}' scheduled successfully.")
        except Exception as e:
            print(f"Error scheduling group training: {e}")

    def register_for_group_training(self, session_topic, participant_name):
        """
        Register a participant for a group training session.
        :param session_topic: Topic of the session to register for
        :param participant_name: Name of the participant
        """
        try:
            for session in self.group_sessions:
                if session["topic"] == session_topic:
                    if len(session["registered_participants"]) < session["max_participants"]:
                        session["registered_participants"].append(participant_name)
                        print(f"{participant_name} successfully registered for '{session_topic}' session.")
                    else:
                        print(f"Registration failed: '{session_topic}' session is full.")
                    return
            print(f"No session found with topic '{session_topic}'.")
        except Exception as e:
            print(f"Error registering participant: {e}")

    def schedule_one_on_one_coaching(self, participant_name, topic, date, time, trainer):
        """
        Schedule a one-on-one coaching session.
        :param participant_name: Name of the participant
        :param topic: Topic of the coaching session
        :param date: Date of the session
        :param time: Time of the session
        :param trainer: Name of the trainer conducting the session
        """
        try:
            session = {
                "participant_name": participant_name,
                "topic": topic,
                "date": date,
                "time": time,
                "trainer": trainer
            }
            self.one_on_one_sessions.append(session)
            print(f"One-on-one coaching for '{participant_name}' on '{topic}' scheduled successfully.")
        except Exception as e:
            print(f"Error scheduling one-on-one coaching: {e}")

    def view_scheduled_sessions(self):
        """
        View all scheduled group and one-on-one sessions.
        """
        try:
            print("\nScheduled Group Sessions:")
            for session in self.group_sessions:
                print(f"Topic: {session['topic']}, Date: {session['date']}, Time: {session['time']}, "
                      f"Trainer: {session['trainer']}, Registered Participants: {session['registered_participants']}")

            print("\nScheduled One-on-One Sessions:")
            for session in self.one_on_one_sessions:
                print(f"Participant: {session['participant_name']}, Topic: {session['topic']}, "
                      f"Date: {session['date']}, Time: {session['time']}, Trainer: {session['trainer']}")
        except Exception as e:
            print(f"Error viewing scheduled sessions: {e}")


# Example Usage
if __name__ == "__main__":
    # Initialize the training module for ARP Group Corporation
    training_module = ITTrainingModule("ARP Group Corporation")

    # Schedule group training sessions
    training_module.schedule_group_training("Cybersecurity Basics", "2023-10-15", "10:00 AM", "Alice Johnson", 30)
    training_module.schedule_group_training("Network Troubleshooting", "2023-10-16", "2:00 PM", "Bob Smith", 20)

    # Register participants for group sessions
    training_module.register_for_group_training("Cybersecurity Basics", "John Doe")
    training_module.register_for_group_training("Cybersecurity Basics", "Jane Doe")

    # Schedule one-on-one coaching sessions
    training_module.schedule_one_on_one_coaching("John Doe", "Advanced Networking", "2023-10-17", "3:00 PM", "Alice Johnson")
    training_module.schedule_one_on_one_coaching("Jane Doe", "System Security", "2023-10-18", "4:00 PM", "Bob Smith")

    # View all scheduled sessions
    training_module.view_scheduled_sessions()
```
