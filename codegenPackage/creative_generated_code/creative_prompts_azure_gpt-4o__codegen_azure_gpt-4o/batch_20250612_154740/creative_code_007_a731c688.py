"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappsconnect.42web.io
Prompt: Generate a script to verify SSL installation on a hosting service that provides free and simple SSL, as described on iFastNet hosting.
Generated: DETERMINISTIC_a731c68819bf7957
Batch ID: 20250612_154740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import socket
import ssl

def verify_ssl(hostname, port=443):
    """
    Verifies SSL installation for a given hostname and port.

    Parameters:
    hostname (str): The domain name to check for SSL installation.
    port (int): The port to connect to (default is 443 for HTTPS).

    Returns:
    dict: A dictionary containing SSL verification details.
    """
    try:
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port), timeout=10) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                # Retrieve certificate details
                cert = ssock.getpeercert()
                return {
                    "success": True,
                    "certificate_details": cert,
                    "message": f"SSL is installed and valid for {hostname}."
                }
    except ssl.SSLError as e:
        return {
            "success": False,
            "error": str(e),
            "message": f"SSL verification failed for {hostname}. SSL error encountered."
        }
    except socket.error as e:
        return {
            "success": False,
            "error": str(e),
            "message": f"Connection error occurred while verifying SSL for {hostname}."
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e),
            "message": f"An unexpected error occurred while verifying SSL for {hostname}."
        }


if __name__ == "__main__":
    # Example usage
    hostname_to_check = "example.com"  # Replace with your domain name
    result = verify_ssl(hostname_to_check)
    
    # Print the result to the console
    if result["success"]:
        print(result["message"])
        print("Certificate Details:")
        for key, value in result["certificate_details"].items():
            print(f"{key}: {value}")
    else:
        print(result["message"])
        print("Error:", result["error"])
```
