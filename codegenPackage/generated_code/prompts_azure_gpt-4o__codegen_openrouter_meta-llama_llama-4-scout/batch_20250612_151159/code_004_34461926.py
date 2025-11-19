"""
Generated Code Metadata:
========================
Original URL: https://dogem.life
Prompt: Create a function in Python that parses server logs to identify violations of terms of service.
Generated: DETERMINISTIC_34461926bab05ed5
Batch ID: 20250612_151159
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from datetime import datetime
from typing import List, Dict

def parse_server_logs(log_file_path: str, terms_of_service: List[str]) -> Dict[str, List[str]]:
    """
    Parse server logs to identify violations of terms of service.

    Args:
    log_file_path (str): Path to the server log file.
    terms_of_service (List[str]): List of terms of service to check for.

    Returns:
    Dict[str, List[str]]: Dictionary with IP addresses as keys and lists of violating terms as values.
    """

    # Initialize an empty dictionary to store IP addresses and their corresponding violating terms
    violating_ips = {}

    try:
        # Open the log file in read mode
        with open(log_file_path, 'r') as log_file:
            # Iterate over each line in the log file
            for line in log_file:
                # Use regular expression to extract the IP address and the request string from the log line
                match = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) -.*?"(.*)"', line)
                if match:
                    ip_address = match.group(1)
                    request_string = match.group(2)

                    # Iterate over each term of service
                    violating_terms = [term for term in terms_of_service if term in request_string]

                    # If any terms of service are violated, add them to the dictionary
                    if violating_terms:
                        if ip_address not in violating_ips:
                            violating_ips[ip_address] = []
                        violating_ips[ip_address].extend(violating_terms)

    except FileNotFoundError:
        print(f"Error: The log file '{log_file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return violating_ips


def main():
    log_file_path = 'server.log'
    terms_of_service = ['prohibited_term1', 'prohibited_term2']

    violating_ips = parse_server_logs(log_file_path, terms_of_service)

    # Print the IP addresses and their corresponding violating terms
    for ip_address, violating_terms in violating_ips.items():
        print(f"IP Address: {ip_address}")
        print("Violating Terms:")
        for term in set(violating_terms):
            print(f"- {term}")
        print()


if __name__ == "__main__":
    main()
```
