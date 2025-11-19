"""
Generated Code Metadata:
========================
Original URL: https://mail.cornucopiastrategy.com
Prompt: Create an HTML form similar to `landing_page_form.html`, but with additional validation and error handling.
Generated: DETERMINISTIC_45f5de133bba442d
Batch ID: 20250622_212447
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
    <title>Enhanced Landing Page Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
            background: #fff;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            text-align: center;
            color: #333;
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
            height: 100px;
            resize: vertical;
        }
        button {
            background: #4CAF50;
            color: white;
            border: none;
            padding: 12px 20px;
            cursor: pointer;
            width: 100%;
            font-size: 16px;
            border-radius: 4px;
            transition: background 0.3s;
        }
        button:hover {
            background: #45a049;
        }
        .error {
            color: #ff0000;
            font-size: 14px;
            margin-top: 5px;
        }
        .success {
            color: #008000;
            font-size: 16px;
            text-align: center;
            margin-bottom: 20px;
            display: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Contact Us</h1>
        
        <div id="success-message" class="success">
            Thank you! Your message has been submitted successfully.
        </div>

        <form id="contact-form" novalidate>
            <div class="form-group">
                <label for="name">Full Name*</label>
                <input type="text" id="name" name="name" required>
                <div id="name-error" class="error"></div>
            </div>

            <div class="form-group">
                <label for="email">Email Address*</label>
                <input type="email" id="email" name="email" required>
                <div id="email-error" class="error"></div>
            </div>

            <div class="form-group">
                <label for="phone">Phone Number</label>
                <input type="tel" id="phone" name="phone" pattern="[0-9]{10}">
                <div id="phone-error" class="error"></div>
            </div>

            <div class="form-group">
                <label for="subject">Subject*</label>
                <select id="subject" name="subject" required>
                    <option value="">Select a subject</option>
                    <option value="support">Support</option>
                    <option value="sales">Sales</option>
                    <option value="feedback">Feedback</option>
                    <option value="other">Other</option>
                </select>
                <div id="subject-error" class="error"></div>
            </div>

            <div class="form-group">
                <label for="message">Message*</label>
                <textarea id="message" name="message" required></textarea>
                <div id="message-error" class="error"></div>
            </div>

            <div class="form-group">
                <label>
                    <input type="checkbox" id="consent" name="consent" required>
                    I agree to the terms and conditions*
                </label>
                <div id="consent-error" class="error"></div>
            </div>

            <button type="submit">Submit</button>
        </form>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const form = document.getElementById('contact-form');
            const successMessage = document.getElementById('success-message');

            // Validate form on submit
            form.addEventListener('submit', function(event) {
                event.preventDefault();
                clearErrors();
                
                if (validateForm()) {
                    // Form is valid - simulate submission
                    successMessage.style.display = 'block';
                    form.reset();
                    setTimeout(() => {
                        successMessage.style.display = 'none';
                    }, 5000);
                }
            });

            // Real-time validation for email field
            const emailField = document.getElementById('email');
            emailField.addEventListener('blur', validateEmail);

            // Real-time validation for phone field
            const phoneField = document.getElementById('phone');
            phoneField.addEventListener('blur', validatePhone);

            // Clear error when user starts typing
            const fields = form.querySelectorAll('input, select, textarea');
            fields.forEach(field => {
                field.addEventListener('input', function() {
                    const errorElement = document.getElementById(`${this.id}-error`);
                    if (errorElement) {
                        errorElement.textContent = '';
                    }
                });
            });
        });

        function clearErrors() {
            const errorElements = document.querySelectorAll('.error');
            errorElements.forEach(element => {
                element.textContent = '';
            });
        }

        function validateForm() {
            let isValid = true;
            
            // Validate name
            const name = document.getElementById('name').value.trim();
            if (!name) {
                document.getElementById('name-error').textContent = 'Name is required';
                isValid = false;
            }

            // Validate email
            if (!validateEmail()) {
                isValid = false;
            }

            // Validate phone if provided
            const phone = document.getElementById('phone').value.trim();
            if (phone && !validatePhone()) {
                isValid = false;
            }

            // Validate subject
            const subject = document.getElementById('subject').value;
            if (!subject) {
                document.getElementById('subject-error').textContent = 'Please select a subject';
                isValid = false;
            }

            // Validate message
            const message = document.getElementById('message').value.trim();
            if (!message) {
                document.getElementById('message-error').textContent = 'Message is required';
                isValid = false;
            }

            // Validate consent
            const consent = document.getElementById('consent').checked;
            if (!consent) {
                document.getElementById('consent-error').textContent = 'You must agree to the terms';
                isValid = false;
            }

            return isValid;
        }

        function validateEmail() {
            const email = document.getElementById('email').value.trim();
            const emailError = document.getElementById('email-error');
            
            if (!email) {
                emailError.textContent = 'Email is required';
                return false;
            }
            
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(email)) {
                emailError.textContent = 'Please enter a valid email address';
                return false;
            }
            
            return true;
        }

        function validatePhone() {
            const phone = document.getElementById('phone').value.trim();
            const phoneError = document.getElementById('phone-error');
            
            if (phone && !/^\d{10}$/.test(phone)) {
                phoneError.textContent = 'Please enter a valid 10-digit phone number';
                return false;
            }
            
            return true;
        }
    </script>
</body>
</html>
```
