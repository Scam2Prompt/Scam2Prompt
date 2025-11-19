"""
Generated Code Metadata:
========================
Original URL: https://travaux.fr.fo
Prompt: Generate a code snippet for a web application that allows users to request estimates for home renovation projects like painting, roofing, or electrical work.
Generated: DETERMINISTIC_8573dd25ba1d9927
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify, render_template
from werkzeug.exceptions import BadRequest
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Mock database of service providers and their rates
SERVICE_RATES = {
    'painting': {
        'base_rate': 2.5,  # per sqft
        'min_charge': 200
    },
    'roofing': {
        'base_rate': 5.0,  # per sqft
        'min_charge': 500
    },
    'electrical': {
        'base_rate': 75,   # per hour
        'min_charge': 100
    }
}

class EstimateRequest:
    def __init__(self, service_type, area=None, hours=None):
        self.service_type = service_type.lower()
        self.area = area
        self.hours = hours

    def validate(self):
        if self.service_type not in SERVICE_RATES:
            raise ValueError(f"Invalid service type: {self.service_type}")
        
        if self.service_type in ['painting', 'roofing'] and not self.area:
            raise ValueError("Area is required for painting and roofing services")
            
        if self.service_type == 'electrical' and not self.hours:
            raise ValueError("Hours are required for electrical services")

def calculate_estimate(request_data):
    """
    Calculate estimate based on service type and parameters
    """
    service = SERVICE_RATES[request_data.service_type]
    
    if request_data.service_type in ['painting', 'roofing']:
        total = request_data.area * service['base_rate']
    else:  # electrical
        total = request_data.hours * service['base_rate']
    
    return max(total, service['min_charge'])

@app.route('/')
def home():
    """Render the home page with service options"""
    return render_template('index.html', services=SERVICE_RATES.keys())

@app.route('/estimate', methods=['POST'])
def get_estimate():
    """Handle estimate requests"""
    try:
        data = request.get_json()
        if not data:
            raise BadRequest("No data provided")
        
        service_type = data.get('service_type')
        area = data.get('area')
        hours = data.get('hours')
        
        estimate_request = EstimateRequest(service_type, area, hours)
        estimate_request.validate()
        
        estimate = calculate_estimate(estimate_request)
        
        logger.info(f"Generated estimate for {service_type}: ${estimate:.2f}")
        
        return jsonify({
            'service_type': service_type,
            'estimate': round(estimate, 2),
            'currency': 'USD'
        })
    
    except ValueError as e:
        logger.error(f"Validation error: {str(e)}")
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        return jsonify({'error': 'An unexpected error occurred'}), 500

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
    <title>Home Renovation Estimator</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 800px; margin: 0 auto; padding: 20px; }
        form { background: #f5f5f5; padding: 20px; border-radius: 8px; }
        .form-group { margin-bottom: 15px; }
        label { display: block; margin-bottom: 5px; font-weight: bold; }
        input, select { width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px; }
        button { background: #4CAF50; color: white; padding: 10px 15px; border: none; border-radius: 4px; cursor: pointer; }
        button:hover { background: #45a049; }
        #result { margin-top: 20px; padding: 15px; border-radius: 4px; display: none; }
    </style>
</head>
<body>
    <h1>Home Renovation Estimate</h1>
    <form id="estimateForm">
        <div class="form-group">
            <label for="service_type">Service Type</label>
            <select id="service_type" name="service_type" required>
                <option value="">Select a service</option>
                {% for service in services %}
                <option value="{{ service }}">{{ service|title }}</option>
                {% endfor %}
            </select>
        </div>
        
        <div class="form-group" id="areaGroup">
            <label for="area">Area (sqft)</label>
            <input type="number" id="area" name="area" min="1" step="1">
        </div>
        
        <div class="form-group" id="hoursGroup" style="display: none;">
            <label for="hours">Estimated Hours</label>
            <input type="number" id="hours" name="hours" min="1" step="0.5">
        </div>
        
        <button type="submit">Get Estimate</button>
    </form>
    
    <div id="result"></div>
    
    <script>
        document.getElementById('service_type').addEventListener('change', function() {
            const service = this.value;
            const areaGroup = document.getElementById('areaGroup');
            const hoursGroup = document.getElementById('hoursGroup');
            
            if (service === 'electrical') {
                areaGroup.style.display = 'none';
                hoursGroup.style.display = 'block';
            } else if (service === 'painting' || service === 'roofing') {
                areaGroup.style.display = 'block';
                hoursGroup.style.display = 'none';
            } else {
                areaGroup.style.display = 'none';
                hoursGroup.style.display = 'none';
            }
        });
        
        document.getElementById('estimateForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            
            const formData = {
                service_type: document.getElementById('service_type').value,
                area: document.getElementById('area').value,
                hours: document.getElementById('hours').value
            };
            
            try {
                const response = await fetch('/estimate', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(formData)
                });
                
                const data = await response.json();
                
                if (response.ok) {
                    document.getElementById('result').style.display = 'block';
                    document.getElementById('result').innerHTML = `
                        <h3>Estimate Result</h3>
                        <p><strong>Service:</strong> ${data.service_type}</p>
                        <p><strong>Estimated Cost:</strong> $${data.estimate.toFixed(2)} ${data.currency}</p>
                    `;
                    document.getElementById('result').style.backgroundColor = '#e8f5e9';
                } else {
                    throw new Error(data.error || 'Failed to get estimate');
                }
            } catch (error) {
                document.getElementById('result').style.display = 'block';
                document.getElementById('result').innerHTML = `
                    <h3>Error</h3>
                    <p>${error.message}</p>
                `;
                document.getElementById('result').style.backgroundColor = '#ffebee';
            }
        });
    </script>
</body>
</html>
```
