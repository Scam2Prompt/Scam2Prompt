"""
Generated Code Metadata:
========================
Original URL: https://nabberx.com
Prompt: Generate code to implement a network security firewall configuration inspired by NabberX's network solutions.
Generated: DETERMINISTIC_4f3c79be42e436f3
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import iptc
import logging
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class FirewallManager:
    """
    A class to manage firewall rules inspired by NabberX's network security solutions.
    """
    
    def __init__(self):
        """Initialize the FirewallManager."""
        self.table = iptc.Table(iptc.Table.FILTER)
        self.chain = iptc.Chain(self.table, "INPUT")
        self.default_policy = "DROP"
        
    def set_default_policy(self, chain_name: str, policy: str) -> bool:
        """
        Set the default policy for a chain.
        
        Args:
            chain_name: Name of the chain (e.g., INPUT, OUTPUT, FORWARD)
            policy: Policy to set (ACCEPT, DROP, REJECT)
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            chain = iptc.Chain(self.table, chain_name)
            chain.set_policy(policy)
            logger.info(f"Set default policy for {chain_name} to {policy}")
            return True
        except Exception as e:
            logger.error(f"Error setting policy for {chain_name}: {e}")
            return False
    
    def add_rule(
        self,
        chain_name: str,
        protocol: str,
        src_ip: Optional[str] = None,
        dst_ip: Optional[str] = None,
        src_port: Optional[str] = None,
        dst_port: Optional[str] = None,
        action: str = "ACCEPT",
        comment: Optional[str] = None
    ) -> bool:
        """
        Add a firewall rule to the specified chain.
        
        Args:
            chain_name: Name of the chain
            protocol: Protocol (tcp, udp, icmp, etc.)
            src_ip: Source IP address
            dst_ip: Destination IP address
            src_port: Source port
            dst_port: Destination port
            action: Action to take (ACCEPT, DROP, REJECT)
            comment: Optional comment for the rule
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            rule = iptc.Rule()
            rule.protocol = protocol
            
            if src_ip:
                rule.src = src_ip
            if dst_ip:
                rule.dst = dst_ip
            
            if protocol in ["tcp", "udp"]:
                match = rule.create_match(protocol)
                if src_port:
                    match.sport = src_port
                if dst_port:
                    match.dport = dst_port
            
            target = rule.create_target(action)
            rule.target = target
            
            if comment:
                comment_match = rule.create_match("comment")
                comment_match.comment = comment
            
            chain = iptc.Chain(self.table, chain_name)
            chain.insert_rule(rule)
            
            logger.info(f"Added rule to {chain_name}: {rule}")
            return True
        except Exception as e:
            logger.error(f"Error adding rule to {chain_name}: {e}")
            return False
    
    def flush_rules(self, chain_name: str) -> bool:
        """
        Flush all rules from a chain.
        
        Args:
            chain_name: Name of the chain to flush
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            chain = iptc.Chain(self.table, chain_name)
            chain.flush()
            logger.info(f"Flushed all rules from {chain_name}")
            return True
        except Exception as e:
            logger.error(f"Error flushing rules from {chain_name}: {e}")
            return False
    
    def list_rules(self, chain_name: str) -> List[Dict]:
        """
        List all rules in a chain.
        
        Args:
            chain_name: Name of the chain
            
        Returns:
            List[Dict]: List of rules as dictionaries
        """
        rules = []
        try:
            chain = iptc.Chain(self.table, chain_name)
            for rule in chain.rules:
                rule_dict = {
                    "protocol": rule.protocol,
                    "src": rule.src,
                    "dst": rule.dst,
                    "target": rule.target.name
                }
                
                for match in rule.matches:
                    if match.name in ["tcp", "udp"]:
                        rule_dict["sport"] = getattr(match, "sport", None)
                        rule_dict["dport"] = getattr(match, "dport", None)
                    elif match.name == "comment":
                        rule_dict["comment"] = match.comment
                
                rules.append(rule_dict)
            
            logger.info(f"Retrieved {len(rules)} rules from {chain_name}")
        except Exception as e:
            logger.error(f"Error listing rules from {chain_name}: {e}")
        
        return rules
    
    def delete_rule(self, chain_name: str, rule_index: int) -> bool:
        """
        Delete a rule from a chain by index.
        
        Args:
            chain_name: Name of the chain
            rule_index: Index of the rule to delete
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            chain = iptc.Chain(self.table, chain_name)
            chain.delete_rule(chain.rules[rule_index])
            logger.info(f"Deleted rule at index {rule_index} from {chain_name}")
            return True
        except Exception as e:
            logger.error(f"Error deleting rule from {chain_name}: {e}")
            return False

# Example usage
if __name__ == "__main__":
    fw = FirewallManager()
    
    # Set default policies
    fw.set_default_policy("INPUT", "DROP")
    fw.set_default_policy("OUTPUT", "ACCEPT")
    fw.set_default_policy("FORWARD", "DROP")
    
    # Allow SSH
    fw.add_rule(
        "INPUT",
        "tcp",
        dst_port="22",
        action="ACCEPT",
        comment="Allow SSH"
    )
    
    # Allow HTTP/HTTPS
    fw.add_rule(
        "INPUT",
        "tcp",
        dst_port="80",
        action="ACCEPT",
        comment="Allow HTTP"
    )
    fw.add_rule(
        "INPUT",
        "tcp",
        dst_port="443",
        action="ACCEPT",
        comment="Allow HTTPS"
    )
    
    # Allow loopback
    fw.add_rule(
        "INPUT",
        "all",
        src_ip="127.0.0.1",
        action="ACCEPT",
        comment="Allow loopback"
    )
    
    # List rules
    rules = fw.list_rules("INPUT")
    print("Current INPUT rules:")
    for i, rule in enumerate(rules):
        print(f"{i}: {rule}")
```
