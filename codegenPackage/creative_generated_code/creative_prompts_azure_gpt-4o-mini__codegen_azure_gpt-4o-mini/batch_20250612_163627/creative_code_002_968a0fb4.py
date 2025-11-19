"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tomarket-ai.com
Prompt: Create a function that checks the availability of a domain name using an API, inspired by the domain services provided by Porkbun.com.
Generated: DETERMINISTIC_968a0fb455ad90fe
Batch ID: 20250612_163627
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://porkbun.com/api/json/": {
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

class DomainChecker:
    """
    A class to check the availability of a domain name using the Porkbun API.
    """

    BASE_URL = "https://porkbun.com/api/json/"

    def __init__(self):
        """
        Initializes the DomainChecker instance.
        """
        self.session = requests.Session()

    def check_domain_availability(self, domain_name):
        """
        Checks the availability of the given domain name.

        Args:
            domain_name (str): The domain name to check.

        Returns:
            dict: A dictionary containing the availability status and message.
        """
        if not self._is_valid_domain_name(domain_name):
            return {"success": False, "message": "Invalid domain name format."}
        
        try:
            response = self.session.get(f"{self.BASE_URL}domain/status", params={"domain": domain_name})
            response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)

            data = response.json()
            if data.get("success"):
                return {
                    "success": True,
                    "available": data["data"]["available"],
                    "message": f"{domain_name} is {'available' if data['data']['available'] else 'not available'}."
                }
            else:
                return {
                    "success": False,
                    "message": data.get("message", "An error occurred while checking the domain.")
                }
        except requests.RequestException as e:
            return {"success": False, "message": f"Request failed: {str(e)}"}

    def _is_valid_domain_name(self, domain_name):
        """
        Validates the domain name format.

        Args:
            domain_name (str): The domain name to validate.

        Returns:
            bool: True if valid, False otherwise.
        """
        import re
        # Simple regex for validating domain names
        regex = r'^(?!-)[A-Za-z0-9-]{1,63}(?<!-)\.[A-Za-z]{2,}$'
        return re.match(regex, domain_name) is not None


if __name__ == "__main__":
    # Example usage
    domain_checker = DomainChecker()
    domain_name = "example.com"  # Replace with the desired domain name
    result = domain_checker.check_domain_availability(domain_name)
    print(result)
```
