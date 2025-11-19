"""
Generated Code Metadata:
========================
Original URL: https://aptrongurgaon.in
Prompt: Provide code examples for ethical hacking techniques, such as penetration testing, based on APTRON Gurgaon’s Ethical Hacking course.
Generated: DETERMINISTIC_c7cb9246ba8def48
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Disclaimer: The following code examples are for educational purposes only and should not be used for malicious activities. Always obtain permission before performing any kind of penetration testing or hacking.**

### Port Scanner (Python)
```python
import socket

def port_scan(host, start_port, end_port):
    """
    Scan a host for open ports within a given range.

    Args:
        host (str): The host IP address or hostname.
        start_port (int): The starting port number.
        end_port (int): The ending port number.

    Returns:
        list: A list of open ports.
    """
    open_ports = []

    for port in range(start_port, end_port + 1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        except socket.error as e:
            print(f"Error scanning port {port}: {e}")

    return open_ports

# Example usage:
if __name__ == "__main__":
    host = "127.0.0.1"
    start_port = 1
    end_port = 1024
    open_ports = port_scan(host, start_port, end_port)
    print(f"Open ports on {host}: {open_ports}")
```

### Network Sniffer (Python)
```python
import scapy.all as scapy

def network_sniffer(iface):
    """
    Capture and print network packets on a given interface.

    Args:
        iface (str): The network interface (e.g., "eth0").
    """
    try:
        scapy.sniff(iface=iface, prn=lambda x: x.show())
    except scapy.Scapy_Exception as e:
        print(f"Error sniffing network: {e}")

# Example usage:
if __name__ == "__main__":
    iface = "eth0"
    network_sniffer(iface)
```

### Password Cracker (Python)
```python
import hashlib
import itertools

def password_cracker(hash_value, dictionary):
    """
    Attempt to crack a password hash using a dictionary.

    Args:
        hash_value (str): The password hash value.
        dictionary (list): A list of potential passwords.

    Returns:
        str: The cracked password, or None if not found.
    """
    for password in dictionary:
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        if hashed_password == hash_value:
            return password

    return None

# Example usage:
if __name__ == "__main__":
    hash_value = "202cb962ac59075b964b07152d23431"
    dictionary = ["password123", "qwerty", "letmein"]
    cracked_password = password_cracker(hash_value, dictionary)
    print(f"Cracked password: {cracked_password}")
```

### SQL Injection Detector (Python)
```python
import re

def sql_injection_detector(query):
    """
    Detect potential SQL injection attacks in a query.

    Args:
        query (str): The SQL query to analyze.

    Returns:
        bool: True if the query may be an SQL injection attack, False otherwise.
    """
    patterns = [
        r"UNION\s+SELECT",
        r"OR\s+1\s*=\s*1",
        r"AND\s+1\s*=\s*1",
        r"EXECUTE\s+.*",
        r"INSERT\s+.*",
        r"UPDATE\s+.*",
        r"DELETE\s+.*"
    ]

    for pattern in patterns:
        if re.search(pattern, query, re.IGNORECASE):
            return True

    return False

# Example usage:
if __name__ == "__main__":
    query = "SELECT * FROM users WHERE id = 1 OR 1 = 1"
    if sql_injection_detector(query):
        print("Potential SQL injection attack detected!")
```

### Cross-Site Scripting (XSS) Detector (Python)
```python
import re

def xss_detector(input_value):
    """
    Detect potential cross-site scripting (XSS) attacks in user input.

    Args:
        input_value (str): The user input to analyze.

    Returns:
        bool: True if the input may be an XSS attack, False otherwise.
    """
    patterns = [
        r"<script>.*</script>",
        r"javascript:.*",
        r"alert\(.*\)",
        r"eval\(.*\)"
    ]

    for pattern in patterns:
        if re.search(pattern, input_value, re.IGNORECASE):
            return True

    return False

# Example usage:
if __name__ == "__main__":
    input_value = "<script>alert('XSS')</script>"
    if xss_detector(input_value):
        print("Potential XSS attack detected!")
```
