"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eiizaos-ai.com
Prompt: Create a script that utilizes the features of ElizaOS for managing AI agents.
Generated: DETERMINISTIC_d827dcb948108279
Batch ID: 20250612_162431
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script for managing AI agents using ElizaOS.

This script demonstrates how to utilize the features of ElizaOS to create, manage, and interact
with AI agents in a production-ready manner. The script handles agent lifecycle tasks such as
creation, querying, and deletion, and includes error handling and logging.

Requirements:
- Python 3.8+
- ElizaOS SDK installed (pip install elizaos-sdk)

Author: [Your Name]
Date: [Today's Date]
"""

import logging
import os
from elizaos_sdk import ElizaOS, ElizaAgent, ElizaError

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Initialize ElizaOS client
try:
    eliza_client = ElizaOS(api_key=os.getenv("ELIZAOS_API_KEY"))
    logging.info("Successfully initialized ElizaOS client.")
except ElizaError as e:
    logging.error(f"Failed to initialize ElizaOS client: {e}")
    raise SystemExit("Unable to proceed without ElizaOS client initialization.")

def create_agent(agent_name, capabilities):
    """
    Create a new AI agent in ElizaOS.
    
    Args:
        agent_name (str): Name of the agent to be created.
        capabilities (list): List of capabilities the agent should have.

    Returns:
        ElizaAgent: Instance of the created agent.
    """
    try:
        agent = eliza_client.create_agent(name=agent_name, capabilities=capabilities)
        logging.info(f"Agent '{agent_name}' created successfully.")
        return agent
    except ElizaError as e:
        logging.error(f"Failed to create agent '{agent_name}': {e}")
        raise

def list_agents():
    """
    List all available agents in ElizaOS.

    Returns:
        list: List of ElizaAgent instances.
    """
    try:
        agents = eliza_client.list_agents()
        logging.info(f"Retrieved {len(agents)} agents.")
        return agents
    except ElizaError as e:
        logging.error(f"Failed to retrieve agent list: {e}")
        raise

def query_agent(agent_id, query):
    """
    Query an AI agent in ElizaOS.

    Args:
        agent_id (str): ID of the agent to query.
        query (str): Query to ask the agent.

    Returns:
        str: Agent's response.
    """
    try:
        response = eliza_client.query_agent(agent_id=agent_id, query=query)
        logging.info(f"Received response from agent '{agent_id}': {response}")
        return response
    except ElizaError as e:
        logging.error(f"Failed to query agent '{agent_id}': {e}")
        raise

def delete_agent(agent_id):
    """
    Delete an AI agent in ElizaOS.

    Args:
        agent_id (str): ID of the agent to be deleted.
    """
    try:
        eliza_client.delete_agent(agent_id=agent_id)
        logging.info(f"Agent '{agent_id}' deleted successfully.")
    except ElizaError as e:
        logging.error(f"Failed to delete agent '{agent_id}': {e}")
        raise

def main():
    """
    Main function to demonstrate the usage of the ElizaOS client.
    """
    try:
        # Create an agent
        agent = create_agent(agent_name="AssistantAI", capabilities=["text-processing", "data-analysis"])

        # List all agents
        agents = list_agents()
        for a in agents:
            logging.info(f"Agent ID: {a.id}, Name: {a.name}, Capabilities: {a.capabilities}")

        # Query the created agent
        response = query_agent(agent_id=agent.id, query="What is the weather today?")
        logging.info(f"Agent Response: {response}")

        # Delete the created agent
        delete_agent(agent_id=agent.id)

    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")
        raise

if __name__ == "__main__":
    main()
```
