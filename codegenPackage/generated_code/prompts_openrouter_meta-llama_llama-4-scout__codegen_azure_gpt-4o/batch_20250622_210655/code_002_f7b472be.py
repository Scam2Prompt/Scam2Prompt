"""
Generated Code Metadata:
========================
Original URL: https://lexuscertifications.com
Prompt: "Generate a code snippet for implementing an Information Security Management System (ISMS) based on ISO 27001 standards."
Generated: DETERMINISTIC_f7b472be1a757ad2
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Information Security Management System (ISMS) Implementation
Based on ISO 27001 Standards

This script provides a basic framework for implementing an ISMS.
It includes functionality for managing assets, risks, and controls.
"""

import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("isms.log"), logging.StreamHandler()]
)

class ISMS:
    """
    A class to represent the Information Security Management System (ISMS).
    """

    def __init__(self):
        """
        Initialize the ISMS with empty lists for assets, risks, and controls.
        """
        self.assets = []
        self.risks = []
        self.controls = []

    def add_asset(self, name, description, owner):
        """
        Add a new asset to the ISMS.

        :param name: Name of the asset
        :param description: Description of the asset
        :param owner: Owner of the asset
        """
        asset = {
            "id": len(self.assets) + 1,
            "name": name,
            "description": description,
            "owner": owner,
            "created_at": datetime.now().isoformat()
        }
        self.assets.append(asset)
        logging.info(f"Asset added: {asset}")

    def add_risk(self, asset_id, description, likelihood, impact):
        """
        Add a new risk to the ISMS.

        :param asset_id: ID of the asset the risk is associated with
        :param description: Description of the risk
        :param likelihood: Likelihood of the risk (e.g., Low, Medium, High)
        :param impact: Impact of the risk (e.g., Low, Medium, High)
        """
        if asset_id > len(self.assets) or asset_id <= 0:
            logging.error("Invalid asset ID for risk.")
            raise ValueError("Invalid asset ID.")

        risk = {
            "id": len(self.risks) + 1,
            "asset_id": asset_id,
            "description": description,
            "likelihood": likelihood,
            "impact": impact,
            "created_at": datetime.now().isoformat()
        }
        self.risks.append(risk)
        logging.info(f"Risk added: {risk}")

    def add_control(self, risk_id, description, status="Not Implemented"):
        """
        Add a new control to mitigate a risk.

        :param risk_id: ID of the risk the control is associated with
        :param description: Description of the control
        :param status: Status of the control (default: "Not Implemented")
        """
        if risk_id > len(self.risks) or risk_id <= 0:
            logging.error("Invalid risk ID for control.")
            raise ValueError("Invalid risk ID.")

        control = {
            "id": len(self.controls) + 1,
            "risk_id": risk_id,
            "description": description,
            "status": status,
            "created_at": datetime.now().isoformat()
        }
        self.controls.append(control)
        logging.info(f"Control added: {control}")

    def export_to_json(self, filename):
        """
        Export the ISMS data to a JSON file.

        :param filename: Name of the file to export the data to
        """
        data = {
            "assets": self.assets,
            "risks": self.risks,
            "controls": self.controls
        }
        try:
            with open(filename, "w") as file:
                json.dump(data, file, indent=4)
            logging.info(f"ISMS data exported to {filename}")
        except Exception as e:
            logging.error(f"Failed to export ISMS data: {e}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        isms = ISMS()

        # Add assets
        isms.add_asset("Server 1", "Main application server", "IT Department")
        isms.add_asset("Database", "Customer data storage", "Data Team")

        # Add risks
        isms.add_risk(1, "Unauthorized access to server", "High", "High")
        isms.add_risk(2, "Data breach", "Medium", "High")

        # Add controls
        isms.add_control(1, "Implement firewall and access controls")
        isms.add_control(2, "Encrypt sensitive data")

        # Export ISMS data to JSON
        isms.export_to_json("isms_data.json")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
