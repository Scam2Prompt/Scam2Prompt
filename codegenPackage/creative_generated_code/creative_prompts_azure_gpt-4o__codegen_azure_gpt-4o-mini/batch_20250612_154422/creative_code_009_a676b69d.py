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

class ArweaveAnalyzer:
    """Class to analyze height and blocks from an Arweave node."""

    def __init__(self, node_url):
        """
        Initializes the ArweaveAnalyzer with the provided node URL.
        
        Args:
            node_url (str): The URL of the Arweave node to fetch data from.
        """
        self.node_url = node_url

    def fetch_data(self):
        """
        Fetches height and blocks data from the Arweave node.

        Returns:
            dict: A dictionary containing 'height' and 'blocks' values.
            
        Raises:
            Exception: If the request to the node fails or the response is invalid.
        """
        try:
            response = requests.get(f"{self.node_url}/status")
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()

            # Check if the expected keys are in the response
            if 'height' not in data or 'blocks' not in data:
                raise ValueError("Response does not contain 'height' or 'blocks' keys.")

            return {
                "height": data['height'],
                "blocks": data['blocks']
            }
        except requests.exceptions.RequestException as e:
            raise Exception(f"Error fetching data from the Arweave node: {e}")
        except ValueError as ve:
            raise Exception(f"Data format error: {ve}")

    def calculate_difference(self, height, blocks):
        """
        Calculates the difference between height and blocks.

        Args:
            height (int): The height value.
            blocks (int): The blocks value.

        Returns:
            int: The difference between height and blocks.
        """
        return height - blocks

    def analyze(self):
        """Main method to fetch data and analyze the difference."""
        try:
            data = self.fetch_data()
            height = data['height']
            blocks = data['blocks']

            difference = self.calculate_difference(height, blocks)

            print(f"Height: {height}, Blocks: {blocks}, Difference: {difference}")
        except Exception as e:
            print(f"Analysis failed: {e}")

if __name__ == "__main__":
    # Replace with the actual Arweave node URL
    arweave_node_url = "https://arweave.net"  
    analyzer = ArweaveAnalyzer(arweave_node_url)
    analyzer.analyze()
```
