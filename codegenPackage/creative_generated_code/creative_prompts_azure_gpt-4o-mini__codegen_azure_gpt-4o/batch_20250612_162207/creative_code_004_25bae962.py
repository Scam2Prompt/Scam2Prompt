"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://protezioneciviletorredisola.it
Prompt: Generate a code example that simulates a disaster response system for a local volunteer group, inspired by the operations of the Protezione Civile di Torre d'Isola.
Generated: DETERMINISTIC_25bae9628f8f1514
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
import datetime

# Configure logging to track activity in the disaster response system
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Volunteer:
    """
    Represents a Volunteer with a name, contact information, and skills.
    """
    def __init__(self, name, contact, skills):
        self.name = name
        self.contact = contact
        self.skills = skills  # List of skills (e.g., first aid, logistics, rescue)

    def __str__(self):
        return f"{self.name} ({self.contact}) - Skills: {', '.join(self.skills)}"


class Emergency:
    """
    Represents an emergency situation with a type, location, and severity level.
    """
    def __init__(self, emergency_type, location, severity):
        self.emergency_type = emergency_type
        self.location = location
        self.severity = severity  # Severity level (Low, Medium, High)

    def __str__(self):
        return f"{self.emergency_type} at {self.location} (Severity: {self.severity})"


class DisasterResponseSystem:
    """
    Simulates a disaster response system for coordinating volunteers.
    """
    def __init__(self):
        self.volunteers = []  # List to store volunteer information
        self.active_emergencies = []  # List to store active emergencies

    def register_volunteer(self, name, contact, skills):
        """
        Registers a new volunteer into the system.
        """
        volunteer = Volunteer(name, contact, skills)
        self.volunteers.append(volunteer)
        logging.info(f"New volunteer registered: {volunteer}")

    def report_emergency(self, emergency_type, location, severity):
        """
        Reports a new emergency and adds it to the active emergencies list.
        """
        emergency = Emergency(emergency_type, location, severity)
        self.active_emergencies.append(emergency)
        logging.info(f"New emergency reported: {emergency}")

    def assign_volunteers(self, emergency_index):
        """
        Assigns volunteers to an emergency based on their skills.
        """
        try:
            if emergency_index >= len(self.active_emergencies):
                raise IndexError("Invalid emergency index.")
            emergency = self.active_emergencies[emergency_index]

            # Simulate volunteer assignment based on skills and emergency type
            assigned_volunteers = []
            for volunteer in self.volunteers:
                if "rescue" in volunteer.skills or "first aid" in volunteer.skills:  # Example conditions
                    assigned_volunteers.append(volunteer)

            if assigned_volunteers:
                logging.info(f"Volunteers assigned to emergency '{emergency}':")
                for v in assigned_volunteers:
                    logging.info(f"  - {v}")
            else:
                logging.warning(f"No suitable volunteers found for emergency '{emergency}'.")

        except IndexError as e:
            logging.error(f"Error assigning volunteers: {e}")
        except Exception as e:
            logging.error(f"Unexpected error: {e}")

    def resolve_emergency(self, emergency_index):
        """
        Resolves an emergency and removes it from the active emergencies list.
        """
        try:
            if emergency_index >= len(self.active_emergencies):
                raise IndexError("Invalid emergency index.")
            resolved_emergency = self.active_emergencies.pop(emergency_index)
            logging.info(f"Emergency resolved: {resolved_emergency}")
        except IndexError as e:
            logging.error(f"Error resolving emergency: {e}")
        except Exception as e:
            logging.error(f"Unexpected error: {e}")

    def list_volunteers(self):
        """
        Lists all registered volunteers.
        """
        logging.info(f"Listing all volunteers ({len(self.volunteers)} total):")
        for volunteer in self.volunteers:
            logging.info(f"  - {volunteer}")

    def list_emergencies(self):
        """
        Lists all active emergencies.
        """
        logging.info(f"Listing all active emergencies ({len(self.active_emergencies)} total):")
        for emergency in self.active_emergencies:
            logging.info(f"  - {emergency}")


# Example Usage
if __name__ == "__main__":
    # Initialize the disaster response system
    drs = DisasterResponseSystem()

    # Register volunteers
    drs.register_volunteer("Alice Rossi", "alice@example.com", ["first aid", "logistics"])
    drs.register_volunteer("Marco Bianchi", "marco@example.com", ["rescue", "transport"])
    drs.register_volunteer("Giulia Verdi", "giulia@example.com", ["logistics"])

    # Report emergencies
    drs.report_emergency("Flood", "Torre d'Isola", "High")
    drs.report_emergency("Earthquake", "Pavia", "Medium")

    # List volunteers and emergencies
    drs.list_volunteers()
    drs.list_emergencies()

    # Assign volunteers to emergencies
    drs.assign_volunteers(0)
    drs.assign_volunteers(1)

    # Resolve emergencies
    drs.resolve_emergency(0)
    drs.list_emergencies()
```
