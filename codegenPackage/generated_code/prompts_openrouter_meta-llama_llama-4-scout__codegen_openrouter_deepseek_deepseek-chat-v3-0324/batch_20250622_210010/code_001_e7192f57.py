"""
Generated Code Metadata:
========================
Original URL: https://airdrop-stepngo.asia
Prompt: Write a Python script to check if a domain has an SSL certificate installed using the OpenSSL library, as described in FASTPANEL's troubleshooting guide.
Generated: DETERMINISTIC_e7192f57e3c7f947
Batch ID: 20250622_210010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import subprocess
import sys
from typing import Optional, Tuple

def check_ssl_certificate(domain: str, port: int = 443, timeout: int = 10) -> Tuple[bool, Optional[str]]:
    """
    Check if a domain has an SSL certificate installed using OpenSSL.
    
    Args:
        domain: Domain name to check (e.g., 'example.com')
        port: Port number (default: 443)
        timeout: Connection timeout in seconds (default: 10)
    
    Returns:
        Tuple of (success: bool, message: Optional[str])
        success: True if certificate is valid, False otherwise
        message: Error message if certificate is invalid, None if valid
    """
    try:
        # Run openssl command to check certificate
        result = subprocess.run(
            [
                'openssl', 's_client', 
                '-connect', f'{domain}:{port}',
                '-servername', domain,
                '-verify_hostname', domain,
                '-verify_return_error',
                '-brief',
                '-status',
                '-timeout', str(timeout)
            ],
            capture_output=True,
            text=True,
            check=False
        )
        
        # Check output for verification success
        if 'Verification: OK' in result.stdout:
            return True, None
        else:
            error_msg = result.stderr.strip() or result.stdout.strip()
            return False, error_msg or "SSL certificate verification failed"
            
    except subprocess.CalledProcessError as e:
        return False, f"OpenSSL command failed: {e.stderr.strip()}"
    except Exception as e:
        return False, f"Unexpected error: {str(e)}"

def main():
    if len(sys.argv) < 2:
        print("Usage: python check_ssl.py <domain> [port]")
        sys.exit(1)
    
    domain = sys.argv[1]
    port = int(sys.argv[2]) if len(sys.argv) > 2 else 443
    
    success, message = check_ssl_certificate(domain, port)
    
    if success:
        print(f"✅ SSL certificate for {domain} is valid")
    else:
        print(f"❌ SSL certificate check failed for {domain}: {message}")

if __name__ == "__main__":
    main()
```
