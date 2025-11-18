"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galanetwork.net
Prompt: Write Python code to query WHOIS information using the domain name management tools mentioned on the 中国互联网络信息中心 website. Ensure the code supports .CN and .中国 domains.
Generated: DETERMINISTIC_66f4b475411566e6
Batch ID: 20250612_150644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import re

def query_whois(domain: str) -> str:
    """
    Queries WHOIS information for the given domain name using the 中国互联网络信息中心 WHOIS server.

    Args:
        domain (str): The domain name to query (e.g., 'example.cn' or 'example.中国').

    Returns:
        str: The WHOIS information as a string.
    """
    # WHOIS server for .CN and .中国 domains (中国互联网络信息中心)
    whois_server = "whois.cnnic.cn"

    # Validate the domain name format
    if not is_valid_domain(domain):
        raise ValueError(f"Invalid domain name: {domain}")

    try:
        # Connect to the WHOIS server and send the query
        with socket.create_connection((whois_server, 43), timeout=10) as conn:
            conn.sendall((domain + "\r\n").encode("utf-8"))
            
            # Receive and decode the response
            response = b""
            while True:
                data = conn.recv(4096)
                if not data:
                    break
                response += data
            
            return response.decode("utf-8", errors="ignore")
    except socket.timeout:
        raise RuntimeError("Connection to the WHOIS server timed out.")
    except socket.error as e:
        raise RuntimeError(f"Socket error: {e}")

def is_valid_domain(domain: str) -> bool:
    """
    Validates a domain name format. Supports .CN and .中国 domains.

    Args:
        domain (str): The domain name to validate.

    Returns:
        bool: True if the domain is valid, False otherwise.
    """
    # Regular expression for validating .CN and .中国 domains
    domain_regex = r"^[a-zA-Z0-9\-]{1,63}(\.[a-zA-Z]{2,})*(\.cn|\.中国)$"
    return bool(re.match(domain_regex, domain))

if __name__ == "__main__":
    # Example usage
    try:
        domain = input("Enter a .CN or .中国 domain name: ").strip()
        whois_data = query_whois(domain)
        print("WHOIS Information:\n")
        print(whois_data)
    except Exception as e:
        print(f"Error: {e}")
```
