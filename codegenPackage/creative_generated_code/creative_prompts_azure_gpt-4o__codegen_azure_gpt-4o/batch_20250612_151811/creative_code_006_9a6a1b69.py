"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://baywords.org
Prompt: Provide code examples for deploying a lightweight DNS server in a "Cabin" environment with limited resources.
Generated: DETERMINISTIC_9a6a1b697d291553
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python implementation for a lightweight DNS server suitable for a resource-constrained ("Cabin") environment:

```python
import socket
import struct
import logging

# Configure logging for debugging and production readiness
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

class LightweightDNSServer:
    def __init__(self, host="0.0.0.0", port=53):
        """
        Initialize the DNS server with specified host and port.
        """
        self.host = host
        self.port = port
        self.domains = {
            "example.com": "1.2.3.4",  # Static mapping of domain names to IPs
            "test.local": "192.168.1.100",
        }

    def start(self):
        """
        Start the DNS server and listen for incoming requests.
        """
        try:
            # Create a UDP socket
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            server_socket.bind((self.host, self.port))
            logging.info(f"DNS server started on {self.host}:{self.port}")

            while True:
                # Listen for incoming DNS queries
                data, client_address = server_socket.recvfrom(512)  # DNS packets are typically small
                logging.info(f"Received query from {client_address}")
                response = self.handle_request(data)
                server_socket.sendto(response, client_address)
                logging.info(f"Response sent to {client_address}")

        except Exception as e:
            logging.error(f"Error: {e}")
        finally:
            server_socket.close()
            logging.info("DNS server shut down.")

    def handle_request(self, data):
        """
        Handle incoming DNS requests and generate a response.
        """
        try:
            # Unpack the DNS request
            transaction_id = data[:2]  # Transaction ID
            flags = struct.pack("!H", 0x8180)  # Standard query response flags
            questions = data[4:6]  # Question count
            answer_rrs = struct.pack("!H", len(self.domains))  # Answer Resource Record count
            authority_rrs = struct.pack("!H", 0)  # Authority Resource Record count
            additional_rrs = struct.pack("!H", 0)  # Additional Resource Record count

            # Extract the domain name from the query
            query = data[12:]
            domain_name = self._extract_domain(query)
            logging.info(f"Query for domain: {domain_name}")

            if domain_name in self.domains:
                ip_address = self.domains[domain_name]
                response = self._build_response(
                    transaction_id, flags, questions, answer_rrs, authority_rrs, additional_rrs, query, ip_address
                )
                return response
            else:
                logging.warning(f"Domain {domain_name} not found.")
                return transaction_id + b"\x81\x83"  # Response indicating 'Name Error'

        except Exception as e:
            logging.error(f"Error handling request: {e}")
            return b""  # Empty response for malformed requests

    def _extract_domain(self, query):
        """
        Extract the domain name from the raw DNS query.
        """
        domain_parts = []
        i = 0
        length = query[i]

        while length != 0:
            i += 1
            domain_parts.append(query[i : i + length].decode("utf-8"))
            i += length
            length = query[i]

        return ".".join(domain_parts)

    def _build_response(self, transaction_id, flags, questions, answer_rrs, authority_rrs, additional_rrs, query, ip_address):
        """
        Build the DNS response packet.
        """
        # DNS Header
        header = transaction_id + flags + questions + answer_rrs + authority_rrs + additional_rrs

        # DNS Question Section (echoing the query)
        question = query + struct.pack("!H", 1) + struct.pack("!H", 1)  # Type A, Class IN

        # DNS Answer Section
        answer = struct.pack("!HHHLH", 0xc00c, 1, 1, 60, 4)  # Pointer, Type A, Class IN, TTL=60s, Data length=4
        answer += socket.inet_aton(ip_address)  # Convert IP address to binary format

        return header + question + answer


if __name__ == "__main__":
    # Start the lightweight DNS server
    dns_server = LightweightDNSServer()
    dns_server.start()
```

### Notes:
- This code listens on port `53` (default DNS port) and resolves a predefined set of domain names to IP addresses.
- The implementation handles DNS data packets in a minimalist fashion and processes basic A-record queries.
- Logging is included to provide visibility into server operations and debugging.
- The `_extract_domain` and `_build_response` methods ensure proper parsing and encoding of DNS packets.
- Proper error handling ensures the server remains operational despite minor issues.
