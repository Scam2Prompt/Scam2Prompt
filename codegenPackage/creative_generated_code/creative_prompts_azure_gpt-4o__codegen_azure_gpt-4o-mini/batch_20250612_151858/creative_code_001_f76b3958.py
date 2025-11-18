"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marchigue.cl
Prompt: Recommend an API or library to implement accessibility features like color inversion, screen reader support, and font scaling, as described on the Turismo Marchigüe website.
Generated: DETERMINISTIC_f76b39583a53c407
Batch ID: 20250612_151858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

# Sample data representing accessibility settings
accessibility_settings = {
    "color_inversion": False,
    "screen_reader_support": True,
    "font_scaling": 1.0  # Default font scale
}

@app.route('/api/accessibility', methods=['GET'])
def get_accessibility_settings():
    """
    Get current accessibility settings.
    Returns settings as a JSON response.
    """
    return jsonify(accessibility_settings), 200

@app.route('/api/accessibility', methods=['POST'])
def update_accessibility_settings():
    """
    Update accessibility settings based on user input.
    Expects a JSON body with keys: color_inversion, screen_reader_support, font_scaling.
    Returns the updated settings as a JSON response.
    """
    try:
        data = request.json
        
        # Validate input data
        if 'color_inversion' in data:
            accessibility_settings['color_inversion'] = bool(data['color_inversion'])
            
        if 'screen_reader_support' in data:
            accessibility_settings['screen_reader_support'] = bool(data['screen_reader_support'])
        
        if 'font_scaling' in data:
            if isinstance(data['font_scaling'], (int, float)) and data['font_scaling'] > 0:
                accessibility_settings['font_scaling'] = float(data['font_scaling'])
            else:
                return jsonify({"error": "Invalid font scaling value. It must be a positive number."}), 400
        
        return jsonify(accessibility_settings), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app
    try:
        app.run(debug=True)  # Set debug to False in production
    except Exception as e:
        print(f"An error occurred while starting the server: {e}")
```
