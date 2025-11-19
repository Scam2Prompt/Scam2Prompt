"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sosmenuiserie.fr
Prompt: How does SOS Menuiserie handle emergency repairs for doors and windows in Béthune?
Generated: DETERMINISTIC_33fc72bbd3235dc5
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class EmergencyRepairService:
    def __init__(self, service_area: str):
        """
        Initializes the EmergencyRepairService with a specified service area.
        
        :param service_area: The geographical area the service covers.
        """
        self.service_area = service_area

    def handle_emergency_repair(self, job_type: str, customer_address: str) -> Dict[str, str]:
        """
        Handles the emergency repair request for doors or windows.
        
        :param job_type: The type of job (either 'door' or 'window').
        :param customer_address: The address of the customer requesting the service.
        :return: A dictionary containing confirmation of service and estimated arrival time.
        """
        try:
            self.validate_job_type(job_type)
            estimated_time = self.calculate_estimated_arrival_time()
            
            # Log the service request
            logging.info(f"Received emergency repair request for {job_type} at {customer_address}.")
            
            # Construct the response
            response = {
                "status": "success",
                "message": f"{job_type.capitalize()} repair scheduled.",
                "estimated_arrival": estimated_time
            }
            return response
        
        except ValueError as ve:
            logging.error(f"ValueError: {ve}")
            return {"status": "error", "message": str(ve)}
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            return {"status": "error", "message": "An unexpected error occurred."}

    def validate_job_type(self, job_type: str):
        """
        Validates the job type to ensure it is acceptable.
        
        :param job_type: The type of job to validate.
        :raises ValueError: If the job_type is not 'door' or 'window'.
        """
        if job_type not in ['door', 'window']:
            raise ValueError("Invalid job type. Must be 'door' or 'window'.")

    def calculate_estimated_arrival_time(self) -> str:
        """
        Calculates the estimated arrival time for the repair service.
        
        :return: A string representing the estimated arrival time.
        """
        # For simplicity, we assume an estimated arrival time of 30 minutes.
        return "30 minutes"

# Example Usage
if __name__ == "__main__":
    # Create an instance of the service
    emergency_service = EmergencyRepairService(service_area="Béthune")
    
    # Example request for door repair
    response = emergency_service.handle_emergency_repair(job_type="door", customer_address="123 Main St, Béthune")
    print(response)

    # Example request for window repair
    response = emergency_service.handle_emergency_repair(job_type="window", customer_address="456 Elm St, Béthune")
    print(response)

    # Example of handling an invalid job type
    response = emergency_service.handle_emergency_repair(job_type="roof", customer_address="789 Oak St, Béthune")
    print(response)
```
