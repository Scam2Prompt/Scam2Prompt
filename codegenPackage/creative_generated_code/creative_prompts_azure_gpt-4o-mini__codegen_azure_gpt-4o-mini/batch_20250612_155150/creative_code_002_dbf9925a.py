"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://specialmetals.co.in
Prompt: Create a sample code to implement a web form that allows users to submit inquiries about Duplex Steel Pipes, referencing the features provided by Dinkar Alloys.
Generated: DETERMINISTIC_dbf9925afc3642e0
Batch ID: 20250612_155150
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
    <title>Duplex Steel Pipes Inquiry Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external stylesheet -->
</head>
<body>
    <h1>Inquiry Form for Duplex Steel Pipes</h1>
    <form id="inquiryForm" action="submitInquiry.php" method="POST">
        <!-- User Name Input -->
        <label for="name">Your Name:</label>
        <input type="text" id="name" name="name" required>
        
        <!-- User Email Input -->
        <label for="email">Your Email:</label>
        <input type="email" id="email" name="email" required>

        <!-- Inquiry Subject Input -->
        <label for="subject">Subject:</label>
        <input type="text" id="subject" name="subject" required>

        <!-- Inquiry Details Input -->
        <label for="message">Your Inquiry:</label>
        <textarea id="message" name="message" rows="4" required></textarea>

        <!-- Submit Button -->
        <button type="submit">Submit Inquiry</button>
    </form>

    <script src="script.js"></script> <!-- Link to external JavaScript -->
</body>
</html>
```

```php
<?php
// submitInquiry.php

// Start the session and enable error reporting
session_start();
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Function to sanitize input data
function sanitizeInput($data) {
    return htmlspecialchars(stripslashes(trim($data)));
}

// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Retrieve and sanitize user input
    $name = sanitizeInput($_POST['name']);
    $email = sanitizeInput($_POST['email']);
    $subject = sanitizeInput($_POST['subject']);
    $message = sanitizeInput($_POST['message']);

    // Validate email format
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        echo "Invalid email format";
        exit;
    }

    // Prepare the email content
    $to = "info@dinkaralloys.com"; // Replace with actual recipient email
    $headers = "From: $email\r\n" .
               "Reply-To: $email\r\n" .
               "Content-Type: text/plain; charset=UTF-8\r\n";

    $emailBody = "Name: $name\n".
                 "Email: $email\n".
                 "Subject: $subject\n".
                 "Message: $message\n";

    // Send email and handle potential errors
    if (mail($to, $subject, $emailBody, $headers)) {
        echo "Inquiry submitted successfully.";
    } else {
        echo "Error sending inquiry. Please try again later.";
    }
} else {
    echo "Invalid request method.";
}
?>
```

```css
/* styles.css */

/* Basic styling for the form */
body {
    font-family: Arial, sans-serif;
    margin: 20px;
}

h1 {
    color: #333;
}

form {
    display: flex;
    flex-direction: column;
    max-width: 400px;
}

label {
    margin-top: 10px;
}

input, textarea {
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
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
```

```javascript
// script.js

// JavaScript for form validation can be added here for more enhanced user experience
document.getElementById('inquiryForm').addEventListener('submit', function(event) {
    // Basic client-side validation can go here if needed
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    
    if (!name || !email) {
        alert("Please fill in all required fields.");
        event.preventDefault(); // Prevent form submission
    }
});
```
