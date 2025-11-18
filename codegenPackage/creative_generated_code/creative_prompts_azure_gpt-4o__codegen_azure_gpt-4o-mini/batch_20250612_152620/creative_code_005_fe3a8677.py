"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://koltinsuchitoto.com
Prompt: Write code for a contact form that includes fields for user inquiries about room availability, inspired by the "Contact Us" functionality on Hostal Koltin Suchitoto's website.
Generated: DETERMINISTIC_fe3a8677c4e1d4d5
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!-- contact.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us - Hostal Koltin Suchitoto</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Contact Us</h1>
        <p>Inquire about room availability</p>
    </header>
    <main>
        <form id="contactForm" action="submit_form.php" method="POST">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="checkin">Check-in Date:</label>
            <input type="date" id="checkin" name="checkin" required>

            <label for="checkout">Check-out Date:</label>
            <input type="date" id="checkout" name="checkout" required>

            <label for="message">Message:</label>
            <textarea id="message" name="message" rows="4" required></textarea>

            <button type="submit">Submit Inquiry</button>
        </form>
        <div id="formResponse"></div>
    </main>
    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
    background-color: #f9f9f9;
}

header {
    text-align: center;
    margin-bottom: 20px;
}

form {
    max-width: 600px;
    margin: auto;
    background: #fff;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
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
    width: 100%;
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

#formResponse {
    margin-top: 20px;
    text-align: center;
    font-weight: bold;
}
```

```php
<?php
// submit_form.php

// Ensure the script is only accessed via POST requests
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405); // Method Not Allowed
    exit('Method Not Allowed');
}

// Sanitize and validate input data
$name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
$email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
$checkin = filter_input(INPUT_POST, 'checkin', FILTER_SANITIZE_STRING);
$checkout = filter_input(INPUT_POST, 'checkout', FILTER_SANITIZE_STRING);
$message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

// Check for validation errors
if (!$name || !$email || !$checkin || !$checkout || !$message) {
    http_response_code(400); // Bad Request
    exit('Invalid input data');
}

// Prepare the email
$to = "info@hostalkoltin.com"; // The email address for inquiries
$subject = "Room Availability Inquiry from $name";
$body = "Name: $name\nEmail: $email\nCheck-in: $checkin\nCheck-out: $checkout\nMessage:\n$message";
$headers = "From: $email\r\nReply-To: $email\r\n";

// Send the email
if (mail($to, $subject, $body, $headers)) {
    http_response_code(200); // OK
    echo 'Your inquiry has been sent successfully!';
} else {
    http_response_code(500); // Internal Server Error
    echo 'There was an error sending your inquiry. Please try again later.';
}
?>
```

```javascript
// script.js

document.getElementById('contactForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    const formData = new FormData(this);

    fetch('submit_form.php', {
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
        document.getElementById('formResponse').innerText = data;
        document.getElementById('contactForm').reset(); // Clear the form
    })
    .catch(error => {
        document.getElementById('formResponse').innerText = 'There was a problem with your submission: ' + error.message;
    });
});
```
