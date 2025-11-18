"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://0.ai
Prompt: Develop a program that generates a list of numerical ".ai" domains (e.g., 1.ai, 2.ai, 3.ai) and checks their registration status, inspired by the domain list on https://0.ai.
Generated: DETERMINISTIC_21382f4f4359e552
Batch ID: 20250612_150040
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://domain-availability.whoisxmlapi.com/api/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://domain-availability.whoisxmlapi.com/api/v1`": {
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
import sys


def is_domain_available(domain):
    """
    Check if a domain is available by querying a WHOIS API or similar service.
    Replace the URL and parameters with the appropriate WHOIS or domain-checking API.
    
    Args:
        domain (str): The domain name to check.

    Returns:
        bool: True if the domain is available, False otherwise.
    """
    try:
        # Example API endpoint for domain availability check (replace with actual API information)
        api_url = f"https://domain-availability.whoisxmlapi.com/api/v1"
        api_key = "your_api_key_here"  # Replace with your API key
        params = {"apiKey": api_key, "domainName": domain}

        response = requests.get(api_url, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

        # Parse the response (modify based on the API's response structure)
        data = response.json()
        return data.get("DomainInfo", {}).get("domainAvailability") == "AVAILABLE"
    except requests.exceptions.RequestException as e:
        # Log the error and handle it gracefully
        print(f"Error checking domain {domain}: {e}", file=sys.stderr)
        return False


def generate_domains(start, end):
    """
    Generate a list of numerical domains within a specified range.

    Args:
        start (int): Starting number for domain generation.
        end (int): Ending number for domain generation.

    Returns:
        list: A list of numerical domains (e.g., ['1.ai', '2.ai', ...]).
    """
    return [f"{i}.ai" for i in range(start, end + 1)]


def main():
    """
    Main function to generate domains, check their availability, and print the results.
    """
    try:
        # Define range for domain generation (1.ai to 100.ai)
        start_range = 1
        end_range = 100

        # Generate the domain list
        domains = generate_domains(start_range, end_range)

        print("Checking domain availability...\n")

        # Check each domain's availability
        for domain in domains:
            is_available = is_domain_available(domain)
            availability_status = "AVAILABLE" if is_available else "UNAVAILABLE"
            print(f"{domain}: {availability_status}")
    except Exception as e:
        # Log any unexpected errors
        print(f"An error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```

**Note:** Replace `https://domain-availability.whoisxmlapi.com/api/v1` and `your_api_key_here` with appropriate API endpoint and valid API key for checking domain availability. Adjust the response parsing based on the specific API documentation.
