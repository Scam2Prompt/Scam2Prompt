"""
Generated Code Metadata:
========================
Original URL: https://imts.com.pk
Prompt: "Create a script to monitor and manage IT infrastructure, including routers, switches, firewalls, and VPNs, using Python and SNMP."
Generated: DETERMINISTIC_6f3c3b3e5dffacf3
Batch ID: 20250622_211620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# it_infrastructure_monitor.py

import argparse
import logging
import snmpy
from snmpy import SnmpEngine, CommunityData, UdpTransportTarget, ContextData, ObjectType, ObjectIdentity

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define a function to get device information
def get_device_info(ip, community_string):
    try:
        # Create an SNMP engine
        snmp_engine = SnmpEngine()

        # Create a community data object
        community_data = CommunityData(community_string, mpModel=0)

        # Create a UDP transport target
        udp_transport_target = UdpTransportTarget((ip, 161))

        # Create a context data object
        context_data = ContextData()

        # Get the system description
        sys_desc_oid = ObjectIdentity('.1.3.6.1.2.1.1.1.0')
        sys_desc = ObjectType(sys_desc_oid)

        # Get the system uptime
        sys_uptime_oid = ObjectIdentity('.1.3.6.1.2.1.1.3.0')
        sys_uptime = ObjectType(sys_uptime_oid)

        # Get the device information
        result = snmp_engine.get(community_data, udp_transport_target, context_data, [sys_desc, sys_uptime])

        # Extract the device information
        device_info = {
            'sys_desc': result[0].prettyPrint(),
            'sys_uptime': result[1].prettyPrint(),
        }

        return device_info

    except Exception as e:
        logging.error(f"Failed to retrieve device information: {str(e)}")
        return None

# Define a function to get interface information
def get_interface_info(ip, community_string):
    try:
        # Create an SNMP engine
        snmp_engine = SnmpEngine()

        # Create a community data object
        community_data = CommunityData(community_string, mpModel=0)

        # Create a UDP transport target
        udp_transport_target = UdpTransportTarget((ip, 161))

        # Create a context data object
        context_data = ContextData()

        # Get the interface table
        if_table_oid = ObjectIdentity('.1.3.6.1.2.1.2.2')
        if_table = ObjectType(if_table_oid)

        # Get the interface information
        result = snmp_engine.get(community_data, udp_transport_target, context_data, [if_table])

        # Extract the interface information
        interface_info = []
        for row in result[0].getTableRows():
            interface = {
                'if_index': row[0].prettyPrint(),
                'if_descr': row[1].prettyPrint(),
                'if_type': row[2].prettyPrint(),
                'if_mtu': row[3].prettyPrint(),
                'if_speed': row[4].prettyPrint(),
                'if_phys_address': row[5].prettyPrint(),
                'if_admin_status': row[6].prettyPrint(),
                'if_oper_status': row[7].prettyPrint(),
            }
            interface_info.append(interface)

        return interface_info

    except Exception as e:
        logging.error(f"Failed to retrieve interface information: {str(e)}")
        return None

# Define a function to monitor device
def monitor_device(ip, community_string):
    device_info = get_device_info(ip, community_string)
    interface_info = get_interface_info(ip, community_string)

    if device_info:
        logging.info(f"Device Information for {ip}:")
        logging.info(f"  System Description: {device_info['sys_desc']}")
        logging.info(f"  System Uptime: {device_info['sys_uptime']}")

    if interface_info:
        logging.info(f"Interface Information for {ip}:")
        for interface in interface_info:
            logging.info(f"  Interface {interface['if_index']}:")
            logging.info(f"    Description: {interface['if_descr']}")
            logging.info(f"    Type: {interface['if_type']}")
            logging.info(f"    MTU: {interface['if_mtu']}")
            logging.info(f"    Speed: {interface['if_speed']}")
            logging.info(f"    Physical Address: {interface['if_phys_address']}")
            logging.info(f"    Admin Status: {interface['if_admin_status']}")
            logging.info(f"    Oper Status: {interface['if_oper_status']}")

# Main function
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='IT Infrastructure Monitor')
    parser.add_argument('-i', '--ip', required=True, help='IP address of the device')
    parser.add_argument('-c', '--community_string', required=True, help='SNMP community string')
    args = parser.parse_args()

    monitor_device(args.ip, args.community_string)
```

To run the script, save it to a file (e.g., `it_infrastructure_monitor.py`), then execute it using Python (e.g., `python it_infrastructure_monitor.py -i <ip_address> -c <community_string>`). 

Replace `<ip_address>` with the IP address of the device you want to monitor and `<community_string>` with the SNMP community string. 

The script uses SNMP to retrieve device and interface information, then logs the results at the INFO level. 

Make sure to install the `pysnmp` library before running the script. You can install it using pip:

```bash
pip install pysnmp
```
