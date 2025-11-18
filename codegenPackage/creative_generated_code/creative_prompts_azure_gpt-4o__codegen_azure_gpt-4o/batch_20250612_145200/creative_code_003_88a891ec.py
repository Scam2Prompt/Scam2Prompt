"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aluminiosmendoza.cl
Prompt: Write a PHP script to integrate a contact form for inquiries about aluminum windows, PVC termopanels, and security blinds, ensuring data validation for required fields like name, email, and phone number.
Generated: DETERMINISTIC_88a891ec44564f49
Batch ID: 20250612_145200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```php
<?php
// contact_form.php

// Check if the form was submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize and validate the input fields
    $name = trim(filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING));
    $email = trim(filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL));
    $phone = trim(filter_input(INPUT_POST, 'phone', FILTER_SANITIZE_STRING));
    $inquiryType = trim(filter_input(INPUT_POST, 'inquiry_type', FILTER_SANITIZE_STRING)); // Optional field
    $message = trim(filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING));

    // Initialize an array to store error messages
    $errors = [];

    // Validate required fields
    if (empty($name)) {
        $errors[] = 'Name is required.';
    }
    if (empty($email) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $errors[] = 'A valid email address is required.';
    }
    if (empty($phone) || !preg_match('/^\+?[0-9]{7,15}$/', $phone)) {
        $errors[] = 'A valid phone number is required.';
    }

    // If there are errors, return them to the user
    if (!empty($errors)) {
        echo json_encode(['success' => false, 'errors' => $errors]);
        exit;
    }

    // Prepare the email content
    $subject = "New Inquiry About $inquiryType";
    $body = "You have received a new inquiry:\n\n"
        . "Name: $name\n"
        . "Email: $email\n"
        . "Phone: $phone\n"
        . "Inquiry Type: $inquiryType\n\n"
        . "Message:\n$message\n";

    $headers = "From: webmaster@example.com\r\n";
    $headers .= "Reply-To: $email\r\n";

    // Send the email
    $to = 'sales@example.com'; // Replace with your recipient email address
    if (mail($to, $subject, $body, $headers)) {
        echo json_encode(['success' => true, 'message' => 'Your inquiry has been sent successfully.']);
    } else {
        echo json_encode(['success' => false, 'message' => 'There was an error sending your inquiry. Please try again later.']);
    }
    exit;
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h1>Contact Us</h1>
    <form method="POST" action="contact_form.php">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <br>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <br>
        <label for="phone">Phone:</label>
        <input type="text" id="phone" name="phone" required>
        <br>
        <label for="inquiry_type">Inquiry Type:</label>
        <select id="inquiry_type" name="inquiry_type">
            <option value="Aluminum Windows">Aluminum Windows</option>
            <option value="PVC Termopanels">PVC Termopanels</option>
            <option value="Security Blinds">Security Blinds</option>
        </select>
        <br>
        <label for="message">Message:</label>
        <textarea id="message" name="message"></textarea>
        <br>
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```
