"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safe-app.morpho.dev
Prompt: Provide an example of delegating tasks using Morpho's Delegate feature, including code to initialize delegation.
Generated: DETERMINISTIC_5e787acadde06a77
Batch ID: 20250612_145444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries for Morpho delegation
from morpho_sdk import MorphoClient, DelegateRequest

def initialize_morpho_client(api_key: str) -> MorphoClient:
    """
    Initialize a Morpho client with the provided API key.

    Args:
        api_key (str): The API key for authenticating with the Morpho service.

    Returns:
        MorphoClient: An instance of the Morpho client.
    """
    try:
        client = MorphoClient(api_key)
        return client
    except Exception as e:
        raise RuntimeError("Failed to initialize Morpho client: " + str(e))

def delegate_task(client: MorphoClient, task_id: str, delegate_to: str) -> str:
    """
    Delegate a task to another user using Morpho's delegation feature.

    Args:
        client (MorphoClient): The initialized Morpho client.
        task_id (str): The ID of the task to be delegated.
        delegate_to (str): The user ID to whom the task will be delegated.

    Returns:
        str: A confirmation message regarding the delegation.
    """
    try:
        # Create a delegate request
        delegation_request = DelegateRequest(task_id=task_id, delegate_to=delegate_to)
        
        # Perform the delegation
        response = client.delegate(delegation_request)
        
        if response.success:
            return f"Task {task_id} successfully delegated to {delegate_to}."
        else:
            raise Exception(f"Failed to delegate task: {response.error_message}")
    except Exception as e:
        raise RuntimeError("Error during delegation: " + str(e))

# Main execution flow
if __name__ == "__main__":
    # Initialize the Morpho client
    api_key = "your_api_key_here"  # Replace with your actual API key
    morpho_client = initialize_morpho_client(api_key)

    # Example task delegation
    task_id = "123456"  # Replace with the actual task ID
    delegate_user_id = "user789"  # Replace with the user ID to delegate to

    try:
        message = delegate_task(morpho_client, task_id, delegate_user_id)
        print(message)
    except RuntimeError as e:
        print(e)
```
