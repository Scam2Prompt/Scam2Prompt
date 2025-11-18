"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gala-games-ezx.blogspot.com
Prompt: Generate code to implement a search functionality for a tool catalog, allowing users to filter by categories such as "auto center," "compressors," and "construction civil," based on the structure of the Anhanguera Ferramentas website.
Generated: DETERMINISTIC_d8b802d29a057183
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample tool catalog data (in a real application, this could come from a database)
TOOL_CATALOG = [
    {"id": 1, "name": "Auto Center Tool A", "category": "auto center"},
    {"id": 2, "name": "Compressor Model X", "category": "compressors"},
    {"id": 3, "name": "Construction Tool B", "category": "construction civil"},
    {"id": 4, "name": "Auto Center Tool B", "category": "auto center"},
    {"id": 5, "name": "Compressor Model Y", "category": "compressors"},
    {"id": 6, "name": "Construction Tool C", "category": "construction civil"},
]

@app.route('/search', methods=['GET'])
def search_tools():
    """
    Search for tools in the catalog based on category filters.
    
    Query Parameters:
        - category (str): The category to filter tools by. Can be 'auto center',
                          'compressors', or 'construction civil'.
    
    Returns:
        - JSON response with a list of matching tools or a message if none found.
    """
    category = request.args.get('category', '').lower()
    
    # Validate input
    if category not in ['auto center', 'compressors', 'construction civil']:
        return jsonify({"error": "Invalid category. Please choose from 'auto center', 'compressors', or 'construction civil'."}), 400
    
    # Filter tools by category
    filtered_tools = [tool for tool in TOOL_CATALOG if tool['category'] == category]
    
    # Create response
    if filtered_tools:
        return jsonify(filtered_tools), 200
    else:
        return jsonify({"message": "No tools found in this category."}), 404

if __name__ == '__main__':
    try:
        app.run(debug=True)
    except Exception as e:
        print(f"An error occurred while starting the server: {e}")
```
