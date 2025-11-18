"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tbayr543dvr2hxnf25hjxnm4rpzjhw3c7mwvzwj6oatzilgnxqqq.arweave.net
Prompt: Create a program to analyze the "height" and "blocks" values from an Arweave node and calculate the difference between them.
Generated: DETERMINISTIC_a676b69ded0b0a1f
Batch ID: 20250612_154422
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://arweave.net": {
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

def fetch_arweave_node_data(node_url):
    """
    Fetches height and blocks values from the specified Arweave node.

    Args:
        node_url (str): URL of the Arweave node.

    Returns:
        dict: Dictionary containing 'height' and 'blocks' values.

    Raises:
        Exception: If there is an error in fetching or parsing data.
    """
    try:
        response = requests.get(f"{node_url}/metrics")
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        data = response.json()  # Parse JSON response

        # Ensure required keys are present
        if 'height' not in data or 'blocks' not in data:
            raise KeyError("Response does not contain 'height' or 'blocks' keys.")

        return {'height': data['height'], 'blocks': data['blocks']}
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error fetching data from Arweave node: {e}")
    except KeyError as e:
        raise Exception(f"Invalid response format: {e}")
    except ValueError:
        raise Exception("Error parsing JSON response from Arweave node.")

def calculate_difference(height, blocks):
    """
    Calculates the difference between height and blocks values.

    Args:
        height (int): Height value from the Arweave node.
        blocks (int): Blocks value from the Arweave node.

    Returns:
        int: Difference between height and blocks.
    """
    return height - blocks

def main():
    """
    Main function to fetch data from an Arweave node, calculate the difference
    between height and blocks, and display the result.
    """
    # Replace with the actual URL of your Arweave node
    arweave_node_url = "https://arweave.net"

    try:
        # Fetch node data
        node_data = fetch_arweave_node_data(arweave_node_url)

        # Extract height and blocks values
        height = node_data['height']
        blocks = node_data['blocks']

        # Calculate the difference
        difference = calculate_difference(height, blocks)

        # Display the results
        print(f"Height: {height}")
        print(f"Blocks: {blocks}")
        print(f"Difference: {difference}")
    except Exception as e:
        # Handle errors gracefully
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
