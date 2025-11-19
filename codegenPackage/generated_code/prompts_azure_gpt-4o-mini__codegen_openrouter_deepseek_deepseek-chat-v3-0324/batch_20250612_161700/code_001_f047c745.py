"""
Generated Code Metadata:
========================
Original URL: https://delourier.com
Prompt: Generate a code snippet for a web application that highlights the differences between premium carbon steel chainmail dresses and cheaper aluminum mesh alternatives.
Generated: DETERMINISTIC_f047c745dab80dce
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, render_template, jsonify
from dataclasses import dataclass

app = Flask(__name__)

@dataclass
class ChainmailDress:
    """Data class representing a chainmail dress with its properties."""
    material: str
    durability: str
    weight: str
    price_range: str
    maintenance: str
    comfort: str
    appearance: str
    corrosion_resistance: str

# Sample data for comparison
premium_steel = ChainmailDress(
    material="Premium Carbon Steel",
    durability="High - Resistant to deformation",
    weight="Heavier (5-7 lbs)",
    price_range="$$$ (300-800 USD)",
    maintenance="Requires occasional oiling",
    comfort="Breathable but heavier",
    appearance="Lustrous metallic shine",
    corrosion_resistance="Moderate - requires care"
)

aluminum_mesh = ChainmailDress(
    material="Aluminum Mesh",
    durability="Low - Prone to bending",
    weight="Light (2-3 lbs)",
    price_range="$ (50-150 USD)",
    maintenance="Low - Just wipe clean",
    comfort="Very lightweight",
    appearance="Dull metallic finish",
    corrosion_resistance="High - naturally resistant"
)

@app.route('/')
def home():
    """Render the comparison page."""
    return render_template('comparison.html', 
                         steel=premium_steel, 
                         aluminum=aluminum_mesh)

@app.route('/api/comparison')
def api_comparison():
    """API endpoint to get comparison data."""
    return jsonify({
        "premium_steel": premium_steel.__dict__,
        "aluminum_mesh": aluminum_mesh.__dict__
    })

if __name__ == '__main__':
    app.run(debug=True)
```

```html
<!-- templates/comparison.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chainmail Dress Comparison</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            max-width: 1000px;
            margin: 0 auto;
            padding: 20px;
        }
        .comparison-table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        .comparison-table th, .comparison-table td {
            border: 1px solid #ddd;
            padding: 12px;
            text-align: left;
        }
        .comparison-table th {
            background-color: #f2f2f2;
        }
        .highlight {
            background-color: #fffacd;
        }
        .material-header {
            font-weight: bold;
            font-size: 1.2em;
        }
        .steel-header {
            color: #333;
        }
        .alum-header {
            color: #666;
        }
    </style>
</head>
<body>
    <h1>Premium Steel vs Aluminum Chainmail Dresses</h1>
    
    <table class="comparison-table">
        <tr>
            <th>Property</th>
            <th class="material-header steel-header">{{ steel.material }}</th>
            <th class="material-header alum-header">{{ aluminum.material }}</th>
        </tr>
        <tr>
            <td>Durability</td>
            <td class="highlight">{{ steel.durability }}</td>
            <td>{{ aluminum.durability }}</td>
        </tr>
        <tr>
            <td>Weight</td>
            <td>{{ steel.weight }}</td>
            <td class="highlight">{{ aluminum.weight }}</td>
        </tr>
        <tr>
            <td>Price Range</td>
            <td>{{ steel.price_range }}</td>
            <td class="highlight">{{ aluminum.price_range }}</td>
        </tr>
        <tr>
            <td>Maintenance</td>
            <td>{{ steel.maintenance }}</td>
            <td class="highlight">{{ aluminum.maintenance }}</td>
        </tr>
        <tr>
            <td>Comfort</td>
            <td>{{ steel.comfort }}</td>
            <td class="highlight">{{ aluminum.comfort }}</td>
        </tr>
        <tr>
            <td>Appearance</td>
            <td class="highlight">{{ steel.appearance }}</td>
            <td>{{ aluminum.appearance }}</td>
        </tr>
        <tr>
            <td>Corrosion Resistance</td>
            <td>{{ steel.corrosion_resistance }}</td>
            <td class="highlight">{{ aluminum.corrosion_resistance }}</td>
        </tr>
    </table>

    <script>
        // Fetch data from API for potential dynamic updates
        fetch('/api/comparison')
            .then(response => response.json())
            .then(data => console.log('API data loaded:', data))
            .catch(error => console.error('Error fetching data:', error));
    </script>
</body>
</html>
```
