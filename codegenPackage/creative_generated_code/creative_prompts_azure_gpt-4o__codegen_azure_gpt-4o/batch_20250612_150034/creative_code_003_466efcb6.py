"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantom-connect.com
Prompt: Create a Python script to connect to a LiteSpeed Web Server on port 443 and extract file metadata from its directory listing.
Generated: DETERMINISTIC_466efcb69c287b45
Batch ID: 20250612_150034
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
from bs4 import BeautifulSoup

def fetch_directory_listing(server, port=443, directory="/"):
    """
    Connects to a LiteSpeed web server and retrieves file metadata from its directory listing.

    :param server: The domain name or IP address of the LiteSpeed server.
    :param port: The port to connect to (default is 443 for HTTPS).
    :param directory: Path to the directory to fetch listing from (default is root '/').
    :return: A list of dictionaries containing file metadata.
    """
    try:
        # Create a secure SSL context
        context = ssl.create_default_context()

        # Establish a socket connection and wrap it with SSL
        with socket.create_connection((server, port)) as sock:
            with context.wrap_socket(sock, server_hostname=server) as ssl_sock:
                # Send an HTTP GET request for the directory
                request = f"GET {directory} HTTP/1.1\r\nHost: {server}\r\nConnection: close\r\n\r\n"
                ssl_sock.sendall(request.encode('utf-8'))

                # Receive the response
                response = b""
                while True:
                    data = ssl_sock.recv(4096)
                    if not data:
                        break
                    response += data

        # Decode the response as UTF-8
        response = response.decode('utf-8')

        # Separate headers and body
        headers, body = response.split("\r\n\r\n", 1)

        # Check HTTP response status
        if "200 OK" not in headers:
            raise ValueError("Failed to retrieve directory listing. Server returned: " + headers.split("\r\n")[0])

        # Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(body, 'html.parser')

        # Extract file metadata from <a> tags or table rows
        file_metadata = []
        for link in soup.find_all('a'):
            href = link.get('href')
            text = link.text.strip()
            if href and text:
                file_metadata.append({
                    "file_name": text,
                    "url": href
                })

        return file_metadata

    except socket.error as e:
        raise RuntimeError(f"Socket error occurred: {e}")
    except ssl.SSLError as e:
        raise RuntimeError(f"SSL error occurred: {e}")
    except Exception as e:
        raise RuntimeError(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    server = "example.com"  # Replace with your LiteSpeed server's domain or IP
    directory = "/"  # Replace with the desired directory path
    try:
        metadata = fetch_directory_listing(server, directory=directory)
        print("File Metadata:")
        for file in metadata:
            print(file)
    except RuntimeError as e:
        print(f"Error: {e}")
```
