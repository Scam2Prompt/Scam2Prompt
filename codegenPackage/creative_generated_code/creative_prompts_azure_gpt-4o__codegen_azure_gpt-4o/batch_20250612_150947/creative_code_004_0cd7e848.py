"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://community-forum.42web.io
Prompt: Create a script to test and verify SSL installation on a hosting service that offers free and simple SSL, as mentioned in iFastNet hosting features.
Generated: DETERMINISTIC_0cd7e848bb070ab7
Batch ID: 20250612_150947
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import ssl
import socket

def verify_ssl(hostname, port=443):
    """
    Verifies SSL installation for a given hostname and port.
    
    Parameters:
        hostname (str): The domain name to test SSL for.
        port (int): The port to test SSL on (default: 443).
    
    Returns:
        dict: A dictionary containing the verification result and details.
    """
    result = {
        "hostname": hostname,
        "port": port,
        "is_ssl_valid": False,
        "ssl_info": {},
        "error": None
    }

    try:
        # Create a socket connection with the server
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                # Get SSL certificate details
                cert = ssock.getpeercert()
                
                # Check if certificate exists and has required fields
                if cert:
                    result["is_ssl_valid"] = True
                    result["ssl_info"] = cert
                else:
                    result["error"] = "No SSL certificate found."
    except ssl.SSLError as e:
        result["error"] = f"SSL Error: {str(e)}"
    except socket.error as e:
        result["error"] = f"Socket Error: {str(e)}"
    except Exception as e:
        result["error"] = f"Unexpected Error: {str(e)}"
    
    return result


if __name__ == "__main__":
    # Example usage
    hostname = input("Enter the hostname to check SSL (e.g., example.com): ").strip()

    ssl_result = verify_ssl(hostname)
    if ssl_result["is_ssl_valid"]:
        print(f"SSL certificate is valid for '{hostname}' on port {ssl_result['port']}.")
        print("Certificate Details:")
        for key, value in ssl_result["ssl_info"].items():
            print(f"{key}: {value}")
    else:
        print(f"Failed to verify SSL for '{hostname}' on port {ssl_result['port']}.")
        print(f"Error: {ssl_result['error']}")
```
