"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cedarinternational.ca
Prompt: Write Python code to automate the procurement process for oil and gas industry materials, incorporating Cedar International Inc.'s supply chain solutions and logistics optimization strategies.
Generated: DETERMINISTIC_721c91ae1b412a20
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
from datetime import datetime
from typing import List, Dict

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("procurement.log"), logging.StreamHandler()]
)

# Define exceptions for error handling
class ProcurementError(Exception):
    pass

class SupplierNotAvailableError(ProcurementError):
    pass

# Mock supplier data for Cedar International Inc.
SUPPLIERS = {
    "Cedar International Inc.": {
        "materials": ["crude oil", "natural gas", "pipeline equipment", "drilling rigs"],
        "lead_time_days": 7,
        "capacity": 1000
    }
}

# Define material procurement request structure
class ProcurementRequest:
    def __init__(self, material: str, quantity: int):
        self.material = material
        self.quantity = quantity
        self.request_date = datetime.now()
        self.status = "Pending"

    def __repr__(self):
        return f"ProcurementRequest(material={self.material}, quantity={self.quantity}, status={self.status})"

# Procurement system class
class ProcurementSystem:
    def __init__(self):
        self.requests = []

    def submit_request(self, material: str, quantity: int) -> str:
        """
        Submit a procurement request and validate against supplier data.
        """
        logging.info(f"Submitting request for {quantity} units of {material}.")
        if material not in SUPPLIERS["Cedar International Inc."]["materials"]:
            raise SupplierNotAvailableError(f"Material '{material}' is not available with Cedar International Inc.")

        if quantity > SUPPLIERS["Cedar International Inc."]["capacity"]:
            raise ProcurementError(f"Requested quantity ({quantity}) exceeds supplier capacity.")

        request = ProcurementRequest(material, quantity)
        self.requests.append(request)
        logging.info(f"Request submitted successfully: {request}")
        return f"Request submitted successfully: {request}"

    def process_requests(self) -> List[Dict]:
        """
        Process all pending procurement requests.
        """
        processed_requests = []
        for request in self.requests:
            if request.status == "Pending":
                request.status = "Approved"
                delivery_date = datetime.now() + timedelta(days=SUPPLIERS["Cedar International Inc."]["lead_time_days"])
                processed_requests.append({
                    "material": request.material,
                    "quantity": request.quantity,
                    "delivery_date": delivery_date.strftime("%Y-%m-%d"),
                })
                logging.info(f"Request approved: {request}")
        return processed_requests

    def get_all_requests(self) -> List[ProcurementRequest]:
        """
        Return all procurement requests for monitoring.
        """
        return self.requests

# Main automation logic
def main():
    try:
        # Initialize procurement system
        system = ProcurementSystem()

        # Submit procurement requests
        system.submit_request("crude oil", 500)
        system.submit_request("natural gas", 300)

        # Process requests
        processed_requests = system.process_requests()
        logging.info("Processed requests:")
        for request in processed_requests:
            logging.info(request)

        # Print all requests for monitoring
        all_requests = system.get_all_requests()
        logging.info("All requests:")
        for r in all_requests:
            logging.info(r)

    except ProcurementError as e:
        logging.error(f"Procurement error occurred: {e}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
