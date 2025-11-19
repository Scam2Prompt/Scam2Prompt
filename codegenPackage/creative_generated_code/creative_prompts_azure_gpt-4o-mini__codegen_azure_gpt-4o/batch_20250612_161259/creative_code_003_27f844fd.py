"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://9af68e44.4d9aa11f0cc24373ec9d6295.workers.dev
Prompt: Generate a Python function that performs a security review of incoming connections to a web server.
Generated: DETERMINISTIC_27f844fd138c964c
Batch ID: 20250612_161259
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import logging
from ipaddress import ip_address, ip_network

# Configure logging for the security review system
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("security_review.log"), logging.StreamHandler()]
)

def perform_security_review(connection_info):
    """
    Performs a security review of incoming connections to a web server.

    Args:
        connection_info (dict): Information about the connection.
                                Expected keys: 'ip', 'user_agent', 'headers'.

    Returns:
        dict: Security review result containing 'status' and 'reason'.
    """
    try:
        # Initialize response dictionary
        review_result = {"status": "Approved", "reason": "Connection passes security review."}

        # Validate input structure
        if not isinstance(connection_info, dict):
            raise ValueError("Invalid connection_info format. Expected a dictionary.")

        # Extract connection details
        ip = connection_info.get('ip')
        user_agent = connection_info.get('user_agent')
        headers = connection_info.get('headers', {})

        # Check if IP is valid
        try:
            ip_obj = ip_address(ip)
        except ValueError:
            review_result["status"] = "Rejected"
            review_result["reason"] = "Invalid IP address format."
            logging.warning(f"Rejected connection due to invalid IP: {ip}")
            return review_result

        # Check if IP is in a blacklist (example static blacklist)
        blacklist = [
            ip_network('192.168.1.0/24'),  # Example: Block private subnet
            ip_network('10.0.0.0/8')       # Example: Block another private subnet
        ]
        if any(ip_obj in blocked for blocked in blacklist):
            review_result["status"] = "Rejected"
            review_result["reason"] = "IP address is blacklisted."
            logging.warning(f"Rejected connection from blacklisted IP: {ip}")
            return review_result

        # Check User-Agent for malicious signatures
        if user_agent:
            malicious_signatures = [
                r"(python-requests)",  # Example: Simple bot signature
                r"(curl)"              # Example: Curl command-line tool
            ]
            for signature in malicious_signatures:
                if re.search(signature, user_agent, re.IGNORECASE):
                    review_result["status"] = "Rejected"
                    review_result["reason"] = "User-Agent matches malicious signature."
                    logging.warning(f"Rejected connection due to malicious User-Agent: {user_agent}")
                    return review_result

        # Perform header validation (e.g., check for suspicious headers)
        suspicious_headers = ['X-Attack-Test', 'X-Malicious-Header']
        for header in suspicious_headers:
            if header in headers:
                review_result["status"] = "Rejected"
                review_result["reason"] = f"Suspicious header detected: {header}"
                logging.warning(f"Rejected connection due to suspicious header: {header}")
                return review_result

        # Log successful connection
        logging.info(f"Approved connection from IP: {ip}, User-Agent: {user_agent}")
        return review_result

    except Exception as e:
        # General error handling
        logging.error(f"Error during security review: {str(e)}")
        return {"status": "Error", "reason": "An internal error occurred during review."}

# Example usage
if __name__ == "__main__":
    connection = {
        "ip": "192.168.1.101",
        "user_agent": "python-requests/2.25.1",
        "headers": {"X-Test": "TestValue"}
    }
    result = perform_security_review(connection)
    print(result)
```
