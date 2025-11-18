"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kroonation.com
Prompt: Write code to create a graphic design portfolio website that includes UI/UX design, branding, brochure, and logo design services, inspired by the offerings described on Kroo Nation's webpage.
Generated: DETERMINISTIC_bce9f067f24656bd
Batch ID: 20250612_152924
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
    <meta name="description" content="Graphic Design Portfolio showcasing UI/UX, Branding, Brochure, and Logo Design services.">
    <title>Graphic Design Portfolio</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>My Graphic Design Portfolio</h1>
        <nav>
            <ul>
                <li><a href="#uiux">UI/UX Design</a></li>
                <li><a href="#branding">Branding</a></li>
                <li><a href="#brochures">Brochure Design</a></li>
                <li><a href="#logos">Logo Design</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <!-- UI/UX Design Section -->
        <section id="uiux">
            <h2>UI/UX Design</h2>
            <p>Creating intuitive and engaging user experiences for web and mobile applications.</p>
            <div class="portfolio-item">
                <img src="uiux-example.jpg" alt="UI/UX Project Example">
                <p>Project Description for UI/UX project.</p>
            </div>
        </section>

        <!-- Branding Section -->
        <section id="branding">
            <h2>Branding</h2>
            <p>Developing unique brand identities that resonate with audiences.</p>
            <div class="portfolio-item">
                <img src="branding-example.jpg" alt="Branding Project Example">
                <p>Project Description for Branding project.</p>
            </div>
        </section>

        <!-- Brochure Design Section -->
        <section id="brochures">
            <h2>Brochure Design</h2>
            <p>Crafting informative and visually appealing brochures.</p>
            <div class="portfolio-item">
                <img src="brochure-example.jpg" alt="Brochure Design Example">
                <p>Project Description for Brochure design project.</p>
            </div>
        </section>

        <!-- Logo Design Section -->
        <section id="logos">
            <h2>Logo Design</h2>
            <p>Designing memorable and impactful logos.</p>
            <div class="portfolio-item">
                <img src="logo-example.jpg" alt="Logo Design Example">
                <p>Project Description for Logo design project.</p>
            </div>
        </section>
    </main>

    <!-- Contact Section -->
    <footer id="contact">
        <h2>Contact Me</h2>
        <form action="submit_form.php" method="POST" id="contactForm">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>
            <label for="message">Message:</label>
            <textarea id="message" name="message" required></textarea>
            <button type="submit">Send Message</button>
        </form>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Resetting default styles */
body, h1, h2, p, ul {
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
}

/* Header styles */
header {
    background: #333;
    color: #fff;
    padding: 1rem 0;
    text-align: center;
}

nav ul {
    list-style: none;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav ul li a {
    color: #fff;
    text-decoration: none;
}

/* Main content styles */
main {
    padding: 20px;
    max-width: 800px;
    margin: auto;
}

.portfolio-item {
    margin: 20px 0;
}

.portfolio-item img {
    max-width: 100%;
    height: auto;
}

/* Footer styles */
footer {
    background: #f4f4f4;
    padding: 10px;
    text-align: center;
}

form {
    max-width: 400px;
    margin: auto;
}

form label {
    display: block;
    margin: 10px 0 5px;
}

form input, form textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
}
```

```javascript
// script.js

// Contact form submission handling
document.getElementById('contactForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    // Validate form fields
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const message = document.getElementById('message').value.trim();

    if (!name || !email || !message) {
        alert("Please fill out all fields.");
        return;
    }

    // Create a FormData object to send via Fetch API
    const formData = new FormData(this);

    // Send data to the server using Fetch API
    fetch('submit_form.php', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        alert("Message sent successfully!");
        this.reset(); // Reset form fields
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
        alert("There was an error sending your message. Please try again later.");
    });
});
```

```php
<?php
// submit_form.php

// Check if the request is POST
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate and sanitize input
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Basic validation (could be expanded)
    if (!$name || !$email || !$message) {
        http_response_code(400);
        echo json_encode(["message" => "Invalid input"]);
        exit;
    }

    // Process the form data (e.g., save to database or send an email)
    // For demonstration, we just echo a success response
    http_response_code(200);
    echo json_encode(["message" => "Message received"]);
} else {
    // Handle invalid request method
    http_response_code(405);
    echo json_encode(["message" => "Method not allowed"]);
}
?>
```
