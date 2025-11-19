"""
Generated Code Metadata:
========================
Original URL: https://al-afdel.com
Prompt: Generate a code snippet for a web application that allows users to request home cleaning services, referencing the unique offerings of the company mentioned in the content.
Generated: DETERMINISTIC_6d0d82dcd8076210
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from flask import Flask, request, jsonify, render_template
from werkzeug.exceptions import BadRequest, InternalServerError

app = Flask(__name__)

# Mock database for demonstration purposes
cleaning_services = {
    "standard": {
        "name": "Standard Cleaning",
        "description": "Basic cleaning including dusting, vacuuming, and bathroom sanitization.",
        "price": 100,
        "unique_offering": "Eco-friendly cleaning products used"
    },
    "deep": {
        "name": "Deep Cleaning",
        "description": "Thorough cleaning including hard-to-reach areas and appliance cleaning.",
        "price": 200,
        "unique_offering": "Specialized tools for grout and tile cleaning"
    },
    "premium": {
        "name": "Premium Cleaning",
        "description": "Comprehensive cleaning with additional services like window washing.",
        "price": 300,
        "unique_offering": "Satisfaction guarantee with free re-cleaning if needed"
    }
}

@app.route('/')
def home():
    """Render the home page with service options"""
    return render_template('index.html', services=cleaning_services)

@app.route('/request-service', methods=['POST'])
def request_service():
    """Handle service request submission"""
    try:
        data = request.get_json()
        
        if not data:
            raise BadRequest("No data provided")
        
        required_fields = ['service_type', 'name', 'email', 'address', 'date']
        for field in required_fields:
            if field not in data:
                raise BadRequest(f"Missing required field: {field}")
        
        service_type = data['service_type']
        if service_type not in cleaning_services:
            raise BadRequest("Invalid service type")
        
        # In a real application, you would save this to a database
        # and potentially process payment here
        confirmation = {
            "status": "success",
            "message": "Service request received",
            "service": cleaning_services[service_type]['name'],
            "price": cleaning_services[service_type]['price'],
            "unique_offering": cleaning_services[service_type]['unique_offering'],
            "customer": {
                "name": data['name'],
                "email": data['email']
            },
            "appointment": {
                "address": data['address'],
                "date": data['date']
            }
        }
        
        return jsonify(confirmation), 201
    
    except BadRequest as e:
        return jsonify({"status": "error", "message": str(e)}), 400
    except Exception as e:
        app.logger.error(f"Error processing request: {str(e)}")
        return jsonify({"status": "error", "message": "Internal server error"}), 500

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
    <title>Home Cleaning Services</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
        }
        .service {
            border: 1px solid #ddd;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 5px;
        }
        .service h3 {
            margin-top: 0;
        }
        .highlight {
            color: #2a6496;
            font-weight: bold;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
        #requestForm {
            display: none;
            margin-top: 20px;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        input, textarea {
            width: 100%;
            padding: 8px;
            margin: 8px 0;
            display: inline-block;
            border: 1px solid #ccc;
            border-radius: 4px;
            box-sizing: border-box;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Professional Home Cleaning Services</h1>
        <p>Book our expert cleaners who pay attention to every detail.</p>
        
        {% for service_type, service in services.items() %}
        <div class="service">
            <h3>{{ service.name }} - ${{ service.price }}</h3>
            <p>{{ service.description }}</p>
            <p class="highlight">Unique Offering: {{ service.unique_offering }}</p>
            <button onclick="showRequestForm('{{ service_type }}')">Request This Service</button>
        </div>
        {% endfor %}
        
        <div id="requestForm">
            <h2>Request Service</h2>
            <form id="serviceForm">
                <input type="hidden" id="service_type" name="service_type">
                
                <label for="name">Full Name:</label>
                <input type="text" id="name" name="name" required>
                
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                
                <label for="address">Address:</label>
                <textarea id="address" name="address" required></textarea>
                
                <label for="date">Preferred Date:</label>
                <input type="date" id="date" name="date" required>
                
                <button type="button" onclick="submitRequest()">Submit Request</button>
            </form>
            <div id="confirmation" style="display: none; margin-top: 20px;"></div>
        </div>
    </div>

    <script>
        function showRequestForm(serviceType) {
            document.getElementById('service_type').value = serviceType;
            document.getElementById('requestForm').style.display = 'block';
            document.getElementById('confirmation').style.display = 'none';
            window.scrollTo(0, document.body.scrollHeight);
        }
        
        function submitRequest() {
            const form = document.getElementById('serviceForm');
            const formData = {
                service_type: form.service_type.value,
                name: form.name.value,
                email: form.email.value,
                address: form.address.value,
                date: form.date.value
            };
            
            fetch('/request-service', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(formData)
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    const confirmationDiv = document.getElementById('confirmation');
                    confirmationDiv.innerHTML = `
                        <h3>Thank you for your request!</h3>
                        <p>Service: ${data.service}</p>
                        <p>Price: $${data.price}</p>
                        <p>Special Offer: ${data.unique_offering}</p>
                        <p>We'll contact you at ${data.customer.email} to confirm your appointment on ${data.appointment.date}.</p>
                    `;
                    confirmationDiv.style.display = 'block';
                    form.reset();
                } else {
                    alert('Error: ' + data.message);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An error occurred. Please try again.');
            });
        }
    </script>
</body>
</html>
```
