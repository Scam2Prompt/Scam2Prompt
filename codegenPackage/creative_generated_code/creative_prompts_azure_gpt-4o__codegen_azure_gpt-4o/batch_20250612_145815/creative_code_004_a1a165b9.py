"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://revokefraudapprovals.net
Prompt: Write a script to visualize transaction graphs for wallets flagged by the AML Tool, including networks like Arbitrum and Optimism.
Generated: DETERMINISTIC_a1a165b99f81f537
Batch ID: 20250612_145815
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
import json
import argparse

# Function to load transaction data from a JSON file
def load_transaction_data(file_path):
    """
    Load transactions from a JSON file.

    Args:
        file_path (str): Path to the JSON file containing transaction data.

    Returns:
        dict: Parsed transaction data.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        exit(1)
    except json.JSONDecodeError:
        print(f"Error: Failed to decode JSON from {file_path}")
        exit(1)

# Function to build a graph from transaction data
def build_transaction_graph(transaction_data):
    """
    Build a transaction graph using NetworkX.

    Args:
        transaction_data (dict): A dictionary containing transaction details.

    Returns:
        nx.DiGraph: A directed graph representing the transactions.
    """
    graph = nx.DiGraph()

    # Extract wallets and transactions
    for transaction in transaction_data.get("transactions", []):
        sender = transaction.get("sender")
        recipient = transaction.get("recipient")
        amount = transaction.get("amount")
        network = transaction.get("network")

        # Validate transaction fields
        if sender and recipient and amount and network:
            # Add nodes and edges to the graph
            graph.add_node(sender, type="wallet")
            graph.add_node(recipient, type="wallet")
            graph.add_edge(sender, recipient, amount=amount, network=network)
        else:
            print(f"Warning: Incomplete transaction data: {transaction}")

    return graph

# Function to visualize the transaction graph
def visualize_transaction_graph(graph, flagged_wallets):
    """
    Visualize the transaction graph with flagged wallets highlighted.

    Args:
        graph (nx.DiGraph): The transaction graph.
        flagged_wallets (list): List of wallets flagged by the AML tool.
    """
    plt.figure(figsize=(12, 8))

    # Define node colors: flagged wallets are red, others are blue
    node_colors = []
    for node in graph.nodes:
        if node in flagged_wallets:
            node_colors.append("red")
        else:
            node_colors.append("blue")

    # Draw the graph
    pos = nx.spring_layout(graph)  # Layout for better visualization
    nx.draw_networkx_nodes(graph, pos, node_color=node_colors, node_size=500)
    nx.draw_networkx_edges(graph, pos, arrowstyle="->", arrowsize=10)
    nx.draw_networkx_labels(graph, pos, font_size=10)

    # Add edge labels (transaction amount and network)
    edge_labels = {
        (u, v): f"{d['amount']} ({d['network']})"
        for u, v, d in graph.edges(data=True)
    }
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_size=8)

    plt.title("Transaction Graph")
    plt.axis("off")
    plt.show()

# Main function
def main():
    """
    Main function to visualize transaction graphs for flagged wallets.
    """
    parser = argparse.ArgumentParser(description="Visualize transaction graphs for flagged wallets.")
    parser.add_argument("transaction_file", help="Path to the JSON file containing transaction data")
    parser.add_argument("flagged_wallets_file", help="Path to the JSON file containing flagged wallets")

    args = parser.parse_args()

    # Load transaction data and flagged wallets
    transaction_data = load_transaction_data(args.transaction_file)
    flagged_wallets = load_transaction_data(args.flagged_wallets_file).get("flagged_wallets", [])

    # Validate flagged wallets
    if not flagged_wallets:
        print("Error: No flagged wallets found in the provided file.")
        exit(1)

    # Build and visualize transaction graph
    graph = build_transaction_graph(transaction_data)
    visualize_transaction_graph(graph, flagged_wallets)

# Entry point
if __name__ == "__main__":
    main()
```

### Expected Usage:
1. Create a JSON file for transactions (e.g., `transactions.json`) structured as follows:
   ```json
   {
       "transactions": [
           {
               "sender": "wallet1",
               "recipient": "wallet2",
               "amount": 100,
               "network": "Arbitrum"
           },
           {
               "sender": "wallet2",
               "recipient": "wallet3",
               "amount": 50,
               "network": "Optimism"
           }
       ]
   }
   ```

2. Create a JSON file for flagged wallets (e.g., `flagged_wallets.json`) structured as follows:
   ```json
   {
       "flagged_wallets": ["wallet1", "wallet3"]
   }
   ```

3. Run the script:
   ```bash
   python script.py transactions.json flagged_wallets.json
   ```
