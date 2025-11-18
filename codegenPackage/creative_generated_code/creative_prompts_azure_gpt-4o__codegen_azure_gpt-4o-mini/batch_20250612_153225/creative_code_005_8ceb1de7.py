"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perumakers.org
Prompt: Write code to implement a contact form for an NGO website, including fields for name, email, phone number, and message, similar to the one described on Perú Makers.
Generated: DETERMINISTIC_8ceb1de7675cade5
Batch ID: 20250612_153225
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
            margin: 0;
            padding: 20px;
            background-color: #f9f9f9;
        }
        .container {
            max-width: 600px;
            margin: auto;
            background: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        input, textarea {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            background-color: #28a745;
            color: white;
            padding: 10px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #218838;
        }
        .error {
            color: red;
            font-size: 0.9em;
        }
    </style>
</head>
<body>

<div class="container">
    <h2>Contact Us</h2>
    <form id="contactForm" method="POST" action="submit_contact.php">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>

        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>

        <label for="phone">Phone Number:</label>
        <input type="tel" id="phone" name="phone" required>

        <label for="message">Message:</label>
        <textarea id="message" name="message" rows="4" required></textarea>

        <button type="submit">Send Message</button>
        <div id="formResponse" class="error"></div>
    </form>
</div>

<script>
    // Add form submission event listener
    document.getElementById('contactForm').addEventListener('submit', function(event) {
        event.preventDefault();  // Prevent default form submission

        // Gather form data
        const formData = new FormData(this);

        // Validate form data
        if (!validateForm(formData)) {
            document.getElementById('formResponse').innerText = 'Please fill in all fields correctly.';
            return;
        }

        // Send data to server
        fetch('submit_contact.php', {
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
            document.getElementById('contactForm').reset();  // Reset form on success
        })
        .catch(error => {
            document.getElementById('formResponse').innerText = 'Error: ' + error.message;
        });
    });

    // Validate form data before submission
    function validateForm(formData) {
        for (const value of formData.values()) {
            if (!value) {
                return false; // Return false if any field is empty
            }
        }
        return true; // Return true if all fields are filled
    }
</script>

</body>
</html>
```

```php
<?php
// submit_contact.php

// Enable error reporting for debugging
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Start session for error message display (if needed)
session_start();

// Check if form data has been submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate input data
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $phone = filter_input(INPUT_POST, 'phone', FILTER_SANITIZE_STRING);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Prepare response array
    $response = [];

    // Check if the email is valid
    if (!$email) {
        $response['error'] = 'Invalid email format';
    }

    // Check if all fields are filled
    if (empty($name) || empty($phone) || empty($message)) {
        $response['error'] = 'All fields are required';
    }

    // If there are no errors, proceed with sending the email
    if (empty($response['error'])) {
        // Prepare the email
        $to = 'your_email@example.com'; // Replace with your email
        $subject = 'New Contact Form Submission';
        $body = "Name: $name\nEmail: $email\nPhone: $phone\nMessage: $message";
        $headers = "From: $email";

        // Send the email
        if (mail($to, $subject, $body, $headers)) {
            $response['success'] = 'Message sent successfully!';
        } else {
            $response['error'] = 'Failed to send message, please try again later.';
        }
    }

    // Return response as JSON
    header('Content-Type: application/json');
    echo json_encode($response);
    exit;
}
?>
```
