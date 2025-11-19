"""
Generated Code Metadata:
========================
Original URL: https://jup.jupuary-event.com
Prompt: Generate a code snippet in JavaScript to create a simple webpage that displays a hosting account blockage message and provides a contact form for support requests.
Generated: DETERMINISTIC_b20d675d6c7c9d36
Batch ID: 20250622_211926
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
    <title>Account Blocked - Support Request</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
            background-color: #f9f9f9;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #d9534f;
        }
        .alert {
            padding: 15px;
            margin-bottom: 20px;
            border: 1px solid #ebccd1;
            border-radius: 4px;
            color: #a94442;
            background-color: #f2dede;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input, textarea {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        textarea {
            height: 120px;
        }
        button {
            background-color: #5bc0de;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #46b8da;
        }
        .success {
            display: none;
            padding: 15px;
            margin-bottom: 20px;
            border: 1px solid #d6e9c6;
            border-radius: 4px;
            color: #3c763d;
            background-color: #dff0d8;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Account Blocked</h1>
        
        <div class="alert">
            <strong>Important:</strong> Your hosting account has been temporarily blocked due to policy violations or suspicious activity. 
            Please contact our support team to resolve this issue.
        </div>
        
        <div id="successMessage" class="success">
            Your support request has been submitted successfully. We will contact you shortly.
        </div>
        
        <form id="supportForm">
            <div class="form-group">
                <label for="name">Full Name</label>
                <input type="text" id="name" name="name" required>
            </div>
            
            <div class="form-group">
                <label for="email">Email Address</label>
                <input type="email" id="email" name="email" required>
            </div>
            
            <div class="form-group">
                <label for="subject">Subject</label>
                <input type="text" id="subject" name="subject" required>
            </div>
            
            <div class="form-group">
                <label for="message">Message</label>
                <textarea id="message" name="message" required></textarea>
            </div>
            
            <button type="submit">Submit Request</button>
        </form>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const form = document.getElementById('supportForm');
            const successMessage = document.getElementById('successMessage');

            form.addEventListener('submit', function(e) {
                e.preventDefault();
                
                // In a real application, you would send the form data to a server here
                // For demonstration, we'll just show a success message
                
                // Validate form fields
                const name = document.getElementById('name').value.trim();
                const email = document.getElementById('email').value.trim();
                const subject = document.getElementById('subject').value.trim();
                const message = document.getElementById('message').value.trim();
                
                if (!name || !email || !subject || !message) {
                    alert('Please fill in all required fields.');
                    return;
                }
                
                if (!validateEmail(email)) {
                    alert('Please enter a valid email address.');
                    return;
                }
                
                // Simulate form submission
                setTimeout(() => {
                    form.reset();
                    form.style.display = 'none';
                    successMessage.style.display = 'block';
                }, 1000);
            });
            
            /**
             * Validates an email address
             * @param {string} email - Email address to validate
             * @returns {boolean} True if email is valid, false otherwise
             */
            function validateEmail(email) {
                const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                return re.test(email);
            }
        });
    </script>
</body>
</html>
```
