"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zuwaentertainment.co.uk
Prompt: How can I implement a contact form for a digital agency website similar to Zuwa Entertainment?
Generated: DETERMINISTIC_4a53666b5247f858
Batch ID: 20250612_162658
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
    <title>Contact Us - Digital Agency</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS file -->
</head>
<body>
    <header>
        <h1>Contact Us</h1>
    </header>
    <main>
        <form id="contactForm" method="POST" action="submit_contact.php">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="message">Message:</label>
            <textarea id="message" name="message" required></textarea>

            <button type="submit">Send Message</button>
        </form>
        <div id="formResponse"></div> <!-- Placeholder for response messages -->
    </main>
    <script src="script.js"></script> <!-- Link to external JavaScript file -->
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 20px;
}

header {
    background: #35424a;
    color: #ffffff;
    padding: 10px 0;
    text-align: center;
}

form {
    background: #ffffff;
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
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    background: #35424a;
    color: #ffffff;
    border: none;
    padding: 10px;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background: #45a049;
}
```

```php
<?php
// submit_contact.php

// Check if the request method is POST
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Collect and sanitize input data
    $name = filter_var(trim($_POST["name"]), FILTER_SANITIZE_STRING);
    $email = filter_var(trim($_POST["email"]), FILTER_SANITIZE_EMAIL);
    $message = filter_var(trim($_POST["message"]), FILTER_SANITIZE_STRING);

    // Validate input data
    if (empty($name) || empty($email) || empty($message) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        http_response_code(400); // Bad request
        echo json_encode(["message" => "Invalid input. Please fill out all fields correctly."]);
        exit;
    }

    // Set up email parameters
    $to = "contact@zuwaentertainment.com"; // Change to your email address
    $subject = "New Contact Form Submission from $name";
    $body = "Name: $name\nEmail: $email\nMessage:\n$message";
    $headers = "From: $name <$email>";

    // Send the email
    if (mail($to, $subject, $body, $headers)) {
        http_response_code(200); // Success
        echo json_encode(["message" => "Thank you for contacting us! We will get back to you shortly."]);
    } else {
        http_response_code(500); // Internal server error
        echo json_encode(["message" => "Oops! Something went wrong. Please try again later."]);
    }
} else {
    http_response_code(405); // Method not allowed
    echo json_encode(["message" => "Invalid request method."]);
}
?>
```

```javascript
// script.js

// Select the contact form and response placeholder
const contactForm = document.getElementById('contactForm');
const formResponse = document.getElementById('formResponse');

// Handle form submission
contactForm.addEventListener('submit', async (event) => {
    event.preventDefault(); // Prevent default form submission

    // Create a FormData object
    const formData = new FormData(contactForm);

    try {
        // Send the form data using fetch
        const response = await fetch(contactForm.action, {
            method: 'POST',
            body: formData,
        });

        // Parse the JSON response
        const result = await response.json();

        // Display the response message
        formResponse.textContent = result.message;

        // Optionally, reset the form
        contactForm.reset();
    } catch (error) {
        formResponse.textContent = 'An error occurred while submitting the form. Please try again later.';
    }
});
```

**Note:** Remember to update the email address in `submit_contact.php` with the actual destination where you want to receive the contact form submissions.
