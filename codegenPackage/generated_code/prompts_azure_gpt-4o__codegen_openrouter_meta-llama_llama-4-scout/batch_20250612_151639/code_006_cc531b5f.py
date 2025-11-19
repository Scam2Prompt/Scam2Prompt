"""
Generated Code Metadata:
========================
Original URL: https://bitbr.com.br
Prompt: Develop a web-based tool to visualize Wi-Fi coverage in a home, using the principles of signal distribution planning mentioned in Maxnet's "Casa Conectada."
Generated: DETERMINISTIC_cc531b5f0aaa57f7
Batch ID: 20250612_151639
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdn.jsdelivr.net/npm/chart.js@3.7.1/dist/chart.min.js": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# app.py

import numpy as np
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Define a function to calculate signal strength at a given point
def calculate_signal_strength(tx_power, distance):
    """
    Calculate signal strength in dBm using the free space path loss formula.

    Args:
        tx_power (float): Transmit power in dBm
        distance (float): Distance from transmitter in meters

    Returns:
        float: Signal strength in dBm
    """
    # Free space path loss formula: FSPL (dB) = 20log10(d) + 20log10(f) + 32.44
    # Assume a frequency of 2.4 GHz (2400 MHz) for Wi-Fi
    frequency = 2400  # MHz
    fspl = 20 * np.log10(distance) + 20 * np.log10(frequency) + 32.44
    signal_strength = tx_power - fspl
    return signal_strength

# Define a function to generate a heatmap of Wi-Fi coverage
def generate_coverage_heatmap(tx_x, tx_y, tx_power, grid_size):
    """
    Generate a heatmap of Wi-Fi coverage.

    Args:
        tx_x (float): Transmitter x-coordinate
        tx_y (float): Transmitter y-coordinate
        tx_power (float): Transmit power in dBm
        grid_size (int): Grid size for the heatmap

    Returns:
        numpy.ndarray: Heatmap of Wi-Fi coverage
    """
    # Create a grid of points
    x = np.linspace(0, grid_size, grid_size)
    y = np.linspace(0, grid_size, grid_size)
    X, Y = np.meshgrid(x, y)

    # Calculate signal strength at each point
    distances = np.sqrt((X - tx_x) ** 2 + (Y - tx_y) ** 2)
    signal_strengths = np.array([calculate_signal_strength(tx_power, distance) for distance in distances.flatten()]).reshape(X.shape)

    return signal_strengths

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate_coverage', methods=['POST'])
def calculate_coverage():
    try:
        tx_x = float(request.form['tx_x'])
        tx_y = float(request.form['tx_y'])
        tx_power = float(request.form['tx_power'])
        grid_size = int(request.form['grid_size'])

        signal_strengths = generate_coverage_heatmap(tx_x, tx_y, tx_power, grid_size)

        # Return the heatmap as a JSON response
        return jsonify({
            'heatmap': signal_strengths.tolist(),
            'grid_size': grid_size
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/index.html -->

<!DOCTYPE html>
<html>
<head>
    <title>Wi-Fi Coverage Visualizer</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js@3.7.1/dist/chart.min.js"></script>
</head>
<body>
    <h1>Wi-Fi Coverage Visualizer</h1>
    <form id="coverage-form">
        <label for="tx_x">Transmitter X-coordinate:</label>
        <input type="number" id="tx_x" name="tx_x"><br><br>
        <label for="tx_y">Transmitter Y-coordinate:</label>
        <input type="number" id="tx_y" name="tx_y"><br><br>
        <label for="tx_power">Transmit Power (dBm):</label>
        <input type="number" id="tx_power" name="tx_power"><br><br>
        <label for="grid_size">Grid Size:</label>
        <input type="number" id="grid_size" name="grid_size"><br><br>
        <input type="submit" value="Calculate Coverage">
    </form>
    <canvas id="coverage-chart"></canvas>

    <script>
        const form = document.getElementById('coverage-form');
        const chartCanvas = document.getElementById('coverage-chart');

        form.addEventListener('submit', async (e) => {
            e.preventDefault();

            const formData = new FormData(form);
            const response = await fetch('/calculate_coverage', {
                method: 'POST',
                body: formData
            });

            const data = await response.json();

            if (data.error) {
                console.error(data.error);
                return;
            }

            const heatmap = data.heatmap;
            const gridSize = data.grid_size;

            const chart = new Chart(chartCanvas, {
                type: 'heatmap',
                data: {
                    datasets: [{
                        data: heatmap,
                        backgroundColor: (context) => {
                            const value = context.dataset.data[context.dataIndex];
                            return `rgba(0, 0, 255, ${value / 100})`;
                        }
                    }]
                },
                options: {
                    scales: {
                        x: {
                            max: gridSize
                        },
                        y: {
                            max: gridSize
                        }
                    }
                }
            });
        });
    </script>
</body>
</html>
```
