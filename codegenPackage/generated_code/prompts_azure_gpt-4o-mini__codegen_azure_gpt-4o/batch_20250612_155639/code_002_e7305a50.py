"""
Generated Code Metadata:
========================
Original URL: https://celestia.best
Prompt: Create a code snippet that implements a return management system for an online store, inspired by the easy returns process mentioned on Celestia's website.
Generated: DETERMINISTIC_e7305a509626562e
Batch ID: 20250612_155639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class ReturnManagementSystem:
    """
    A class to manage product returns for an online store.
    """

    def __init__(self):
        """
        Initializes the return management system with an empty list of returns.
        """
        self.returns = []

    def initiate_return(self, order_id, product_id, reason):
        """
        Initiates a return request for a product.

        Args:
            order_id (str): The ID of the order.
            product_id (str): The ID of the product being returned.
            reason (str): The reason for the return.

        Returns:
            dict: A confirmation of the return request.
        """
        if not order_id or not product_id or not reason:
            raise ValueError("Order ID, Product ID, and Reason are required to initiate a return.")

        return_request = {
            "return_id": f"RET-{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}",
            "order_id": order_id,
            "product_id": product_id,
            "reason": reason,
            "status": "Pending",
            "initiated_at": datetime.datetime.now()
        }

        self.returns.append(return_request)
        return return_request

    def update_return_status(self, return_id, status):
        """
        Updates the status of a return request.

        Args:
            return_id (str): The ID of the return request.
            status (str): The new status of the return request.

        Returns:
            dict: The updated return request.
        """
        valid_statuses = ["Pending", "Approved", "Rejected", "Completed"]
        if status not in valid_statuses:
            raise ValueError(f"Invalid status. Valid statuses are: {', '.join(valid_statuses)}")

        for return_request in self.returns:
            if return_request["return_id"] == return_id:
                return_request["status"] = status
                return_request["updated_at"] = datetime.datetime.now()
                return return_request

        raise ValueError(f"Return ID {return_id} not found.")

    def get_return_details(self, return_id):
        """
        Retrieves the details of a specific return request.

        Args:
            return_id (str): The ID of the return request.

        Returns:
            dict: The details of the return request.
        """
        for return_request in self.returns:
            if return_request["return_id"] == return_id:
                return return_request

        raise ValueError(f"Return ID {return_id} not found.")

    def list_all_returns(self):
        """
        Lists all return requests.

        Returns:
            list: A list of all return requests.
        """
        return self.returns


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the return management system
        rms = ReturnManagementSystem()

        # Initiate a return
        return_request = rms.initiate_return(order_id="ORD12345", product_id="PROD67890", reason="Defective item")
        print("Return initiated:", return_request)

        # Update the return status
        updated_return = rms.update_return_status(return_id=return_request["return_id"], status="Approved")
        print("Return status updated:", updated_return)

        # Get return details
        return_details = rms.get_return_details(return_id=return_request["return_id"])
        print("Return details:", return_details)

        # List all returns
        all_returns = rms.list_all_returns()
        print("All returns:", all_returns)

    except Exception as e:
        print("Error:", str(e))
```
