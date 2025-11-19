"""
Generated Code Metadata:
========================
Original URL: https://sembradordevidaac.org
Prompt: What are the steps to create a web form for users to contact Sembrador de Vida and request group training?
Generated: DETERMINISTIC_3b00aeed6d8fe135
Batch ID: 20250612_135557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Sembrador de Vida</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <div class="container">
        <h1>Contact Sembrador de Vida</h1>
        <form id="contactForm" action="submit_form.php" method="POST">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="message">Message:</label>
            <textarea id="message" name="message" rows="4" required></textarea>

            <button type="submit">Request Group Training</button>
        </form>
        <div id="formResponse" class="response"></div> <!-- Placeholder for form submission response -->
    </div>

    <script>
        // Handle form submission
        document.getElementById('contactForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            // Gather form data
            const formData = new FormData(this);

            // Send form data to the server using Fetch API
            fetch('submit_form.php', {
                method: 'POST',
                body: formData
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.text(); // Parse response as text
            })
            .then(data => {
                document.getElementById('formResponse').innerText = data; // Display response
                document.getElementById('contactForm').reset(); // Reset form fields
            })
            .catch(error => {
                document.getElementById('formResponse').innerText = 'Error: ' + error.message; // Display error
            });
        });
    </script>
</body>
</html>
```

```php
<?php
// submit_form.php

// Check if the request method is POST
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate input data
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Check if email is valid
    if ($email === false) {
        http_response_code(400); // Bad Request
        echo "Invalid email address.";
        exit;
    }

    // Prepare email parameters
    $to = "contact@sembradordevida.org"; // Replace with actual email
    $subject = "Group Training Request from $name";
    $body = "Name: $name\nEmail: $email\nMessage:\n$message";
    $headers = "From: $email\r\n";

    // Send email
    if (mail($to, $subject, $body, $headers)) {
        echo "Thank you for your request, $name. We will get back to you soon.";
    } else {
        http_response_code(500); // Internal Server Error
        echo "There was an error sending your request. Please try again later.";
    }
} else {
    http_response_code(405); // Method Not Allowed
    echo "Invalid request method.";
}
?>
```

```css
/* styles.css */

/* Basic styling for the contact form */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 20px;
}

.container {
    max-width: 600px;
    margin: auto;
    background: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
    text-align: center;
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

.response {
    margin-top: 20px;
    text-align: center;
    color: green;
}
```
