"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agora-ai.market
Prompt: What are the steps to integrate AI agents into existing workflows using Agora AI's seamless integration APIs?
Generated: DETERMINISTIC_2cb7bf989df49b67
Batch ID: 20250612_155557
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.agoraai.com": {
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
This Python script demonstrates how to integrate AI agents into existing workflows using Agora AI's seamless integration APIs.
The steps include:
1. Authentication with Agora API.
2. Retrieving available AI agents.
3. Selecting and assigning an AI agent to a specific workflow.
4. Utilizing the agent for processing tasks in the workflow.
"""

import requests

# Define constants
AGORA_API_BASE_URL = "https://api.agoraai.com"
API_KEY = "your_api_key_here"  # Replace with your Agora API key

def authenticate(api_key):
    """
    Authenticates with Agora AI API using the provided API key.
    
    Parameters:
        api_key (str): API key for authentication.
    
    Returns:
        dict: Response containing authentication status or error message.
    """
    endpoint = f"{AGORA_API_BASE_URL}/auth"
    headers = {"Authorization": f"Bearer {api_key}"}

    try:
        response = requests.post(endpoint, headers=headers)
        response.raise_for_status()  # Raise exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Authentication failed: {e}")
        return {"error": str(e)}

def get_available_agents():
    """
    Retrieves a list of available AI agents from Agora API.
    
    Returns:
        list: List of available AI agents or error details.
    """
    endpoint = f"{AGORA_API_BASE_URL}/agents"
    headers = {"Authorization": f"Bearer {API_KEY}"}

    try:
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()
        return response.json()["agents"]
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve agents: {e}")
        return []

def assign_agent_to_workflow(agent_id, workflow_id):
    """
    Assigns a selected AI agent to a specific workflow.
    
    Parameters:
        agent_id (str): ID of the AI agent.
        workflow_id (str): ID of the workflow.
    
    Returns:
        dict: Response indicating success or failure of the operation.
    """
    endpoint = f"{AGORA_API_BASE_URL}/workflows/{workflow_id}/assign-agent"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    payload = {"agent_id": agent_id}

    try:
        response = requests.post(endpoint, headers=headers, json=payload)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to assign agent to workflow: {e}")
        return {"error": str(e)}

def process_workflow_task(workflow_id, task_data):
    """
    Sends a task to the workflow for processing using the assigned AI agent.
    
    Parameters:
        workflow_id (str): ID of the workflow.
        task_data (dict): Data to process.
    
    Returns:
        dict: Response containing task results or error details.
    """
    endpoint = f"{AGORA_API_BASE_URL}/workflows/{workflow_id}/process"
    headers = {"Authorization": f"Bearer {API_KEY}"}

    try:
        response = requests.post(endpoint, headers=headers, json=task_data)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to process task: {e}")
        return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    # Step 1: Authenticate
    auth_response = authenticate(API_KEY)
    if "error" in auth_response:
        print("Authentication failed. Exiting...")
        exit()

    print("Authentication successful.")

    # Step 2: Retrieve available agents
    agents = get_available_agents()
    if not agents:
        print("No agents available. Exiting...")
        exit()

    print(f"Available agents: {agents}")

    # Step 3: Assign an agent to a workflow
    workflow_id = "example_workflow_id"  # Replace with your workflow ID
    agent_id = agents[0]["id"]  # Select the first agent (customize as needed)
    assign_response = assign_agent_to_workflow(agent_id, workflow_id)
    if "error" in assign_response:
        print("Failed to assign agent. Exiting...")
        exit()

    print(f"Agent {agent_id} assigned to workflow {workflow_id} successfully.")

    # Step 4: Process a task using the workflow
    task_data = {"input": "example input data"}  # Replace with your task data
    process_response = process_workflow_task(workflow_id, task_data)
    if "error" in process_response:
        print("Failed to process task. Exiting...")
        exit()

    print(f"Task processed successfully. Output: {process_response['output']}")
```
