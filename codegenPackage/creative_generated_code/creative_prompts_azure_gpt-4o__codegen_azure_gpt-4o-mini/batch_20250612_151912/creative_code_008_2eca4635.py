"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bettermost.net
Prompt: Recommend tools or libraries to build a keyword-based search engine for the "All Things Brokeback: Books, Interviews and More" section of the BetterMost forum.
Generated: DETERMINISTIC_2eca4635f936170b
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import whoosh
from whoosh.index import create_in
from whoosh.fields import Schema, TEXT
from whoosh.qparser import QueryParser

# Define the schema for the search engine
schema = Schema(
    title=TEXT(stored=True),
    content=TEXT(stored=True)
)

# Function to create an index directory if it doesn't exist
def create_index(index_dir):
    """Creates a Whoosh index in the specified directory."""
    if not os.path.exists(index_dir):
        os.mkdir(index_dir)
    return create_in(index_dir, schema)

# Function to add documents to the index
def add_documents_to_index(index_dir, documents):
    """Adds a list of documents to the Whoosh index."""
    ix = whoosh.index.open_dir(index_dir)
    writer = ix.writer()
    for doc in documents:
        writer.add_document(title=doc['title'], content=doc['content'])
    writer.commit()

# Function to search the index
def search_index(index_dir, query_str):
    """Searches the Whoosh index for the given query string."""
    ix = whoosh.index.open_dir(index_dir)
    with ix.searcher() as searcher:
        query = QueryParser("content", ix.schema).parse(query_str)
        results = searcher.search(query)
        return [(result['title'], result['content']) for result in results]

# Example usage
if __name__ == "__main__":
    index_directory = "indexdir"

    # Sample documents to be indexed
    documents = [
        {"title": "Brokeback Mountain", "content": "A story of love and loss."},
        {"title": "Interviews with the Cast", "content": "Insights from the actors."},
        {"title": "Behind the Scenes", "content": "Making of the iconic film."},
    ]

    try:
        # Create index
        index = create_index(index_directory)

        # Add documents to index
        add_documents_to_index(index_directory, documents)

        # Perform a search
        search_query = "love"
        results = search_index(index_directory, search_query)

        # Display search results
        if results:
            for title, content in results:
                print(f"Title: {title}\nContent: {content}\n")
        else:
            print("No results found.")

    except Exception as e:
        print(f"An error occurred: {e}")
```
