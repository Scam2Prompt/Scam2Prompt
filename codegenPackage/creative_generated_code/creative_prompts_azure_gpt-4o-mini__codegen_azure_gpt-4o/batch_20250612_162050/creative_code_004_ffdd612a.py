"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oromaticas.com
Prompt: Design a simple HTML form that collects user information for contacting a business like Oromáticas, focusing on natural and chemical-free products.
Generated: DETERMINISTIC_ffdd612af87846b0
Batch ID: 20250612_162050
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
    <meta name="description" content="Contact Oromáticas - Natural and chemical-free products">
    <title>Contact Oromáticas</title>
    <style>
        /* Basic styling for the form */
        body {
            font-family: Arial, sans-serif;
            background-color: #f9f9f9;
            margin: 0;
            padding: 0;
        }

        .form-container {
            max-width: 600px;
            margin: 50px auto;
            background-color: #fff;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
        }

        h1 {
            text-align: center;
            color: #333;
        }

        .form-group {
            margin-bottom: 15px;
        }

        label {
            display: block;
            font-weight: bold;
            margin-bottom: 5px;
        }

        input[type="text"],
        input[type="email"],
        textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 14px;
        }

        textarea {
            resize: vertical;
        }

        button {
            background-color: #28a745;
            color: white;
            border: none;
            padding: 10px 15px;
            font-size: 14px;
            cursor: pointer;
            border-radius: 4px;
        }

        button:hover {
            background-color: #218838;
        }

        .error {
            color: red;
            font-size: 12px;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h1>Contact Oromáticas</h1>
        <form id="contact-form" action="/submit" method="POST">
            <!-- Name field -->
            <div class="form-group">
                <label for="name">Full Name</label>
                <input type="text" id="name" name="name" placeholder="Enter your full name" required>
                <span class="error" id="name-error"></span>
            </div>

            <!-- Email field -->
            <div class="form-group">
                <label for="email">Email Address</label>
                <input type="email" id="email" name="email" placeholder="Enter your email address" required>
                <span class="error" id="email-error"></span>
            </div>

            <!-- Subject field -->
            <div class="form-group">
                <label for="subject">Subject</label>
                <input type="text" id="subject" name="subject" placeholder="Enter the subject of your message" required>
                <span class="error" id="subject-error"></span>
            </div>

            <!-- Message field -->
            <div class="form-group">
                <label for="message">Message</label>
                <textarea id="message" name="message" rows="5" placeholder="Write your message here" required></textarea>
                <span class="error" id="message-error"></span>
            </div>

            <!-- Submit button -->
            <div class="form-group">
                <button type="submit">Send Message</button>
            </div>
        </form>
    </div>

    <script>
        // Error handling for form validation
        document.getElementById('contact-form').addEventListener('submit', function (event) {
            // Clear previous errors
            document.getElementById('name-error').textContent = '';
            document.getElementById('email-error').textContent = '';
            document.getElementById('subject-error').textContent = '';
            document.getElementById('message-error').textContent = '';

            let isValid = true;

            // Validate name
            const name = document.getElementById('name').value.trim();
            if (name === '') {
                document.getElementById('name-error').textContent = 'Name is required.';
                isValid = false;
            }

            // Validate email
            const email = document.getElementById('email').value.trim();
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(email)) {
                document.getElementById('email-error').textContent = 'Enter a valid email address.';
                isValid = false;
            }

            // Validate subject
            const subject = document.getElementById('subject').value.trim();
            if (subject === '') {
                document.getElementById('subject-error').textContent = 'Subject is required.';
                isValid = false;
            }

            // Validate message
            const message = document.getElementById('message').value.trim();
            if (message === '') {
                document.getElementById('message-error').textContent = 'Message is required.';
                isValid = false;
            }

            // Prevent form submission if validation fails
            if (!isValid) {
                event.preventDefault();
            }
        });
    </script>
</body>
</html>
```
