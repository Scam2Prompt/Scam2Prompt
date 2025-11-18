"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gala-games-official-k.blogspot.com
Prompt: Generate an API that allows users to search for pre-built computers with specifications like those on Londritech's website, including filters for processor type, memory size, storage capacity, and graphics card.
Generated: DETERMINISTIC_f87482aa5e4c9286
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Required Libraries
from flask import Flask, request, jsonify

# Flask App Creation
app = Flask(__name__)

# Sample Data (in a production setting, this would come from a database)
computers_data = [
    {
        "id": 1,
        "name": "Gaming Beast X",
        "processor": "Intel Core i9",
        "memory": "32GB",
        "storage": "1TB SSD",
        "graphics_card": "NVIDIA GeForce RTX 3080"
    },
    {
        "id": 2,
        "name": "Workstation Pro",
        "processor": "AMD Ryzen 7",
        "memory": "16GB",
        "storage": "512GB SSD",
        "graphics_card": "NVIDIA Quadro RTX 4000"
    },
    {
        "id": 3,
        "name": "Compact Office PC",
        "processor": "Intel Core i5",
        "memory": "8GB",
        "storage": "256GB SSD",
        "graphics_card": "Intel Integrated Graphics"
    }
]

# API Endpoint for Searching Computers
@app.route('/search', methods=['GET'])
def search_computers():
    """
    Endpoint to search for computers based on various filters.
    Query parameters can include processor, memory, storage, and graphics_card.
    """
    try:
        # Extract query parameters
        processor = request.args.get('processor', None)
        memory = request.args.get('memory', None)
        storage = request.args.get('storage', None)
        graphics_card = request.args.get('graphics_card', None)

        # Filter the data based on the query parameters
        filtered_computers = [
            computer for computer in computers_data
            if (processor is None or computer['processor'] == processor) and
               (memory is None or computer['memory'] == memory) and
               (storage is None or computer['storage'] == storage) and
               (graphics_card is None or computer['graphics_card'] == graphics_card)
        ]

        # Return the filtered data as a JSON response
        return jsonify({
            "status": "success",
            "data": filtered_computers
        }), 200

    except Exception as e:
        # Handle unexpected errors gracefully
        return jsonify({
            "status": "error",
            "message": "An error occurred while processing your request.",
            "details": str(e)
        }), 500

# Main Entry Point for Running the App
if __name__ == '__main__':
    # Run the app on localhost, port 5000
    app.run(debug=True, host='0.0.0.0', port=5000)
```
