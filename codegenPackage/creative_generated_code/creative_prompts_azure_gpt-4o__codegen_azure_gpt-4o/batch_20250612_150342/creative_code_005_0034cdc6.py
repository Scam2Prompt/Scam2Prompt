"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://graphpool.net
Prompt: Provide a code example for creating and querying a graph database, referencing specific details from graphpool.net.
Generated: DETERMINISTIC_0034cdc626b61047
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script demonstrates how to create and query a graph database using the Neo4j Python driver.
Neo4j is a popular graph database often used for storing, managing, and querying graph data.
Graphpool.net is a resource for exploring graph-based solutions like Neo4j.
"""

from neo4j import GraphDatabase

class GraphDatabaseExample:
    def __init__(self, uri, user, password):
        """
        Initialize the connection to the Neo4j database.
        
        :param uri: The URI of the Neo4j instance (e.g., bolt://localhost:7687)
        :param user: Username for authentication
        :param password: Password for authentication
        """
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        """
        Close the connection to the database.
        """
        self.driver.close()

    def create_data(self):
        """
        Create nodes and relationships in the graph database.
        """
        with self.driver.session() as session:
            # Create nodes and relationships
            session.write_transaction(self._create_nodes_and_relationships)

    @staticmethod
    def _create_nodes_and_relationships(tx):
        """
        Helper method to create nodes and relationships in a transaction.

        :param tx: Transaction object
        """
        # Create nodes
        tx.run("""
            CREATE (a:Person {name: 'Alice', age: 30})
            CREATE (b:Person {name: 'Bob', age: 25})
            CREATE (c:Person {name: 'Charlie', age: 35})
        """)

        # Create relationships
        tx.run("""
            MATCH (a:Person {name: 'Alice'}), (b:Person {name: 'Bob'})
            CREATE (a)-[:FRIEND]->(b)
        """)
        tx.run("""
            MATCH (b:Person {name: 'Bob'}), (c:Person {name: 'Charlie'})
            CREATE (b)-[:FRIEND]->(c)
        """)

    def query_data(self):
        """
        Query the graph database to retrieve information.
        """
        with self.driver.session() as session:
            # Execute a read transaction to query data
            result = session.read_transaction(self._find_friends_of_bob)
            for record in result:
                print(f"Bob is friends with: {record['friend']}")

    @staticmethod
    def _find_friends_of_bob(tx):
        """
        Helper method to find all friends of Bob.

        :param tx: Transaction object
        :return: Friends of Bob
        """
        query = """
            MATCH (:Person {name: 'Bob'})-[:FRIEND]->(friend)
            RETURN friend.name AS friend
        """
        return tx.run(query)

if __name__ == "__main__":
    # Configuration details (update with your Neo4j credentials)
    URI = "bolt://localhost:7687"
    USER = "neo4j"
    PASSWORD = "password"

    try:
        # Instantiate the graph database example class
        graph_db = GraphDatabaseExample(URI, USER, PASSWORD)

        # Create data
        graph_db.create_data()

        # Query data
        graph_db.query_data()
    except Exception as e:
        # Handle any errors that occur during database operations
        print(f"An error occurred: {e}")
    finally:
        # Ensure the connection is closed
        graph_db.close()
```
