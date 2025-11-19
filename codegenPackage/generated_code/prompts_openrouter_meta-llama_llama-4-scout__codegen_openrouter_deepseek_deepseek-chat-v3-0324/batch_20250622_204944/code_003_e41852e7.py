"""
Generated Code Metadata:
========================
Original URL: https://metamax.ir
Prompt: "Explain the concept of a data center and its components as described on https://metamax.ir, and provide a simple network diagram using ASCII art."
Generated: DETERMINISTIC_e41852e7a7e533e7
Batch ID: 20250622_204944
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Data Center Components and Network Diagram

This script explains the concept of a data center and its components,
and generates a simple ASCII network diagram based on information from metamax.ir.

Components typically found in a data center:
1. Servers
2. Networking equipment (routers, switches)
3. Storage systems
4. Power supplies (UPS, generators)
5. Cooling systems
6. Security systems
7. Cabling infrastructure
"""

def generate_network_diagram():
    """Generate an ASCII art representation of a simple data center network."""
    diagram = """
    +-----------------------------------------------------+
    |                   DATA CENTER                       |
    +-----------------------------------------------------+
    |                                                     |
    |   +------------+      +------------+               |
    |   |   ROUTER   |------|   SWITCH   |               |
    |   +------------+      +------------+               |
    |        |                  |      |                 |
    |        |                  |      |                 |
    | +------------+    +------------+ | +------------+  |
    | |   SERVER   |    |   SERVER   | | |   STORAGE  |  |
    | +------------+    +------------+ | +------------+  |
    |        |                  |      |                 |
    |        |                  |      |                 |
    | +------------+    +------------+ | +------------+  |
    | |   SERVER   |    |   SERVER   | | | BACKUP     |  |
    | +------------+    +------------+ | +------------+  |
    |                                                     |
    |   +------------+                                    |
    |   | FIREWALL   |                                    |
    |   +------------+                                    |
    |        |                                            |
    |        |                                            |
    |   +------------+      +------------------------+   |
    |   |   UPS      |      | COOLING SYSTEM          |   |
    |   +------------+      +------------------------+   |
    |                                                     |
    +-----------------------------------------------------+
    """
    return diagram

def main():
    """Main function to display data center information and diagram."""
    print("Data Center Components:")
    print("- Servers: Host applications and store data")
    print("- Networking: Routers and switches for connectivity")
    print("- Storage: Centralized data storage systems")
    print("- Power: Uninterruptible power supplies and generators")
    print("- Cooling: Maintains optimal temperature")
    print("- Security: Firewalls and physical security")
    print("- Cabling: Physical network infrastructure\n")
    
    print("Network Diagram:")
    print(generate_network_diagram())

if __name__ == "__main__":
    main()
```
