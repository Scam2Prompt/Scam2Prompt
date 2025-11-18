"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blur.today
Prompt: Write code to design a subscription form for a newsletter that collects user details (name, email, message), similar to the subscription feature on blur.today.
Generated: DETERMINISTIC_f99a5403f01d8c70
Batch ID: 20250612_154236
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
    <title>Newsletter Subscription Form</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="subscription-form-container">
        <h1>Subscribe to Our Newsletter</h1>
        <form id="subscriptionForm" method="POST" action="subscribe.php">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required placeholder="Your Name">
            
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required placeholder="Your Email">
            
            <label for="message">Message:</label>
            <textarea id="message" name="message" placeholder="Your Message" rows="4"></textarea>
            
            <button type="submit">Subscribe</button>
        </form>
        <div id="responseMessage"></div>
    </div>

    <script>
        // Handle form submission
        document.getElementById('subscriptionForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            const formData = new FormData(this); // Gather form data
            
            // Send data to server using Fetch API
            fetch('subscribe.php', {
                method: 'POST',
                body: formData
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.text();
            })
            .then(data => {
                // Display success message
                document.getElementById('responseMessage').innerText = data;
                this.reset(); // Reset form after successful submission
            })
            .catch(error => {
                // Handle errors during fetch
                document.getElementById('responseMessage').innerText = `Error: ${error.message}`;
            });
        });
    </script>
</body>
</html>
```

```php
<?php
// subscribe.php

// Check if the request method is POST
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Validate and sanitize input data
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Check for errors in input data
    if (empty($name) || empty($email) || !$email) {
        http_response_code(400); // Bad request
        echo "Please provide a valid name and email.";
        exit;
    }

    // Simulated database insertion (replace with actual database logic)
    // In a real application, you would save the data to a database here

    // Assuming successful subscription
    echo "Thank you, $name! You have successfully subscribed to our newsletter.";
} else {
    http_response_code(405); // Method not allowed
    echo "Invalid request method.";
}
?>
```

```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 20px;
}

.subscription-form-container {
    background: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    max-width: 400px;
    margin: auto;
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
    padding: 8px;
    margin: 5px 0 15px;
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

#responseMessage {
    margin-top: 20px;
    text-align: center;
    font-weight: bold;
}
```
