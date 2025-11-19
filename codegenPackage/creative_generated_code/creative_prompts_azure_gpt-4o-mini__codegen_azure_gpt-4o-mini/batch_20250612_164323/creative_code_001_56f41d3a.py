"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.apos.cl
Prompt: How can I implement a contact form for a business like Apos that specializes in thermal paper roll distribution?
Generated: DETERMINISTIC_56f41d3a225c7130
Batch ID: 20250612_164323
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
    <title>Contact Us - Apos Thermal Paper Rolls</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="contact-container">
        <h1>Contact Us</h1>
        <form id="contactForm" action="submit_contact.php" method="POST">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="message">Message:</label>
            <textarea id="message" name="message" rows="4" required></textarea>

            <button type="submit">Send Message</button>
        </form>
        <div id="formResponse"></div>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    background-color: #f7f7f7;
    color: #333;
}

.contact-container {
    width: 50%;
    margin: 0 auto;
    padding: 20px;
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
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
    border: 1px solid #ccc;
    border-radius: 4px;
    margin-bottom: 10px;
}

button {
    background-color: #007BFF;
    color: white;
    border: none;
    padding: 10px;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}
```

```javascript
// script.js
document.getElementById('contactForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent form from submitting the default way

    // Create a FormData object from the form
    const formData = new FormData(this);

    // Send the form data using Fetch API
    fetch('submit_contact.php', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.text(); // Assuming the server sends back some response text
    })
    .then(data => {
        document.getElementById('formResponse').innerText = "Message sent successfully!";
        document.getElementById('contactForm').reset(); // Reset form fields
    })
    .catch(error => {
        document.getElementById('formResponse').innerText = "Error: " + error.message;
    });
});
```

```php
<?php
// submit_contact.php

// Check if form data is received
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate and sanitize input
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Check if email is valid
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        http_response_code(400);
        echo "Invalid email address.";
        exit;
    }

    // Prepare the email
    $to = "contact@apos.com"; // Change to your business email
    $subject = "New Contact Form Submission from $name";
    $body = "Name: $name\nEmail: $email\nMessage:\n$message";
    $headers = "From: $email";

    // Send the email
    if (mail($to, $subject, $body, $headers)) {
        http_response_code(200);
        echo "Message sent successfully.";
    } else {
        http_response_code(500);
        echo "Error sending message.";
    }
} else {
    // Method not allowed
    http_response_code(405);
    echo "Method Not Allowed";
}
?>
```

This code provides an HTML contact form, CSS for styling, JavaScript for form submission via AJAX, and PHP for processing the form data. Proper validations and error handling are included to ensure robustness.
