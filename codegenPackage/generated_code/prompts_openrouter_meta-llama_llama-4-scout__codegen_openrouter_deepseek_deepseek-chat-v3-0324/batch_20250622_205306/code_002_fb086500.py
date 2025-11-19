"""
Generated Code Metadata:
========================
Original URL: https://sembradordevidaac.org
Prompt: Generate a sample code snippet in JavaScript that creates a basic webpage with a contact form, similar to the one on Sembrador de Vida's website, to help other organizations create their own contact pages.
Generated: DETERMINISTIC_fb086500dc212ed9
Batch ID: 20250622_205306
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
    <title>Contact Us</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            color: #333;
            background-color: #f9f9f9;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        header {
            background-color: #4CAF50;
            color: white;
            text-align: center;
            padding: 1rem 0;
            margin-bottom: 2rem;
        }
        h1 {
            margin: 0;
        }
        .contact-form {
            background: white;
            padding: 2rem;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        .form-group {
            margin-bottom: 1rem;
        }
        label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: bold;
        }
        input, textarea {
            width: 100%;
            padding: 0.5rem;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 1rem;
        }
        textarea {
            min-height: 150px;
            resize: vertical;
        }
        button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 0.75rem 1.5rem;
            font-size: 1rem;
            cursor: pointer;
            border-radius: 4px;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #45a049;
        }
        .error {
            color: red;
            font-size: 0.875rem;
            margin-top: 0.25rem;
        }
        .success-message {
            background-color: #dff0d8;
            color: #3c763d;
            padding: 1rem;
            margin-bottom: 1rem;
            border-radius: 4px;
            display: none;
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <h1>Contact Us</h1>
        </div>
    </header>

    <div class="container">
        <div id="success-message" class="success-message">
            Thank you for your message! We'll get back to you soon.
        </div>

        <form id="contactForm" class="contact-form">
            <div class="form-group">
                <label for="name">Name</label>
                <input type="text" id="name" name="name" required>
                <div id="name-error" class="error"></div>
            </div>

            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" id="email" name="email" required>
                <div id="email-error" class="error"></div>
            </div>

            <div class="form-group">
                <label for="phone">Phone (Optional)</label>
                <input type="tel" id="phone" name="phone">
                <div id="phone-error" class="error"></div>
            </div>

            <div class="form-group">
                <label for="subject">Subject</label>
                <input type="text" id="subject" name="subject" required>
                <div id="subject-error" class="error"></div>
            </div>

            <div class="form-group">
                <label for="message">Message</label>
                <textarea id="message" name="message" required></textarea>
                <div id="message-error" class="error"></div>
            </div>

            <button type="submit">Send Message</button>
        </form>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const form = document.getElementById('contactForm');
            const successMessage = document.getElementById('success-message');

            form.addEventListener('submit', function(e) {
                e.preventDefault();
                
                // Reset error messages
                const errorElements = document.querySelectorAll('.error');
                errorElements.forEach(el => el.textContent = '');
                
                // Validate form
                let isValid = true;
                
                // Name validation
                const name = document.getElementById('name').value.trim();
                if (!name) {
                    document.getElementById('name-error').textContent = 'Name is required';
                    isValid = false;
                }
                
                // Email validation
                const email = document.getElementById('email').value.trim();
                if (!email) {
                    document.getElementById('email-error').textContent = 'Email is required';
                    isValid = false;
                } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
                    document.getElementById('email-error').textContent = 'Please enter a valid email';
                    isValid = false;
                }
                
                // Subject validation
                const subject = document.getElementById('subject').value.trim();
                if (!subject) {
                    document.getElementById('subject-error').textContent = 'Subject is required';
                    isValid = false;
                }
                
                // Message validation
                const message = document.getElementById('message').value.trim();
                if (!message) {
                    document.getElementById('message-error').textContent = 'Message is required';
                    isValid = false;
                }
                
                if (isValid) {
                    // In a real application, you would send the form data to a server here
                    // For demonstration, we'll just show a success message
                    form.reset();
                    successMessage.style.display = 'block';
                    
                    // Hide success message after 5 seconds
                    setTimeout(() => {
                        successMessage.style.display = 'none';
                    }, 5000);
                }
            });
        });
    </script>
</body>
</html>
```
