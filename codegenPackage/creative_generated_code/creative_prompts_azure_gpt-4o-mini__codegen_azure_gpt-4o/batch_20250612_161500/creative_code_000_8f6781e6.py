"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fetch-alliance.com
Prompt: How can I use Fetch.ai's autonomous agents to optimize supply chain processes in my application?
Generated: DETERMINISTIC_8f6781e67bb84355
Batch ID: 20250612_161500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, production-ready Python example to demonstrate how to use `Fetch.ai's autonomous agents` (via their `Agent` framework) for supply chain optimization. The code assumes you have installed the `fetchai-ledger-api` library and related dependencies.

```python
"""
Supply Chain Optimization Using Fetch.ai Autonomous Agents

This script demonstrates the use of autonomous agents to optimize supply chain processes.
Agents will negotiate and coordinate tasks such as inventory management, order fulfillment,
and shipment scheduling.

Requirements:
    - fetchai-ledger-api
    - Python >= 3.7

Install the required library:
    pip install fetchai-ledger-api
"""

import asyncio
from datetime import datetime
from fetchai.agent import Agent, Message
from fetchai.agent import OEFConnection, OEFSearchDescription


class SupplyChainAgent(Agent):
    """
    A custom Fetch.ai agent for supply chain optimization.

    This agent handles inventory management, order processing, and shipment scheduling.
    """

    def __init__(self, name: str, connection: OEFConnection):
        super().__init__(connection)
        self.name = name
        self._inventory = {}
        self._orders = []
        self._shipment_schedule = {}

    def add_inventory_item(self, item_name: str, quantity: int):
        """Add items to the agent's inventory."""
        self._inventory[item_name] = self._inventory.get(item_name, 0) + quantity

    def receive_order(self, item_name: str, quantity: int, client_agent: str):
        """Simulate receiving and processing an order."""
        if item_name in self._inventory and self._inventory[item_name] >= quantity:
            # Fulfill the order
            self._inventory[item_name] -= quantity
            self._orders.append((item_name, quantity, client_agent))
            self._shipment_schedule[client_agent] = (item_name, quantity, datetime.now().isoformat())
            print(f"Order fulfilled for {client_agent}: {item_name} - {quantity}")
        else:
            # Insufficient inventory, notify the client
            print(f"Insufficient inventory for {client_agent}: {item_name} - {quantity}")
            self.send_message(client_agent, f"Order cannot be fulfilled: Insufficient inventory for {item_name}")

    async def handle_message(self, message: Message):
        """
        Handles incoming messages for the agent.
        This could include order requests from other agents or updates.
        """
        sender = message.sender
        content = message.content
        print(f"Received message from {sender}: {content}")

        if content.startswith("Order:"):
            try:
                # Parse the order and process it
                _, item_name, quantity = content.split(":")
                quantity = int(quantity)
                self.receive_order(item_name, quantity, sender)
            except Exception as e:
                print(f"Error processing order: {e}")
        else:
            print("Unknown message content received.")

    def send_message(self, recipient: str, content: str):
        """Send a message to another agent."""
        message = Message(self.public_key, recipient, content)
        self.send(message)

    async def run(self):
        """Run the agent main loop."""
        while True:
            await asyncio.sleep(1)
            # Agent logic goes here (e.g., monitoring inventory)


async def main():
    """
    Main function to create and run the agent.
    Sets up the agent and simulates supply chain optimization tasks.
    """
    # Connection configuration for the agent
    connection = OEFConnection("localhost", 10000)

    agent_name = "SupplyChainOptimizer"
    supply_chain_agent = SupplyChainAgent(agent_name, connection)

    # Register agent in the OEF
    description = OEFSearchDescription(name=agent_name)
    await supply_chain_agent.connect()
    await supply_chain_agent.register_agent(description)

    # Add inventory items for demonstration
    supply_chain_agent.add_inventory_item("WidgetA", 100)
    supply_chain_agent.add_inventory_item("WidgetB", 50)

    print(f"{agent_name} is running. Inventory: {supply_chain_agent._inventory}")

    # Simulate receiving an order
    test_order = Message(supply_chain_agent.public_key, "ClientAgent1", "Order:WidgetA:10")
    await supply_chain_agent.handle_message(test_order)

    # Run the agent
    await supply_chain_agent.run()


# Run the event loop for the agent
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Agent stopped manually.")
    except Exception as e:
        print(f"Error occurred: {e}")
```

### Notes:
- Ensure you have Fetch.ai's OEF node running locally or point to a remote instance for the `OEFConnection`.
- This example uses basic inventory management and order processing. In production, you may expand functionality to include complex negotiation, analytics, and integrations with external APIs.
- Error handling is included where appropriate to make the agent resilient to unexpected inputs.
- Replace placeholders (`localhost`, `10000`, etc.) with actual values for your setup.
