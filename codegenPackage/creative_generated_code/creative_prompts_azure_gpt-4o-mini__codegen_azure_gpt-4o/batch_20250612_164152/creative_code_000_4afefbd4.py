"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://0.ai
Prompt: Generate a Python script that checks the availability of AI-related domain names like 1.ai, 2.ai, and others listed on the Ultimate AI Domains page.
Generated: DETERMINISTIC_4afefbd440b8eb7d
Batch ID: 20250612_164152
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.example.com/v1/check": {
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

def check_domain_availability(domain):
    """
    Checks the availability of a domain using a WHOIS API.
    
    Args:
        domain (str): The domain name to check (e.g., '1.ai').
    
    Returns:
        str: Status of the domain ('Available', 'Taken', or 'Error').
    """
    # Replace with your chosen WHOIS API endpoint and API key
    WHOIS_API_URL = "https://api.example.com/v1/check"
    WHOIS_API_KEY = "your_api_key_here"
    
    try:
        # Send GET request to WHOIS API
        response = requests.get(
            WHOIS_API_URL,
            params={"domain": domain, "api_key": WHOIS_API_KEY},
            timeout=10  # Set a reasonable timeout
        )
        response.raise_for_status()  # Raise an error for HTTP codes >= 400
        
        # Parse the API response
        data = response.json()
        if "availability" in data:
            return "Available" if data["availability"] else "Taken"
        else:
            return "Error: Unexpected API response format"
    
    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        return f"Error: {str(e)}"

def main():
    """
    Main function to check the availability of AI-related domains.
    
    Reads domain names from a predefined list and checks each domain's availability.
    """
    # List of AI-related domain names to check
    ai_domains = [
        "1.ai", "2.ai", "3.ai", "chat.ai", "bot.ai", "ml.ai", "deeplearning.ai", "data.ai"
    ]
    
    print("Checking domain availability...")
    print("-" * 30)
    
    # Iterate through the domain list and check availability
    for domain in ai_domains:
        status = check_domain_availability(domain)
        print(f"{domain}: {status}")
    
    print("-" * 30)
    print("Domain availability check complete!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProcess interrupted by the user.")
        sys.exit(0)
```

### Notes:
- Replace the placeholder `WHOIS_API_URL` and `WHOIS_API_KEY` with actual values from your preferred WHOIS API provider.
- Install the `requests` library if it’s not already installed: `pip install requests`. 
- Ensure you comply with the API provider’s terms for domain queries.
