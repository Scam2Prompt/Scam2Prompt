"""
Generated Code Metadata:
========================
Original URL: https://perezbernalte.com
Prompt: Write a code snippet for a web form that allows users to contact a law firm, similar to the contact form used by Pérez Bernalte Abogados.
Generated: DETERMINISTIC_e55669fbe5a9ae2e
Batch ID: 20250612_162051
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
    <title>Contact Us - Law Firm</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
            text-align: center;
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
        }
        .required {
            color: #e74c3c;
        }
        button {
            background-color: #2c3e50;
            color: white;
            border: none;
            padding: 12px 20px;
            cursor: pointer;
            width: 100%;
            font-size: 16px;
            border-radius: 4px;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #1a252f;
        }
        .error {
            color: #e74c3c;
            font-size: 14px;
            margin-top: 5px;
        }
        .success-message {
            background-color: #2ecc71;
            color: white;
            padding: 15px;
            margin-bottom: 20px;
            border-radius: 4px;
            display: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Contact Our Law Firm</h1>
        
        <div id="successMessage" class="success-message">
            Thank you for your message. We will contact you shortly.
        </div>
        
        <form id="contactForm" novalidate>
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
                <label for="phone">Phone Number</label>
                <input type="tel" id="phone" name="phone">
            </div>
            
            <div class="form-group">
                <label for="subject">Subject <span class="required">*</span></label>
                <select id="subject" name="subject" required>
                    <option value="">Select a subject</option>
                    <option value="general">General Inquiry</option>
                    <option value="family">Family Law</option>
                    <option value="business">Business Law</option>
                    <option value="real-estate">Real Estate</option>
                    <option value="litigation">Litigation</option>
                    <option value="other">Other</option>
                </select>
                <div id="subjectError" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="message">Your Message <span class="required">*</span></label>
                <textarea id="message" name="message" required></textarea>
                <div id="messageError" class="error"></div>
            </div>
            
            <div class="form-group">
                <button type="submit">Send Message</button>
            </div>
        </form>
    </div>

    <script>
        document.getElementById('contactForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Reset error messages
            document.querySelectorAll('.error').forEach(el => el.textContent = '');
            
            // Get form values
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const subject = document.getElementById('subject').value;
            const message = document.getElementById('message').value.trim();
            
            let isValid = true;
            
            // Validate name
            if (!name) {
                document.getElementById('nameError').textContent = 'Please enter your name';
                isValid = false;
            }
            
            // Validate email
            if (!email) {
                document.getElementById('emailError').textContent = 'Please enter your email';
                isValid = false;
            } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
                document.getElementById('emailError').textContent = 'Please enter a valid email';
                isValid = false;
            }
            
            // Validate subject
            if (!subject) {
                document.getElementById('subjectError').textContent = 'Please select a subject';
                isValid = false;
            }
            
            // Validate message
            if (!message) {
                document.getElementById('messageError').textContent = 'Please enter your message';
                isValid = false;
            }
            
            if (isValid) {
                // In a real application, you would send the form data to the server here
                // For demonstration, we'll just show the success message
                document.getElementById('successMessage').style.display = 'block';
                document.getElementById('contactForm').reset();
                
                // Hide success message after 5 seconds
                setTimeout(() => {
                    document.getElementById('successMessage').style.display = 'none';
                }, 5000);
            }
        });
    </script>
</body>
</html>
```
