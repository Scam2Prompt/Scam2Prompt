"""
Generated Code Metadata:
========================
Original URL: https://sonic-labs.vercel.app
Prompt: How can developers leverage SonicDB for low-latency transactions in their applications?
Generated: DETERMINISTIC_e103901202a21d0c
Batch ID: 20250612_164046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sonic
import json
import time

class SonicDBClient:
    """
    A client for interacting with SonicDB for low-latency transactions.
    """

    def __init__(self, host='localhost', port=1491):
        """
        Initializes the SonicDB client.

        :param host: The hostname of the SonicDB server.
        :param port: The port number of the SonicDB server.
        """
        self.client = sonic.Sonic(host, port)
        self.client.connect()

    def add_document(self, collection, document_id, document):
        """
        Adds a document to the specified collection.

        :param collection: The name of the collection to add the document to.
        :param document_id: The unique ID for the document.
        :param document: The document data as a dictionary.
        :raises Exception: If there is an error adding the document.
        """
        try:
            # Convert the document to JSON format
            json_document = json.dumps(document)
            # Add the document to the collection
            self.client.push(collection, document_id, json_document)
            print(f"Document {document_id} added to collection '{collection}'.")
        except Exception as e:
            print(f"Error adding document: {e}")

    def get_document(self, collection, document_id):
        """
        Retrieves a document from the specified collection.

        :param collection: The name of the collection to retrieve the document from.
        :param document_id: The unique ID of the document to retrieve.
        :return: The document data as a dictionary, or None if not found.
        :raises Exception: If there is an error retrieving the document.
        """
        try:
            # Retrieve the document from the collection
            document = self.client.fetch(collection, document_id)
            if document:
                return json.loads(document)
            else:
                print(f"Document {document_id} not found in collection '{collection}'.")
                return None
        except Exception as e:
            print(f"Error retrieving document: {e}")
            return None

    def delete_document(self, collection, document_id):
        """
        Deletes a document from the specified collection.

        :param collection: The name of the collection to delete the document from.
        :param document_id: The unique ID of the document to delete.
        :raises Exception: If there is an error deleting the document.
        """
        try:
            # Delete the document from the collection
            self.client.delete(collection, document_id)
            print(f"Document {document_id} deleted from collection '{collection}'.")
        except Exception as e:
            print(f"Error deleting document: {e}")

    def close(self):
        """
        Closes the connection to the SonicDB server.
        """
        self.client.close()
        print("Connection to SonicDB closed.")

# Example usage
if __name__ == "__main__":
    sonic_client = SonicDBClient()

    # Example document
    example_document = {
        "title": "Low Latency Transactions",
        "content": "Using SonicDB for efficient data retrieval."
    }

    # Add a document
    sonic_client.add_document("example_collection", "doc1", example_document)

    # Retrieve the document
    retrieved_doc = sonic_client.get_document("example_collection", "doc1")
    print("Retrieved Document:", retrieved_doc)

    # Delete the document
    sonic_client.delete_document("example_collection", "doc1")

    # Close the client
    sonic_client.close()
```
