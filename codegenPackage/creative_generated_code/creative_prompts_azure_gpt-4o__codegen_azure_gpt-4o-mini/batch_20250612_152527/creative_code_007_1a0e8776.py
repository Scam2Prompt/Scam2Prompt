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
    <title>Contact Us - Educational Institution</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>

<body>
    <header>
        <h1>Contact Us</h1>
    </header>

    <main>
        <form id="contactForm" action="process_contact.php" method="post">
            <fieldset>
                <legend>Contact Details</legend>

                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required placeholder="Your Name">

                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required placeholder="Your Email">

                <label for="phone">Phone Number:</label>
                <input type="tel" id="phone" name="phone" required placeholder="Your Phone Number">

                <label for="message">Message:</label>
                <textarea id="message" name="message" rows="4" required placeholder="Your Message"></textarea>

                <button type="submit">Send Message</button>
            </fieldset>
        </form>

        <section id="contactInfo">
            <h2>Our Contact Details</h2>
            <p><strong>Address:</strong> 123 Education St, Knowledge City, 12345</p>
            <p><strong>Email:</strong> info@iebca.edu</p>
            <p><strong>Phone:</strong> +1 (555) 123-4567</p>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Educational Institution. All Rights Reserved.</p>
    </footer>
    
    <script src="script.js"></script> <!-- Link to external JavaScript for any client-side validation -->
</body>

</html>
```

```php
<?php
// process_contact.php

// Start the session
session_start();

// Check if the request method is POST
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Retrieve and sanitize input data
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
    $phone = filter_input(INPUT_POST, 'phone', FILTER_SANITIZE_STRING);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Validate email
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        die("Invalid email format");
    }

    // Prepare the email
    $to = "info@iebca.edu"; // Change this to the institution's email
    $subject = "New Contact Form Submission from $name";
    $body = "Name: $name\nEmail: $email\nPhone: $phone\nMessage:\n$message";
    $headers = "From: $email\r\n";

    // Attempt to send the email
    if (mail($to, $subject, $body, $headers)) {
        // Redirect to a thank you page or display success message
        header('Location: thank_you.html');
        exit();
    } else {
        // Log error and display a user-friendly message
        error_log("Email sending failed for: $name <$email>");
        echo "There was an error sending your message. Please try again later.";
    }
} else {
    // If the request method is not POST, redirect to the contact form
    header('Location: contact_form.html');
    exit();
}
?>
```

```css
/* styles.css */

/* Basic styling for the body */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 0;
}

/* Styling for header */
header, footer {
    background-color: #333;
    color: white;
    padding: 10px 20px;
    text-align: center;
}

/* Main content styling */
main {
    margin: 20px;
}

/* Form styling */
form {
    background: #f4f4f4;
    padding: 20px;
    border-radius: 5px;
}

/* Fieldset styling */
fieldset {
    border: none;
}

/* Input styling */
input, textarea {
    width: 100%;
    padding: 10px;
    margin: 10px 0;
    border: 1px solid #ccc;
    border-radius: 5px;
}

/* Button styling */
button {
    background: #333;
    color: white;
    border: none;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer;
}

/* Button hover effect */
button:hover {
    background: #555;
}
```

```javascript
// script.js

// Client-side validation can be added here if needed
document.getElementById('contactForm').addEventListener('submit', function(event) {
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const phone = document.getElementById('phone').value;
    const message = document.getElementById('message').value;

    // Basic validation (can be enhanced)
    if (name === "" || email === "" || phone === "" || message === "") {
        alert("Please fill out all fields.");
        event.preventDefault(); // Prevent form submission
    }
});
```

This code creates a simple yet fully functional contact form for an educational institution's website, including proper validation, error handling, and styling.
