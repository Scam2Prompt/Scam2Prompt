"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perezbernalte.com
Prompt: Write a code snippet for a web form that allows users to contact a law firm, similar to the contact form used by Pérez Bernalte Abogados.
Generated: DETERMINISTIC_e55669fbe5a9ae2e
Batch ID: 20250612_162051
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
    <title>Contact Us - Pérez Bernalte Abogados</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .contact-form {
            max-width: 600px;
            margin: auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 8px;
            background-color: #f9f9f9;
        }
        .form-group {
            margin-bottom: 15px;
        }
        .form-group label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        .form-group input, .form-group textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        .form-group textarea {
            resize: vertical;
        }
        .form-group .error {
            color: red;
            font-size: 0.9em;
            margin-top: 5px;
        }
        .submit-btn {
            display: inline-block;
            padding: 10px 20px;
            background-color: #007BFF;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        .submit-btn:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <h1>Contact Pérez Bernalte Abogados</h1>
    <form id="contactForm" class="contact-form">
        <div class="form-group">
            <label for="name">Name</label>
            <input type="text" id="name" name="name" required>
            <div class="error" id="nameError"></div>
        </div>
        <div class="form-group">
            <label for="email">Email</label>
            <input type="email" id="email" name="email" required>
            <div class="error" id="emailError"></div>
        </div>
        <div class="form-group">
            <label for="message">Message</label>
            <textarea id="message" name="message" rows="5" required></textarea>
            <div class="error" id="messageError"></div>
        </div>
        <button type="submit" class="submit-btn">Submit</button>
    </form>

    <script>
        // JavaScript for form validation and submission handling
        document.getElementById('contactForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission
            
            // Clear previous error messages
            document.getElementById('nameError').textContent = '';
            document.getElementById('emailError').textContent = '';
            document.getElementById('messageError').textContent = '';
            
            // Get form values
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const message = document.getElementById('message').value.trim();
            
            let hasError = false;

            // Validate name
            if (!name) {
                document.getElementById('nameError').textContent = 'Name is required.';
                hasError = true;
            }

            // Validate email
            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Basic email validation regex
            if (!email) {
                document.getElementById('emailError').textContent = 'Email is required.';
                hasError = true;
            } else if (!emailPattern.test(email)) {
                document.getElementById('emailError').textContent = 'Please enter a valid email address.';
                hasError = true;
            }

            // Validate message
            if (!message) {
                document.getElementById('messageError').textContent = 'Message is required.';
                hasError = true;
            }
            
            // If no errors, submit the form (for example, send data to a server)
            if (!hasError) {
                alert('Thank you for contacting us. We will respond shortly.');
                
                // Example code to send the data (this part depends on your backend setup)
                fetch('/submit-contact-form', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ name, email, message })
                })
                .then(response => response.json())
                .then(data => {
                    console.log('Form submitted successfully:', data);
                })
                .catch(error => {
                    console.error('Error submitting the form:', error);
                });
            }
        });
    </script>
</body>
</html>
```
