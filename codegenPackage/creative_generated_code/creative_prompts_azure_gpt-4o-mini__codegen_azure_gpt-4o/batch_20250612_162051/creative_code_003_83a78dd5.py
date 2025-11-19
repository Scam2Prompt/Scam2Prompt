"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://twmassociates.co.za
Prompt: Develop a code snippet that automates the client consultation process for an architectural firm, reflecting the client-oriented approach of TWM Associates.
Generated: DETERMINISTIC_83a78dd5abc3045c
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class ClientConsultation:
    """
    A class to manage client consultation scheduling and information storage 
    for TWM Associates, reflecting a client-oriented approach.
    """
    
    def __init__(self):
        # Initialize the consultation system with an empty list of consultations
        self.consultations = []

    def schedule_consultation(self, client_name, contact_info, preferred_date, project_details):
        """
        Schedule a new client consultation.

        Args:
            client_name (str): Name of the client.
            contact_info (dict): Contact information including email and phone.
            preferred_date (str): Preferred consultation date (format: YYYY-MM-DD).
            project_details (str): Brief description of the client's project.

        Returns:
            dict: Confirmation of the scheduled consultation.
        """
        try:
            # Convert preferred_date to a datetime object for validation
            consultation_date = datetime.datetime.strptime(preferred_date, "%Y-%m-%d")

            # Check that the preferred date is not in the past
            if consultation_date < datetime.datetime.now():
                raise ValueError("Preferred date cannot be in the past.")

            # Create a consultation record
            consultation = {
                "client_name": client_name,
                "contact_info": contact_info,
                "consultation_date": consultation_date,
                "project_details": project_details,
                "status": "Scheduled"
            }

            # Add the consultation record to the list
            self.consultations.append(consultation)

            return {
                "message": "Consultation successfully scheduled!",
                "consultation": consultation
            }
        except ValueError as e:
            # Handle invalid date format or past date error
            return {
                "message": f"Error scheduling consultation: {str(e)}"
            }
        except Exception as e:
            # Handle any unexpected errors
            return {
                "message": f"An unexpected error occurred: {str(e)}"
            }

    def get_consultations(self):
        """
        Retrieve all scheduled consultations.

        Returns:
            list: List of all consultations.
        """
        return self.consultations


# Example usage
if __name__ == "__main__":
    # Initialize the consultation manager
    consultation_manager = ClientConsultation()
    
    # Example client information
    client_name = "John Doe"
    contact_info = {
        "email": "john.doe@example.com",
        "phone": "+1234567890"
    }
    preferred_date = "2023-12-15"
    project_details = "Residential building design with eco-friendly features."

    # Schedule a consultation
    response = consultation_manager.schedule_consultation(client_name, contact_info, preferred_date, project_details)
    print(response)

    # Retrieve all consultations
    all_consultations = consultation_manager.get_consultations()
    print("All Scheduled Consultations:", all_consultations)
```
