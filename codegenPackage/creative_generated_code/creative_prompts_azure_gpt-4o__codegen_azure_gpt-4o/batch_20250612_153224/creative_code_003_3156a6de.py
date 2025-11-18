"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arpgroupcorp.com
Prompt: Write code to implement firewall management and intrusion detection for network security, inspired by ARP Group Corporation's cybersecurity services.
Generated: DETERMINISTIC_3156a6de9c0e692b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
import os
import socket
from scapy.all import ARP, sniff

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("firewall_intrusion.log"),
        logging.StreamHandler()
    ]
)

# Firewall rules storage
FIREWALL_RULES = {
    "allow": set(),  # Set of allowed IPs
    "block": set()   # Set of blocked IPs
}

def add_firewall_rule(ip_address: str, rule_type: str) -> None:
    """
    Adds a firewall rule for a specific IP address.

    Args:
        ip_address (str): The IP address to add to the rules.
        rule_type (str): Type of rule ('allow' or 'block').

    Raises:
        ValueError: If the rule type is invalid.
    """
    if rule_type not in ["allow", "block"]:
        raise ValueError("Invalid rule type. Must be 'allow' or 'block'.")
    
    FIREWALL_RULES[rule_type].add(ip_address)
    logging.info(f"Firewall rule added: {rule_type} {ip_address}")

def check_firewall(ip_address: str) -> str:
    """
    Checks an IP address against firewall rules.

    Args:
        ip_address (str): The IP address to check.

    Returns:
        str: 'allow' if allowed, 'block' if blocked, 'neutral' otherwise.
    """
    if ip_address in FIREWALL_RULES["block"]:
        return "block"
    elif ip_address in FIREWALL_RULES["allow"]:
        return "allow"
    return "neutral"

def detect_arp_spoof(packet) -> None:
    """
    Detects ARP spoofing by analyzing packets.

    Args:
        packet: A scapy packet object.
    """
    if ARP in packet and packet[ARP].op in (1, 2):  # ARP request (op=1) or reply (op=2)
        real_mac = os.popen(f"arp -n {packet[ARP].psrc}").read().strip()
        packet_mac = packet[ARP].hwsrc
        
        if real_mac and real_mac != packet_mac:
            logging.warning(f"Potential ARP spoofing detected from {packet[ARP].psrc} with MAC {packet_mac}")
        else:
            logging.info(f"ARP packet from {packet[ARP].psrc} verified.")

def packet_handler(packet) -> None:
    """
    Handles incoming packets for firewall and intrusion detection.

    Args:
        packet: A scapy packet object.
    """
    if packet.haslayer("IP"):
        source_ip = packet["IP"].src
        
        rule = check_firewall(source_ip)
        if rule == "block":
            logging.warning(f"Blocked packet from {source_ip}")
            return
        elif rule == "allow":
            logging.info(f"Allowed packet from {source_ip}")
        
    detect_arp_spoof(packet)

def start_firewall_monitoring(interface: str) -> None:
    """
    Starts monitoring network traffic for firewall and intrusion detection.

    Args:
        interface (str): Network interface to monitor.
    """
    try:
        logging.info(f"Starting firewall and intrusion detection on interface {interface}")
        sniff(iface=interface, prn=packet_handler, store=False)
    except Exception as e:
        logging.error(f"Error starting monitoring: {e}")

if __name__ == "__main__":
    # Example usage
    add_firewall_rule("192.168.1.100", "allow")
    add_firewall_rule("192.168.1.200", "block")
    
    # Replace 'eth0' with the name of your network interface
    start_firewall_monitoring("eth0")
```
