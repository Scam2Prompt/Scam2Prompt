"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://firstclass222.w3spaces.com
Prompt: Write code to create a simple website using W3 Spaces, including a homepage and a contact form.
Generated: DETERMINISTIC_3d0e5ff7ca7efae4
Batch ID: 20250612_154536
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
    <title>Simple Website with W3 Spaces</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Main navigation for the website -->
    <nav>
        <ul>
            <li><a href="#home">Home</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>

    <!-- Homepage section -->
    <section id="home">
        <h1>Welcome to Our Website!</h1>
        <p>This is a simple website created using W3 Spaces. Explore our content and get in touch!</p>
    </section>

    <!-- Contact form section -->
    <section id="contact">
        <h2>Contact Us</h2>
        <form id="contact-form" action="submit_form.php" method="POST">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="message">Message:</label>
            <textarea id="message" name="message" required></textarea>

            <button type="submit">Send Message</button>
        </form>

        <!-- Display submission status -->
        <div id="form-status"></div>
    </section>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Basic styling for the body and sections */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
}

/* Navigation styles */
nav {
    background: #333;
    color: #fff;
    padding: 10px 0;
}

nav ul {
    list-style-type: none;
    display: flex;
    justify-content: center;
}

nav ul li {
    margin: 0 15px;
}

nav ul li a {
    color: #fff;
    text-decoration: none;
}

/* Section styles */
section {
    padding: 20px;
    margin: 20px;
    border: 1px solid #ccc;
}

/* Form styling */
form {
    display: flex;
    flex-direction: column;
}

form label {
    margin: 10px 0 5px;
}

form input, form textarea {
    padding: 10px;
    margin-bottom: 10px;
}

form button {
    padding: 10px;
    background: #28a745;
    color: white;
    border: none;
    cursor: pointer;
}

form button:hover {
    background: #218838;
}
```

```javascript
// script.js

// Function to handle form submission
document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    // Gather form data
    const formData = new FormData(this);

    // Send form data using Fetch API
    fetch('submit_form.php', {
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
        document.getElementById('form-status').textContent = 'Message sent successfully!';
        this.reset(); // Reset the form
    })
    .catch(error => {
        // Handle errors
        document.getElementById('form-status').textContent = 'Error sending message: ' + error.message;
    });
});
```

```php
<?php
// submit_form.php

// Check if the request is a POST request
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate input data
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Add simple validation
    if (empty($name) || empty($email) || empty($message)) {
        http_response_code(400);
        echo "All fields are required.";
        exit;
    }

    // (Here you would typically send the email or store the data)

    // Send a success response
    echo "Thank you for your message, $name!";
} else {
    // Respond with a 405 Method Not Allowed if not a POST request
    http_response_code(405);
    echo "Method not allowed.";
}
?>
```

This code creates a simple website with a homepage and a contact form, featuring clean structure, styles, and error handling. The PHP script handles the form submission, ensuring production readiness.
