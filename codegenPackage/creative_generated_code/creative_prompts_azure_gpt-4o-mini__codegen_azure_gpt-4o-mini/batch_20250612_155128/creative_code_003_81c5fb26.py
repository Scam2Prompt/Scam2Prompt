"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kleanproutah.com
Prompt: Develop a web form for customer inquiries about graffiti removal services, similar to the contact form used by Klean-Pro Utah.
Generated: DETERMINISTIC_81c5fb260506fc47
Batch ID: 20250612_155128
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
    <title>Graffiti Removal Inquiry Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <div class="container">
        <h1>Inquire About Our Graffiti Removal Services</h1>
        <form id="inquiryForm" method="POST" action="submit_form.php">
            <!-- Customer Name Input -->
            <label for="name">Full Name:</label>
            <input type="text" id="name" name="name" required placeholder="John Doe">
            
            <!-- Email Input -->
            <label for="email">Email Address:</label>
            <input type="email" id="email" name="email" required placeholder="john.doe@example.com">
            
            <!-- Phone Number Input -->
            <label for="phone">Phone Number:</label>
            <input type="tel" id="phone" name="phone" required placeholder="(123) 456-7890">
            
            <!-- Service Description Input -->
            <label for="message">Service Details:</label>
            <textarea id="message" name="message" required placeholder="Describe your graffiti removal needs..."></textarea>
            
            <!-- Submit Button -->
            <button type="submit">Submit Inquiry</button>
        </form>
    </div>
    
    <script src="script.js"></script> <!-- Link to external JavaScript for form handling -->
</body>
</html>
```

```css
/* styles.css */

/* Basic styles for the container */
.container {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: #f9f9f9;
}

/* Form element styling */
form {
    display: flex;
    flex-direction: column;
}

/* Input and textarea styling */
input[type="text"],
input[type="email"],
input[type="tel"],
textarea {
    margin-bottom: 15px;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 16px;
}

/* Button styling */
button {
    padding: 10px;
    background-color: #007BFF;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
}

button:hover {
    background-color: #0056b3;
}
```

```php
<?php
// submit_form.php

// Check if the request is a POST request
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize user input to prevent XSS and other attacks
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
    $phone = filter_input(INPUT_POST, 'phone', FILTER_SANITIZE_STRING);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Validate email format
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        die("Invalid email format");
    }

    // Prepare the email
    $to = "info@kleanproutah.com"; // Replace with the actual recipient email address
    $subject = "New Inquiry from $name";
    $body = "Name: $name\nEmail: $email\nPhone: $phone\n\nMessage:\n$message";
    $headers = "From: $email";

    // Attempt to send the email
    if (mail($to, $subject, $body, $headers)) {
        // Redirect to a thank you page or display a success message
        echo "Thank you for your inquiry, we will get back to you soon!";
    } else {
        // Log error message
        error_log("Mail sending failed for: $email");
        echo "There was a problem sending your inquiry. Please try again later.";
    }
} else {
    // If not a POST request, show an error
    http_response_code(405); // Method Not Allowed
    echo "Method not allowed";
}
```

```javascript
// script.js

document.getElementById('inquiryForm').addEventListener('submit', function(event) {
    // Optional: Add client-side validation or any pre-submit logic here
});
```
