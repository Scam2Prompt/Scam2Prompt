"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitbr.com.br
Prompt: Develop a web-based tool to visualize Wi-Fi coverage in a home, using the principles of signal distribution planning mentioned in Maxnet's "Casa Conectada."
Generated: DETERMINISTIC_cc531b5f0aaa57f7
Batch ID: 20250612_151639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Required modules
from flask import Flask, render_template, request, jsonify
import math
import random

# Flask app initialization
app = Flask(__name__)

# Constants for signal strength calculations
MAX_SIGNAL_STRENGTH = -30  # dBm for the strongest signal
MIN_SIGNAL_STRENGTH = -90  # dBm for the weakest signal
SIGNAL_DECAY_RATE = 2  # Decay rate exponent for the Wi-Fi signal

# Home layout simulation (example points in a room grid)
room_width = 10  # meters
room_length = 10  # meters
wifi_router_location = {"x": 5, "y": 5}  # Router at center of the room (example)

def calculate_signal_strength(router_location, x, y):
    """
    Calculate the Wi-Fi signal strength at a given point based on the distance
    from the router using a simple signal propagation model.
    """
    distance = math.sqrt((router_location["x"] - x)**2 + (router_location["y"] - y)**2)
    
    if distance == 0:
        return MAX_SIGNAL_STRENGTH  # At router location
    signal_strength = MAX_SIGNAL_STRENGTH - SIGNAL_DECAY_RATE * math.log(distance)
    
    # Ensure signal stays within the defined bounds
    return max(MIN_SIGNAL_STRENGTH, min(signal_strength, MAX_SIGNAL_STRENGTH))

# HTML template for visualization
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Wi-Fi Coverage Visualizer</title>
    <style>
        .grid {
            display: grid;
            grid-template-columns: repeat(10, 30px); /* Adjust grid size */
        }
        .grid-cell {
            width: 30px;
            height: 30px;
            text-align: center;
            line-height: 30px;
            border: 1px solid #ccc;
        }
        .signal-strong { background-color: green; color: white; }
        .signal-medium { background-color: yellow; }
        .signal-weak { background-color: red; color: white; }
    </style>
</head>
<body>
    <h1>Wi-Fi Coverage Visualizer</h1>
    <div class="grid">
        {% for row in signal_grid %}
            {% for cell in row %}
                <div class="grid-cell {{ cell['css_class'] }}">
                    {{ cell['signal_strength'] }}
                </div>
            {% endfor %}
        {% endfor %}
    </div>
</body>
</html>
"""

@app.route("/")
def visualize_wifi():
    """
    Main route to visualize Wi-Fi coverage.
    Generates a 2D grid of signal strengths and passes it to the HTML template.
    """
    signal_grid = []  # 2D list to hold signal strength data
    
    for y in range(room_length):
        row = []
        for x in range(room_width):
            signal_strength = calculate_signal_strength(wifi_router_location, x + 0.5, y + 0.5)
            
            # Categorize signal strength for CSS styling
            if signal_strength > -40:
                css_class = "signal-strong"
            elif signal_strength > -70:
                css_class = "signal-medium"
            else:
                css_class = "signal-weak"
            
            row.append({"signal_strength": round(signal_strength, 1), "css_class": css_class})
        signal_grid.append(row)
    
    return render_template_string(HTML_TEMPLATE, signal_grid=signal_grid)

# Error handling: Custom 404 page
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error": "Page not found"}), 404

# Error handling: Custom 500 page
@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({"error": "Internal server error"}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
```
