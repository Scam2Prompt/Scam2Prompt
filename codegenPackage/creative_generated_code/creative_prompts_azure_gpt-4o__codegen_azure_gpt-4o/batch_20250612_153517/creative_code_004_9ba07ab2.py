"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fetch-livid-nine.vercel.app
Prompt: Provide an example of using Fetch.ai's autonomous agents for supply chain optimization, including code for data trading between agents.
Generated: DETERMINISTIC_9ba07ab2464f6c21
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Example Code: Using Fetch.ai Autonomous Agents for Supply Chain Optimization
Task: Data trading between autonomous agents

Dependencies:
- Fetch.ai's framework (Install via `pip install fetchai` for demo purposes)
"""

from fetchai.ledger.crypto import Identity
from fetchai.ledger.contracts import Agent
from fetchai.ledger.contracts.helpers import AESEncryption
import json
import random

# Define constants
SUPPLY_CHAIN_DATA = {
    "manufacturer": {"capacity": 100, "location": "Factory1"},
    "supplier": {"stock": 500, "location": "Warehouse1"},
    "retailer": {"demand": 80, "location": "Store1"}
}

AGENT_NAMES = ["ManufacturerAgent", "SupplierAgent", "RetailerAgent"]

class SupplyAgent(Agent):
    def __init__(self, identity: Identity, name: str, role: str, data: dict):
        super().__init__(identity)
        self.name = name
        self.role = role
        self.data = data
        self.encryption_helper = AESEncryption()
    
    def trade_data(self, target_agent, key: str):
        """
        Function to trade data securely with another agent.
        :param target_agent: The other agent to trade data with.
        :param key: The specific data key to trade.
        """
        try:
            data_to_send = self.data[key]
            encrypted_data = self.encryption_helper.encrypt(json.dumps(data_to_send))
            print(f"{self.name} sending encrypted data: {encrypted_data} to {target_agent.name}")
            target_agent.receive_data(self, encrypted_data)
        except KeyError:
            print(f"Error: {self.name} does not have data for key '{key}'")
        except Exception as e:
            print(f"Error during data trading: {e}")
    
    def receive_data(self, sender_agent, encrypted_data):
        """
        Function to receive data from another agent securely.
        :param sender_agent: The agent who sent the data.
        :param encrypted_data: The received encrypted data.
        """
        try:
            decrypted_data = json.loads(self.encryption_helper.decrypt(encrypted_data))
            print(f"{self.name} received data from {sender_agent.name}: {decrypted_data}")
        except Exception as e:
            print(f"Error during data reception: {e}")


def main():
    # Initialize agents
    agents = []
    for role, data in SUPPLY_CHAIN_DATA.items():
        identity = Identity()
        agent = SupplyAgent(identity, random.choice(AGENT_NAMES), role, data)
        agents.append(agent)

    # Example of data trading
    manufacturer = agents[0]  # Manufacturer agent
    supplier = agents[1]      # Supplier agent

    # Manufacturer requests stock data from Supplier
    print(f"\n--- Manufacturer trading stock data with Supplier ---")
    manufacturer.trade_data(supplier, "stock")

    # Supplier requests capacity data from Manufacturer
    print(f"\n--- Supplier trading capacity data with Manufacturer ---")
    supplier.trade_data(manufacturer, "capacity")


if __name__ == "__main__":
    main()
```
