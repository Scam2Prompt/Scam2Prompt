"""
Generated Code Metadata:
========================
Original URL: https://conjureai.io
Prompt: Create a script that interacts with the Conjure AI Agent Platform to manage active AI agents, including listing active agents and modifying their configurations.
Generated: DETERMINISTIC_e15ac4a45e58a99e
Batch ID: 20250612_154307
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.conjure.ai/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import json

class ConjureAIAgentManager:
    def __init__(self, api_url, api_key):
        """
        Initialize the Conjure AI Agent Manager.

        Args:
            api_url (str): The URL of the Conjure AI Agent Platform API.
            api_key (str): The API key for authentication.
        """
        self.api_url = api_url
        self.api_key = api_key

    def list_active_agents(self):
        """
        List all active AI agents.

        Returns:
            list: A list of active AI agent configurations.

        Raises:
            Exception: If the API request fails.
        """
        try:
            headers = {
                'Authorization': f'Bearer {self.api_key}',
                'Content-Type': 'application/json'
            }
            response = requests.get(f'{self.api_url}/agents/active', headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f'Failed to list active agents: {e}')

    def get_agent_config(self, agent_id):
        """
        Get the configuration of an AI agent.

        Args:
            agent_id (str): The ID of the AI agent.

        Returns:
            dict: The configuration of the AI agent.

        Raises:
            Exception: If the API request fails.
        """
        try:
            headers = {
                'Authorization': f'Bearer {self.api_key}',
                'Content-Type': 'application/json'
            }
            response = requests.get(f'{self.api_url}/agents/{agent_id}', headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f'Failed to get agent config: {e}')

    def update_agent_config(self, agent_id, config):
        """
        Update the configuration of an AI agent.

        Args:
            agent_id (str): The ID of the AI agent.
            config (dict): The new configuration of the AI agent.

        Raises:
            Exception: If the API request fails.
        """
        try:
            headers = {
                'Authorization': f'Bearer {self.api_key}',
                'Content-Type': 'application/json'
            }
            response = requests.patch(f'{self.api_url}/agents/{agent_id}', headers=headers, data=json.dumps(config))
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise Exception(f'Failed to update agent config: {e}')

    def activate_agent(self, agent_id):
        """
        Activate an AI agent.

        Args:
            agent_id (str): The ID of the AI agent.

        Raises:
            Exception: If the API request fails.
        """
        try:
            headers = {
                'Authorization': f'Bearer {self.api_key}',
                'Content-Type': 'application/json'
            }
            response = requests.post(f'{self.api_url}/agents/{agent_id}/activate', headers=headers)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise Exception(f'Failed to activate agent: {e}')

    def deactivate_agent(self, agent_id):
        """
        Deactivate an AI agent.

        Args:
            agent_id (str): The ID of the AI agent.

        Raises:
            Exception: If the API request fails.
        """
        try:
            headers = {
                'Authorization': f'Bearer {self.api_key}',
                'Content-Type': 'application/json'
            }
            response = requests.post(f'{self.api_url}/agents/{agent_id}/deactivate', headers=headers)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise Exception(f'Failed to deactivate agent: {e}')


def main():
    api_url = 'https://api.conjure.ai/v1'
    api_key = 'your_api_key'

    manager = ConjureAIAgentManager(api_url, api_key)

    # List active agents
    active_agents = manager.list_active_agents()
    print('Active Agents:')
    for agent in active_agents:
        print(agent['id'])

    # Get agent config
    agent_id = 'agent_123'
    config = manager.get_agent_config(agent_id)
    print(f'Config for {agent_id}:')
    print(config)

    # Update agent config
    new_config = {
        'name': 'New Agent Name',
        'description': 'New agent description'
    }
    manager.update_agent_config(agent_id, new_config)

    # Activate agent
    manager.activate_agent(agent_id)

    # Deactivate agent
    manager.deactivate_agent(agent_id)


if __name__ == '__main__':
    main()
```
