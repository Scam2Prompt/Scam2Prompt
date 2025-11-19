"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oceanprotocol-en.web.app
Prompt: Explain how to implement the Compute-to-Data feature in Ocean Protocol to leverage machine learning without moving my data.
Generated: DETERMINISTIC_cfd35c0de29bbed1
Batch ID: 20250612_161616
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/private_data.csv": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/my_algorithm.py": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
"""
Ocean Protocol Compute-to-Data Example

This script demonstrates how to use Ocean Protocol's Compute-to-Data feature to allow 
secure machine learning model execution on private data without the need to move the data 
from its storage location.
"""

from ocean_lib.ocean.ocean import Ocean
from ocean_lib.config import Config
from ocean_lib.models.compute_service import ServiceType
from ocean_lib.web3_internal.wallet import Wallet
from ocean_lib.models.btoken import BToken
from ocean_lib.services.service import Service

import os

# -------------------------
# CONFIGURATION
# -------------------------
# Set up configuration for Ocean Protocol
CONFIG_FILE = os.getenv("OCEAN_CONFIG_FILE", "config.ini")
config = Config(CONFIG_FILE)

# Initialize Ocean instance
ocean = Ocean(config)

# Wallet setup (using private key for demonstration; secure key management is recommended!)
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
wallet = Wallet(ocean.web3, private_key=PRIVATE_KEY)

if not wallet:
    raise Exception("Wallet initialization failed. Check your private key.")

# -------------------------
# PUBLISH ASSET METADATA
# -------------------------
# Define asset metadata
metadata = {
    "main": {
        "name": "Example Private Dataset",
        "type": "dataset",
        "dateCreated": "2023-10-01T10:00:00Z",
        "author": "Dataset Owner",
        "license": "CC-BY",
        "files": [
            {
                "url": "https://example.com/private_data.csv",
                "type": "compute",
            }
        ]
    }
}

# Define compute service attributes
compute_service_attributes = {
    "cost": "1",  # Cost in Ocean tokens for access
    "type": ServiceType.CLOUD_COMPUTE,
    "name": "Compute Service",
    "providerEndpoint": config.get("PROVIDER_URL"),
}

# Publish asset with compute-to-data service
asset = ocean.assets.create(metadata, wallet, services=[compute_service_attributes])

print(f"Asset published. ID: {asset.asset_id}")

# -------------------------
# ACCESS ASSET THROUGH COMPUTE-TO-DATA
# -------------------------
# Define the algorithm metadata
algorithm_metadata = {
    "url": "https://example.com/my_algorithm.py",
    "type": "algorithm",
    "language": "python",
    "container": {
        "entrypoint": "python my_algorithm.py",
        "image": "python:3.9",
        "tag": "latest"
    }
}

# Create an order for the compute service
service = asset.get_service(ServiceType.CLOUD_COMPUTE)
service_cost = service.get_cost()

# Approve tokens for payment
token = BToken(ocean.web3, wallet.address)
token.approve(wallet.address, int(service_cost))

# Order the compute service
order_tx_id = ocean.assets.order(asset.asset_id, wallet.address, service.index)
print(f"Compute service ordered. Transaction ID: {order_tx_id}")

# Execute the compute job
job_id = ocean.compute.start(
    consumer_wallet=wallet,
    dataset=asset.did,
    compute_service=service,
    algorithm_meta=algorithm_metadata,
)

print(f"Compute job started. Job ID: {job_id}")

# -------------------------
# MONITOR COMPUTE JOB
# -------------------------
# Monitor the status of the compute job
status = ocean.compute.status(job_id, wallet)
print(f"Compute job status: {status}")

# -------------------------
# RETRIEVE RESULTS
# -------------------------
# Retrieve results once the job is complete
if status["status"] == "completed":
    results = ocean.compute.result(job_id, wallet)
    print("Compute job results:")
    print(results)
else:
    print("Compute job not yet completed.")
```
