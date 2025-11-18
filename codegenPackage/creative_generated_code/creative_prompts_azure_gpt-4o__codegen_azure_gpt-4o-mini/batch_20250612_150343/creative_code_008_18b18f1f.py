"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wingerrandr.ca
Prompt: Generate PHP code for a contact form that sends service inquiries (e.g., "bathroom updating & repair") to the email "jesse.winger@protonmail.com."
Generated: DETERMINISTIC_18b18f1f7cf58ea2
Batch ID: 20250612_150343
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

// Check if the form has been submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate input data
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $serviceInquiry = filter_input(INPUT_POST, 'service_inquiry', FILTER_SANITIZE_STRING);

    // Initialize an array to hold error messages
    $errors = [];

    // Validate input data
    if (empty($name)) {
        $errors[] = "Name is required.";
    }
    if (empty($email)) {
        $errors[] = "A valid email is required.";
    }
    if (empty($serviceInquiry)) {
        $errors[] = "Service inquiry cannot be empty.";
    }

    // If no errors, proceed to send the email
    if (empty($errors)) {
        $to = "jesse.winger@protonmail.com";
        $subject = "Service Inquiry from $name";
        $message = "You have received a new service inquiry.\n\n" .
                   "Name: $name\n" .
                   "Email: $email\n" .
                   "Inquiry: $serviceInquiry\n";
        $headers = "From: $name <$email>\r\n" .
                   "Reply-To: $email\r\n";

        // Attempt to send the email and handle potential errors
        if (mail($to, $subject, $message, $headers)) {
            echo "Thank you for your inquiry, $name. We will get back to you shortly.";
        } else {
            echo "Oops! Something went wrong. Please try again later.";
        }
    } else {
        // Output errors if there are any
        foreach ($errors as $error) {
            echo "<p>Error: $error</p>";
        }
    }
}
?>

<!-- HTML form for the contact inquiry -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
    <style>
        /* Basic styles for the contact form */
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        form {
            margin-top: 20px;
        }
        label {
            display: block;
            margin: 10px 0 5px;
        }
        input, textarea {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
        }
        button {
            padding: 10px 15px;
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h1>Contact Us</h1>
    <form method="post" action="">
        <label for="name">Your Name:</label>
        <input type="text" id="name" name="name" required>
        
        <label for="email">Your Email:</label>
        <input type="email" id="email" name="email" required>
        
        <label for="service_inquiry">Service Inquiry:</label>
        <textarea id="service_inquiry" name="service_inquiry" rows="4" required></textarea>
        
        <button type="submit">Send Inquiry</button>
    </form>
</body>
</html>
```
