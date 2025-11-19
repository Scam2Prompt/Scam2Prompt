"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://la-guarida.com.ar
Prompt: Write a function in JavaScript to create a contact form for a web design service, inspired by the contact options on La Guarida's site.
Generated: DETERMINISTIC_4fa5d5cb0abaeeed
Batch ID: 20250612_162127
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
    <title>Contact Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        .contact-form {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            max-width: 400px;
            margin: auto;
        }
        .form-group {
            margin-bottom: 15px;
        }
        .form-group label {
            display: block;
            margin-bottom: 5px;
        }
        .form-group input, .form-group textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        .form-group button {
            background-color: #007bff;
            color: white;
            border: none;
            padding: 10px;
            border-radius: 4px;
            cursor: pointer;
        }
        .form-group button:hover {
            background-color: #0056b3;
        }
        .message {
            margin-top: 10px;
            display: none;
        }
    </style>
</head>
<body>

    <div class="contact-form">
        <h2>Contact Us</h2>
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
                <textarea id="message" name="message" rows="4" required></textarea>
            </div>
            <div class="form-group">
                <button type="submit">Send Message</button>
            </div>
            <div class="message" id="messageDisplay"></div>
        </form>
    </div>

    <script>
        // Function to handle form submission
        document.getElementById('contactForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent the default form submission

            // Get form values
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const message = document.getElementById('message').value.trim();

            // Basic validation for the fields
            if (!name || !email || !message) {
                displayMessage('Please fill in all fields.', 'error');
                return;
            }

            // Simulate sending the data (you would normally send this to a server)
            // You can replace this part with an actual AJAX call to your backend
            try {
                // Example: Simulated API call
                const simulatedResponse = sendToServer({ name, email, message });
                displayMessage(simulatedResponse, 'success');
                clearForm();
            } catch (error) {
                displayMessage('There was an error sending your message. Please try again later.', 'error');
                console.error(error); // Log the error for debugging
            }
        });

        // Function to display messages to the user
        function displayMessage(message, type) {
            const messageDisplay = document.getElementById('messageDisplay');
            messageDisplay.textContent = message;
            messageDisplay.style.display = 'block';
            messageDisplay.style.color = type === 'success' ? 'green' : 'red';
        }

        // Function to clear the form fields
        function clearForm() {
            document.getElementById('contactForm').reset();
        }

        // Simulate server response (for demonstration purposes)
        function sendToServer(data) {
            // Replace this with actual server logic
            if (data.name && data.email && data.message) {
                return 'Your message has been sent successfully!';
            } else {
                throw new Error('Validation failed');
            }
        }
    </script>

</body>
</html>
```
