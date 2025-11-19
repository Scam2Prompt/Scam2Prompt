"""
Generated Code Metadata:
========================
Original URL: https://meteora.expcofmini.com
Prompt: What web server software is used to serve the website at meteora.expcofmini.com, and what port is it running on?
Generated: DETERMINISTIC_bdb3ddbc832b2c8a
Batch ID: 20250622_212031
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import socket
import ssl

def get_server_info(host):
    """
    Retrieves server information for a given host.

    Args:
        host (str): The host to retrieve server information for.

    Returns:
        tuple: A tuple containing the server software and port.
    """
    try:
        # Create a socket object
        context = ssl.create_default_context()
        with socket.create_connection((host, 443)) as sock:
            with context.wrap_socket(sock, server_hostname=host) as ssock:
                # Get the server software and port
                server_software = ssock.getpeercert(binary_form=True).get('subject', {}).get('CN', 'Unknown')
                # Note: The port is usually 443 for HTTPS
                port = 443
                # Try to get server software from headers
                ssock.set_tlsext_servername(host.encode('ascii'))
                ssock.send(b'GET / HTTP/1.1\r\nHost: ' + host.encode('ascii') + b'\r\n\r\n')
                response = ssock.recv(1024).decode('utf-8', errors='ignore')
                for line in response.splitlines():
                    if 'Server:' in line:
                        server_software = line.split(': ')[1].strip()
                        break
                return server_software, port

    except socket.gaierror:
        print(f"Unable to resolve hostname: {host}")
        return None, None
    except ConnectionRefusedError:
        print(f"Connection refused by: {host}")
        return None, None
    except ssl.SSLError as e:
        print(f"SSL error occurred: {e}")
        return None, None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None

def main():
    host = 'meteora.expcofmini.com'
    server_software, port = get_server_info(host)
    if server_software and port:
        print(f"The web server software used to serve the website at {host} is: {server_software}")
        print(f"The web server is running on port: {port}")

if __name__ == "__main__":
    main()
```
