"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pressaction.in
Prompt: Suggest a library for creating a keyword-based search tool for the "Press Action" website, and write code to implement it for categories like "क्राइम" and "खेल."
Generated: DETERMINISTIC_5668d893721951f5
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, request, jsonify
from whoosh.index import create_in, open_dir
from whoosh.fields import Schema, TEXT, KEYWORD
from whoosh.qparser import QueryParser
import os

# Initialize Flask app
app = Flask(__name__)

# Define schema for the keyword-based search
schema = Schema(title=TEXT(stored=True), content=TEXT(stored=True), category=KEYWORD(stored=True))

# Directory for storing the search index
INDEX_DIR = "search_index"

# Function to create the search index
def create_search_index():
    if not os.path.exists(INDEX_DIR):
        os.mkdir(INDEX_DIR)
        ix = create_in(INDEX_DIR, schema)
        writer = ix.writer()
        
        # Add sample data
        writer.add_document(title="क्राइम की खबर", content="यह एक क्राइम की खबर है।", category="क्राइम")
        writer.add_document(title="खेल की खबर", content="यह एक खेल की खबर है।", category="खेल")
        writer.add_document(title="क्राइम और खेल", content="क्राइम और खेल दोनों पर आधारित खबर।", category="क्राइम,खेल")
        writer.commit()

# Create the index if it doesn't exist
create_search_index()

# Route for searching based on category
@app.route('/search', methods=['GET'])
def search():
    try:
        # Get the category from the query parameters
        category = request.args.get('category', '').strip()
        
        # Open the existing index
        ix = open_dir(INDEX_DIR)
        searcher = ix.searcher()
        
        # Parse the query for the category field
        query = QueryParser("category", ix.schema).parse(category)
        results = searcher.search(query)
        
        # Prepare the response
        response = []
        for result in results:
            response.append({
                "title": result["title"],
                "content": result["content"],
                "category": result["category"]
            })
        
        return jsonify(response), 200
    except Exception as e:
        # Handle errors gracefully
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```
