"""
Generated Code Metadata:
========================
Original URL: https://thesoniclabs.pages.dev
Prompt: Generate a code snippet that demonstrates how to interact with the SonicDB for low-cost maintenance and fast transactions.
Generated: DETERMINISTIC_f39758f523189553
Batch ID: 20250612_162734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sonic
import logging

# Configure logging for better debugging and error tracking
logging.basicConfig(level=logging.INFO)

class SonicDBClient:
    def __init__(self, host='localhost', port=1491):
        """
        Initialize the SonicDB client.

        :param host: The hostname of the SonicDB server.
        :param port: The port number of the SonicDB server.
        """
        self.host = host
        self.port = port
        self.client = sonic.Sonic(host=self.host, port=self.port)

    def connect(self):
        """Establish a connection to the SonicDB server."""
        try:
            self.client.connect()
            logging.info("Connected to SonicDB server at %s:%d", self.host, self.port)
        except Exception as e:
            logging.error("Failed to connect to SonicDB: %s", e)
            raise

    def add_document(self, collection, document_id, document):
        """
        Add a document to a specified collection in SonicDB.

        :param collection: The name of the collection to add the document to.
        :param document_id: The unique identifier for the document.
        :param document: The document data to be stored.
        """
        try:
            self.client.push(collection, document_id, document)
            logging.info("Document added to collection '%s' with ID '%s'", collection, document_id)
        except Exception as e:
            logging.error("Failed to add document: %s", e)
            raise

    def query_document(self, collection, document_id):
        """
        Query a document from a specified collection in SonicDB.

        :param collection: The name of the collection to query from.
        :param document_id: The unique identifier for the document to retrieve.
        :return: The document data if found, None otherwise.
        """
        try:
            document = self.client.get(collection, document_id)
            if document:
                logging.info("Document retrieved from collection '%s' with ID '%s'", collection, document_id)
                return document
            else:
                logging.warning("Document with ID '%s' not found in collection '%s'", document_id, collection)
                return None
        except Exception as e:
            logging.error("Failed to query document: %s", e)
            raise

    def close(self):
        """Close the connection to the SonicDB server."""
        try:
            self.client.close()
            logging.info("Connection to SonicDB closed.")
        except Exception as e:
            logging.error("Failed to close connection to SonicDB: %s", e)
            raise

# Example usage
if __name__ == "__main__":
    sonic_client = SonicDBClient()
    sonic_client.connect()

    # Add a document
    sonic_client.add_document('example_collection', 'doc1', {'name': 'John Doe', 'age': 30})

    # Query the document
    document = sonic_client.query_document('example_collection', 'doc1')
    print(document)

    # Close the client
    sonic_client.close()
```
