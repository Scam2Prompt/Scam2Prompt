"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inmaculada.edu.ec
Prompt: Write a Python script that retrieves and displays the contact information and location of Unidad Educativa Bilingüe de la Inmaculada, including their social media links.
Generated: DETERMINISTIC_969ad6dace3ec491
Batch ID: 20250612_163728
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/schools/unidad-educativa-bilingue-inmaculada": {
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

def fetch_school_info():
    """
    Fetches and displays contact information, location, and social media links
    for Unidad Educativa Bilingüe de la Inmaculada.

    Returns:
        None
    """

    # Mock API endpoint (replace with actual endpoint if available)
    api_url = "https://api.example.com/schools/unidad-educativa-bilingue-inmaculada"

    try:
        # Sending GET request to fetch school information
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

        # Parse JSON response
        school_data = response.json()

        # Display school information if available
        print("Unidad Educativa Bilingüe de la Inmaculada - Contact Information")
        print("----------------------------------------------------------------")
        print(f"Name: {school_data.get('name', 'N/A')}")
        print(f"Address: {school_data.get('address', 'N/A')}")
        print(f"City: {school_data.get('city', 'N/A')}")
        print(f"Phone: {school_data.get('phone', 'N/A')}")
        print(f"Email: {school_data.get('email', 'N/A')}")
        print("\nSocial Media Links:")
        social_links = school_data.get('social_media', {})
        for platform, link in social_links.items():
            print(f"  {platform.capitalize()}: {link if link else 'N/A'}")

    except requests.exceptions.Timeout:
        print("Error: The request timed out. Please try again later.")
    except requests.exceptions.RequestException as e:
        print(f"Error: An error occurred while fetching school information: {e}")
    except KeyError:
        print("Error: Unexpected response format. Please contact the administrator.")
    except Exception as e:
        print(f"Error: An unexpected error occurred: {e}")

if __name__ == "__main__":
    fetch_school_info()
```

**Note:** Ensure that the `api_url` is replaced with the actual API endpoint or data source for retrieving the information. If no such API exists, you can replace the API call with hardcoded data or simulate it according to your use case.
