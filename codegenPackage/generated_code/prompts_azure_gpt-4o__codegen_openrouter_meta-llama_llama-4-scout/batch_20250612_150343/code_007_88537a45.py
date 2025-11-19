"""
Generated Code Metadata:
========================
Original URL: https://strk.site
Prompt: Develop a Django or Flask application that replicates the functionality of the webpage's cost calculator for renovation services.
Generated: DETERMINISTIC_88537a45e4cb66ee
Batch ID: 20250612_150343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Renovation Cost Calculator Application using Flask**

### Directory Structure
```markdown
renovation_cost_calculator/
|---- app.py
|---- templates/
|       |---- index.html
|---- static/
|       |---- style.css
|---- requirements.txt
|---- config.py
```

### requirements.txt
```markdown
Flask==2.2.2
```

### config.py
```python
class Config:
    SECRET_KEY = 'secret_key_here'
```

### app.py
```python
from flask import Flask, render_template, request, jsonify
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Define renovation services with their respective costs per unit
renovation_services = {
    'flooring': {'cost_per_unit': 5.0, 'units': 'sqft'},
    'painting': {'cost_per_unit': 0.5, 'units': 'sqft'},
    'plumbing': {'cost_per_unit': 100.0, 'units': 'fixture'},
    'electrical': {'cost_per_unit': 50.0, 'units': 'fixture'},
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Get user input from the form
            service = request.form.get('service')
            area = float(request.form.get('area', 0))
            quantity = int(request.form.get('quantity', 0))

            # Calculate the cost based on user input
            if service in renovation_services:
                cost_per_unit = renovation_services[service]['cost_per_unit']
                total_cost = cost_per_unit * area * quantity
                return jsonify({'total_cost': f'${total_cost:.2f}'}),
                              200, {'ContentType': 'application/json'}
            else:
                return jsonify({'error': 'Invalid service selected'}), 400
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

### templates/index.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Renovation Cost Calculator</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
    <h1>Renovation Cost Calculator</h1>
    <form id="cost-calculator-form">
        <label for="service">Select Service:</label>
        <select id="service" name="service">
            <option value="flooring">Flooring</option>
            <option value="painting">Painting</option>
            <option value="plumbing">Plumbing</option>
            <option value="electrical">Electrical</option>
        </select><br><br>
        <label for="area">Enter Area (sqft):</label>
        <input type="number" id="area" name="area" step="0.01"><br><br>
        <label for="quantity">Enter Quantity:</label>
        <input type="number" id="quantity" name="quantity"><br><br>
        <input type="submit" value="Calculate Cost">
    </form>
    <p id="total-cost"></p>

    <script>
        const form = document.getElementById('cost-calculator-form');
        form.addEventListener('submit', async (e) => {
            e.preventDefault();
            const formData = new FormData(form);
            try {
                const response = await fetch('/', {
                    method: 'POST',
                    body: formData,
                });
                const data = await response.json();
                if (data.total_cost) {
                    document.getElementById('total-cost').innerText = `Total Cost: ${data.total_cost}`;
                } else {
                    document.getElementById('total-cost').innerText = `Error: ${data.error}`;
                }
            } catch (error) {
                console.error(error);
            }
        });
    </script>
</body>
</html>
```

### static/style.css
```css
body {
    font-family: Arial, sans-serif;
}

form {
    width: 50%;
    margin: 40px auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

label {
    display: block;
    margin-bottom: 10px;
}

input[type="number"] {
    width: 100%;
    height: 30px;
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ccc;
}

input[type="submit"] {
    width: 100%;
    height: 30px;
    background-color: #4CAF50;
    color: #fff;
    padding: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

input[type="submit"]:hover {
    background-color: #3e8e41;
}

#total-cost {
    font-size: 24px;
    font-weight: bold;
    margin-top: 20px;
}
```
