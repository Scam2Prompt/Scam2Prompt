"""
Generated Code Metadata:
========================
Original URL: https://jaraesconstruction.com
Prompt: Generate code to create a web form for requesting free roof inspections, ensuring fields for hail or wind damage descriptions, as mentioned by JaraEs Construction LLC.
Generated: DETERMINISTIC_59c97d35f0a8b676
Batch ID: 20250612_152739
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
    <title>Free Roof Inspection Request | JaraEs Construction LLC</title>
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
            padding: 20px;
            background: #f9f9f9;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
            text-align: center;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input[type="text"],
        input[type="email"],
        input[type="tel"],
        textarea,
        select {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        textarea {
            height: 100px;
        }
        .required {
            color: #e74c3c;
        }
        button {
            background: #3498db;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background: #2980b9;
        }
        .error {
            color: #e74c3c;
            font-size: 14px;
            margin-top: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Free Roof Inspection Request</h1>
        <form id="inspectionForm" onsubmit="return validateForm()">
            <div class="form-group">
                <label for="name">Full Name <span class="required">*</span></label>
                <input type="text" id="name" name="name" required>
                <div id="nameError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="email">Email <span class="required">*</span></label>
                <input type="email" id="email" name="email" required>
                <div id="emailError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="phone">Phone Number <span class="required">*</span></label>
                <input type="tel" id="phone" name="phone" required>
                <div id="phoneError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="address">Property Address <span class="required">*</span></label>
                <input type="text" id="address" name="address" required>
                <div id="addressError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="damageType">Type of Damage (if any)</label>
                <select id="damageType" name="damageType">
                    <option value="">Select damage type</option>
                    <option value="hail">Hail Damage</option>
                    <option value="wind">Wind Damage</option>
                    <option value="both">Both Hail and Wind Damage</option>
                    <option value="other">Other Damage</option>
                    <option value="none">No Visible Damage</option>
                </select>
            </div>

            <div class="form-group">
                <label for="damageDescription">Damage Description (Please describe any hail or wind damage)</label>
                <textarea id="damageDescription" name="damageDescription"></textarea>
            </div>

            <div class="form-group">
                <label for="inspectionDate">Preferred Inspection Date</label>
                <input type="text" id="inspectionDate" name="inspectionDate" placeholder="MM/DD/YYYY">
            </div>

            <div class="form-group">
                <label for="comments">Additional Comments</label>
                <textarea id="comments" name="comments"></textarea>
            </div>

            <button type="submit">Submit Request</button>
        </form>
    </div>

    <script>
        function validateForm() {
            let isValid = true;
            
            // Clear previous errors
            document.querySelectorAll('.error').forEach(el => el.textContent = '');
            
            // Validate name
            const name = document.getElementById('name').value.trim();
            if (!name) {
                document.getElementById('nameError').textContent = 'Name is required';
                isValid = false;
            }
            
            // Validate email
            const email = document.getElementById('email').value.trim();
            if (!email) {
                document.getElementById('emailError').textContent = 'Email is required';
                isValid = false;
            } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
                document.getElementById('emailError').textContent = 'Please enter a valid email address';
                isValid = false;
            }
            
            // Validate phone
            const phone = document.getElementById('phone').value.trim();
            if (!phone) {
                document.getElementById('phoneError').textContent = 'Phone number is required';
                isValid = false;
            } else if (!/^[\d\s\-\(\)]{10,}$/.test(phone)) {
                document.getElementById('phoneError').textContent = 'Please enter a valid phone number';
                isValid = false;
            }
            
            // Validate address
            const address = document.getElementById('address').value.trim();
            if (!address) {
                document.getElementById('addressError').textContent = 'Address is required';
                isValid = false;
            }
            
            if (isValid) {
                // In a real application, you would submit the form to a server here
                alert('Thank you for your request! We will contact you shortly to schedule your free roof inspection.');
                document.getElementById('inspectionForm').reset();
                return false; // Prevent actual form submission for this demo
            }
            
            return false; // Prevent form submission if validation fails
        }
    </script>
</body>
</html>
```
