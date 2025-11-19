"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qwaliconnect.com
Prompt: Generate a code snippet for a contact form that captures user input similar to the one described on Qwali Connect's contact page.
Generated: DETERMINISTIC_72c9734497e38c72
Batch ID: 20250612_155509
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
    <title>Contact Form</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <div class="contact-container">
        <h1>Contact Us</h1>
        <form id="contactForm" method="POST" action="submit_contact.php">
            <label for="name">Full Name:</label>
            <input type="text" id="name" name="name" required placeholder="Your full name">
            
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required placeholder="Your email address">
            
            <label for="subject">Subject:</label>
            <input type="text" id="subject" name="subject" required placeholder="Subject of your message">
            
            <label for="message">Message:</label>
            <textarea id="message" name="message" required placeholder="Your message" rows="4"></textarea>
            
            <button type="submit">Send Message</button>
        </form>
        <div id="formResponse" class="response-message"></div>
    </div>

    <script>
        // Handle form submission with AJAX to prevent page reload
        document.getElementById('contactForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            const formData = new FormData(this);
            const responseDiv = document.getElementById('formResponse');

            fetch('submit_contact.php', {
                method: 'POST',
                body: formData
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok ' + response.statusText);
                }
                return response.text();
            })
            .then(data => {
                responseDiv.innerText = 'Your message has been sent successfully!';
                responseDiv.className = 'success';
                this.reset(); // Reset the form after successful submission
            })
            .catch(error => {
                responseDiv.innerText = 'There was a problem with your submission: ' + error.message;
                responseDiv.className = 'error';
            });
        });
    </script>
</body>
</html>
```

```php
<?php
// submit_contact.php

// Check if the request method is POST
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate and sanitize input data
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
    $subject = filter_input(INPUT_POST, 'subject', FILTER_SANITIZE_STRING);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Basic validation
    if (empty($name) || empty($email) || empty($subject) || empty($message)) {
        http_response_code(400); // Bad request
        echo "All fields are required.";
        exit;
    }

    // Validate email format
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        http_response_code(400); // Bad request
        echo "Invalid email format.";
        exit;
    }

    // Here you would typically send the email or save to a database
    // For this example, we'll just simulate success
    http_response_code(200); // OK
    echo "Message sent successfully.";
} else {
    http_response_code(405); // Method Not Allowed
    echo "Invalid request method.";
}
?>
```

```css
/* styles.css */

/* Basic styles for the contact form */
.contact-container {
    max-width: 600px;
    margin: auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: #f9f9f9;
}

label {
    display: block;
    margin: 10px 0 5px;
}

input[type="text"], 
input[type="email"], 
textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    padding: 10px 15px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}

.response-message {
    margin-top: 15px;
}

.success {
    color: green;
}

.error {
    color: red;
}
```
