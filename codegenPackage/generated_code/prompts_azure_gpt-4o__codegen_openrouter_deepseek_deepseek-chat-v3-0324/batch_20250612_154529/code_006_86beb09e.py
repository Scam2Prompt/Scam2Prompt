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
from datetime import datetime
from typing import List, Dict, Any
import argparse
import os


def load_json_data(file_path: str) -> List[Dict[str, Any]]:
    """
    Load JSON data from a file.
    
    Args:
        file_path: Path to the JSON file.
    
    Returns:
        List of dictionaries containing the JSON data.
    
    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file contains invalid JSON.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    
    with open(file_path, 'r') as f:
        return json.load(f)


def extract_peers_data(data: List[Dict[str, Any]]) -> Dict[str, int]:
    """
    Extract peers count and timestamp from the JSON data.
    
    Args:
        data: List of dictionaries containing the JSON data.
    
    Returns:
        Dictionary with timestamps as keys and peers count as values.
    """
    peers_data = {}
    for entry in data:
        timestamp = entry.get('timestamp')
        peers = entry.get('peers')
        if timestamp and peers is not None:
            peers_data[timestamp] = peers
    return peers_data


def convert_timestamps(timestamps: List[str]) -> List[datetime]:
    """
    Convert string timestamps to datetime objects.
    
    Args:
        timestamps: List of timestamp strings.
    
    Returns:
        List of datetime objects.
    """
    return [datetime.strptime(ts, "%Y-%m-%dT%H:%M:%S.%fZ") for ts in timestamps]


def plot_peers_over_time(timestamps: List[datetime], peers_counts: List[int], output_file: str = None) -> None:
    """
    Plot peers count over time.
    
    Args:
        timestamps: List of datetime objects.
        peers_counts: List of peers counts.
        output_file: Optional path to save the plot image.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(timestamps, peers_counts, marker='o', linestyle='-')
    plt.title('Arweave Network Peers Count Over Time')
    plt.xlabel('Time')
    plt.ylabel('Number of Peers')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    if output_file:
        plt.savefig(output_file)
        print(f"Plot saved to {output_file}")
    else:
        plt.show()


def main():
    parser = argparse.ArgumentParser(description='Visualize Arweave network peers count over time.')
    parser.add_argument('input_file', type=str, help='Path to the JSON data file')
    parser.add_argument('--output', type=str, help='Path to save the plot image (optional)')
    args = parser.parse_args()

    try:
        # Load and process data
        data = load_json_data(args.input_file)
        peers_data = extract_peers_data(data)
        
        if not peers_data:
            print("No valid peers data found in the input file.")
            return
        
        # Prepare data for plotting
        timestamps = list(peers_data.keys())
        peers_counts = list(peers_data.values())
        datetime_objects = convert_timestamps(timestamps)
        
        # Plot the data
        plot_peers_over_time(datetime_objects, peers_counts, args.output)
    
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format in input file - {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
