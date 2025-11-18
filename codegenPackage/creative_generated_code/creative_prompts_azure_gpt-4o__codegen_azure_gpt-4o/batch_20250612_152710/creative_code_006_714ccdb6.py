"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phi-f1z.pages.dev
Prompt: Create a script that uses Phi Protocol to generate a social graph based on onchain transactions, and visualize it using eBoy-style pixel art.
Generated: DETERMINISTIC_714ccdb6ff21f79d
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import networkx as nx
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

# Function to fetch on-chain transactions (mocked for this example)
def fetch_onchain_data(address):
    """
    Simulate fetching on-chain transactions for a given address.
    Replace with actual API calls to Phi Protocol or blockchain data provider.
    """
    # Mock data for demonstration purposes
    return [
        {"from": address, "to": "0x123", "value": 10},
        {"from": "0x123", "to": "0x456", "value": 5},
        {"from": "0x456", "to": "0x789", "value": 15},
    ]

# Function to generate a social graph from transactions
def generate_social_graph(transactions):
    """
    Generate a NetworkX graph from on-chain transactions.
    """
    graph = nx.DiGraph()  # Create a directed graph
    for tx in transactions:
        graph.add_edge(tx["from"], tx["to"], weight=tx["value"])
    return graph

# Function to convert the graph into pixel art
def generate_pixel_art(graph, filename="pixel_art.png", pixel_size=20):
    """
    Generate eBoy-style pixel art visualization from the graph.
    """
    nodes = list(graph.nodes)
    size = len(nodes) * pixel_size  # Determine canvas size
    image = Image.new("RGB", (size, size), "white")
    draw = ImageDraw.Draw(image)

    # Assign each node a position in the grid
    positions = {}
    for i, node in enumerate(nodes):
        x = (i % len(nodes)) * pixel_size
        y = (i // len(nodes)) * pixel_size
        positions[node] = (x, y)

        # Draw node as a square (pixel)
        draw.rectangle([x, y, x + pixel_size, y + pixel_size], fill="blue")

    # Draw edges as lines between pixels
    for edge in graph.edges(data=True):
        from_pos = positions[edge[0]]
        to_pos = positions[edge[1]]
        draw.line(
            [from_pos[0] + pixel_size // 2, from_pos[1] + pixel_size // 2,
             to_pos[0] + pixel_size // 2, to_pos[1] + pixel_size // 2],
            fill="black", width=1
        )

    # Save the generated pixel art
    image.save(filename)
    print(f"Pixel art saved to {filename}")

# Main execution
def main():
    """
    Main function to generate a social graph and visualize it.
    """
    try:
        # Replace with a real blockchain address or user input
        blockchain_address = "0xABC"

        # Step 1: Fetch on-chain transactions
        transactions = fetch_onchain_data(blockchain_address)

        # Step 2: Generate social graph
        social_graph = generate_social_graph(transactions)

        # Step 3: Visualize as pixel art
        generate_pixel_art(social_graph)

    except Exception as e:
        print(f"An error occurred: {e}")

# Entry point
if __name__ == "__main__":
    main()
```
