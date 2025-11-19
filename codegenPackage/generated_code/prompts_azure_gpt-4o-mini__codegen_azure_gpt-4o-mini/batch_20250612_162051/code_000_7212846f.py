"""
Generated Code Metadata:
========================
Original URL: https://jgendreau.fr
Prompt: Generate a code snippet to set up a basic website using LWS hosting services for beginners.
Generated: DETERMINISTIC_7212846fa622c4af
Batch ID: 20250612_162051
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
    <title>My Basic Website</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS file -->
</head>
<body>
    <header>
        <h1>Welcome to My Basic Website</h1>
        <nav>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="home">
            <h2>Home</h2>
            <p>This is a simple website hosted on LWS.</p>
        </section>

        <section id="about">
            <h2>About</h2>
            <p>This website is created for beginners to learn web development.</p>
        </section>

        <section id="contact">
            <h2>Contact</h2>
            <form id="contactForm" action="submit_form.php" method="POST">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                
                <label for="message">Message:</label>
                <textarea id="message" name="message" required></textarea>
                
                <button type="submit">Send Message</button>
            </form>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 My Basic Website. All rights reserved.</p>
    </footer>

    <script src="script.js"></script> <!-- Link to external JavaScript file -->
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
}

/* Header styles */
header {
    background: #35424a;
    color: #ffffff;
    padding: 20px 0;
    text-align: center;
}

/* Navigation styles */
nav ul {
    list-style: none;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav ul li a {
    color: #ffffff;
    text-decoration: none;
}

/* Main content styles */
main {
    padding: 20px;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 10px 0;
    background: #35424a;
    color: #ffffff;
    position: relative;
    bottom: 0;
    width: 100%;
}
```

```javascript
// script.js

// Function to handle form submission
document.getElementById('contactForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

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
        alert('Form submitted successfully: ' + data);
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });
});
```

```php
<?php
// submit_form.php

// Check if the request method is POST
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate and sanitize input data
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Check if the data is valid
    if ($name && $email && $message) {
        // Here you would typically send an email or save to a database
        // For demonstration, we will just return a success message
        echo "Thank you, $name! Your message has been received.";
    } else {
        // Return an error message if validation fails
        http_response_code(400);
        echo "Invalid input. Please fill out all fields correctly.";
    }
} else {
    // Return an error message for invalid request method
    http_response_code(405);
    echo "Method Not Allowed. Please use POST.";
}
?>
```
