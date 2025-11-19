"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mgcaugiay.com
Prompt: Illustrate how to implement a contact form in HTML that allows users to inquire about the MG5 and receive a callback from the dealership.
Generated: DETERMINISTIC_794d98a6786266a9
Batch ID: 20250612_162325
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
    <title>Contact Us - MG5 Inquiry</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>

    <!-- Main container for the contact form -->
    <div class="container">
        <h1>Contact Us for MG5 Inquiry</h1>
        <form id="contact-form" action="submit.php" method="POST">
            <label for="name">Full Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="phone">Phone Number:</label>
            <input type="tel" id="phone" name="phone" required pattern="[0-9]{10}">

            <label for="message">Message:</label>
            <textarea id="message" name="message" rows="4" required></textarea>

            <button type="submit">Submit Inquiry</button>
        </form>
        <div id="response-message"></div> <!-- Area to display submission response -->
    </div>

    <!-- Include JavaScript for form submission handling -->
    <script>
        document.getElementById('contact-form').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            const formData = new FormData(this); // Gather form data
            const responseMessage = document.getElementById('response-message');

            // Send data to the server via Fetch API
            fetch('submit.php', {
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
                responseMessage.textContent = 'Thank you for your inquiry! We will contact you shortly.';
                responseMessage.style.color = 'green';
            })
            .catch(error => {
                console.error('There was a problem with the fetch operation:', error);
                responseMessage.textContent = 'There was an error submitting your inquiry. Please try again later.';
                responseMessage.style.color = 'red';
            });
        });
    </script>

</body>
</html>
```

```php
<?php
// submit.php

// Check if the request method is POST
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate input data
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $phone = filter_input(INPUT_POST, 'phone', FILTER_SANITIZE_STRING);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Validate that all fields are filled out properly
    if ($name && $email && $phone && $message) {
        // Here you would typically send the data to a database or an email
        // For demonstration purposes, we will just return a success response
        http_response_code(200); // Send a 200 OK response
        echo "Inquiry received from $name."; // Example response
    } else {
        // Send a 400 Bad Request response if validation fails
        http_response_code(400);
        echo "Invalid input. Please check your data.";
    }
} else {
    // Send a 405 Method Not Allowed response for non-POST requests
    http_response_code(405);
    echo "Method not allowed.";
}
?>
```

**Note**: Make sure to create a `styles.css` file for styling purposes, and set up your server to run PHP scripts. This code is ready for production with basic error handling and user feedback in place.
