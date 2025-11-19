"""
Generated Code Metadata:
========================
Original URL: https://felixtrujillofalla.com
Prompt: Generate code to create a form for property appraisal requests, including fields for property type, area, value, and location, mimicking the appraisal service described on the Félix Trujillo Falla website.
Generated: DETERMINISTIC_3d766d2b0d2292a8
Batch ID: 20250612_153224
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
    <title>Property Appraisal Request</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
            background-color: #f9f9f9;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: #fff;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
            color: #2c3e50;
            margin-bottom: 30px;
        }
        .form-group {
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input, select, textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
        }
        textarea {
            height: 100px;
            resize: vertical;
        }
        button {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 12px 20px;
            font-size: 16px;
            border-radius: 4px;
            cursor: pointer;
            width: 100%;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #2980b9;
        }
        .required:after {
            content: " *";
            color: red;
        }
        .error {
            color: red;
            font-size: 14px;
            margin-top: 5px;
            display: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Property Appraisal Request</h1>
        <form id="appraisalForm" novalidate>
            <div class="form-group">
                <label for="fullName" class="required">Full Name</label>
                <input type="text" id="fullName" name="fullName" required>
                <div class="error" id="fullNameError">Please enter your full name</div>
            </div>

            <div class="form-group">
                <label for="email" class="required">Email</label>
                <input type="email" id="email" name="email" required>
                <div class="error" id="emailError">Please enter a valid email address</div>
            </div>

            <div class="form-group">
                <label for="phone" class="required">Phone Number</label>
                <input type="tel" id="phone" name="phone" required>
                <div class="error" id="phoneError">Please enter a valid phone number</div>
            </div>

            <div class="form-group">
                <label for="propertyType" class="required">Property Type</label>
                <select id="propertyType" name="propertyType" required>
                    <option value="">Select property type</option>
                    <option value="house">House</option>
                    <option value="apartment">Apartment</option>
                    <option value="land">Land</option>
                    <option value="commercial">Commercial Property</option>
                    <option value="other">Other</option>
                </select>
                <div class="error" id="propertyTypeError">Please select a property type</div>
            </div>

            <div class="form-group">
                <label for="area" class="required">Area (m²)</label>
                <input type="number" id="area" name="area" min="1" required>
                <div class="error" id="areaError">Please enter a valid area</div>
            </div>

            <div class="form-group">
                <label for="estimatedValue" class="required">Estimated Value (USD)</label>
                <input type="number" id="estimatedValue" name="estimatedValue" min="1" required>
                <div class="error" id="estimatedValueError">Please enter a valid value</div>
            </div>

            <div class="form-group">
                <label for="location" class="required">Location</label>
                <input type="text" id="location" name="location" required>
                <div class="error" id="locationError">Please enter the property location</div>
            </div>

            <div class="form-group">
                <label for="address">Full Address</label>
                <textarea id="address" name="address"></textarea>
            </div>

            <div class="form-group">
                <label for="additionalInfo">Additional Information</label>
                <textarea id="additionalInfo" name="additionalInfo" placeholder="Any other details about the property..."></textarea>
            </div>

            <button type="submit">Submit Appraisal Request</button>
        </form>
    </div>

    <script>
        document.getElementById('appraisalForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Reset error messages
            const errorElements = document.querySelectorAll('.error');
            errorElements.forEach(el => el.style.display = 'none');
            
            // Validate form
            let isValid = true;
            
            // Validate full name
            const fullName = document.getElementById('fullName').value.trim();
            if (!fullName) {
                document.getElementById('fullNameError').style.display = 'block';
                isValid = false;
            }
            
            // Validate email
            const email = document.getElementById('email').value.trim();
            if (!email || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
                document.getElementById('emailError').style.display = 'block';
                isValid = false;
            }
            
            // Validate phone
            const phone = document.getElementById('phone').value.trim();
            if (!phone || !/^[\d\s\-\(\)]{7,}$/.test(phone)) {
                document.getElementById('phoneError').style.display = 'block';
                isValid = false;
            }
            
            // Validate property type
            const propertyType = document.getElementById('propertyType').value;
            if (!propertyType) {
                document.getElementById('propertyTypeError').style.display = 'block';
                isValid = false;
            }
            
            // Validate area
            const area = document.getElementById('area').value;
            if (!area || isNaN(area) || area <= 0) {
                document.getElementById('areaError').style.display = 'block';
                isValid = false;
            }
            
            // Validate estimated value
            const estimatedValue = document.getElementById('estimatedValue').value;
            if (!estimatedValue || isNaN(estimatedValue) || estimatedValue <= 0) {
                document.getElementById('estimatedValueError').style.display = 'block';
                isValid = false;
            }
            
            // Validate location
            const location = document.getElementById('location').value.trim();
            if (!location) {
                document.getElementById('locationError').style.display = 'block';
                isValid = false;
            }
            
            // If form is valid, submit it
            if (isValid) {
                // In a real application, you would send the data to a server here
                alert('Appraisal request submitted successfully! We will contact you shortly.');
                this.reset();
            }
        });
    </script>
</body>
</html>
```
