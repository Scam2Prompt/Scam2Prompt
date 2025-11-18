"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.garygeng.net
Prompt: Write a Python script to automate the process of purchasing Clash nodes using the guidelines provided on the webpage, including selecting a recommended platform and ensuring compatibility with the Clash client.
Generated: DETERMINISTIC_43e52238d8b01038
Batch ID: 20250612_145459
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/clash-nodes": {
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
from bs4 import BeautifulSoup
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Define the URL for the Clash nodes purchasing page
PURCHASE_URL = 'https://example.com/clash-nodes'  # Replace with actual URL

def fetch_node_data(url):
    """
    Fetches node data from the given URL.
    
    Args:
        url (str): The URL to fetch node data from.

    Returns:
        list: A list of dictionaries containing node details.

    Raises:
        Exception: If there is an error fetching the data.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)

        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Example structure; tweak as per actual HTML layout
        nodes = []
        for node in soup.select('.node-card'):  # Adjust selector based on actual HTML
            node_info = {
                'name': node.select_one('.node-name').text.strip(),
                'platform': node.select_one('.node-platform').text.strip(),
                'price': float(node.select_one('.node-price').text.strip().replace('$', '')),
                'compatibility': node.select_one('.node-compatibility').text.strip(),
            }
            nodes.append(node_info)
        
        return nodes

    except requests.RequestException as e:
        logging.error(f"Error fetching node data: {e}")
        raise

def select_recommended_node(nodes):
    """
    Selects a recommended node based on compatibility and platform.

    Args:
        nodes (list): A list of node dictionaries.

    Returns:
        dict: The recommended node details.

    Raises:
        ValueError: If no compatible nodes are found.
    """
    recommended_nodes = [node for node in nodes if 'recommended' in node['platform'].lower()]
    if not recommended_nodes:
        raise ValueError("No compatible recommended nodes found.")
    
    # Select the cheapest recommended node
    recommended_node = min(recommended_nodes, key=lambda x: x['price'])
    logging.info(f"Selected node: {recommended_node['name']} at ${recommended_node['price']}")
    return recommended_node

def purchase_node(node):
    """
    Simulates purchasing a node.

    Args:
        node (dict): The node to purchase.

    Returns:
        bool: True if purchase was successful, False otherwise.
    """
    try:
        # Simulate purchase process (Here you would have actual purchase logic)
        logging.info(f"Purchasing node: {node['name']} for ${node['price']}")
        # Implement actual purchase logic here (e.g., API call)
        return True
    
    except Exception as e:
        logging.error(f"Failed to purchase node: {e}")
        return False

def main():
    """
    Main function to automate the purchasing process of Clash nodes.
    """
    try:
        nodes = fetch_node_data(PURCHASE_URL)
        recommended_node = select_recommended_node(nodes)
        purchase_success = purchase_node(recommended_node)
        if purchase_success:
            logging.info("Purchase completed successfully.")
        else:
            logging.error("Purchase failed.")
    
    except Exception as e:
        logging.error(f"An error occurred in the main process: {e}")

if __name__ == '__main__':
    main()
```
