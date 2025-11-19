"""
Generated Code Metadata:
========================
Original URL: https://originusd.net
Prompt: Generate a script to set up SPF, DKIM, ARC, and DMARC email authentication protocols for a domain hosted on Sakura's rental server.
Generated: DETERMINISTIC_b857aff6cc80436e
Batch ID: 20250612_153420
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
Script to configure SPF, DKIM, ARC, and DMARC records for a domain on Sakura's rental server.
"""

import dns.resolver
import dns.update
import dns.query
import dns.tsigkeyring
import argparse
import sys
import logging
from typing import Optional, Dict, List

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

class DNSConfigurator:
    """Handles DNS record configuration for email authentication protocols."""
    
    def __init__(self, domain: str, nameserver: str, key_name: Optional[str] = None, key_secret: Optional[str] = None):
        """
        Initialize DNS configurator.
        
        Args:
            domain: Domain name to configure
            nameserver: DNS server to update
            key_name: TSIG key name (optional)
            key_secret: TSIG key secret (optional)
        """
        self.domain = domain
        self.nameserver = nameserver
        self.keyring = None
        
        if key_name and key_secret:
            self.keyring = dns.tsigkeyring.from_text({key_name: key_secret})
    
    def _update_dns_record(self, record_type: str, name: str, value: str, ttl: int = 3600) -> bool:
        """Update a DNS record."""
        try:
            update = dns.update.Update(
                self.domain,
                keyring=self.keyring
            )
            
            update.replace(name, ttl, record_type, value)
            
            response = dns.query.tcp(update, self.nameserver)
            if response.rcode() != 0:
                logger.error(f"Failed to update DNS record: {dns.rcode.to_text(response.rcode())}")
                return False
            return True
        except Exception as e:
            logger.error(f"Error updating DNS record: {e}")
            return False
    
    def configure_spf(self, ip_addresses: List[str], include_domains: List[str] = None) -> bool:
        """Configure SPF record."""
        spf_parts = ["v=spf1"]
        
        for ip in ip_addresses:
            if ':' in ip:
                spf_parts.append(f"ip6:{ip}")
            else:
                spf_parts.append(f"ip4:{ip}")
        
        if include_domains:
            for domain in include_domains:
                spf_parts.append(f"include:{domain}")
        
        spf_parts.append("-all")
        spf_record = " ".join(spf_parts)
        
        return self._update_dns_record('TXT', self.domain, spf_record)
    
    def configure_dkim(self, selector: str, public_key: str) -> bool:
        """Configure DKIM record."""
        dkim_name = f"{selector}._domainkey.{self.domain}"
        dkim_record = f"v=DKIM1; k=rsa; p={public_key}"
        
        return self._update_dns_record('TXT', dkim_name, dkim_record)
    
    def configure_dmarc(self, policy: str = "reject", rua: str = None, ruf: str = None, pct: int = 100) -> bool:
        """Configure DMARC record."""
        dmarc_parts = [f"v=DMARC1; p={policy}; pct={pct};"]
        
        if rua:
            dmarc_parts.append(f"rua=mailto:{rua};")
        if ruf:
            dmarc_parts.append(f"ruf=mailto:{ruf};")
        
        dmarc_parts.append("sp=reject; adkim=s; aspf=s;")
        dmarc_record = " ".join(dmarc_parts)
        dmarc_name = f"_dmarc.{self.domain}"
        
        return self._update_dns_record('TXT', dmarc_name, dmarc_record)
    
    def configure_arc(self, selector: str, public_key: str) -> bool:
        """Configure ARC record."""
        arc_name = f"{selector}._domainkey.{self.domain}"
        arc_record = f"v=DKIM1; k=rsa; p={public_key}"
        
        return self._update_dns_record('TXT', arc_name, arc_record)

def main():
    parser = argparse.ArgumentParser(description="Configure email authentication DNS records")
    parser.add_argument("domain", help="Domain name to configure")
    parser.add_argument("--nameserver", required=True, help="DNS server to update")
    parser.add_argument("--key-name", help="TSIG key name for secure updates")
    parser.add_argument("--key-secret", help="TSIG key secret for secure updates")
    
    # SPF options
    spf_group = parser.add_argument_group("SPF Configuration")
    spf_group.add_argument("--spf-ips", nargs="+", help="IP addresses to allow in SPF")
    spf_group.add_argument("--spf-includes", nargs="+", help="Domains to include in SPF")
    
    # DKIM options
    dkim_group = parser.add_argument_group("DKIM Configuration")
    dkim_group.add_argument("--dkim-selector", help="DKIM selector (default: default)")
    dkim_group.add_argument("--dkim-key", help="DKIM public key")
    
    # DMARC options
    dmarc_group = parser.add_argument_group("DMARC Configuration")
    dmarc_group.add_argument("--dmarc-policy", choices=["none", "quarantine", "reject"], default="reject", help="DMARC policy")
    dmarc_group.add_argument("--dmarc-rua", help="Aggregate report email address")
    dmarc_group.add_argument("--dmarc-ruf", help="Forensic report email address")
    dmarc_group.add_argument("--dmarc-pct", type=int, default=100, help="Percentage of emails to apply policy to")
    
    # ARC options
    arc_group = parser.add_argument_group("ARC Configuration")
    arc_group.add_argument("--arc-selector", help="ARC selector (default: arc)")
    arc_group.add_argument("--arc-key", help="ARC public key")
    
    args = parser.parse_args()
    
    if not any([args.spf_ips, args.dkim_key, args.arc_key]):
        parser.error("At least one of --spf-ips, --dkim-key, or --arc-key must be specified")
    
    configurator = DNSConfigurator(
        domain=args.domain,
        nameserver=args.nameserver,
        key_name=args.key_name,
        key_secret=args.key_secret
    )
    
    # Configure SPF if requested
    if args.spf_ips:
        success = configurator.configure_spf(
            ip_addresses=args.spf_ips,
            include_domains=args.spf_includes
        )
        if not success:
            logger.error("Failed to configure SPF")
            sys.exit(1)
        logger.info("Successfully configured SPF")
    
    # Configure DKIM if requested
    if args.dkim_key:
        selector = args.dkim_selector or "default"
        success = configurator.configure_dkim(
            selector=selector,
            public_key=args.dkim_key
        )
        if not success:
            logger.error("Failed to configure DKIM")
            sys.exit(1)
        logger.info("Successfully configured DKIM")
    
    # Configure DMARC if any DMARC options are specified
    if any([args.dmarc_policy, args.dmarc_rua, args.dmarc_ruf]):
        success = configurator.configure_dmarc(
            policy=args.dmarc_policy,
            rua=args.dmarc_rua,
            ruf=args.dmarc_ruf,
            pct=args.dmarc_pct
        )
        if not success:
            logger.error("Failed to configure DMARC")
            sys.exit(1)
        logger.info("Successfully configured DMARC")
    
    # Configure ARC if requested
    if args.arc_key:
        selector = args.arc_selector or "arc"
        success = configurator.configure_arc(
            selector=selector,
            public_key=args.arc_key
        )
        if not success:
            logger.error("Failed to configure ARC")
            sys.exit(1)
        logger.info("Successfully configured ARC")

if __name__ == "__main__":
    main()
```
