"""
Generated Code Metadata:
========================
Original URL: https://la-guarida.com.ar
Prompt: Develop a landing page for a digital campaign, including features such as call-to-action buttons and email subscription forms, inspired by La Guarida's services.
Generated: DETERMINISTIC_3859d1493904b19d
Batch ID: 20250612_155000
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
    <meta name="description" content="Join La Guarida's digital campaign and stay updated with our services.">
    <title>La Guarida Digital Campaign</title>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js" defer></script>
</head>
<body>
    <header>
        <h1>Welcome to La Guarida</h1>
        <p>Your gateway to exceptional services.</p>
    </header>

    <main>
        <section id="cta-section">
            <h2>Join Our Campaign</h2>
            <p>Discover our services and stay informed about our latest offerings.</p>
            <button id="learn-more-btn">Learn More</button>
        </section>

        <section id="subscription-section">
            <h2>Subscribe to Our Newsletter</h2>
            <form id="subscription-form" action="subscribe.php" method="POST">
                <label for="email">Email Address:</label>
                <input type="email" id="email" name="email" required placeholder="you@example.com">
                <button type="submit">Subscribe</button>
            </form>
            <p id="subscription-message"></p>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 La Guarida. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for margins and paddings */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body styles */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
    color: #333;
}

/* Header styles */
header {
    background: #007BFF;
    color: white;
    padding: 20px;
    text-align: center;
}

/* Main section styles */
main {
    padding: 20px;
}

/* Call-to-action section styles */
#cta-section {
    background: #e9ecef;
    padding: 20px;
    text-align: center;
    margin-bottom: 20px;
}

/* Subscription section styles */
#subscription-section {
    background: #ffffff;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

/* Form styles */
form {
    display: flex;
    flex-direction: column;
    align-items: center;
}

input[type="email"] {
    padding: 10px;
    margin: 10px 0;
    width: 80%;
    max-width: 400px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

button {
    padding: 10px 20px;
    background: #007BFF;
    color: white;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background: #0056b3;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 10px;
    background: #007BFF;
    color: white;
    position: relative;
    bottom: 0;
    width: 100%;
}
```

```javascript
// script.js

// Wait for the DOM to fully load
document.addEventListener("DOMContentLoaded", function() {
    // Get the subscription form and message elements
    const subscriptionForm = document.getElementById('subscription-form');
    const subscriptionMessage = document.getElementById('subscription-message');

    // Handle form submission
    subscriptionForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent the default form submission

        // Get the email value
        const email = document.getElementById('email').value;

        // Simple email validation
        if (validateEmail(email)) {
            // Simulate a successful subscription
            subscriptionMessage.textContent = "Thank you for subscribing!";
            subscriptionMessage.style.color = "green";
            subscriptionForm.reset(); // Reset the form
        } else {
            // Show an error message for invalid email
            subscriptionMessage.textContent = "Please enter a valid email address.";
            subscriptionMessage.style.color = "red";
        }
    });

    // Function to validate email format
    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(String(email).toLowerCase());
    }

    // Learn more button functionality
    document.getElementById('learn-more-btn').addEventListener('click', function() {
        window.location.href = 'services.html'; // Redirect to services page
    });
});
```

```php
<?php
// subscribe.php

// Check if the request method is POST
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get the email from the form
    $email = filter_var(trim($_POST["email"]), FILTER_SANITIZE_EMAIL);

    // Validate the email
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        http_response_code(400); // Bad request
        echo "Invalid email address.";
        exit;
    }

    // Here you would typically save the email to a database or send it to an API
    // For demonstration, we'll just return a success message
    echo "Subscription successful for: " . htmlspecialchars($email);
} else {
    // If the request method is not POST, return a 405 Method Not Allowed
    http_response_code(405);
    echo "Method not allowed.";
}
?>
```
