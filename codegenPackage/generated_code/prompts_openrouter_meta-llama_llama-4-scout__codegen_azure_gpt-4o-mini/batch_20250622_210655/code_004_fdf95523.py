"""
Generated Code Metadata:
========================
Original URL: https://www.haim-lawyer.co.il
Prompt: Generate a code snippet for a simple contact form, similar to the one on the haim-lawyer.co.il website, that captures the user's name, email, phone number, and message.
Generated: DETERMINISTIC_fdf9552313d431ed
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
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <div class="contact-form-container">
        <h1>Contact Us</h1>
        <form id="contactForm" method="POST" action="submit_form.php">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="phone">Phone Number:</label>
            <input type="tel" id="phone" name="phone" required>

            <label for="message">Message:</label>
            <textarea id="message" name="message" rows="4" required></textarea>

            <button type="submit">Send Message</button>
        </form>
        <div id="formResponse" class="response-message"></div> <!-- Placeholder for response messages -->
    </div>

    <script>
        // Handle form submission
        document.getElementById('contactForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            // Gather form data
            const formData = new FormData(this);

            // Send form data using Fetch API
            fetch('submit_form.php', {
                method: 'POST',
                body: formData
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.text();
            })
            .then(data => {
                document.getElementById('formResponse').innerText = 'Message sent successfully!';
                this.reset(); // Reset the form after successful submission
            })
            .catch(error => {
                document.getElementById('formResponse').innerText = 'There was a problem with your submission: ' + error.message;
            });
        });
    </script>
</body>
</html>
```

```php
<?php
// submit_form.php

// Check if the request method is POST
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate input data
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $phone = filter_input(INPUT_POST, 'phone', FILTER_SANITIZE_STRING);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Check for validation errors
    if (!$name || !$email || !$phone || !$message) {
        http_response_code(400); // Bad Request
        echo 'Invalid input data.';
        exit;
    }

    // Here you would typically send the email or save the data to a database
    // For demonstration, we'll just simulate a successful response
    // mail($to, $subject, $message, $headers); // Uncomment to send email

    // Send a success response
    http_response_code(200); // OK
    echo 'Message sent successfully!';
} else {
    // If the request method is not POST, return a 405 Method Not Allowed
    http_response_code(405);
    echo 'Method not allowed.';
}
?>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 20px;
}

.contact-form-container {
    background: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    max-width: 400px;
    margin: auto;
}

h1 {
    text-align: center;
}

label {
    display: block;
    margin: 10px 0 5px;
}

input, textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    width: 100%;
    padding: 10px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}

.response-message {
    margin-top: 10px;
    text-align: center;
    color: red;
}
```
