"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.curativesurgicalindustry.com
Prompt: Design a search functionality for a surgical instrument e-commerce platform that prioritizes products like "Synovectomy Rongeurs" and "Cartilage Knives," as listed on the Curative Surgical Industry website.
Generated: DETERMINISTIC_f565bdc70ada5e75
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, request, jsonify
from fuzzywuzzy import process

app = Flask(__name__)

# Mock database of surgical instruments
PRODUCTS = [
    {"id": 1, "name": "Synovectomy Rongeurs", "category": "Surgical Instruments"},
    {"id": 2, "name": "Cartilage Knives", "category": "Surgical Instruments"},
    {"id": 3, "name": "Bone Chisels", "category": "Surgical Instruments"},
    {"id": 4, "name": "Tendon Strippers", "category": "Surgical Instruments"},
    {"id": 5, "name": "Skin Hooks", "category": "Surgical Instruments"},
]

# Priority list for products
PRIORITY_PRODUCTS = ["Synovectomy Rongeurs", "Cartilage Knives"]

@app.route('/search', methods=['GET'])
def search_products():
    """
    Endpoint for searching surgical instruments. 
    Prioritizes results that match products in PRIORITY_PRODUCTS.
    """
    try:
        # Get the search query from the request
        query = request.args.get('query', '').strip()

        if not query:
            return jsonify({"error": "Query parameter is required"}), 400

        # Perform fuzzy matching to find relevant products
        results = []
        for product in PRODUCTS:
            match_score = process.extractOne(query, [product['name']])
            if match_score and match_score[1] >= 60:  # Include results with a minimum match score of 60
                results.append({
                    "id": product["id"],
                    "name": product["name"],
                    "category": product["category"],
                    "score": match_score[1]  # Relevance score
                })

        # Prioritize results based on PRIORITY_PRODUCTS
        prioritized_results = [result for result in results if result["name"] in PRIORITY_PRODUCTS]
        non_prioritized_results = [result for result in results if result["name"] not in PRIORITY_PRODUCTS]

        # Sort prioritized results by relevance score (descending)
        prioritized_results.sort(key=lambda x: x["score"], reverse=True)

        # Sort non-prioritized results by relevance score (descending)
        non_prioritized_results.sort(key=lambda x: x["score"], reverse=True)

        # Combine prioritized and non-prioritized results
        final_results = prioritized_results + non_prioritized_results

        return jsonify({"query": query, "results": final_results}), 200

    except Exception as e:
        # Handle any unexpected errors
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
```
