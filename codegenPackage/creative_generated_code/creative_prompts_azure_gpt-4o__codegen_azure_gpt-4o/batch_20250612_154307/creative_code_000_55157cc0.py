"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://conjureai.io
Prompt: Write Python code using the Conjure AI Agent Platform to create and deploy a custom AI agent for text generation. Include steps to select an agent and view past creations from the Vault.
Generated: DETERMINISTIC_55157cc0df97faf6
Batch ID: 20250612_154307
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python script to create, deploy, and manage a custom AI agent for text generation 
using the Conjure AI Agent Platform.
"""

from conjure_api import ConjureClient, ConjureError

# Constants
API_KEY = "your_api_key_here"  # Replace with your actual Conjure API key
AGENT_NAME = "CustomTextGeneratorAgent"  # Name of the new agent
DEPLOYMENT_CONFIG = {
    "model": "text-davinci-003",  # Specify the text generation model
    "parameters": {
        "temperature": 0.7,  # Control creativity (higher values = more creative)
        "max_tokens": 500,  # Set maximum response length
    },
}

def create_client(api_key):
    """
    Initialize the Conjure client with the provided API key.
    :param api_key: API key for authentication
    :return: ConjureClient instance
    """
    try:
        return ConjureClient(api_key)
    except ConjureError as e:
        print(f"Error initializing client: {e}")
        raise


def select_agent(client, agent_name):
    """
    Select or create an AI agent.
    :param client: ConjureClient instance
    :param agent_name: Name of the agent to select or create
    :return: Selected or newly created agent
    """
    try:
        # Check if agent already exists
        agent = client.get_agent(agent_name)
        print(f"Agent '{agent_name}' found.")
    except ConjureError:
        # If agent doesn't exist, create a new one
        print(f"Agent '{agent_name}' not found. Creating a new agent...")
        agent = client.create_agent(agent_name, DEPLOYMENT_CONFIG)
        print(f"Agent '{agent_name}' created successfully.")
    return agent


def deploy_agent(agent):
    """
    Deploy the selected AI agent to make it available for usage.
    :param agent: The agent to deploy
    """
    try:
        agent.deploy()
        print(f"Agent '{agent.name}' deployed successfully.")
    except ConjureError as e:
        print(f"Error deploying agent: {e}")
        raise


def view_vault(client):
    """
    View past creations in the Vault.
    :param client: ConjureClient instance
    """
    try:
        vault = client.get_vault()
        print("Vault contents:")
        for creation in vault:
            print(f"- {creation['name']}: {creation['description']}")
    except ConjureError as e:
        print(f"Error retrieving Vault contents: {e}")
        raise


def main():
    """
    Main function to create, deploy, and manage a custom AI agent.
    """
    try:
        # Step 1: Initialize the client
        client = create_client(API_KEY)
        
        # Step 2: Select or create the agent
        agent = select_agent(client, AGENT_NAME)
        
        # Step 3: Deploy the agent
        deploy_agent(agent)
        
        # Step 4: View past creations in the Vault
        view_vault(client)
        
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
