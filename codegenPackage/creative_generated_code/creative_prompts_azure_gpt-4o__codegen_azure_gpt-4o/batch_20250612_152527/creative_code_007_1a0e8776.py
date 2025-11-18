"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iebcatitiribi.edu.co
Prompt: Generate code to create a contact form for an educational institution's website, using the contact details (address, email, phone number) provided on the IEBCA website.
Generated: DETERMINISTIC_1a0e8776a902f0c4
Batch ID: 20250612_152527
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
    <title>Contact Form - Educational Institution</title>
    <link rel="stylesheet" href="styles.css"> <!-- External stylesheet for styling -->
</head>
<body>
    <header>
        <h1>Contact Us</h1>
        <p>Feel free to reach out to us using the form below or contact us directly through the provided details.</p>
    </header>
    
    <section>
        <!-- Contact Details -->
        <div id="contact-details">
            <h2>Contact Information</h2>
            <p><strong>Address:</strong> Example Street, Example City, Country</p> <!-- Replace with IEBCA address -->
            <p><strong>Email:</strong> contact@example.edu</p> <!-- Replace with IEBCA email -->
            <p><strong>Phone:</strong> +1 (123) 456-7890</p> <!-- Replace with IEBCA phone number -->
        </div>
    </section>
    
    <section>
        <!-- Contact Form -->
        <form id="contact-form" action="submit_form.php" method="POST">
            <h2>Send Us a Message</h2>
            
            <!-- Full Name -->
            <label for="name">Full Name:</label>
            <input type="text" id="name" name="name" required minlength="2" maxlength="100">
            
            <!-- Email -->
            <label for="email">Email Address:</label>
            <input type="email" id="email" name="email" required>
            
            <!-- Subject -->
            <label for="subject">Subject:</label>
            <input type="text" id="subject" name="subject" required maxlength="200">
            
            <!-- Message -->
            <label for="message">Message:</label>
            <textarea id="message" name="message" rows="5" required maxlength="1000"></textarea>
            
            <!-- Submit Button -->
            <button type="submit">Send Message</button>
        </form>
    </section>
    
    <footer>
        <p>&copy; 2023 Educational Institution. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* General Styles */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    line-height: 1.6;
    color: #333;
    background-color: #f4f4f4;
}
header, section, footer {
    margin: 20px auto;
    padding: 20px;
    max-width: 800px;
    background: #fff;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
h1, h2 {
    color: #2c3e50;
}
label {
    display: block;
    margin: 10px 0 5px;
}
input, textarea, button {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    box-sizing: border-box;
}
button {
    background-color: #3498db;
    color: #fff;
    border: none;
    cursor: pointer;
    font-size: 16px;
}
button:hover {
    background-color: #2980b9;
}

/* Footer */
footer {
    text-align: center;
    margin-top: 20px;
    padding-top: 10px;
    font-size: 14px;
}
```

```php
<?php
// submit_form.php

// Ensure proper error reporting during development
error_reporting(E_ALL);
ini_set('display_errors', "1");

// Check if the form is submitted via POST
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    // Validate and sanitize inputs
    $name = htmlspecialchars(trim($_POST['name']));
    $email = filter_var(trim($_POST['email']), FILTER_VALIDATE_EMAIL);
    $subject = htmlspecialchars(trim($_POST['subject']));
    $message = htmlspecialchars(trim($_POST['message']));

    // Basic validation
    if (empty($name) || empty($email) || empty($subject) || empty($message)) {
        die("Error: All fields are required.");
    }

    if (!$email) {
        die("Error: Invalid email address.");
    }

    // Email configuration
    $to = "contact@example.edu"; // Replace with the institution's email
    $headers = "From: $email\r\n";
    $headers .= "Reply-To: $email\r\n";
    $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

    // Send email
    $emailSent = mail($to, $subject, $message, $headers);

    if ($emailSent) {
        echo "Thank you for reaching out. Your message has been sent successfully.";
    } else {
        echo "Error: Unable to send your message. Please try again later.";
    }
} else {
    // If accessed directly, display an error message
    die("Error: Invalid request.");
}
?>
```
