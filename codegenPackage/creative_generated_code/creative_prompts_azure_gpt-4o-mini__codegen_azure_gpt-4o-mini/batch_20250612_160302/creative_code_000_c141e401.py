"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idex.xyz
Prompt: How can I create a price request form for a domain like Idex.xyz to facilitate domain sales?
Generated: DETERMINISTIC_c141e4017d1b5550
Batch ID: 20250612_160302
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
    <title>Domain Price Request Form</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Request a Price for Idex.xyz</h1>
        <form id="priceRequestForm" method="POST" action="submit_request.php">
            <!-- User's name input -->
            <label for="name">Your Name:</label>
            <input type="text" id="name" name="name" required>

            <!-- User's email input -->
            <label for="email">Your Email:</label>
            <input type="email" id="email" name="email" required>

            <!-- Domain name input -->
            <label for="domain">Domain Name:</label>
            <input type="text" id="domain" name="domain" value="Idex.xyz" readonly>

            <!-- Message input for additional information -->
            <label for="message">Additional Message:</label>
            <textarea id="message" name="message" rows="4"></textarea>

            <!-- Submit button -->
            <button type="submit">Request Price</button>
        </form>
        <div id="responseMessage" class="hidden"></div>
    </div>

    <script>
        // Handle form submission
        document.getElementById('priceRequestForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            const formData = new FormData(this);

            // Send the request to the server
            fetch('submit_request.php', {
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
                // Display success message
                document.getElementById('responseMessage').innerText = 'Your request has been submitted successfully!';
                document.getElementById('responseMessage').classList.remove('hidden');
            })
            .catch(error => {
                // Display error message
                document.getElementById('responseMessage').innerText = 'There was an error: ' + error.message;
                document.getElementById('responseMessage').classList.remove('hidden');
            });
        });
    </script>
</body>
</html>
```

```php
<?php
// submit_request.php

// Check if the request method is POST
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Sanitize and validate input data
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_VALIDATE_EMAIL);
    $domain = filter_input(INPUT_POST, 'domain', FILTER_SANITIZE_STRING);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    if (!$email) {
        // If email is invalid, return an error response
        http_response_code(400);
        echo 'Invalid email address.';
        exit;
    }

    // Here you would typically handle the request, e.g., save to a database or send an email
    // For demonstration, we're just simulating a successful response
    // In production, ensure to log errors and handle exceptions properly

    http_response_code(200);
    echo 'Success';
} else {
    // If the request method is not POST, return a 405 Method Not Allowed
    http_response_code(405);
    echo 'Method Not Allowed';
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

.container {
    max-width: 500px;
    margin: auto;
    background: white;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
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

.hidden {
    display: none;
}

#responseMessage {
    margin-top: 10px;
    text-align: center;
    font-weight: bold;
}
```
