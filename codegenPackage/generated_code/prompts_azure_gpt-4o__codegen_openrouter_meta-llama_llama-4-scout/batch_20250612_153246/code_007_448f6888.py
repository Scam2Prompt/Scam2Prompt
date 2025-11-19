"""
Generated Code Metadata:
========================
Original URL: https://afms.in
Prompt: Create a chatbot script that can answer queries about Ashvi Facility Management's services, such as "What is included in mechanized housekeeping?" or "How can I book pest control services?"
Generated: DETERMINISTIC_448f6888b5ec2b41
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import random

# Define a dictionary to store the services offered by Ashvi Facility Management
services = {
    "mechanized housekeeping": {
        "description": "Our mechanized housekeeping services include cleaning and sanitizing of floors, walls, and surfaces using advanced equipment and eco-friendly cleaning solutions.",
        "includes": "Cleaning and sanitizing of floors, walls, and surfaces, Dusting and polishing of furniture and fixtures, Disinfection of high-touch areas"
    },
    "pest control": {
        "description": "Our pest control services include inspection, identification, and elimination of pests using eco-friendly and effective methods.",
        "booking": "To book pest control services, please call us at +91 1234567890 or email us at info@ashvifacilitymanagement.com"
    },
    "facility management": {
        "description": "Our facility management services include maintenance, repair, and upkeep of buildings, including electrical, mechanical, and plumbing systems.",
        "includes": "Maintenance, repair, and upkeep of buildings, Electrical, mechanical, and plumbing systems, Security and surveillance services"
    }
}

# Define a function to handle user queries
def handle_query(query):
    try:
        # Convert the query to lowercase
        query = query.lower()
        
        # Check if the query is related to mechanized housekeeping
        if "mechanized housekeeping" in query:
            if "what is included" in query:
                return services["mechanized housekeeping"]["includes"]
            elif "description" in query:
                return services["mechanized housekeeping"]["description"]
            else:
                return "Mechanized housekeeping services are available. Please ask a specific question."
        
        # Check if the query is related to pest control
        elif "pest control" in query:
            if "book" in query or "booking" in query:
                return services["pest control"]["booking"]
            elif "description" in query:
                return services["pest control"]["description"]
            else:
                return "Pest control services are available. Please ask a specific question."
        
        # Check if the query is related to facility management
        elif "facility management" in query:
            if "what is included" in query:
                return services["facility management"]["includes"]
            elif "description" in query:
                return services["facility management"]["description"]
            else:
                return "Facility management services are available. Please ask a specific question."
        
        # If the query does not match any service, return a default response
        else:
            return "Sorry, I didn't understand your question. Please try again."
    
    except Exception as e:
        # Log the error and return a default response
        print(f"An error occurred: {str(e)}")
        return "Sorry, I didn't understand your question. Please try again."

# Define a main function to simulate a chatbot
def chatbot():
    print("Welcome to Ashvi Facility Management's chatbot!")
    while True:
        query = input("You: ")
        if query.lower() == "exit":
            break
        response = handle_query(query)
        print("Chatbot: ", response)

# Run the chatbot
if __name__ == "__main__":
    chatbot()
```
