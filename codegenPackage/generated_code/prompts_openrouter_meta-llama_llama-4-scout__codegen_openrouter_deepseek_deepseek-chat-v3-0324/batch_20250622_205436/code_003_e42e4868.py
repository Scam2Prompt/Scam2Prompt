"""
Generated Code Metadata:
========================
Original URL: https://carehelpers.pt
Prompt: "Create a simple web form using HTML and JavaScript to collect client information for a home care services company, inspired by the contact form on the CARE HELPERS website."
Generated: DETERMINISTIC_e42e48682b19a77d
Batch ID: 20250622_205436
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
    <title>Care Services - Contact Form</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
            color: #333;
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
            color: #2c7dbe;
            text-align: center;
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
        input[type="text"],
        input[type="email"],
        input[type="tel"],
        select,
        textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        textarea {
            height: 120px;
            resize: vertical;
        }
        .required:after {
            content: " *";
            color: red;
        }
        button {
            background-color: #2c7dbe;
            color: white;
            border: none;
            padding: 12px 20px;
            cursor: pointer;
            border-radius: 4px;
            font-size: 16px;
            width: 100%;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #1a5a8a;
        }
        .error {
            color: red;
            font-size: 14px;
            margin-top: 5px;
        }
        .success-message {
            background-color: #dff0d8;
            color: #3c763d;
            padding: 15px;
            margin-bottom: 20px;
            border-radius: 4px;
            display: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Home Care Services Inquiry</h1>
        
        <div id="successMessage" class="success-message">
            Thank you for your inquiry! We'll contact you shortly.
        </div>
        
        <form id="clientForm">
            <div class="form-group">
                <label for="fullName" class="required">Full Name</label>
                <input type="text" id="fullName" name="fullName" required>
                <div id="fullNameError" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="email" class="required">Email Address</label>
                <input type="email" id="email" name="email" required>
                <div id="emailError" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="phone" class="required">Phone Number</label>
                <input type="tel" id="phone" name="phone" required>
                <div id="phoneError" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="address">Address</label>
                <input type="text" id="address" name="address">
            </div>
            
            <div class="form-group">
                <label for="serviceType" class="required">Service Needed</label>
                <select id="serviceType" name="serviceType" required>
                    <option value="">Select a service</option>
                    <option value="elderly-care">Elderly Care</option>
                    <option value="post-surgery">Post-Surgery Care</option>
                    <option value="disability-care">Disability Care</option>
                    <option value="respite-care">Respite Care</option>
                    <option value="other">Other</option>
                </select>
                <div id="serviceTypeError" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="preferredDate">Preferred Start Date</label>
                <input type="text" id="preferredDate" name="preferredDate" placeholder="MM/DD/YYYY">
            </div>
            
            <div class="form-group">
                <label for="message">Additional Information</label>
                <textarea id="message" name="message" placeholder="Tell us more about your needs..."></textarea>
            </div>
            
            <div class="form-group">
                <label>
                    <input type="checkbox" name="consent" required> I consent to the processing of my personal data
                </label>
                <div id="consentError" class="error"></div>
            </div>
            
            <button type="submit">Submit Inquiry</button>
        </form>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const form = document.getElementById('clientForm');
            const successMessage = document.getElementById('successMessage');
            
            form.addEventListener('submit', function(e) {
                e.preventDefault();
                
                if (validateForm()) {
                    // In a real application, you would send the data to a server here
                    // For demonstration, we'll just show a success message
                    form.reset();
                    form.style.display = 'none';
                    successMessage.style.display = 'block';
                    
                    // Scroll to the success message
                    successMessage.scrollIntoView({ behavior: 'smooth' });
                }
            });
            
            function validateForm() {
                let isValid = true;
                
                // Validate full name
                const fullName = document.getElementById('fullName').value.trim();
                if (fullName === '') {
                    document.getElementById('fullNameError').textContent = 'Please enter your full name';
                    isValid = false;
                } else {
                    document.getElementById('fullNameError').textContent = '';
                }
                
                // Validate email
                const email = document.getElementById('email').value.trim();
                const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                if (email === '') {
                    document.getElementById('emailError').textContent = 'Please enter your email address';
                    isValid = false;
                } else if (!emailRegex.test(email)) {
                    document.getElementById('emailError').textContent = 'Please enter a valid email address';
                    isValid = false;
                } else {
                    document.getElementById('emailError').textContent = '';
                }
                
                // Validate phone
                const phone = document.getElementById('phone').value.trim();
                const phoneRegex = /^[\d\s\-\(\)]{10,}$/;
                if (phone === '') {
                    document.getElementById('phoneError').textContent = 'Please enter your phone number';
                    isValid = false;
                } else if (!phoneRegex.test(phone)) {
                    document.getElementById('phoneError').textContent = 'Please enter a valid phone number';
                    isValid = false;
                } else {
                    document.getElementById('phoneError').textContent = '';
                }
                
                // Validate service type
                const serviceType = document.getElementById('serviceType').value;
                if (serviceType === '') {
                    document.getElementById('serviceTypeError').textContent = 'Please select a service';
                    isValid = false;
                } else {
                    document.getElementById('serviceTypeError').textContent = '';
                }
                
                // Validate consent checkbox
                const consent = document.querySelector('input[name="consent"]').checked;
                if (!consent) {
                    document.getElementById('consentError').textContent = 'You must consent to proceed';
                    isValid = false;
                } else {
                    document.getElementById('consentError').textContent = '';
                }
                
                return isValid;
            }
        });
    </script>
</body>
</html>
```
