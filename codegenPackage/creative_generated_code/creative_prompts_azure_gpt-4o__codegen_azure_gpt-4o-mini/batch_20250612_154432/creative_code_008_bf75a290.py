"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://oeg-group.com
Prompt: Write code to implement a contact form for scheduling consultations about outdoor environment design and build services, referencing the "Connect" section of Outdoor Environments Group.
Generated: DETERMINISTIC_bf75a290c899f5d0
Batch ID: 20250612_154432
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
    <title>Contact Us - Outdoor Environments Group</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Contact Outdoor Environments Group</h1>
        <p>Schedule a consultation for our design and build services.</p>
    </header>

    <main>
        <form id="contactForm" action="submit_form.php" method="POST" novalidate>
            <label for="name">Full Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="phone">Phone Number:</label>
            <input type="tel" id="phone" name="phone" required>

            <label for="message">Message:</label>
            <textarea id="message" name="message" rows="4" required></textarea>

            <button type="submit">Schedule Consultation</button>
        </form>
    </main>

    <footer>
        <p>&copy; 2023 Outdoor Environments Group. All rights reserved.</p>
    </footer>

    <script>
        // Client-side form validation
        document.getElementById('contactForm').addEventListener('submit', function(event) {
            const form = event.target;

            // Check if the form is valid
            if (!form.checkValidity()) {
                event.preventDefault();
                alert('Please fill in all required fields.');
            }
        });
    </script>
</body>
</html>
```

```php
<?php
// submit_form.php

// Function to sanitize user input
function sanitizeInput($data) {
    return htmlspecialchars(stripslashes(trim($data)));
}

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Initialize variables and sanitize inputs
    $name = sanitizeInput($_POST['name']);
    $email = sanitizeInput($_POST['email']);
    $phone = sanitizeInput($_POST['phone']);
    $message = sanitizeInput($_POST['message']);

    // Validate email
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        die("Invalid email format");
    }

    // Prepare email
    $to = "info@outdoorenvironmentsgroup.com"; // Change to the appropriate recipient
    $subject = "New Consultation Request from $name";
    $body = "You have received a new consultation request.\n\n"
          . "Name: $name\n"
          . "Email: $email\n"
          . "Phone: $phone\n"
          . "Message:\n$message";

    // Set the content-type header for HTML emails
    $headers = "From: $email\r\n" .
               "Reply-To: $email\r\n" .
               "Content-Type: text/plain;charset=UTF-8\r\n";

    // Attempt to send the email
    if (mail($to, $subject, $body, $headers)) {
        echo "Thank you for your request, $name. We will get back to you soon!";
    } else {
        echo "There was a problem sending your request. Please try again later.";
    }
} else {
    // Handle cases where the form is not submitted via POST
    http_response_code(405);
    echo "Method not allowed";
}
?>
```

```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
    background-color: #f4f4f4;
}

header {
    background: #007BFF;
    color: white;
    padding: 15px;
    text-align: center;
}

form {
    background: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    max-width: 600px;
    margin: auto;
}

label {
    display: block;
    margin: 10px 0 5px;
}

input, textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    background-color: #007BFF;
    color: white;
    border: none;
    padding: 10px 15px;
    cursor: pointer;
    border-radius: 5px;
}

button:hover {
    background-color: #0056b3;
}

footer {
    text-align: center;
    margin-top: 20px;
}
```
