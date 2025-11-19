"""
Generated Code Metadata:
========================
Original URL: https://rupakparajuli.com.np
Prompt: Generate code for a simple blog contact form using HTML, CSS, and JavaScript, inspired by the design on Rupak Parajuli's website.
Generated: DETERMINISTIC_5ea63a5516346b39
Batch ID: 20250622_210655
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
    <title>Contact Form</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: #f5f5f5;
            color: #333;
            line-height: 1.6;
            padding: 20px;
        }

        .container {
            max-width: 600px;
            margin: 0 auto;
            padding: 30px;
            background: white;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        h1 {
            text-align: center;
            margin-bottom: 20px;
            color: #2c3e50;
        }

        .form-group {
            margin-bottom: 20px;
        }

        label {
            display: block;
            margin-bottom: 5px;
            font-weight: 600;
            color: #2c3e50;
        }

        input[type="text"],
        input[type="email"],
        textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
            transition: border 0.3s;
        }

        input[type="text"]:focus,
        input[type="email"]:focus,
        textarea:focus {
            border-color: #3498db;
            outline: none;
        }

        textarea {
            min-height: 150px;
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

        .status-message {
            margin-top: 20px;
            padding: 10px;
            border-radius: 4px;
            text-align: center;
            display: none;
        }

        .success {
            background-color: #d4edda;
            color: #155724;
            display: block;
        }

        .error {
            background-color: #f8d7da;
            color: #721c24;
            display: block;
        }

        @media (max-width: 768px) {
            .container {
                padding: 20px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Get in Touch</h1>
        <form id="contactForm">
            <div class="form-group">
                <label for="name">Name</label>
                <input type="text" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="message">Message</label>
                <textarea id="message" name="message" required></textarea>
            </div>
            <button type="submit">Send Message</button>
        </form>
        <div id="statusMessage" class="status-message"></div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const contactForm = document.getElementById('contactForm');
            const statusMessage = document.getElementById('statusMessage');

            contactForm.addEventListener('submit', function(e) {
                e.preventDefault();
                
                // Get form values
                const name = document.getElementById('name').value.trim();
                const email = document.getElementById('email').value.trim();
                const message = document.getElementById('message').value.trim();

                // Simple validation
                if (!name || !email || !message) {
                    showStatus('Please fill in all fields', 'error');
                    return;
                }

                if (!validateEmail(email)) {
                    showStatus('Please enter a valid email address', 'error');
                    return;
                }

                // Simulate form submission (in a real app, you would use fetch/axios)
                setTimeout(() => {
                    showStatus('Message sent successfully!', 'success');
                    contactForm.reset();
                }, 1000);
            });

            function showStatus(message, type) {
                statusMessage.textContent = message;
                statusMessage.className = 'status-message ' + type;
                
                // Hide message after 5 seconds
                setTimeout(() => {
                    statusMessage.className = 'status-message';
                    statusMessage.textContent = '';
                }, 5000);
            }

            function validateEmail(email) {
                const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                return re.test(email);
            }
        });
    </script>
</body>
</html>
```
