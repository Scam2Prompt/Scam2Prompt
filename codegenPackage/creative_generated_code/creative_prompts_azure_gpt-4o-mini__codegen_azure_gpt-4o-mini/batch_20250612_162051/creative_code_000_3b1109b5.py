"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://createxpro.com
Prompt: Generate a code snippet for a web application that allows users to customize promotional items using CreatexPro's unique personalization techniques like serigraphy and DTF printing.
Generated: DETERMINISTIC_3b1109b5dc649964
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://code.jquery.com/jquery-3.6.0.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
from flask import Flask, render_template, request, jsonify
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Sample data for promotional items
PROMOTIONAL_ITEMS = [
    {"id": 1, "name": "T-Shirt", "techniques": ["Serigraphy", "DTF Printing"]},
    {"id": 2, "name": "Mug", "techniques": ["Serigraphy"]},
    {"id": 3, "name": "Cap", "techniques": ["DTF Printing"]},
]

@app.route('/')
def index():
    """Render the main page for customizing promotional items."""
    return render_template('index.html', items=PROMOTIONAL_ITEMS)

@app.route('/customize', methods=['POST'])
def customize():
    """Handle customization requests for promotional items.
    
    Args:
        user_data (dict): Data submitted by the user for customization.
        
    Returns:
        json: A JSON response indicating success or failure.
    """
    try:
        # Extract user data from the request
        user_data = request.json
        
        # Validate input
        if 'item_id' not in user_data or 'technique' not in user_data:
            raise ValueError("Invalid input: item_id and technique are required.")
        
        item_id = user_data['item_id']
        technique = user_data['technique']

        # Check if the item exists and supports the selected technique
        item = next((item for item in PROMOTIONAL_ITEMS if item['id'] == item_id), None)
        
        if item is None or technique not in item['techniques']:
            return jsonify({"success": False, "message": "Invalid item or technique."}), 400
        
        # Process customization (placeholder for actual logic)
        logging.info(f"Customizing item {item['name']} with technique {technique}.")
        
        return jsonify({"success": True, "message": f"{item['name']} customized successfully!"}), 200

    except ValueError as ve:
        logging.error(f"ValueError: {ve}")
        return jsonify({"success": False, "message": str(ve)}), 400
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return jsonify({"success": False, "message": "An unexpected error occurred."}), 500

if __name__ == '__main__':
    app.run(debug=False)  # Set debug=True for development, False for production
```

### index.html (Template File) - A basic structure for rendering
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Customize Promotional Items</title>
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
</head>
<body>
    <h1>Customize Your Promotional Items</h1>
    <select id="itemSelect">
        {% for item in items %}
            <option value="{{ item.id }}">{{ item.name }}</option>
        {% endfor %}
    </select>
    <select id="techniqueSelect">
        <option value="Serigraphy">Serigraphy</option>
        <option value="DTF Printing">DTF Printing</option>
    </select>
    <button id="customizeButton">Customize</button>

    <div id="resultMessage"></div>

    <script>
        $(document).ready(function() {
            $('#customizeButton').click(function() {
                const itemId = $('#itemSelect').val();
                const technique = $('#techniqueSelect').val();
                
                $.ajax({
                    url: '/customize',
                    type: 'POST',
                    contentType: 'application/json',
                    data: JSON.stringify({ item_id: itemId, technique: technique }),
                    success: function(response) {
                        $('#resultMessage').text(response.message);
                    },
                    error: function(xhr) {
                        $('#resultMessage').text(xhr.responseJSON.message);
                    }
                });
            });
        });
    </script>
</body>
</html>
```
