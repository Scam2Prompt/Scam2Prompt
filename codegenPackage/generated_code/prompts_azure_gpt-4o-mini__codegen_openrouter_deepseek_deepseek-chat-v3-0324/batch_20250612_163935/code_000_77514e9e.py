"""
Generated Code Metadata:
========================
Original URL: https://2ms.pt
Prompt: Generate a code snippet to create a contact form for a real estate website, including fields for name, email, and phone number, similar to the one found on 2ms.pt.
Generated: DETERMINISTIC_77514e9efda0cd88
Batch ID: 20250612_163935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready contact form implementation for a real estate website:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us - Real Estate</title>
    <style>
        .contact-form {
            max-width: 500px;
            margin: 0 auto;
            padding: 20px;
            background: #f9f9f9;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
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
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        button {
            background: #0066cc;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background: #0052a3;
        }
        .error {
            color: red;
            font-size: 14px;
            margin-top: 5px;
        }
        .success-message {
            color: green;
            margin-bottom: 15px;
        }
    </style>
</head>
<body>
    <div class="contact-form">
        <h2>Contact Our Real Estate Team</h2>
        
        <div id="form-messages"></div>
        
        <form id="contactForm" method="POST">
            <div class="form-group">
                <label for="name">Full Name*</label>
                <input type="text" id="name" name="name" required>
                <div id="name-error" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="email">Email*</label>
                <input type="email" id="email" name="email" required>
                <div id="email-error" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="phone">Phone Number*</label>
                <input type="tel" id="phone" name="phone" required>
                <div id="phone-error" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="message">Message</label>
                <textarea id="message" name="message" rows="4"></textarea>
            </div>
            
            <button type="submit">Send Message</button>
        </form>
    </div>

    <script>
        document.getElementById('contactForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Clear previous errors
            document.querySelectorAll('.error').forEach(el => el.textContent = '');
            document.getElementById('form-messages').textContent = '';
            
            // Get form values
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const phone = document.getElementById('phone').value.trim();
            const message = document.getElementById('message').value.trim();
            
            // Validate inputs
            let isValid = true;
            
            if (!name) {
                document.getElementById('name-error').textContent = 'Please enter your name';
                isValid = false;
            }
            
            if (!email) {
                document.getElementById('email-error').textContent = 'Please enter your email';
                isValid = false;
            } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
                document.getElementById('email-error').textContent = 'Please enter a valid email';
                isValid = false;
            }
            
            if (!phone) {
                document.getElementById('phone-error').textContent = 'Please enter your phone number';
                isValid = false;
            } else if (!/^[\d\s\+\-\(\)]{10,}$/.test(phone)) {
                document.getElementById('phone-error').textContent = 'Please enter a valid phone number';
                isValid = false;
            }
            
            if (!isValid) return;
            
            // Form submission logic (in a real app, this would be an AJAX call)
            const formMessages = document.getElementById('form-messages');
            formMessages.textContent = 'Thank you for your message! We will contact you shortly.';
            formMessages.className = 'success-message';
            
            // Reset form
            document.getElementById('contactForm').reset();
            
            // In a real implementation, you would send the data to your server here
            // Example using fetch:
            /*
            fetch('/api/contact', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ name, email, phone, message })
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    formMessages.textContent = 'Thank you for your message! We will contact you shortly.';
                    formMessages.className = 'success-message';
                    document.getElementById('contactForm').reset();
                } else {
                    formMessages.textContent = 'There was an error sending your message. Please try again.';
                    formMessages.className = 'error';
                }
            })
            .catch(error => {
                formMessages.textContent = 'There was an error sending your message. Please try again.';
                formMessages.className = 'error';
            });
            */
        });
    </script>
</body>
</html>
```
