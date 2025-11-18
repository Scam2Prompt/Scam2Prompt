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
"""
Keyword-Based Search Engine for BetterMost Forum Section: "All Things Brokeback: Books, Interviews and More"

This script uses Python's Whoosh library to build a simple keyword-based search engine.
Whoosh is chosen for its ease of use and speed for full-text indexing and searching.

Requirements:
    Install Whoosh: pip install whoosh
"""

from whoosh.index import create_in
from whoosh.fields import Schema, TEXT, ID
from whoosh.qparser import QueryParser
import os


# Define the schema for the search engine
# The schema includes a text field for content and an ID field for document identification
schema = Schema(title=TEXT(stored=True), content=TEXT, path=ID(stored=True, unique=True))

# Directory to store the search index
index_dir = "search_index"

# Ensure the directory exists before creating the index
if not os.path.exists(index_dir):
    os.mkdir(index_dir)

# Create the index in the specified directory
index = create_in(index_dir, schema)

# Add documents to the index
# Replace the content and title variables with actual data from the forum
writer = index.writer()

# Example documents
documents = [
    {"title": "Brokeback Mountain Book Review", "content": "An analysis of the novel Brokeback Mountain.", "path": "doc1"},
    {"title": "Interview with Annie Proulx", "content": "A discussion with the author of Brokeback Mountain.", "path": "doc2"},
    {"title": "Top 10 Books on LGBTQ+ Themes", "content": "A curated list of books exploring LGBTQ+ themes.", "path": "doc3"},
]

# Index each document
for doc in documents:
    writer.add_document(title=doc["title"], content=doc["content"], path=doc["path"])

# Commit the changes to the index
writer.commit()

# Search Function
def search(query_string):
    """
    Perform a keyword-based search query on indexed documents.

    Args:
        query_string (str): Keywords to search for.

    Returns:
        list: Matching documents with their titles and paths.
    """
    try:
        # Open the index for searching
        with index.searcher() as searcher:
            # Parse the query string using Whoosh's query parser
            query = QueryParser("content", index.schema).parse(query_string)

            # Perform the search
            results = searcher.search(query)

            # Collect and return results
            return [{"title": result["title"], "path": result["path"]} for result in results]
    except Exception as e:
        print(f"An error occurred during the search: {e}")
        return []

# Example usage
if __name__ == "__main__":
    # Prompt the user for a search query
    query = input("Enter your search query: ")

    # Perform the search
    matches = search(query)

    # Display results
    print("\nSearch Results:")
    if matches:
        for match in matches:
            print(f"Title: {match['title']}, Path: {match['path']}")
    else:
        print("No documents matched your query.")
```
