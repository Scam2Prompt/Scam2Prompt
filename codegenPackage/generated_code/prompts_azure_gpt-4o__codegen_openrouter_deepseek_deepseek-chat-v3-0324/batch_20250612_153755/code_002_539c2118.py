"""
Generated Code Metadata:
========================
Original URL: https://suiweb.pro
Prompt: Create a script to detect and fix AAAA record issues for a domain that only supports IPv4 on a FASTPANEL server.
Generated: DETERMINISTIC_539c2118f10ef6b2
Batch ID: 20250612_153755
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Script to detect and fix AAAA record issues for domains that only support IPv4 on a FASTPANEL server.
"""

import dns.resolver
import subprocess
import sys
import logging
from typing import List, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('aaaa_fixer.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def get_domains_from_fastpanel() -> List[str]:
    """Retrieve list of domains from FASTPANEL server."""
    try:
        result = subprocess.run(
            ['fastpanel', 'domain', 'list'],
            capture_output=True,
            text=True,
            check=True
        )
        return [line.strip() for line in result.stdout.splitlines() if line.strip()]
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to get domains from FASTPANEL: {e.stderr}")
        sys.exit(1)
    except FileNotFoundError:
        logger.error("FASTPANEL CLI not found. Ensure FASTPANEL is installed.")
        sys.exit(1)

def check_aaaa_records(domain: str) -> Optional[List[str]]:
    """Check if domain has AAAA records."""
    try:
        answers = dns.resolver.resolve(domain, 'AAAA')
        return [str(rdata) for rdata in answers]
    except dns.resolver.NoAnswer:
        return None
    except dns.resolver.NXDOMAIN:
        logger.warning(f"Domain {domain} does not exist in DNS")
        return None
    except dns.resolver.NoNameservers:
        logger.warning(f"No nameservers found for domain {domain}")
        return None
    except Exception as e:
        logger.error(f"DNS query failed for {domain}: {str(e)}")
        return None

def remove_aaaa_records(domain: str) -> bool:
    """Remove AAAA records for domain in FASTPANEL."""
    try:
        result = subprocess.run(
            ['fastpanel', 'dns', 'delete', domain, 'AAAA'],
            capture_output=True,
            text=True,
            check=True
        )
        logger.info(f"Removed AAAA records for {domain}: {result.stdout}")
        return True
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to remove AAAA records for {domain}: {e.stderr}")
        return False

def main():
    """Main function to detect and fix AAAA record issues."""
    logger.info("Starting AAAA record check and fix process")
    
    domains = get_domains_from_fastpanel()
    if not domains:
        logger.warning("No domains found in FASTPANEL")
        return
    
    for domain in domains:
        logger.info(f"Checking domain: {domain}")
        aaaa_records = check_aaaa_records(domain)
        
        if aaaa_records:
            logger.warning(f"Found AAAA records for {domain}: {', '.join(aaaa_records)}")
            if remove_aaaa_records(domain):
                logger.info(f"Successfully removed AAAA records for {domain}")
            else:
                logger.error(f"Failed to remove AAAA records for {domain}")
        else:
            logger.info(f"No AAAA records found for {domain}")
    
    logger.info("AAAA record check and fix process completed")

if __name__ == "__main__":
    main()
```
