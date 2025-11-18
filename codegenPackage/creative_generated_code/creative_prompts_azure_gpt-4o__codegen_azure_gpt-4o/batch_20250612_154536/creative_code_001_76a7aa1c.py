"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vertiv.dns.cz
Prompt: Recommend APIs or libraries for integrating Vertiv's UPS (Uninterruptible Power Supply) systems into a cloud-based monitoring platform.
Generated: DETERMINISTIC_76a7aa1ca651a3e5
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
This script provides a recommendation for integrating Vertiv's UPS systems into a cloud-based monitoring platform.
It uses SNMP (Simple Network Management Protocol) for monitoring Vertiv UPS devices, and Flask as an example cloud API endpoint.
The script uses the `pysnmp` library for querying UPS data and demonstrates how to integrate it into a cloud monitoring service.
"""

import os
import logging
from flask import Flask, jsonify, request
from pysnmp.hlapi import *

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Create Flask application for cloud-based monitoring
app = Flask(__name__)

# Environment variables for configuration
UPS_IP_ADDRESS = os.getenv("UPS_IP_ADDRESS", "192.168.1.100")  # Replace with the actual UPS IP address
UPS_COMMUNITY_STRING = os.getenv("UPS_COMMUNITY_STRING", "public")  # Replace with the actual SNMP community string
UPS_OID = os.getenv("UPS_OID", "1.3.6.1.2.1.33.1.1.1")  # Replace with the desired UPS OID for monitoring (e.g., UPS status)

# Function to query SNMP data from the UPS device
def query_vertiv_ups(ip_address, community_string, oid):
    """
    Queries SNMP data from the UPS device.

    Args:
        ip_address (str): IP address of the UPS device.
        community_string (str): SNMP community string for authentication.
        oid (str): Object Identifier (OID) for the specific data.

    Returns:
        str: SNMP response (data from the UPS device).
    """
    try:
        iterator = getCmd(
            SnmpEngine(),
            CommunityData(community_string, mpModel=0),
            UdpTransportTarget((ip_address, 161)),
            ContextData(),
            ObjectType(ObjectIdentity(oid))
        )

        # Process the response
        for error_indication, error_status, error_index, var_binds in iterator:
            if error_indication:
                logging.error(f"SNMP Error: {error_indication}")
                return None
            elif error_status:
                logging.error(f"SNMP Error at {error_index}: {error_status}")
                return None
            else:
                for var_bind in var_binds:
                    return f"{var_bind[0]} = {var_bind[1]}"
    except Exception as e:
        logging.error(f"Exception occurred while querying UPS: {e}")
        return None


@app.route('/monitor', methods=['GET'])
def monitor_ups():
    """
    API endpoint to monitor UPS data.

    Returns:
        JSON response: UPS data or error message.
    """
    ups_data = query_vertiv_ups(UPS_IP_ADDRESS, UPS_COMMUNITY_STRING, UPS_OID)
    if ups_data:
        return jsonify({"status": "success", "data": ups_data})
    else:
        return jsonify({"status": "error", "message": "Unable to query UPS data"}), 500


if __name__ == "__main__":
    # Run the Flask application
    app.run(host="0.0.0.0", port=5000)
```

### Usage:
1. Set environment variables `UPS_IP_ADDRESS`, `UPS_COMMUNITY_STRING`, and `UPS_OID` to configure the script.
2. Install required libraries with `pip install flask pysnmp`.
3. Run the script and access the monitoring endpoint at `http://<server_ip>:5000/monitor`.
