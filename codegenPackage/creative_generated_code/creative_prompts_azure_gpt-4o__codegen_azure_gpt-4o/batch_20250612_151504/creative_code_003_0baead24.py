"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.himsdemo.bste.live
Prompt: Provide an example of how to use `Utility.Client("clientName")` to display client-specific information in a Health Information Management System.
Generated: DETERMINISTIC_0baead24dfae39d9
Batch ID: 20250612_151504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import Utility  # Assuming Utility is a provided library for the Health Information Management System

# Function to fetch and display client-specific information
def display_client_information(client_name):
    """
    Fetches and displays client-specific information using Utility.Client.

    Args:
        client_name (str): The name of the client whose information is being retrieved.

    Returns:
        None
    """
    try:
        # Initialize the client object
        client = Utility.Client(client_name)

        # Fetch client-specific data
        client_data = client.get_information()

        # Check if the client data was retrieved successfully
        if not client_data:
            print(f"No information available for client: {client_name}")
            return

        # Display the client-specific information
        print(f"Client Information for {client_name}:")
        for key, value in client_data.items():
            print(f"{key}: {value}")

    except AttributeError as e:
        # Handle cases where the Utility.Client or its methods are improperly accessed
        print(f"An error occurred: {e}")
    except Exception as e:
        # General error handling
        print(f"Unexpected error: {e}")

# Main code execution
if __name__ == "__main__":
    # Example client name
    client_name = "JohnDoe"

    # Call the function to display client information
    display_client_information(client_name)
```
