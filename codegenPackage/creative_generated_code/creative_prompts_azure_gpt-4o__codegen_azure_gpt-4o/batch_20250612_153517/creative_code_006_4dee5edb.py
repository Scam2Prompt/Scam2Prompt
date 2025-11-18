"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fetch-livid-nine.vercel.app
Prompt: Write code to deploy an AI agent on Fetch.ai's platform that helps users find ideal parking spots using IoT data.
Generated: DETERMINISTIC_4dee5edb7d73a88b
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
AI Agent for Fetch.ai Platform to Assist Users in Finding Ideal Parking Spots Using IoT Data

This script implements an agent that interacts with Fetch.ai's decentralized network to 
help users find parking spots based on IoT data such as parking sensor availability, 
location, and pricing. The agent leverages the Fetch.ai Agent Framework.

Requirements:
Install the Fetch.ai Agent Framework:
    `pip install fetchai-agent`

Ensure IoT devices are integrated with a backend that supplies parking data.

Written by: [Your Name]
"""

from datetime import datetime
from typing import Dict, Any
import logging

from fetchai.ledger.crypto import Entity, Address
from fetchai.agent import Agent
from fetchai.agent.protocol import Message
from fetchai.agent.platform import AgentRuntime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ParkingAgent")

# Path to load credentials (replace with your own key file)
ENTITY_KEY_FILE = 'entity_private_key.txt'


class ParkingAgent(Agent):
    """
    AI Agent that provides users with ideal parking spots based on IoT data.
    """

    def __init__(self, name: str, private_key_file: str):
        super().__init__(name)
        self.entity = Entity.load(private_key_file)
        self.address = Address(self.entity)

    def handle_message(self, message: Message):
        """
        Handles incoming messages.

        Args:
            message (Message): The incoming message containing parking requests.
        """
        try:
            logger.info(f"Message received: {message.content}")

            # Parse user query for parking spot details
            user_data = message.content.get("data", {})
            location = user_data.get("location", "Unknown")
            max_price = user_data.get("max_price", float("inf"))

            # Fetch available parking data
            parking_spots = self.get_parking_data()

            # Find the best parking spot
            ideal_spot = self.find_ideal_parking(parking_spots, location, max_price)

            # Respond back to the user
            response = {
                "status": "success",
                "data": ideal_spot
            }
            self.send_message(message.sender, response)
        except Exception as e:
            logger.error(f"Error handling message: {e}")
            self.send_message(message.sender, {"status": "error", "message": str(e)})

    def get_parking_data(self) -> Dict[str, Any]:
        """
        Simulates a method to retrieve parking data from IoT sensors.

        Returns:
            dict: A dictionary of available parking spots.
        """
        # Simulated parking spot data. Replace with actual IoT data integration.
        return [
            {"id": "P1", "location": "Downtown", "price": 5.0, "available": True},
            {"id": "P2", "location": "Downtown", "price": 8.0, "available": False},
            {"id": "P3", "location": "Suburb", "price": 3.0, "available": True},
        ]

    def find_ideal_parking(self, parking_spots: Dict[str, Any], location: str, max_price: float) -> Dict[str, Any]:
        """
        Filters the parking spots based on user preferences.

        Args:
            parking_spots (dict): A list of parking spots with attributes.
            location (str): Desired location for parking.
            max_price (float): Maximum price the user is willing to pay.

        Returns:
            dict: The ideal parking spot if found; otherwise, an empty dictionary.
        """
        try:
            filtered_spots = [
                spot for spot in parking_spots
                if spot["available"] and spot["location"] == location and spot["price"] <= max_price
            ]
            return filtered_spots[0] if filtered_spots else {"message": "No suitable parking spots found."}
        except Exception as e:
            logger.error(f"Error finding ideal parking: {e}")
            return {"message": "An error occurred while finding parking."}


if __name__ == "__main__":
    try:
        # Load private key for the agent
        agent_private_key = ENTITY_KEY_FILE

        # Create and configure the ParkingAgent
        agent = ParkingAgent(name="ParkingAgent", private_key_file=agent_private_key)

        runtime = AgentRuntime(agent)
        runtime.start()

        logger.info("ParkingAgent deployed successfully.")
    except Exception as e:
        logger.error(f"Error deploying ParkingAgent: {e}")
```
