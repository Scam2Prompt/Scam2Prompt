"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ptei.edu.bd
Prompt: Illustrate how to use an API to access the syllabus data for the Electronics Technology department at Pabna Textile Engineering Institute (PTEI).
Generated: DETERMINISTIC_6a4bf53f516c6ed7
Batch ID: 20250612_164021
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/api/syllabus": {
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

# Define a function to fetch syllabus data from the API
def fetch_syllabus_data(department, institute):
    """
    Fetch syllabus data for a specified department and institute from the API.

    Args:
        department (str): The name of the department (e.g., 'Electronics Technology').
        institute (str): The name of the institute (e.g., 'Pabna Textile Engineering Institute').

    Returns:
        dict: Parsed JSON data containing syllabus information.

    Raises:
        ValueError: If the response from the API is not successful or if data is not found.
        requests.RequestException: For issues with the API request.
    """
    # Base URL of the API
    base_url = "https://example.com/api/syllabus"
    
    # Prepare parameters for the API query
    params = {
        "department": department,
        "institute": institute
    }

    try:
        # Send a GET request to the API
        response = requests.get(base_url, params=params)
        
        # Raise an HTTP error if the request was not successful
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()

        # Check if the data exists in the response
        if not data.get("syllabus"):
            raise ValueError("No syllabus data found for the specified department and institute.")

        return data

    except requests.RequestException as e:
        # Handle exceptions related to HTTP requests
        raise requests.RequestException(f"An error occurred while fetching syllabus data: {e}")

    except ValueError as e:
        # Handle cases where the data is not as expected
        raise ValueError(f"Data error: {e}")

# Main execution block to demonstrate usage
if __name__ == "__main__":
    # Define department and institute
    department = "Electronics Technology"
    institute = "Pabna Textile Engineering Institute"

    try:
        # Fetch syllabus data
        syllabus_data = fetch_syllabus_data(department, institute)

        # Print the syllabus data
        print("Syllabus Data:")
        print(syllabus_data)

    except Exception as e:
        # Handle any errors gracefully
        print(f"Error: {e}")
```
