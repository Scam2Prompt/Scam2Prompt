"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://la-guarida.com.ar
Prompt: Write JavaScript code to implement a "Contact Us" form with email functionality, as highlighted on La Guarida's website.
Generated: DETERMINISTIC_b47f6c1662b37d57
Batch ID: 20250612_155000
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
    <title>Contact Us Form</title>
    <style>
        /* Basic styling for the form */
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
            background-color: #f4f4f4;
        }
        .form-container {
            max-width: 600px;
            margin: auto;
            background: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        input, textarea {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
        button {
            background-color: #28a745;
            color: white;
            border: none;
            padding: 10px;
            border-radius: 5px;
            cursor: pointer;
        }
        button:hover {
            background-color: #218838;
        }
        .error {
            color: red;
            margin: 10px 0;
        }
    </style>
</head>
<body>

<div class="form-container">
    <h2>Contact Us</h2>
    <form id="contactForm">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required />

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required />

        <label for="message">Message:</label>
        <textarea id="message" name="message" rows="5" required></textarea>

        <button type="submit">Send Message</button>
        <div class="error" id="error" style="display:none;"></div>
        <div class="success" id="success" style="display:none;">Message sent successfully!</div>
    </form>
</div>

<script>
    document.getElementById('contactForm').addEventListener('submit', async function(event) {
        event.preventDefault(); // Prevent the default form submission

        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const message = document.getElementById('message').value;

        // Basic client-side validation
        if (!name || !email || !message) {
            showError('All fields are required.');
            return;
        }

        // Clear previous messages
        clearMessages();

        try {
            // Send form data to backend using fetch API
            const response = await fetch('/send-email', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ name, email, message }),
            });

            // Check if the response is okay
            if (!response.ok) {
                const errorData = await response.json();
                showError(errorData.message || 'An error occurred while sending the message.');
                return;
            }

            // Clear form fields
            document.getElementById('contactForm').reset();
            document.getElementById('success').style.display = 'block';
        } catch (error) {
            showError('An unexpected error occurred: ' + error.message);
        }
    });

    function showError(message) {
        const errorDiv = document.getElementById('error');
        errorDiv.textContent = message;
        errorDiv.style.display = 'block';
    }

    function clearMessages() {
        document.getElementById('error').style.display = 'none';
        document.getElementById('success').style.display = 'none';
    }
</script>

</body>
</html>
```

### Server-side Note:
Make sure to implement the `/send-email` endpoint on the server-side (e.g., using Node.js, PHP, Python, etc.) to handle the email sending functionality using appropriate email sending libraries (like Nodemailer for Node.js, PHPMailer for PHP, etc.).
