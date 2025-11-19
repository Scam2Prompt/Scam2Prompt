"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sistemabox.com.br
Prompt: Write a Python script that automates the management of IT support requests based on the services offered by Sistema Box.
Generated: DETERMINISTIC_e5b7351bebe17f9b
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import datetime
import os

# Define the services offered by Sistema Box
SERVICES_OFFERED = [
    "Network Troubleshooting",
    "Software Installation",
    "Hardware Repair",
    "Data Recovery",
    "System Updates",
    "Security Checks"
]

# File to store support requests (JSON format)
SUPPORT_REQUESTS_FILE = "support_requests.json"

# Function to load support requests from file
def load_support_requests():
    """Loads support requests from a JSON file."""
    if not os.path.exists(SUPPORT_REQUESTS_FILE):
        return []
    try:
        with open(SUPPORT_REQUESTS_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Error: Unable to decode support requests file. Starting with an empty list.")
        return []

# Function to save support requests to file
def save_support_requests(requests):
    """Saves support requests to a JSON file."""
    try:
        with open(SUPPORT_REQUESTS_FILE, "w") as file:
            json.dump(requests, file, indent=4)
    except Exception as e:
        print(f"Error: Unable to save support requests. Details: {e}")

# Function to add a new support request
def add_support_request(name, email, service, description):
    """
    Adds a new IT support request.

    Parameters:
        name (str): Name of the requester.
        email (str): Email of the requester.
        service (str): Requested service.
        description (str): Description of the issue/request.

    Returns:
        bool: True if the request is successfully added, False otherwise.
    """
    if service not in SERVICES_OFFERED:
        print("Error: Invalid service requested. Please choose from the available services.")
        return False

    support_requests = load_support_requests()
    new_request = {
        "id": len(support_requests) + 1,
        "name": name,
        "email": email,
        "service": service,
        "description": description,
        "status": "Pending",
        "created_at": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    support_requests.append(new_request)
    save_support_requests(support_requests)
    print("Support request added successfully.")
    return True

# Function to update the status of a support request
def update_support_request_status(request_id, status):
    """
    Updates the status of an existing support request.

    Parameters:
        request_id (int): ID of the support request to update.
        status (str): New status for the support request.

    Returns:
        bool: True if the status is successfully updated, False otherwise.
    """
    support_requests = load_support_requests()
    for request in support_requests:
        if request["id"] == request_id:
            request["status"] = status
            save_support_requests(support_requests)
            print("Support request status updated successfully.")
            return True
    print("Error: Support request with the given ID not found.")
    return False

# Function to display all support requests
def list_support_requests():
    """Displays all IT support requests."""
    support_requests = load_support_requests()
    if not support_requests:
        print("No support requests found.")
        return

    print("Support Requests:")
    print("-" * 60)
    for request in support_requests:
        print(f"ID: {request['id']}")
        print(f"Name: {request['name']}")
        print(f"Email: {request['email']}")
        print(f"Service: {request['service']}")
        print(f"Description: {request['description']}")
        print(f"Status: {request['status']}")
        print(f"Created At: {request['created_at']}")
        print("-" * 60)

# Main function to drive the script
def main():
    """Main function to manage IT support requests."""
    while True:
        print("\nIT Support Request Management - Sistema Box")
        print("1. Add new support request")
        print("2. Update support request status")
        print("3. List all support requests")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            print("Available Services:")
            for service in SERVICES_OFFERED:
                print(f"- {service}")
            service = input("Enter the requested service: ")
            description = input("Enter a brief description of the issue/request: ")
            add_support_request(name, email, service, description)
        elif choice == "2":
            request_id = int(input("Enter the ID of the support request to update: "))
            status = input("Enter the new status (e.g., Pending, In Progress, Completed): ")
            update_support_request_status(request_id, status)
        elif choice == "3":
            list_support_requests()
        elif choice == "4":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point for the script
if __name__ == "__main__":
    main()
```
