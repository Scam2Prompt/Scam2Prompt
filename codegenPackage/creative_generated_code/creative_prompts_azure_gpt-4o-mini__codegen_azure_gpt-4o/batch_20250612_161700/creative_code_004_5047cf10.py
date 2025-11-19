"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cristalesgraf.com
Prompt: Design a simple HTML form that captures customer information for glass and aluminum service inquiries, reflecting the contact methods available on CristalesGraf's site.
Generated: DETERMINISTIC_5047cf10ffce1dc9
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Glass and Aluminum Service Inquiry</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f9f9f9;
        }
        .form-container {
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            background-color: #ffffff;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
            color: #333;
        }
        .form-group {
            margin-bottom: 15px;
        }
        .form-group label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        .form-group input,
        .form-group textarea,
        .form-group select,
        .form-group button {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
            box-sizing: border-box;
        }
        .form-group button {
            background-color: #007bff;
            color: #fff;
            border: none;
            cursor: pointer;
            font-weight: bold;
        }
        .form-group button:hover {
            background-color: #0056b3;
        }
        .error-message {
            color: red;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h1>Glass and Aluminum Service Inquiry</h1>
        <form id="service-inquiry-form" action="/submit-inquiry" method="POST">
            <!-- Customer Name -->
            <div class="form-group">
                <label for="customer-name">Full Name:</label>
                <input 
                    type="text" 
                    id="customer-name" 
                    name="customerName" 
                    placeholder="Enter your name" 
                    required>
            </div>

            <!-- Email Address -->
            <div class="form-group">
                <label for="email">Email Address:</label>
                <input 
                    type="email" 
                    id="email" 
                    name="email" 
                    placeholder="Enter your email"
                    required>
            </div>

            <!-- Phone Number -->
            <div class="form-group">
                <label for="phone">Phone Number:</label>
                <input 
                    type="tel" 
                    id="phone" 
                    name="phone" 
                    placeholder="Enter your phone number"
                    pattern="[0-9]{10}" 
                    title="Please enter a valid phone number (10 digits)"
                    required>
            </div>

            <!-- Preferred Contact Method -->
            <div class="form-group">
                <label for="contact-method">Preferred Contact Method:</label>
                <select id="contact-method" name="contactMethod" required>
                    <option value="">Select an option</option>
                    <option value="email">Email</option>
                    <option value="phone">Phone</option>
                </select>
            </div>

            <!-- Service Inquiry Details -->
            <div class="form-group">
                <label for="inquiry-details">Inquiry Details:</label>
                <textarea 
                    id="inquiry-details" 
                    name="inquiryDetails" 
                    placeholder="Describe your requirements or questions" 
                    rows="5" 
                    required></textarea>
            </div>

            <!-- Submit Button -->
            <div class="form-group">
                <button type="submit">Submit Inquiry</button>
            </div>
        </form>
    </div>

    <script>
        // JavaScript for additional validation or error handling
        document.getElementById('service-inquiry-form').addEventListener('submit', function(event) {
            const name = document.getElementById('customer-name').value.trim();
            const email = document.getElementById('email').value.trim();
            const phone = document.getElementById('phone').value.trim();
            const contactMethod = document.getElementById('contact-method').value;

            // Basic validation before submission
            if (!name || !email || !phone || !contactMethod) {
                event.preventDefault();
                alert('Please fill in all required fields.');
            }
        });
    </script>
</body>
</html>
```
