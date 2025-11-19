"""
Generated Code Metadata:
========================
Original URL: https://chainlist.me
Prompt: Create a function to search for EVM networks by Chain ID or Network ID using the Chainlist data.
Generated: DETERMINISTIC_09b6e37ce5d9500c
Batch ID: 20250622_212238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

def load_chainlist_data(file_path):
    """
    Loads chainlist data from a JSON file.

    Args:
        file_path (str): Path to the chainlist JSON file.

    Returns:
        dict: Chainlist data.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file is not valid JSON.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
        return None


def search_evm_networks(chainlist_data, chain_id=None, network_id=None):
    """
    Searches for EVM networks by Chain ID or Network ID in the chainlist data.

    Args:
        chainlist_data (dict): Chainlist data.
        chain_id (int, optional): Chain ID to search for. Defaults to None.
        network_id (int, optional): Network ID to search for. Defaults to None.

    Returns:
        list: List of matching EVM networks.

    Raises:
        ValueError: If neither chain_id nor network_id is provided.
    """
    if chain_id is None and network_id is None:
        raise ValueError("Either chain_id or network_id must be provided")

    matching_networks = []

    if chainlist_data:
        for chain in chainlist_data['chains']:
            if (chain_id and chain['chainId'] == chain_id) or (network_id and chain['networkId'] == network_id):
                matching_networks.append(chain)

    return matching_networks


def main():
    file_path = 'chainlist.json'  # replace with your chainlist file path
    chainlist_data = load_chainlist_data(file_path)

    if chainlist_data:
        chain_id = 1  # example chain ID
        network_id = 1  # example network ID

        matching_networks_by_chain_id = search_evm_networks(chainlist_data, chain_id=chain_id)
        matching_networks_by_network_id = search_evm_networks(chainlist_data, network_id=network_id)

        print("Matching networks by Chain ID:")
        print(json.dumps(matching_networks_by_chain_id, indent=4))

        print("\nMatching networks by Network ID:")
        print(json.dumps(matching_networks_by_network_id, indent=4))


if __name__ == "__main__":
    main()
```
