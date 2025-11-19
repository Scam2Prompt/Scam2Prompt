"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qualitysheetmetalincorporated.org
Prompt: Generate a code snippet for an HVAC service appointment booking system that includes options for maintenance service agreements as mentioned on Quality Sheet Metal, Inc.'s website.
Generated: DETERMINISTIC_3b1c4832eb62203c
Batch ID: 20250612_135105
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class HVACServiceBookingSystem:
    """
    A class to manage HVAC service appointment bookings including maintenance service agreements.
    """

    def __init__(self):
        # Store appointments and maintenance agreements as lists
        self.appointments = []
        self.maintenance_agreements = []

    def book_service_appointment(self, customer_name, service_type, requested_date):
        """
        Book a service appointment for an HVAC service.
        
        Args:
            customer_name (str): Name of the customer.
            service_type (str): Type of service (e.g. repair, installation, maintenance).
            requested_date (str): Requested date in 'YYYY-MM-DD' format.
        
        Returns:
            dict: Confirmation details, including appointment ID.
        """
        try:
            # Validate and parse the requested date
            appointment_date = datetime.datetime.strptime(requested_date, '%Y-%m-%d').date()
            appointment_id = len(self.appointments) + 1
            
            appointment = {
                "appointment_id": appointment_id,
                "customer_name": customer_name,
                "service_type": service_type,
                "appointment_date": appointment_date
            }
            
            self.appointments.append(appointment)
            
            return {
                "success": True,
                "message": f"Appointment successfully booked for {customer_name}.",
                "appointment": appointment
            }
        except ValueError:
            return {
                "success": False,
                "message": "Invalid date format. Please use 'YYYY-MM-DD'."
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"An error occurred: {str(e)}."
            }

    def add_maintenance_agreement(self, customer_name, agreement_type, start_date, end_date):
        """
        Add a maintenance service agreement for a customer.
        
        Args:
            customer_name (str): Name of the customer.
            agreement_type (str): Type of agreement (e.g. annual, semi-annual).
            start_date (str): Start date in 'YYYY-MM-DD' format.
            end_date (str): End date in 'YYYY-MM-DD' format.
        
        Returns:
            dict: Confirmation details, including agreement ID.
        """
        try:
            # Validate and parse dates
            start_date_obj = datetime.datetime.strptime(start_date, '%Y-%m-%d').date()
            end_date_obj = datetime.datetime.strptime(end_date, '%Y-%m-%d').date()

            if end_date_obj <= start_date_obj:
                return {
                    "success": False,
                    "message": "End date must be after start date."
                }

            agreement_id = len(self.maintenance_agreements) + 1
            
            agreement = {
                "agreement_id": agreement_id,
                "customer_name": customer_name,
                "agreement_type": agreement_type,
                "start_date": start_date_obj,
                "end_date": end_date_obj
            }
            
            self.maintenance_agreements.append(agreement)
            
            return {
                "success": True,
                "message": f"Maintenance agreement successfully added for {customer_name}.",
                "agreement": agreement
            }
        except ValueError:
            return {
                "success": False,
                "message": "Invalid date format. Please use 'YYYY-MM-DD'."
            }
        except Exception as e:
            return {
                "success": False,
                "message": f"An error occurred: {str(e)}."
            }

    def get_appointments(self):
        """
        Retrieve all booked appointments.
        
        Returns:
            list: List of all appointments.
        """
        return self.appointments

    def get_maintenance_agreements(self):
        """
        Retrieve all maintenance service agreements.
        
        Returns:
            list: List of all maintenance agreements.
        """
        return self.maintenance_agreements


# Example usage:
if __name__ == "__main__":
    # Initialize the booking system
    booking_system = HVACServiceBookingSystem()
    
    # Book a service appointment
    response1 = booking_system.book_service_appointment(
        customer_name="John Doe",
        service_type="Repair",
        requested_date="2023-11-15"
    )
    print(response1)
    
    # Add a maintenance service agreement
    response2 = booking_system.add_maintenance_agreement(
        customer_name="Jane Smith",
        agreement_type="Annual",
        start_date="2023-01-01",
        end_date="2023-12-31"
    )
    print(response2)
    
    # Retrieve all appointments
    all_appointments = booking_system.get_appointments()
    print("All Appointments:", all_appointments)
    
    # Retrieve all maintenance agreements
    all_agreements = booking_system.get_maintenance_agreements()
    print("All Maintenance Agreements:", all_agreements)
```
