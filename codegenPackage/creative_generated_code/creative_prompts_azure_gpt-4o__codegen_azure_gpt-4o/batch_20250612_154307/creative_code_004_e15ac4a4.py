"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
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

# Creative Generated Code:
# ========================

```python
import requests

# Define constants for the API endpoint and access token
API_BASE_URL = "https://api.conjure.ai/v1"  # Replace with the actual API base URL
API_ACCESS_TOKEN = "your_access_token_here"  # Replace with your API access token

# Headers for authentication
HEADERS = {
    "Authorization": f"Bearer {API_ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

def list_active_agents():
    """
    Fetch and list active AI agents from the Conjure AI Agent Platform.
    
    Returns:
        List of active agents or None if an error occurs.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/agents/active", headers=HEADERS)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()  # Return the list of active agents
    except requests.exceptions.RequestException as e:
        print(f"Error while fetching active agents: {e}")
        return None

def modify_agent_configuration(agent_id, configuration_updates):
    """
    Modify the configuration of a specific AI agent.
    
    Args:
        agent_id (str): The ID of the agent to be modified.
        configuration_updates (dict): The configuration updates to apply.
        
    Returns:
        Response data or None if an error occurs.
    """
    try:
        endpoint = f"{API_BASE_URL}/agents/{agent_id}/configuration"
        response = requests.put(endpoint, headers=HEADERS, json=configuration_updates)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()  # Return the response data
    except requests.exceptions.RequestException as e:
        print(f"Error while modifying agent configuration: {e}")
        return None

def main():
    """
    Main function to interact with the Conjure AI Agent Platform.
    """
    print("Fetching active agents...")
    active_agents = list_active_agents()
    
    if active_agents is not None:
        print("Active agents:")
        for agent in active_agents:
            print(f"Agent ID: {agent['id']}, Name: {agent['name']}")
        
        # Example: Modify the configuration of the first agent (if any exist)
        if active_agents:
            agent_id = active_agents[0]['id']
            configuration_updates = {
                "max_concurrent_tasks": 5,  # Example configuration update
                "status": "active"  # Example status update
            }
            print(f"Modifying configuration for agent ID: {agent_id}")
            response = modify_agent_configuration(agent_id, configuration_updates)
            
            if response is not None:
                print(f"Configuration updated successfully: {response}")
            else:
                print("Failed to update agent configuration.")
    else:
        print("No active agents found or an error occurred.")

if __name__ == "__main__":
    main()
```
