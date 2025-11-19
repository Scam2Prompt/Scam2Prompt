"""
Generated Code Metadata:
========================
Original URL: https://perrigo-claims.info
Prompt: Generate a code snippet that demonstrates how to implement a contact form for a pharmaceutical company, including fields for name, email, and message, similar to the contact details provided on the Perrigo Claims website.
Generated: DETERMINISTIC_77ab82ed04f35d58
Batch ID: 20250612_135906
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
    <title>Contact Us - Pharmaceutical Company</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <div class="container">
        <h1>Contact Us</h1>
        <form id="contactForm" action="submit_contact.php" method="POST">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required placeholder="Your Name">

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required placeholder="Your Email">

            <label for="message">Message:</label>
            <textarea id="message" name="message" required placeholder="Your Message"></textarea>

            <button type="submit">Submit</button>
        </form>
        <div id="formResponse" class="response"></div> <!-- Placeholder for response messages -->
    </div>

    <script>
        // Handle form submission
        document.getElementById('contactForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            // Gather form data
            const formData = new FormData(this);

            // Send data to the server using Fetch API
            fetch('submit_contact.php', {
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
                document.getElementById('formResponse').innerText = data; // Display success message
                this.reset(); // Reset the form
            })
            .catch(error => {
                document.getElementById('formResponse').innerText = 'Error: ' + error.message; // Display error message
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
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate input data
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Check for validation errors
    if (!$name || !$email || !$message) {
        http_response_code(400); // Bad Request
        echo "Please fill in all fields correctly.";
        exit;
    }

    // Here you would typically send the email or save the data to a database
    // For demonstration, we will just simulate a successful response
    // mail($to, $subject, $message, $headers); // Uncomment to send email

    // Send a success response
    http_response_code(200); // OK
    echo "Thank you for contacting us, $name. We will get back to you shortly.";
} else {
    // If the request method is not POST, return a 405 Method Not Allowed response
    http_response_code(405); // Method Not Allowed
    echo "Method not allowed.";
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
    background-color: #5cb85c;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #4cae4c;
}

.response {
    margin-top: 20px;
    text-align: center;
    color: green;
}
```
