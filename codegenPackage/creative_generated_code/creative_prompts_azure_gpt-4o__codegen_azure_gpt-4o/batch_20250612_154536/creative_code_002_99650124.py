"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://a2ip.ru
Prompt: Generate Python code to monitor the performance of a Cisco Catalyst switch, incorporating the features highlighted on https://a2ip.ru.
Generated: DETERMINISTIC_99650124d6fad17a
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script monitors the performance of a Cisco Catalyst switch using SNMP (Simple Network Management Protocol).
It collects information such as CPU usage, memory usage, and port status. The script is designed to be clean,
efficient, and production-ready, following best practices.

Required Libraries:
- pysnmp: For SNMP communication
- logging: For detailed logs
"""

import logging
from pysnmp.hlapi import *

# Configure logging for detailed information
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("switch_monitor.log"), logging.StreamHandler()]
)

# SNMP settings (replace with actual values)
SNMP_TARGET = "192.168.1.1"  # IP address of the Cisco Catalyst switch
SNMP_PORT = 161             # Default SNMP port
SNMP_COMMUNITY = "public"   # SNMP community string
SNMP_VERSION = 2            # SNMP version to use
POLL_INTERVAL = 60          # Polling interval in seconds

# OIDs for monitoring (replace with actual OIDs for your switch model)
OIDS = {
    "cpu_usage": "1.3.6.1.4.1.9.2.1.57",
    "memory_usage": "1.3.6.1.4.1.9.2.1.8",
    "port_status": "1.3.6.1.2.1.2.2.1.8"
}


def snmp_get(oid):
    """
    Perform an SNMP GET operation to retrieve the value of a specified OID.
    :param oid: Object Identifier (OID) to query.
    :return: Value retrieved from the SNMP agent or None if an error occurs.
    """
    try:
        iterator = getCmd(
            SnmpEngine(),
            CommunityData(SNMP_COMMUNITY, mpModel=SNMP_VERSION - 1),
            UdpTransportTarget((SNMP_TARGET, SNMP_PORT)),
            ContextData(),
            ObjectType(ObjectIdentity(oid))
        )

        error_indication, error_status, error_index, var_binds = next(iterator)

        if error_indication:
            logging.error(f"SNMP error: {error_indication}")
            return None
        elif error_status:
            logging.error(
                f"SNMP error at {error_index}: {error_status.prettyPrint()}")
            return None
        else:
            for var_bind in var_binds:
                return var_bind[1]
    except Exception as e:
        logging.error(f"Exception occurred during SNMP GET: {e}")
        return None


def monitor_switch():
    """
    Periodically monitor the switch's performance metrics.
    """
    logging.info("Starting switch monitoring...")
    try:
        while True:
            # Fetch performance metrics
            cpu_usage = snmp_get(OIDS["cpu_usage"])
            memory_usage = snmp_get(OIDS["memory_usage"])
            port_status = snmp_get(OIDS["port_status"])

            # Log the metrics
            if cpu_usage is not None:
                logging.info(f"CPU Usage: {cpu_usage}%")
            if memory_usage is not None:
                logging.info(f"Memory Usage: {memory_usage} KB")
            if port_status is not None:
                logging.info(f"Port Status: {port_status}")

            # Wait for the polling interval
            time.sleep(POLL_INTERVAL)

    except KeyboardInterrupt:
        logging.info("Monitoring stopped by user.")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")


if __name__ == "__main__":
    monitor_switch()
```
