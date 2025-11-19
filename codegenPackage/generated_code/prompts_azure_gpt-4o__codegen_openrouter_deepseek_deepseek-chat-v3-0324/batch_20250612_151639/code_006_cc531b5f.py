"""
Generated Code Metadata:
========================
Original URL: https://bitbr.com.br
Prompt: Develop a web-based tool to visualize Wi-Fi coverage in a home, using the principles of signal distribution planning mentioned in Maxnet's "Casa Conectada."
Generated: DETERMINISTIC_cc531b5f0aaa57f7
Batch ID: 20250612_151639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# wifi_coverage_visualizer.py
import json
import math
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
from collections import defaultdict

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'json'}

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

class WiFiCoverageCalculator:
    """
    Class to calculate WiFi signal coverage based on router position and home layout.
    """
    def __init__(self):
        self.signal_strength = {
            'excellent': -50,
            'good': -60,
            'fair': -70,
            'weak': -80
        }
        self.router_specs = {
            'default': {
                'frequency': 2.4,  # GHz
                'tx_power': 20,    # dBm
                'antenna_gain': 2, # dBi
                'sensitivity': -90 # dBm
            }
        }

    def calculate_signal_strength(self, distance, router_type='default', obstacles=0):
        """
        Calculate signal strength at a given distance from the router.
        Uses free space path loss model with obstacle attenuation.
        """
        specs = self.router_specs[router_type]
        frequency = specs['frequency']
        tx_power = specs['tx_power']
        antenna_gain = specs['antenna_gain']
        
        # Free space path loss
        fspl = 20 * math.log10(distance) + 20 * math.log10(frequency) + 32.44
        # Total signal strength
        signal = tx_power + antenna_gain * 2 - fspl - (obstacles * 5)
        
        return signal

    def get_coverage_quality(self, signal):
        """
        Determine coverage quality based on signal strength.
        """
        if signal >= self.signal_strength['excellent']:
            return 'excellent'
        elif signal >= self.signal_strength['good']:
            return 'good'
        elif signal >= self.signal_strength['fair']:
            return 'fair'
        elif signal >= self.signal_strength['weak']:
            return 'weak'
        else:
            return 'none'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/')
def index():
    """Render the main visualization page."""
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    """Handle floor plan upload."""
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        try:
            with open(filepath, 'r') as f:
                floor_data = json.load(f)
            return jsonify({'message': 'File uploaded successfully', 'data': floor_data}), 200
        except json.JSONDecodeError:
            return jsonify({'error': 'Invalid JSON file'}), 400
    
    return jsonify({'error': 'File type not allowed'}), 400

@app.route('/calculate_coverage', methods=['POST'])
def calculate_coverage():
    """Calculate WiFi coverage based on input parameters."""
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        floor_plan = data.get('floor_plan')
        router_position = data.get('router_position')
        router_type = data.get('router_type', 'default')
        
        if not floor_plan or not router_position:
            return jsonify({'error': 'Missing required parameters'}), 400
        
        calculator = WiFiCoverageCalculator()
        coverage_data = defaultdict(dict)
        
        # Calculate coverage for each point in the floor plan
        for y, row in enumerate(floor_plan):
            for x, cell in enumerate(row):
                if cell == 'wall':
                    continue
                
                # Calculate distance from router
                distance = math.sqrt((x - router_position['x'])**2 + (y - router_position['y'])**2)
                obstacles = data.get('obstacles', {}).get(f'{x},{y}', 0)
                
                # Calculate signal strength
                signal = calculator.calculate_signal_strength(
                    distance, router_type, obstacles
                )
                
                # Determine coverage quality
                quality = calculator.get_coverage_quality(signal)
                coverage_data[y][x] = quality
        
        return jsonify({
            'coverage': coverage_data,
            'router_position': router_position
        }), 200
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WiFi Coverage Visualizer</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
            text-align: center;
        }
        .grid-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            margin: 20px 0;
        }
        .grid {
            display: grid;
            gap: 1px;
            background-color: #ddd;
            border: 1px solid #ddd;
        }
        .cell {
            width: 30px;
            height: 30px;
            background-color: white;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
        }
        .cell.wall {
            background-color: #333;
        }
        .cell.router {
            background-color: #ff5722;
        }
        .cell.excellent {
            background-color: #4CAF50;
        }
        .cell.good {
            background-color: #8BC34A;
        }
        .cell.fair {
            background-color: #FFC107;
        }
        .cell.weak {
            background-color: #FF9800;
        }
        .cell.none {
            background-color: #F44336;
        }
        .controls {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            margin-bottom: 20px;
        }
        .control-group {
            flex: 1;
            min-width: 200px;
        }
        button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 4px;
            cursor: pointer;
            margin-top: 10px;
        }
        button:hover {
            background-color: #45a049;
        }
        .legend {
            display: flex;
            justify-content: center;
            gap: 15px;
            margin: 20px 0;
            flex-wrap: wrap;
        }
        .legend-item {
            display: flex;
            align-items: center;
            gap: 5px;
        }
        .legend-color {
            width: 20px;
            height: 20px;
            border: 1px solid #ddd;
        }
        input, select {
            padding: 8px;
            width: 100%;
            box-sizing: border-box;
            margin: 5px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>WiFi Coverage Visualizer</h1>
        
        <div class="controls">
            <div class="control-group">
                <h3>Floor Plan</h3>
                <input type="file" id="floorPlanFile" accept=".json">
                <button id="uploadBtn">Upload Floor Plan</button>
                <div>
                    <label for="gridWidth">Width:</label>
                    <input type="number" id="gridWidth" min="5" max="50" value="15">
                    <label for="gridHeight">Height:</label>
                    <input type="number" id="gridHeight" min="5" max="50" value="10">
                    <button id
