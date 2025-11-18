"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btc-tools.org
Prompt: Develop a script to group network segments and assign custom names to each group for easier management in BTC Tools.
Generated: DETERMINISTIC_fee211f98aff45dd
Batch ID: 20250612_151710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import ipaddress
import json

def group_network_segments(segments, group_definitions):
    """
    Groups network segments based on provided definitions and assigns custom names to each group.

    Args:
        segments (list): List of network segments (subnets) in CIDR notation.
        group_definitions (dict): Dictionary containing group names as keys and lists of subnets as values.

    Returns:
        dict: Dictionary where keys are group names and values are lists of matched network segments.
    """
    # Dictionary to store grouped segments
    grouped_segments = {group: [] for group in group_definitions.keys()}

    try:
        # Iterate through each network segment
        for segment in segments:
            segment_network = ipaddress.ip_network(segment)

            # Check each group definition for matches
            for group_name, group_subnets in group_definitions.items():
                for group_subnet in group_subnets:
                    group_network = ipaddress.ip_network(group_subnet)

                    # If the segment fits within the group subnet, add it to the group
                    if segment_network.subnet_of(group_network):
                        grouped_segments[group_name].append(segment)
                        break  # Stop checking once this segment is grouped

        return grouped_segments
    except ValueError as e:
        # Handle invalid segment or group subnet input
        print(f"Error processing network segments: {e}")
        return None

if __name__ == "__main__":
    # Example usage: List of network segments to group
    network_segments = [
        "192.168.1.0/24",
        "192.168.2.0/24",
        "10.0.0.0/8",
        "172.16.0.0/16"
    ]

    # Group definitions: Define custom group names and their associated subnets
    group_definitions = {
        "Home Network": ["192.168.1.0/24", "192.168.2.0/24"],
        "Private Network": ["10.0.0.0/8", "172.16.0.0/12"]
    }

    # Group the network segments
    grouped_result = group_network_segments(network_segments, group_definitions)

    # Output the grouping result
    if grouped_result:
        print("Grouped Network Segments:")
        print(json.dumps(grouped_result, indent=4))
```
