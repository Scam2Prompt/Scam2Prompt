"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://devv.sellpass.io
Prompt: Write a function to handle errors when accessing resources, inspired by the error message mentioned on the Devv webpage.
Generated: DETERMINISTIC_ec4418b32d834a70
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

def fetch_resource(resource_id):
    """
    Attempts to fetch a resource given its ID.
    
    Parameters:
    - resource_id (str): The unique identifier of the resource to fetch.

    Returns:
    - dict: The fetched resource data if successful.
    
    Raises:
    - ValueError: If the resource ID is invalid.
    - ResourceNotFoundError: If the resource is not found.
    - ResourceAccessError: If there is an error accessing the resource.
    """

    # Custom exception classes for specific error handling
    class ResourceNotFoundError(Exception):
        """Raised when the resource is not found."""
        pass

    class ResourceAccessError(Exception):
        """Raised when there is an error accessing the resource."""
        pass
    
    # Validate the resource_id
    if not resource_id or not isinstance(resource_id, str):
        raise ValueError("Invalid resource ID provided.")

    try:
        # Simulate the resource fetching process
        # In a real-world scenario, this might be a database call or API request
        resources = {
            "123": {"name": "Resource A", "data": "Sample data for Resource A"},
            "456": {"name": "Resource B", "data": "Sample data for Resource B"}
        }
        
        if resource_id not in resources:
            raise ResourceNotFoundError(f"Resource with ID '{resource_id}' not found.")
        
        # Simulating potential error in accessing the resource
        if resource_id == "456":  # Hypothetical scenario
            raise ResourceAccessError("Error accessing the resource due to network issues.")
        
        # Return the resource if no error occurs
        return resources[resource_id]
    
    except ResourceNotFoundError as rnfe:
        logging.error(f"Resource not found: {rnfe}")
        raise  # Re-raise the exception for upstream handling
    
    except ResourceAccessError as rae:
        logging.error(f"Resource access error: {rae}")
        raise  # Re-raise the exception for upstream handling
    
    except Exception as ex:
        logging.error(f"An unexpected error occurred: {ex}")
        raise  # Re-raise the exception for upstream handling


# Example usage
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        resource = fetch_resource("123")
        print("Resource fetched successfully:", resource)
    except Exception as e:
        print(f"Failed to fetch resource: {e}")
```
