"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://segretoskincare.it
Prompt: Design a simple HTML form that allows users to subscribe to a skincare newsletter, incorporating a discount feature like the one offered by Segreto Skincare for new subscribers.
Generated: DETERMINISTIC_4dcd9a21d5ea1314
Batch ID: 20250612_162051
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
    <title>Skincare Newsletter Subscription</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external stylesheet -->
    <script src="script.js" defer></script> <!-- Link to external JavaScript file -->
</head>
<body>
    <header>
        <h1>Subscribe to Our Skincare Newsletter</h1>
        <p>Get exclusive discounts on your first purchase!</p>
    </header>

    <main>
        <form id="subscriptionForm" action="subscribe.php" method="POST">
            <label for="name">Full Name:</label>
            <input type="text" id="name" name="name" required placeholder="Enter your full name">
            
            <label for="email">Email Address:</label>
            <input type="email" id="email" name="email" required placeholder="Enter your email address">
            
            <label for="discountCode">Discount Code:</label>
            <input type="text" id="discountCode" name="discountCode" placeholder="Optional discount code">
            
            <button type="submit">Subscribe</button>
        </form>

        <div id="responseMessage" class="hidden"></div> <!-- Response message will be displayed here -->
    </main>

    <footer>
        <p>&copy; 2023 Segreto Skincare. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset */
body, h1, p, label {
    margin: 0;
    padding: 0;
    font-family: Arial, sans-serif;
}

header, main, footer {
    padding: 20px;
}

h1 {
    color: #333;
}

form {
    display: flex;
    flex-direction: column;
    max-width: 400px;
    margin: auto;
}

label {
    margin-top: 10px;
}

input {
    padding: 10px;
    margin-top: 5px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    margin-top: 15px;
    padding: 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #45a049;
}

.hidden {
    display: none;
}

#responseMessage {
    margin-top: 20px;
    color: red;
}
```

```javascript
// script.js

// Event listener for the form submission
document.getElementById('subscriptionForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the default form submission behavior

    const formData = new FormData(this); // Create a FormData object from the form
    const responseMessage = document.getElementById('responseMessage'); // Get the response message element

    // Send form data using Fetch API
    fetch(this.action, {
        method: this.method,
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.text();
    })
    .then(data => {
        responseMessage.textContent = 'Subscription successful! Check your email for the discount.';
        responseMessage.classList.remove('hidden');
        this.reset(); // Reset the form after successful submission
    })
    .catch(error => {
        responseMessage.textContent = 'An error occurred: ' + error.message;
        responseMessage.classList.remove('hidden');
    });
});
```

```php
<?php
// subscribe.php

// Enable error reporting for debugging purposes (remove in production)
ini_set('display_errors', 1);
error_reporting(E_ALL);

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate input data
    $name = filter_var(trim($_POST['name']), FILTER_SANITIZE_STRING);
    $email = filter_var(trim($_POST['email']), FILTER_SANITIZE_EMAIL);
    $discountCode = filter_var(trim($_POST['discountCode']), FILTER_SANITIZE_STRING);

    // Validate email
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        http_response_code(400);
        echo 'Invalid email address.';
        exit;
    }

    // Here you can add the logic to save the subscriber's data, e.g., to a database
    // For demonstration, we will just echo a success message
    echo 'Subscription successful for ' . htmlspecialchars($name) . '!';
} else {
    http_response_code(405);
    echo 'Method not allowed.';
    exit;
}
?>
```
