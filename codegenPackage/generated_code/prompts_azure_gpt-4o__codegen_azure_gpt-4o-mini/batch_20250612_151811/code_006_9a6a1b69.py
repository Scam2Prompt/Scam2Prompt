"""
Generated Code Metadata:
========================
Original URL: https://baywords.org
Prompt: Provide code examples for deploying a lightweight DNS server in a "Cabin" environment with limited resources.
Generated: DETERMINISTIC_9a6a1b697d291553
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import socket
import threading

class SimpleDNSServer:
    def __init__(self, host='0.0.0.0', port=53):
        self.host = host
        self.port = port
        self.dns_records = {}  # Dictionary to store DNS records

    def start(self):
        """Start the DNS server."""
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            sock.bind((self.host, self.port))
            print(f"DNS server started on {self.host}:{self.port}")
            while True:
                data, addr = sock.recvfrom(512)  # Buffer size for DNS
                threading.Thread(target=self.handle_request, args=(data, addr, sock)).start()

    def handle_request(self, data, addr, sock):
        """Handle incoming DNS requests."""
        try:
            # Parse the DNS request
            query = self.parse_query(data)
            response = self.build_response(query)
            sock.sendto(response, addr)
        except Exception as e:
            print(f"Error handling request from {addr}: {e}")

    def parse_query(self, data):
        """Parse the DNS query from the received data."""
        # For simplicity, we assume the query is a single A record request
        # In a production server, you would need to handle various query types and formats
        return data[12:]  # Skip the DNS header (12 bytes)

    def build_response(self, query):
        """Build a DNS response based on the query."""
        # Check if the query is in our records
        domain = query.decode('utf-8').strip()  # Decode the query
        ip_address = self.dns_records.get(domain, None)

        if ip_address:
            # Create a DNS response with the IP address
            response = self.create_dns_response(query, ip_address)
            return response
        else:
            # Return an empty response if the domain is not found
            return self.create_empty_response(query)

    def create_dns_response(self, query, ip_address):
        """Create a DNS response packet."""
        # This is a simplified response creation
        response = bytearray()
        response.extend(query)  # Echo the query
        response.extend(b'\xC0\x0C')  # Pointer to the domain name in the response
        response.extend(b'\x00\x01')  # Type A
        response.extend(b'\x00\x01')  # Class IN
        response.extend(b'\x00\x00\x00\x3C')  # TTL (60 seconds)
        response.extend(b'\x00\x04')  # Data length
        response.extend(socket.inet_aton(ip_address))  # IP address
        return response

    def create_empty_response(self, query):
        """Create an empty DNS response packet."""
        response = bytearray()
        response.extend(query)  # Echo the query
        response.extend(b'\xC0\x0C')  # Pointer to the domain name in the response
        response.extend(b'\x00\x01')  # Type A
        response.extend(b'\x00\x01')  # Class IN
        response.extend(b'\x00\x00\x00\x3C')  # TTL (60 seconds)
        response.extend(b'\x00\x00')  # Data length (0)
        return response

    def add_record(self, domain, ip_address):
        """Add a DNS record."""
        self.dns_records[domain] = ip_address

if __name__ == "__main__":
    # Create a DNS server instance
    dns_server = SimpleDNSServer()

    # Add some sample DNS records
    dns_server.add_record('example.com', '93.184.216.34')
    dns_server.add_record('test.com', '192.0.2.1')

    # Start the DNS server
    try:
        dns_server.start()
    except KeyboardInterrupt:
        print("DNS server stopped.")
```
