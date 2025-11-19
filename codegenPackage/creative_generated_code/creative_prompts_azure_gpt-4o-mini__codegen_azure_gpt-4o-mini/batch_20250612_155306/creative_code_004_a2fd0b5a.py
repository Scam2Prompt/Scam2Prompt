"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polyhedra-consulting.com
Prompt: Write a code snippet that demonstrates how to set up a contact form for a consulting website focused on polyhedra.
Generated: DETERMINISTIC_a2fd0b5aedb2003e
Batch ID: 20250612_155306
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
    <title>Contact Us - Polyhedra Consulting</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external stylesheet -->
</head>
<body>
    <header>
        <h1>Contact Polyhedra Consulting</h1>
    </header>

    <main>
        <form id="contactForm" action="submit_contact.php" method="POST">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required placeholder="Your Name">

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required placeholder="Your Email">

            <label for="message">Message:</label>
            <textarea id="message" name="message" required placeholder="Your Message"></textarea>

            <button type="submit">Send Message</button>
        </form>

        <div id="formResponse" class="response"></div> <!-- Container for form submission response -->
    </main>

    <script>
        // Add event listener to handle form submission
        document.getElementById('contactForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission
            
            // Serialize form data
            const formData = new FormData(this);
            
            // Send form data to the server using Fetch API
            fetch(this.action, {
                method: this.method,
                body: formData
            })
            .then(response => {
                // Check if response is OK
                if (!response.ok) {
                    throw new Error('Network response was not ok ' + response.statusText);
                }
                return response.text(); // Parse response as text
            })
            .then(data => {
                // Display success message
                document.getElementById('formResponse').innerText = 'Message sent successfully!';
                document.getElementById('contactForm').reset(); // Reset the form
            })
            .catch(error => {
                // Handle errors appropriately
                document.getElementById('formResponse').innerText = 'There was a problem sending your message: ' + error.message;
            });
        });
    </script>

    <footer>
        <p>&copy; 2023 Polyhedra Consulting. All rights reserved.</p>
    </footer>
</body>
</html>
```

```php
<?php
// submit_contact.php

// Check if the request method is POST
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Collect and sanitize input data
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Validate email format
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        http_response_code(400); // Bad Request response code
        die("Invalid email format");
    }

    // Prepare email details
    $to = 'info@polyhedronconsulting.com'; // Change to your email
    $subject = 'New Contact Form Submission';
    $body = "Name: $name\nEmail: $email\nMessage:\n$message";
    $headers = "From: $email\r\n";

    // Attempt to send the email
    if (mail($to, $subject, $body, $headers)) {
        http_response_code(200); // OK response code
        echo "Message sent successfully!";
    } else {
        http_response_code(500); // Internal Server Error response code
        echo "Failed to send message.";
    }
} else {
    http_response_code(405); // Method Not Allowed response code
    echo "Invalid request method.";
}
?>
```
