"""
Generated Code Metadata:
========================
Original URL: https://laboratoriosavaz.com
Prompt: Generate code using Flask or Django to implement a feature that calculates the cost of medical tests based on user input, including tests like "hemograma completo" and "examen completo de orina."
Generated: DETERMINISTIC_746e6d9f634f2426
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Flask implementation for medical test cost calculator

from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Medical test prices (in USD)
TEST_PRICES = {
    "hemograma_completo": 25.00,
    "examen_completo_orina": 18.50,
    "perfil_bioquimico": 35.75,
    "prueba_embarazo": 12.00,
    "prueba_hepatitis": 42.30,
    "prueba_vih": 38.20
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_tests = request.form.getlist('tests')
        insurance_discount = float(request.form.get('insurance_discount', 0))
        
        try:
            total = calculate_total_cost(selected_tests, insurance_discount)
            return render_template('result.html', 
                                selected_tests=selected_tests,
                                total=total,
                                discount=insurance_discount)
        except Exception as e:
            return render_template('error.html', error=str(e))
    
    return render_template('index.html', tests=TEST_PRICES.keys())

def calculate_total_cost(selected_tests, discount=0):
    if not selected_tests:
        raise ValueError("No tests selected")
    
    if discount < 0 or discount > 100:
        raise ValueError("Discount must be between 0 and 100")
    
    subtotal = sum(TEST_PRICES[test] for test in selected_tests)
    discount_amount = subtotal * (discount / 100)
    total = subtotal - discount_amount
    
    return {
        'subtotal': round(subtotal, 2),
        'discount_amount': round(discount_amount, 2),
        'total': round(total, 2)
    }

@app.route('/api/calculate', methods=['POST'])
def api_calculate():
    try:
        data = request.get_json()
        selected_tests = data.get('tests', [])
        insurance_discount = float(data.get('insurance_discount', 0))
        
        result = calculate_total_cost(selected_tests, insurance_discount)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

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
    <title>Medical Test Cost Calculator</title>
</head>
<body>
    <h1>Medical Test Cost Calculator</h1>
    <form method="POST">
        <h2>Select Tests:</h2>
        {% for test in tests %}
        <div>
            <input type="checkbox" id="{{ test }}" name="tests" value="{{ test }}">
            <label for="{{ test }}">{{ test.replace('_', ' ').title() }} (${"{:.2f}".format(TEST_PRICES[test])})</label>
        </div>
        {% endfor %}
        
        <h2>Insurance Discount (%):</h2>
        <input type="number" name="insurance_discount" min="0" max="100" value="0">
        
        <br><br>
        <button type="submit">Calculate Total</button>
    </form>
</body>
</html>
```

```html
<!-- templates/result.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculation Result</title>
</head>
<body>
    <h1>Medical Test Cost Calculation Result</h1>
    
    <h2>Selected Tests:</h2>
    <ul>
        {% for test in selected_tests %}
        <li>{{ test.replace('_', ' ').title() }}</li>
        {% endfor %}
    </ul>
    
    <h2>Cost Breakdown:</h2>
    <p>Subtotal: ${{ "{:.2f}".format(total.subtotal) }}</p>
    <p>Discount ({{ discount }}%): ${{ "{:.2f}".format(total.discount_amount) }}</p>
    <p><strong>Total: ${{ "{:.2f}".format(total.total) }}</strong></p>
    
    <a href="/">Back to Calculator</a>
</body>
</html>
```

```html
<!-- templates/error.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Error</title>
</head>
<body>
    <h1>Error</h1>
    <p style="color: red;">{{ error }}</p>
    <a href="/">Back to Calculator</a>
</body>
</html>
```
