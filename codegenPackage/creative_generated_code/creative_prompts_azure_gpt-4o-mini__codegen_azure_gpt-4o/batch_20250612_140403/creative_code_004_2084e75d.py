"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clientfuel.digital
Prompt: How can I design a self-booking appointment system that filters out unqualified leads, based on the techniques shared by Client Fuel?
Generated: DETERMINISTIC_2084e75d8269e3de
Batch ID: 20250612_140403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class AppointmentBookingSystem:
    """
    A self-booking appointment system that filters out unqualified leads 
    based on predefined criteria such as budget, goals, and readiness.
    """

    def __init__(self):
        self.appointments = []
        self.lead_qualification_criteria = {
            "budget": lambda b: b >= 500,  # Minimum budget requirement
            "goal": lambda g: g in ["Increase revenue", "Scale business", "Brand growth"],  # Supported goals
            "readiness": lambda r: r in ["Ready now", "Within 30 days"]  # Readiness to proceed
        }

    def qualify_lead(self, lead_data):
        """
        Filters out unqualified leads by checking against predefined criteria.
        
        Args:
            lead_data (dict): A dictionary containing lead information.
                Example: {"budget": 1000, "goal": "Scale business", "readiness": "Ready now"}
        
        Returns:
            bool: True if the lead is qualified, False otherwise.
        """
        try:
            return all(
                criteria(lead_data[key])
                for key, criteria in self.lead_qualification_criteria.items()
                if key in lead_data
            )
        except KeyError as e:
            print(f"Missing key in lead data: {e}")
            return False

    def book_appointment(self, lead_data, preferred_datetime):
        """
        Books an appointment for qualified leads.

        Args:
            lead_data (dict): Contains information about the lead.
            preferred_datetime (str): Desired datetime for the appointment in the format 'YYYY-MM-DD HH:MM'.

        Returns:
            str: Confirmation message or rejection reason.
        """
        try:
            # Validate the datetime format
            appointment_datetime = datetime.datetime.strptime(preferred_datetime, '%Y-%m-%d %H:%M')

            # Check if the lead is qualified
            if not self.qualify_lead(lead_data):
                return "Lead did not meet qualification criteria. Appointment not booked."

            # Check for conflicts
            for existing_appointment in self.appointments:
                if existing_appointment['datetime'] == appointment_datetime:
                    return "Requested appointment slot is not available."

            # Book the appointment
            self.appointments.append({
                "lead_data": lead_data,
                "datetime": appointment_datetime
            })
            return f"Appointment successfully booked for {appointment_datetime}."

        except ValueError:
            return "Invalid datetime format. Please use 'YYYY-MM-DD HH:MM'."
        except Exception as e:
            return f"An error occurred while booking the appointment: {e}"

    def view_appointments(self):
        """
        Displays all booked appointments.

        Returns:
            list: A list of all appointments.
        """
        return [
            {"lead_data": appointment["lead_data"], "datetime": appointment["datetime"].strftime('%Y-%m-%d %H:%M')}
            for appointment in self.appointments
        ]


# Example Usage:
if __name__ == "__main__":
    system = AppointmentBookingSystem()

    lead1 = {"budget": 1000, "goal": "Scale business", "readiness": "Ready now"}
    lead2 = {"budget": 300, "goal": "Increase revenue", "readiness": "Later"}

    print(system.book_appointment(lead1, "2023-11-15 14:00"))  # Should succeed
    print(system.book_appointment(lead2, "2023-11-15 15:00"))  # Should fail

    print("Currently booked appointments:")
    print(system.view_appointments())
```
