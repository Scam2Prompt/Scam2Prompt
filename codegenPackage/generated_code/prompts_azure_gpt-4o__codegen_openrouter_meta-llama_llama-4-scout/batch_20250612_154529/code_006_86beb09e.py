"""
Generated Code Metadata:
========================
Original URL: https://p3gnmpkzz7bdg3pxf7p4hgpwb4d7u77rhdcllh4h54gp7m5pl2qa.arweave.net
Prompt: Develop a tool to visualize the `peers` count over time using the JSON data format provided by the Arweave network.
Generated: DETERMINISTIC_86beb09ee831d130
Batch ID: 20250612_154529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

def load_json_data(file_path):
    """
    Load JSON data from a file.

    Args:
        file_path (str): Path to the JSON file.

    Returns:
        dict: Loaded JSON data.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file is not valid JSON.
    """
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON - {e}")
        return None

def extract_peers_data(data):
    """
    Extract peers count data from the Arweave network JSON data.

    Args:
        data (dict): JSON data from the Arweave network.

    Returns:
        list: List of tuples containing the timestamp and peers count.
    """
    peers_data = []
    for block in data['blocks']:
        timestamp = datetime.fromtimestamp(block['timestamp'])
        peers = block.get('peers', 0)
        peers_data.append((timestamp, peers))
    return peers_data

def visualize_peers_data(peers_data):
    """
    Visualize the peers count over time.

    Args:
        peers_data (list): List of tuples containing the timestamp and peers count.
    """
    timestamps, peers = zip(*peers_data)

    plt.figure(figsize=(12, 6))
    plt.plot(timestamps, peers, marker='o')

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.gcf().autofmt_xdate()

    plt.title('Peers Count Over Time')
    plt.xlabel('Timestamp')
    plt.ylabel('Peers Count')

    plt.grid(True)
    plt.show()

def main():
    file_path = 'arweave_data.json'  # replace with your JSON file path
    data = load_json_data(file_path)
    if data:
        peers_data = extract_peers_data(data)
        visualize_peers_data(peers_data)

if __name__ == '__main__':
    main()
```
