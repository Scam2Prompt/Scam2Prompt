"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.tiktokshopvn.com.vn
Prompt: Write a code example for a return and exchange policy management system that aligns with the easy return process highlighted on TikTok Shop Vietnam.
Generated: DETERMINISTIC_185af33b04b82de8
Batch ID: 20250612_164238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict, Optional

class Product:
    """
    Represents a product in the system.
    """
    def __init__(self, product_id: str, name: str, price: float):
        self.product_id = product_id
        self.name = name
        self.price = price

class ReturnRequest:
    """
    Represents a return request made by the customer.
    """
    def __init__(self, request_id: str, product: Product, reason: str, request_date: datetime.date):
        self.request_id = request_id
        self.product = product
        self.reason = reason
        self.request_date = request_date
        self.status = "Pending"  # Possible statuses: Pending, Approved, Rejected, Completed

class ExchangeRequest:
    """
    Represents an exchange request made by the customer.
    """
    def __init__(self, request_id: str, old_product: Product, new_product: Product, reason: str, request_date: datetime.date):
        self.request_id = request_id
        self.old_product = old_product
        self.new_product = new_product
        self.reason = reason
        self.request_date = request_date
        self.status = "Pending"  # Possible statuses: Pending, Approved, Rejected, Completed

class PolicyManager:
    """
    Manages return and exchange policies.
    """
    def __init__(self):
        self.return_requests: List[ReturnRequest] = []
        self.exchange_requests: List[ExchangeRequest] = []
        self.return_window_days = 7  # Configurable return window (in days)
    
    def _validate_return_window(self, request_date: datetime.date) -> bool:
        """
        Validates if the return or exchange request is within the allowed window.
        """
        current_date = datetime.date.today()
        days_elapsed = (current_date - request_date).days
        return days_elapsed <= self.return_window_days

    def create_return_request(self, product: Product, reason: str) -> Optional[ReturnRequest]:
        """
        Creates a new return request if it meets the policy conditions.
        """
        request_date = datetime.date.today()
        if not self._validate_return_window(request_date):
            print(f"Error: Return request for product '{product.name}' exceeds the allowable window of {self.return_window_days} days.")
            return None
        request_id = f"RR{len(self.return_requests) + 1}"
        return_request = ReturnRequest(request_id, product, reason, request_date)
        self.return_requests.append(return_request)
        print(f"Return request '{request_id}' created successfully.")
        return return_request

    def create_exchange_request(self, old_product: Product, new_product: Product, reason: str) -> Optional[ExchangeRequest]:
        """
        Creates a new exchange request if it meets the policy conditions.
        """
        request_date = datetime.date.today()
        if not self._validate_return_window(request_date):
            print(f"Error: Exchange request for product '{old_product.name}' exceeds the allowable window of {self.return_window_days} days.")
            return None
        request_id = f"ER{len(self.exchange_requests) + 1}"
        exchange_request = ExchangeRequest(request_id, old_product, new_product, reason, request_date)
        self.exchange_requests.append(exchange_request)
        print(f"Exchange request '{request_id}' created successfully.")
        return exchange_request

    def process_return_request(self, request_id: str, approve: bool) -> None:
        """
        Processes a return request (approve or reject).
        """
        request = next((r for r in self.return_requests if r.request_id == request_id), None)
        if not request:
            print(f"Error: Return request '{request_id}' not found.")
            return
        request.status = "Approved" if approve else "Rejected"
        print(f"Return request '{request_id}' has been {'approved' if approve else 'rejected'}.")

    def process_exchange_request(self, request_id: str, approve: bool) -> None:
        """
        Processes an exchange request (approve or reject).
        """
        request = next((r for r in self.exchange_requests if r.request_id == request_id), None)
        if not request:
            print(f"Error: Exchange request '{request_id}' not found.")
            return
        request.status = "Approved" if approve else "Rejected"
        print(f"Exchange request '{request_id}' has been {'approved' if approve else 'rejected'}.")

    def list_requests(self) -> Dict[str, List[Dict[str, str]]]:
        """
        Lists all return and exchange requests in the system.
        """
        return {
            "return_requests": [
                {"request_id": r.request_id, "product_name": r.product.name, "status": r.status}
                for r in self.return_requests
            ],
            "exchange_requests": [
                {"request_id": e.request_id, "old_product_name": e.old_product.name, "new_product_name": e.new_product.name, "status": e.status}
                for e in self.exchange_requests
            ]
        }

# Example usage
if __name__ == "__main__":
    # Create a policy manager
    policy_manager = PolicyManager()
    
    # Add some products
    product_1 = Product("P001", "Smartphone", 300.00)
    product_2 = Product("P002", "Headphones", 50.00)

    # Create return and exchange requests
    return_request = policy_manager.create_return_request(product_1, "Defective item")
    exchange_request = policy_manager.create_exchange_request(product_1, product_2, "Want different item")

    # Process requests
    if return_request:
        policy_manager.process_return_request(return_request.request_id, approve=True)
    if exchange_request:
        policy_manager.process_exchange_request(exchange_request.request_id, approve=False)

    # List all requests
    print("All Requests:")
    print(policy_manager.list_requests())
```
