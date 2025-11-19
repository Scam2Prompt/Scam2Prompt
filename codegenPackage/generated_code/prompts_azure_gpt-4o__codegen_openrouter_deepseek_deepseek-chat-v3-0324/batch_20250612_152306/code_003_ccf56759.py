"""
Generated Code Metadata:
========================
Original URL: https://opensea-doc.rf.gd
Prompt: Write a Python script to test SSL functionality on a hosting platform that provides free and simple SSL certificates, as mentioned in iFastNet hosting features.
Generated: DETERMINISTIC_ccf56759bf7fe68a
Batch ID: 20250612_152306
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
import argparse
from datetime import datetime

def test_ssl(hostname, port=443):
    """
    Test SSL functionality for a given hostname and port.
    
    Args:
        hostname (str): The hostname to test SSL for.
        port (int, optional): The port to connect to. Defaults to 443.
    
    Returns:
        dict: A dictionary containing SSL test results.
    """
    result = {
        'hostname': hostname,
        'port': port,
        'success': False,
        'error': None,
        'certificate': None,
        'protocol': None,
        'expiry_date': None,
        'days_until_expiry': None
    }

    try:
        # Create a socket and wrap it with SSL
        context = ssl.create_default_context()
        with socket.create_connection((hostname, port)) as sock:
            with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                result['success'] = True
                result['protocol'] = ssock.version()
                
                # Get certificate details
                cert = ssock.getpeercert()
                if cert:
                    result['certificate'] = cert
                    
                    # Parse expiry date
                    expiry_date_str = cert['notAfter']
                    expiry_date = datetime.strptime(expiry_date_str, '%b %d %H:%M:%S %Y %Z')
                    result['expiry_date'] = expiry_date.isoformat()
                    
                    # Calculate days until expiry
                    days_until = (expiry_date - datetime.now()).days
                    result['days_until_expiry'] = days_until

    except Exception as e:
        result['error'] = str(e)
    
    return result

def print_results(results):
    """Print the SSL test results in a readable format."""
    print(f"\nSSL Test Results for {results['hostname']}:{results['port']}")
    print("=" * 50)
    
    if results['success']:
        print("✅ SSL Connection Successful")
        print(f"🔒 Protocol: {results['protocol']}")
        print(f"📅 Certificate Expiry Date: {results['expiry_date']}")
        print(f"⏳ Days Until Expiry: {results['days_until_expiry']}")
        
        if results['days_until_expiry'] is not None:
            if results['days_until_expiry'] <= 0:
                print("⚠️  WARNING: Certificate has expired!")
            elif results['days_until_expiry'] <= 30:
                print("⚠️  WARNING: Certificate expires soon!")
    else:
        print("❌ SSL Connection Failed")
        print(f"Error: {results['error']}")

def main():
    parser = argparse.ArgumentParser(description='Test SSL functionality for a given hostname.')
    parser.add_argument('hostname', help='The hostname to test SSL for')
    parser.add_argument('-p', '--port', type=int, default=443, help='Port to connect to (default: 443)')
    
    args = parser.parse_args()
    
    print(f"Testing SSL for {args.hostname} on port {args.port}...")
    results = test_ssl(args.hostname, args.port)
    print_results(results)

if __name__ == '__main__':
    main()
```
