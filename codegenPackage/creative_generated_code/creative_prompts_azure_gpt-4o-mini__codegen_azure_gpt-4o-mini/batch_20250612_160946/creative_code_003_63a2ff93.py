"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://virtue.guru
Prompt: Write a code snippet that demonstrates a specific use case of the Virtue Guru library.
Generated: DETERMINISTIC_63a2ff933dc8328d
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary modules from the Virtue Guru library
from virtue_guru import VirtueGuru, Virtue

# Initialize the Virtue Guru client
virtue_guru_client = VirtueGuru(api_key='your_api_key_here')  # Replace with your actual API key

def fetch_and_display_virtue(virtue_name):
    """
    Fetch a virtue by name and display its details.

    Parameters:
        virtue_name (str): The name of the virtue to fetch.

    Raises:
        ValueError: If the virtue_name is empty or not found.
    """

    # Validate the input
    if not virtue_name:
        raise ValueError("Virtue name must not be empty.")

    try:
        # Fetch the virtue from the Virtue Guru API
        virtue = virtue_guru_client.get_virtue(virtue_name)
        
        # Display the virtue details
        print(f"Virtue: {virtue.name}")
        print(f"Description: {virtue.description}")
        print(f"Benefits: {', '.join(virtue.benefits)}")
    
    except Exception as e:
        print(f"An error occurred while fetching the virtue: {e}")

if __name__ == "__main__":
    # Example usage of the fetch_and_display_virtue function
    try:
        fetch_and_display_virtue('Courage')  # Replace 'Courage' with the desired virtue
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
