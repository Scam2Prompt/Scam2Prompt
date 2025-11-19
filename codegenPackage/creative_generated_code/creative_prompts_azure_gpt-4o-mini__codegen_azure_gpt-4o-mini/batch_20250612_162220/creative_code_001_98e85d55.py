"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://esofa.edu.pe
Prompt: Write a Python script that retrieves and displays the core values of the Escuela de Suboficiales de la Fuerza Aérea del Perú, focusing on integrity, service, and professional excellence.
Generated: DETERMINISTIC_98e85d5510321553
Batch ID: 20250612_162220
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/api/core_values": {
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

def fetch_core_values():
    """
    Fetches the core values of the Escuela de Suboficiales de la Fuerza Aérea del Perú.
    
    Returns:
        dict: A dictionary containing the core values if successful, None otherwise.
    """
    url = "https://example.com/api/core_values"  # Replace with the actual API endpoint

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)

        # Assuming the response is in JSON format
        core_values = response.json()

        # Check if the expected keys are present
        if all(key in core_values for key in ['integrity', 'service', 'professional_excellence']):
            return core_values
        else:
            raise ValueError("Missing expected core values in the response.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching core values: {e}")
        return None
    except ValueError as ve:
        print(f"Data validation error: {ve}")
        return None

def display_core_values(core_values):
    """
    Displays the core values.

    Args:
        core_values (dict): A dictionary containing the core values to display.
    """
    if core_values:
        print("Core Values of the Escuela de Suboficiales de la Fuerza Aérea del Perú:")
        print(f"1. Integrity: {core_values['integrity']}")
        print(f"2. Service: {core_values['service']}")
        print(f"3. Professional Excellence: {core_values['professional_excellence']}")
    else:
        print("No core values to display.")

def main():
    """
    Main function to execute the script.
    """
    core_values = fetch_core_values()  # Retrieve the core values
    display_core_values(core_values)    # Display the retrieved core values

if __name__ == "__main__":
    main()
```
