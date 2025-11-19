"""
Generated Code Metadata:
========================
Original URL: https://iplis.ru
Prompt: Create a function that generates random IP addresses for testing purposes, similar to the Random IP generator feature on IP Logger.
Generated: DETERMINISTIC_3220c2ff9c4f6344
Batch ID: 20250612_163826
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import ipaddress
from typing import List, Optional, Union

def generate_random_ip(
    count: int = 1,
    ip_version: int = 4,
    public_only: bool = True,
    network: Optional[str] = None
) -> Union[str, List[str]]:
    """
    Generates random IP addresses for testing purposes.

    Args:
        count: Number of IP addresses to generate. Defaults to 1.
        ip_version: IP version (4 or 6). Defaults to 4.
        public_only: Whether to generate only public IPs. Defaults to True.
        network: Generate IPs within a specific network (CIDR notation). 
                If None, generates from entire address space. Defaults to None.

    Returns:
        Single IP string if count=1, otherwise list of IP strings.

    Raises:
        ValueError: If invalid parameters are provided.
    """
    if ip_version not in (4, 6):
        raise ValueError("ip_version must be 4 or 6")
    
    if count < 1:
        raise ValueError("count must be at least 1")
    
    if network is not None:
        try:
            network_obj = ipaddress.ip_network(network)
            if network_obj.version != ip_version:
                raise ValueError(f"Network version doesn't match requested IP version {ip_version}")
        except ValueError as e:
            raise ValueError(f"Invalid network: {e}")

    results = []
    for _ in range(count):
        while True:
            if network:
                # Generate within specified network
                ip = str(network_obj[random.randint(0, network_obj.num_addresses - 1)])
            else:
                # Generate random IP
                if ip_version == 4:
                    ip = ".".join(str(random.randint(0, 255)) for _ in range(4))
                else:
                    ip = ":".join(f"{random.randint(0, 65535):x}" for _ in range(8))
            
            ip_obj = ipaddress.ip_address(ip)
            
            # Check public-only constraint if needed
            if not public_only or (public_only and ip_obj.is_global):
                results.append(ip)
                break
    
    return results[0] if count == 1 else results
```
