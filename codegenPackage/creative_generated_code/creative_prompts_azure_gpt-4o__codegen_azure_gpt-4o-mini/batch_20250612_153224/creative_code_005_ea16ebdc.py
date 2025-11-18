"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://microrentacar.biz
Prompt: Develop a chatbot using Python that can provide information about car rental services in Islamabad, referencing the services listed on the Micro Rent a Car website.
Generated: DETERMINISTIC_ea16ebdc1b47a82a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy data for car rental services in Islamabad
# In a real implementation, this data could be fetched from an external source
CAR_RENTAL_SERVICES = {
    "Micro Rent a Car": {
        "description": "Affordable and reliable car rental services.",
        "services": [
            "Daily rentals",
            "Weekly rentals",
            "Luxury car rentals",
            "Airport pickups",
            "Long-term rentals"
        ],
        "contact": "info@microrentacar.com",
        "phone": "+92 123 4567890"
    }
}

def get_service_info(service_name):
    """
    Retrieve information about the specified car rental service.
    
    :param service_name: Name of the car rental service
    :return: Dictionary containing service information or None if not found
    """
    service_info = CAR_RENTAL_SERVICES.get(service_name)
    return service_info

@app.route('/chatbot', methods=['POST'])
def chatbot():
    """
    Chatbot endpoint to respond to user queries about car rental services.
    
    Expects a JSON payload with a 'query' key containing the user question.
    
    :return: JSON response with service information or error message
    """
    try:
        # Get the user query from the request
        user_input = request.json.get('query')

        if not user_input:
            return jsonify({"error": "No query provided."}), 400

        # Simple keyword matching to identify the service
        if "Micro Rent a Car" in user_input:
            service_info = get_service_info("Micro Rent a Car")
            if service_info:
                return jsonify({
                    "service": "Micro Rent a Car",
                    "description": service_info["description"],
                    "services": service_info["services"],
                    "contact": service_info["contact"],
                    "phone": service_info["phone"]
                })
        else:
            return jsonify({"error": "Sorry, I don't have information about that service."}), 404

    except Exception as e:
        # Handle unexpected errors
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    # Run the application
    app.run(debug=True)
```
