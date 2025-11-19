"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://the-graph.network
Prompt: What are the roles of Indexer, Curator, and Delegator in The Graph Network, and how can I implement them in an application?
Generated: DETERMINISTIC_29d81c513fa39652
Batch ID: 20250612_164236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class GraphNetwork:
    def __init__(self):
        """
        Initialize the Graph Network with empty roles.
        """
        self.indexers = {}
        self.curators = {}
        self.delegators = {}

    def add_indexer(self, indexer_id, stake):
        """
        Add an indexer to the network.

        :param indexer_id: Unique identifier for the indexer
        :param stake: Amount of stake the indexer is putting into the network
        """
        if indexer_id in self.indexers:
            raise ValueError(f"Indexer {indexer_id} already exists.")
        self.indexers[indexer_id] = {'stake': stake, 'subgraphs': []}
        print(f"Indexer {indexer_id} added with stake {stake}.")

    def add_curator(self, curator_id, shares):
        """
        Add a curator to the network.

        :param curator_id: Unique identifier for the curator
        :param shares: Amount of shares the curator is committing to subgraphs
        """
        if curator_id in self.curators:
            raise ValueError(f"Curator {curator_id} already exists.")
        self.curators[curator_id] = {'shares': shares}
        print(f"Curator {curator_id} added with shares {shares}.")

    def delegate(self, delegator_id, indexer_id, amount):
        """
        Delegate funds to an indexer.

        :param delegator_id: Unique identifier for the delegator
        :param indexer_id: The indexer to whom funds are being delegated
        :param amount: Amount of funds to delegate
        """
        if indexer_id not in self.indexers:
            raise ValueError(f"Indexer {indexer_id} does not exist.")
        if delegator_id in self.delegators:
            raise ValueError(f"Delegator {delegator_id} has already delegated.")
        self.delegators[delegator_id] = {'indexer_id': indexer_id, 'amount': amount}
        print(f"Delegator {delegator_id} has delegated {amount} to indexer {indexer_id}.")

    def get_indexer_info(self, indexer_id):
        """
        Retrieve information about a specific indexer.

        :param indexer_id: Unique identifier for the indexer
        :return: Information about the indexer or None if it doesn't exist
        """
        return self.indexers.get(indexer_id, None)

    def get_curator_info(self, curator_id):
        """
        Retrieve information about a specific curator.

        :param curator_id: Unique identifier for the curator
        :return: Information about the curator or None if it doesn't exist
        """
        return self.curators.get(curator_id, None)

    def get_delegator_info(self, delegator_id):
        """
        Retrieve information about a specific delegator.

        :param delegator_id: Unique identifier for the delegator
        :return: Information about the delegator or None if it doesn't exist
        """
        return self.delegators.get(delegator_id, None)


# Example of using the GraphNetwork class
if __name__ == "__main__":
    graph_network = GraphNetwork()

    try:
        graph_network.add_indexer("indexer1", 1000)
        graph_network.add_curator("curator1", 500)
        graph_network.delegate("delegator1", "indexer1", 250)

        print(graph_network.get_indexer_info("indexer1"))
        print(graph_network.get_curator_info("curator1"))
        print(graph_network.get_delegator_info("delegator1"))
    except Exception as e:
        print(f"Error occurred: {e}")
```
