"""
Generated Code Metadata:
========================
Original URL: https://oromaticas.com
Prompt: Design a simple HTML form that collects user information for contacting a business like Oromáticas, focusing on natural and chemical-free products.
Generated: DETERMINISTIC_ffdd612af87846b0
Batch ID: 20250612_162050
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
    <title>Contact Oromáticas - Natural Products</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f9f9f9;
        }
        h1 {
            color: #2a7221;
            text-align: center;
        }
        .form-container {
            background-color: white;
            padding: 25px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
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
        textarea,
        select {
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
        .required {
            color: #e74c3c;
        }
        button {
            background-color: #2a7221;
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            width: 100%;
        }
        button:hover {
            background-color: #1e5a17;
        }
        .error-message {
            color: #e74c3c;
            font-size: 14px;
            margin-top: 5px;
            display: none;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h1>Contact Oromáticas</h1>
        <p>Please fill out this form to contact us about our natural and chemical-free products.</p>
        
        <form id="contactForm" onsubmit="return validateForm()">
            <div class="form-group">
                <label for="name">Full Name <span class="required">*</span></label>
                <input type="text" id="name" name="name" required>
                <div id="nameError" class="error-message">Please enter your name</div>
            </div>
            
            <div class="form-group">
                <label for="email">Email Address <span class="required">*</span></label>
                <input type="email" id="email" name="email" required>
                <div id="emailError" class="error-message">Please enter a valid email address</div>
            </div>
            
            <div class="form-group">
                <label for="phone">Phone Number</label>
                <input type="tel" id="phone" name="phone">
            </div>
            
            <div class="form-group">
                <label for="interest">Product Interest</label>
                <select id="interest" name="interest">
                    <option value="">Select an option</option>
                    <option value="essential-oils">Essential Oils</option>
                    <option value="natural-cosmetics">Natural Cosmetics</option>
                    <option value="aromatherapy">Aromatherapy Products</option>
                    <option value="other">Other</option>
                </select>
            </div>
            
            <div class="form-group">
                <label for="message">Your Message <span class="required">*</span></label>
                <textarea id="message" name="message" required></textarea>
                <div id="messageError" class="error-message">Please enter your message</div>
            </div>
            
            <div class="form-group">
                <label>
                    <input type="checkbox" name="newsletter" checked>
                    Subscribe to our newsletter about natural products
                </label>
            </div>
            
            <button type="submit">Send Message</button>
        </form>
    </div>

    <script>
        function validateForm() {
            let isValid = true;
            
            // Reset error messages
            document.querySelectorAll('.error-message').forEach(el => {
                el.style.display = 'none';
            });
            
            // Validate name
            const name = document.getElementById('name').value.trim();
            if (name === '') {
                document.getElementById('nameError').style.display = 'block';
                isValid = false;
            }
            
            // Validate email
            const email = document.getElementById('email').value.trim();
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(email)) {
                document.getElementById('emailError').style.display = 'block';
                isValid = false;
            }
            
            // Validate message
            const message = document.getElementById('message').value.trim();
            if (message === '') {
                document.getElementById('messageError').style.display = 'block';
                isValid = false;
            }
            
            if (isValid) {
                // In a real application, you would submit the form to a server here
                alert('Thank you for your message! We will contact you soon.');
                document.getElementById('contactForm').reset();
            }
            
            return false; // Prevent actual form submission for this demo
        }
    </script>
</body>
</html>
```
