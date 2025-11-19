"""
Generated Code Metadata:
========================
Original URL: https://recuperacionjc.com
Prompt: Generate code for a contact form with multiple versions (e.g., Contact v.1, Contact v.2) as described on the Recuperación JC website.
Generated: DETERMINISTIC_44ab8d1791dce131
Batch ID: 20250612_153224
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
    <h1>Contact Us</h1>
    
    <!-- Contact Form Version 1 -->
    <form id="contactFormV1" method="POST" action="submit_form.php">
        <h2>Contact v.1</h2>
        <label for="nameV1">Name:</label>
        <input type="text" id="nameV1" name="name" required>
        
        <label for="emailV1">Email:</label>
        <input type="email" id="emailV1" name="email" required>
        
        <label for="messageV1">Message:</label>
        <textarea id="messageV1" name="message" required></textarea>
        
        <button type="submit">Send</button>
    </form>

    <!-- Contact Form Version 2 -->
    <form id="contactFormV2" method="POST" action="submit_form.php">
        <h2>Contact v.2</h2>
        <label for="nameV2">Full Name:</label>
        <input type="text" id="nameV2" name="full_name" required>
        
        <label for="emailV2">Email Address:</label>
        <input type="email" id="emailV2" name="email_address" required>
        
        <label for="subjectV2">Subject:</label>
        <input type="text" id="subjectV2" name="subject" required>
        
        <label for="messageV2">Your Message:</label>
        <textarea id="messageV2" name="your_message" required></textarea>
        
        <button type="submit">Submit</button>
    </form>

    <script src="script.js"></script> <!-- Link to external JavaScript for form handling -->
</body>
</html>
```

```php
<?php
// submit_form.php

// Check if the request method is POST
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate input data
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING) ?? '';
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL) ?? '';
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING) ?? '';
    
    // Check if the email is valid
    if (!$email) {
        die("Invalid email address.");
    }

    // Prepare the email content
    $to = "your-email@example.com"; // Replace with your email address
    $subject = "New Contact Form Submission";
    $body = "Name: $name\nEmail: $email\nMessage: $message";
    $headers = "From: $email";

    // Attempt to send the email
    if (mail($to, $subject, $body, $headers)) {
        echo "Message sent successfully!";
    } else {
        echo "Failed to send message. Please try again later.";
    }
} else {
    // Handle invalid request method
    http_response_code(405);
    echo "Method Not Allowed";
}
?>
```

```css
/* styles.css */

/* Basic styling for the contact forms */
body {
    font-family: Arial, sans-serif;
    margin: 20px;
    padding: 20px;
    background-color: #f4f4f4;
}

h1 {
    color: #333;
}

form {
    background: #fff;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    margin-bottom: 20px;
}

label {
    display: block;
    margin-bottom: 5px;
}

input[type="text"],
input[type="email"],
textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    background-color: #5cb85c;
    color: white;
    padding: 10px 15px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #4cae4c;
}
```

```javascript
// script.js

// Add any necessary JavaScript for form handling or validation here
document.addEventListener("DOMContentLoaded", function() {
    // Example: Add event listeners for form submissions if needed
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            // Perform any client-side validation if necessary
            // For example, check if all required fields are filled
            const inputs = form.querySelectorAll('input, textarea');
            let valid = true;
            inputs.forEach(input => {
                if (!input.value) {
                    valid = false;
                    alert(`${input.name} is required.`);
                }
            });
            if (!valid) {
                event.preventDefault(); // Prevent form submission if validation fails
            }
        });
    });
});
```
