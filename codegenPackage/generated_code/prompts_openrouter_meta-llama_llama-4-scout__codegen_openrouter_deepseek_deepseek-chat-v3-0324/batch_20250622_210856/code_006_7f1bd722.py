"""
Generated Code Metadata:
========================
Original URL: https://uniquehomestagingandredesignbydee.com
Prompt: Create a simple calculator using JavaScript to estimate home staging costs based on factors like the number of rooms, furniture rental rates, and service areas in Eastern North Carolina.
Generated: DETERMINISTIC_7f1bd7223f4bcd0e
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home Staging Cost Calculator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            color: #333;
        }
        h1 {
            color: #2c3e50;
            text-align: center;
        }
        .calculator {
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input, select {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        button {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            width: 100%;
        }
        button:hover {
            background-color: #2980b9;
        }
        #result {
            margin-top: 20px;
            padding: 15px;
            background-color: #e8f4fc;
            border-radius: 4px;
            display: none;
        }
        .error {
            color: #e74c3c;
            font-size: 14px;
            margin-top: 5px;
        }
    </style>
</head>
<body>
    <h1>Home Staging Cost Calculator</h1>
    <div class="calculator">
        <div class="form-group">
            <label for="rooms">Number of Rooms:</label>
            <input type="number" id="rooms" min="1" max="20" value="1">
            <div id="rooms-error" class="error"></div>
        </div>
        
        <div class="form-group">
            <label for="furniture">Furniture Rental Rate ($ per room per month):</label>
            <input type="number" id="furniture" min="0" step="50" value="500">
            <div id="furniture-error" class="error"></div>
        </div>
        
        <div class="form-group">
            <label for="duration">Staging Duration (months):</label>
            <input type="number" id="duration" min="1" max="12" value="1">
            <div id="duration-error" class="error"></div>
        </div>
        
        <div class="form-group">
            <label for="area">Service Area:</label>
            <select id="area">
                <option value="1">Wilmington</option>
                <option value="1.1">Jacksonville</option>
                <option value="1.2">New Bern</option>
                <option value="1.3">Greenville</option>
                <option value="1.4">Other Eastern NC Areas</option>
            </select>
        </div>
        
        <div class="form-group">
            <label for="consultation">Include Consultation Fee ($200)?</label>
            <input type="checkbox" id="consultation" checked>
        </div>
        
        <button id="calculate">Calculate Estimated Cost</button>
        
        <div id="result"></div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const calculateBtn = document.getElementById('calculate');
            const resultDiv = document.getElementById('result');
            
            calculateBtn.addEventListener('click', function() {
                // Clear previous errors
                document.querySelectorAll('.error').forEach(el => el.textContent = '');
                
                // Get input values
                const rooms = parseInt(document.getElementById('rooms').value);
                const furniture = parseFloat(document.getElementById('furniture').value);
                const duration = parseInt(document.getElementById('duration').value);
                const areaMultiplier = parseFloat(document.getElementById('area').value);
                const includeConsultation = document.getElementById('consultation').checked;
                
                // Validate inputs
                let isValid = true;
                
                if (isNaN(rooms) || rooms < 1 || rooms > 20) {
                    document.getElementById('rooms-error').textContent = 'Please enter a valid number of rooms (1-20)';
                    isValid = false;
                }
                
                if (isNaN(furniture) || furniture < 0) {
                    document.getElementById('furniture-error').textContent = 'Please enter a valid furniture rate';
                    isValid = false;
                }
                
                if (isNaN(duration) || duration < 1 || duration > 12) {
                    document.getElementById('duration-error').textContent = 'Please enter a valid duration (1-12 months)';
                    isValid = false;
                }
                
                if (!isValid) return;
                
                // Calculate costs
                let baseCost = rooms * furniture * duration;
                let areaCost = baseCost * (areaMultiplier - 1);
                let consultationFee = includeConsultation ? 200 : 0;
                let totalCost = baseCost + areaCost + consultationFee;
                
                // Display result
                resultDiv.style.display = 'block';
                resultDiv.innerHTML = `
                    <h3>Estimated Staging Cost</h3>
                    <p><strong>Base Cost:</strong> $${baseCost.toFixed(2)}</p>
                    ${areaCost > 0 ? `<p><strong>Area Surcharge (${(areaMultiplier - 1) * 100}%):</strong> $${areaCost.toFixed(2)}</p>` : ''}
                    ${includeConsultation ? `<p><strong>Consultation Fee:</strong> $200.00</p>` : ''}
                    <p><strong>Total Estimated Cost:</strong> $${totalCost.toFixed(2)}</p>
                `;
            });
        });
    </script>
</body>
</html>
```
