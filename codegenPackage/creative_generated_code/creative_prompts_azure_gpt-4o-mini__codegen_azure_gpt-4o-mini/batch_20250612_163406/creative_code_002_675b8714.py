"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teslax.in
Prompt: Can you provide a code snippet to create a contact form similar to the one on teslax.in for reaching out to public figures?
Generated: DETERMINISTIC_675b87140194bd03
Batch ID: 20250612_163406
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
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="contact-form-container">
        <h1>Contact Us</h1>
        <form id="contactForm" action="submit_form.php" method="POST">
            <div class="form-group">
                <label for="name">Full Name:</label>
                <input type="text" id="name" name="name" required placeholder="John Doe">
                <span class="error" id="nameError"></span>
            </div>
            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required placeholder="john.doe@example.com">
                <span class="error" id="emailError"></span>
            </div>
            <div class="form-group">
                <label for="message">Message:</label>
                <textarea id="message" name="message" required placeholder="Your message here..." rows="4"></textarea>
                <span class="error" id="messageError"></span>
            </div>
            <button type="submit">Send Message</button>
        </form>
        <div id="formResponse" class="response"></div>
    </div>
    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    padding: 20px;
}

.contact-form-container {
    max-width: 500px;
    margin: auto;
    background: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.form-group {
    margin-bottom: 15px;
}

label {
    display: block;
    margin-bottom: 5px;
}

input[type="text"],
input[type="email"],
textarea {
    width: 100%;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

.error {
    color: red;
    font-size: 0.9em;
}

button {
    background-color: #007BFF;
    color: white;
    border: none;
    padding: 10px 15px;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}

.response {
    margin-top: 10px;
    font-size: 1.1em;
}
```

```javascript
// script.js
document.getElementById('contactForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    // Clear previous errors
    document.getElementById('nameError').textContent = '';
    document.getElementById('emailError').textContent = '';
    document.getElementById('messageError').textContent = '';
    document.getElementById('formResponse').textContent = '';

    // Form validation
    let hasError = false;
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const message = document.getElementById('message').value.trim();

    // Basic validation
    if (name.length < 2) {
        document.getElementById('nameError').textContent = 'Name must be at least 2 characters long.';
        hasError = true;
    }
    if (!validateEmail(email)) {
        document.getElementById('emailError').textContent = 'Please enter a valid email address.';
        hasError = true;
    }
    if (message.length < 10) {
        document.getElementById('messageError').textContent = 'Message must be at least 10 characters long.';
        hasError = true;
    }

    // If no errors, submit the form
    if (!hasError) {
        const formData = new FormData(this);
        fetch('submit_form.php', {
            method: 'POST',
            body: formData,
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                document.getElementById('formResponse').textContent = 'Message sent successfully!';
                this.reset(); // Reset form on success
            } else {
                document.getElementById('formResponse').textContent = 'Error sending message. Please try again.';
            }
        })
        .catch(error => {
            document.getElementById('formResponse').textContent = 'An error occurred. Please try again later.';
            console.error('Error:', error);
        });
    }
});

// Utility function to validate email format
function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(String(email).toLowerCase());
}
```

```php
<?php
// submit_form.php

// Check if the request is a POST request
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate inputs
    $name = filter_var(trim($_POST['name']), FILTER_SANITIZE_STRING);
    $email = filter_var(trim($_POST['email']), FILTER_SANITIZE_EMAIL);
    $message = filter_var(trim($_POST['message']), FILTER_SANITIZE_STRING);

    $response = ['success' => false];

    // Validate required fields
    if (empty($name) || empty($email) || empty($message) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        http_response_code(400);
        echo json_encode($response);
        exit;
    }

    // Send the email (dummy email function for illustration)
    $to = "recipient@example.com"; // Replace with the recipient's email
    $subject = "New Contact Form Submission from $name";
    $body = "Name: $name\nEmail: $email\nMessage:\n$message";
    $headers = "From: $email";

    if (mail($to, $subject, $body, $headers)) {
        $response['success'] = true;
    }

    // Return JSON response
    echo json_encode($response);
} else {
    // If not a POST request, return a 405 Method Not Allowed
    http_response_code(405);
}
?>
```
