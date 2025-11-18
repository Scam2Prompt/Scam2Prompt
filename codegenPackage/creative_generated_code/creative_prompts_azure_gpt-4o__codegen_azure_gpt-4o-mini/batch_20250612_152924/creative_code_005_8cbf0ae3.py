"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://managementenred.com
Prompt: Provide code to implement a web form for talent acquisition inquiries, including fields for name, email, phone number, and message, as seen on Management en Red's contact section.
Generated: DETERMINISTIC_8cbf0ae3808eab1f
Batch ID: 20250612_152924
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
    <title>Talent Acquisition Inquiry Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <h1>Talent Acquisition Inquiry</h1>
    <form id="inquiryForm" method="POST" action="process_inquiry.php">
        <!-- Name Field -->
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        
        <!-- Email Field -->
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        
        <!-- Phone Number Field -->
        <label for="phone">Phone Number:</label>
        <input type="tel" id="phone" name="phone" required>
        
        <!-- Message Field -->
        <label for="message">Message:</label>
        <textarea id="message" name="message" required></textarea>
        
        <!-- Submit Button -->
        <button type="submit">Submit Inquiry</button>
    </form>

    <script src="script.js"></script> <!-- Link to external JavaScript for form validation -->
</body>
</html>
```

```php
<?php
// process_inquiry.php

// Check if the form was submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Retrieve form data with proper sanitization
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
    $phone = filter_input(INPUT_POST, 'phone', FILTER_SANITIZE_STRING);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Basic validation
    if (empty($name) || empty($email) || empty($phone) || empty($message)) {
        echo "All fields are required.";
        exit;
    }

    // Validate email format
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        echo "Invalid email format.";
        exit;
    }

    // Here you would typically send the data to a database or send an email
    // For demonstration, we will just echo the sanitized inputs
    echo "Inquiry Received:<br>";
    echo "Name: " . htmlspecialchars($name) . "<br>";
    echo "Email: " . htmlspecialchars($email) . "<br>";
    echo "Phone: " . htmlspecialchars($phone) . "<br>";
    echo "Message: " . nl2br(htmlspecialchars($message)) . "<br>";
} else {
    // Handle invalid access to the script
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
}

label {
    display: block;
    margin-bottom: 5px;
}

input, textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    background-color: #28a745;
    color: white;
    padding: 10px 15px;
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

// Function to handle form submission and validate inputs
document.getElementById('inquiryForm').addEventListener('submit', function(event) {
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;
    const message = document.getElementById('message').value;

    // Basic client-side validation
    if (!name || !email || !phone || !message) {
        alert("All fields are required.");
        event.preventDefault(); // Prevent form submission
    }
});
```
