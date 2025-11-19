"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://itamarationlinebraz.blogspot.com
Prompt: Describe how to set up a delivery tracking system for an online tire shop using Mercado Envios, referencing the features of Itamarati Online.
Generated: DETERMINISTIC_6c413a25e03b9d05
Batch ID: 20250612_163406
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mercadolibre.com/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import requests
import json

class DeliveryTrackingSystem:
    """
    A class to manage the delivery tracking system for an online tire shop using Mercado Envios.
    """
    
    BASE_URL = "https://api.mercadolibre.com/"

    def __init__(self, access_token):
        """
        Initializes the DeliveryTrackingSystem with an access token.
        
        :param access_token: str - The access token for authenticating with the Mercado Libre API.
        """
        self.access_token = access_token

    def get_tracking_info(self, tracking_number):
        """
        Retrieves the tracking information for a given tracking number.
        
        :param tracking_number: str - The tracking number of the shipment.
        :return: dict - The tracking information or an error message.
        """
        try:
            # Construct the tracking URL
            url = f"{self.BASE_URL}tracking/{tracking_number}?access_token={self.access_token}"
            response = requests.get(url)
            
            # Check for HTTP errors
            response.raise_for_status()
            
            # Parse the JSON response
            tracking_info = response.json()
            return {
                "status": "success",
                "data": tracking_info
            }
        except requests.exceptions.HTTPError as http_err:
            return {
                "status": "error",
                "message": f"HTTP error occurred: {http_err}"
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"An error occurred: {e}"
            }

    def create_shipment(self, order_id, address, weight):
        """
        Creates a new shipment based on the order details.
        
        :param order_id: str - The ID of the order.
        :param address: dict - The shipping address.
        :param weight: float - The weight of the shipment in kilograms.
        :return: dict - The response from the Mercado Envios API.
        """
        try:
            # Define the shipment details
            shipment_data = {
                "order_id": order_id,
                "address": address,
                "weight": weight
            }

            # API endpoint for creating a shipment
            url = f"{self.BASE_URL}shipments?access_token={self.access_token}"
            headers = {"Content-Type": "application/json"}
            response = requests.post(url, headers=headers, data=json.dumps(shipment_data))

            # Check for HTTP errors
            response.raise_for_status()
            return {
                "status": "success",
                "data": response.json()
            }
        except requests.exceptions.HTTPError as http_err:
            return {
                "status": "error",
                "message": f"HTTP error occurred: {http_err}"
            }
        except Exception as e:
            return {
                "status": "error",
                "message": f"An error occurred: {e}"
            }

# Example usage
if __name__ == "__main__":
    # Replace with your actual Mercado Libre access token
    ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
    
    delivery_system = DeliveryTrackingSystem(ACCESS_TOKEN)

    # Track a shipment
    tracking_number = "YOUR_TRACKING_NUMBER"
    tracking_info = delivery_system.get_tracking_info(tracking_number)
    print(tracking_info)

    # Create a shipment
    order_id = "ORDER_ID"
    address = {
        "street_name": "Main St",
        "street_number": "123",
        "zip_code": "12345",
        "city": "City",
        "state": "State",
        "country": "Country"
    }
    weight = 5.0  # Weight in kilograms
    shipment_response = delivery_system.create_shipment(order_id, address, weight)
    print(shipment_response)
```
