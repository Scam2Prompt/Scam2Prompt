"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fantom.de
Prompt: Generate a code snippet for a custom web design solution that incorporates multimedia elements as described on the Fantom Internet Dienst website.
Generated: DETERMINISTIC_55c0e235d9488462
Batch ID: 20250612_164152
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
    <meta name="description" content="Custom Web Design Solution with Multimedia Elements">
    <title>Custom Web Design - Fantom Internet Dienst</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <header>
        <h1>Welcome to Fantom Internet Dienst</h1>
        <nav>
            <ul>
                <li><a href="#services">Services</a></li>
                <li><a href="#portfolio">Portfolio</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="services">
            <h2>Our Services</h2>
            <article>
                <h3>Web Design</h3>
                <p>We create custom websites tailored to your needs.</p>
                <video controls>
                    <source src="video/service-overview.mp4" type="video/mp4">
                    Your browser does not support HTML5 video.
                </video>
            </article>
            <article>
                <h3>SEO Optimization</h3>
                <p>Boost your online visibility with our SEO services.</p>
                <img src="images/seo-optimization.jpg" alt="SEO Optimization" loading="lazy">
            </article>
        </section>

        <section id="portfolio">
            <h2>Our Portfolio</h2>
            <div class="gallery">
                <figure>
                    <img src="images/project1.jpg" alt="Project 1" loading="lazy">
                    <figcaption>Project 1 Description</figcaption>
                </figure>
                <figure>
                    <img src="images/project2.jpg" alt="Project 2" loading="lazy">
                    <figcaption>Project 2 Description</figcaption>
                </figure>
            </div>
        </section>

        <section id="contact">
            <h2>Contact Us</h2>
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
        <p>&copy; 2023 Fantom Internet Dienst. All rights reserved.</p>
    </footer>

    <script src="scripts.js"></script> <!-- Link to external JavaScript for interactivity -->
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for styling */
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
    background: #333;
    color: #fff;
    padding: 10px 0;
}

nav ul {
    list-style: none;
    display: flex;
    justify-content: center;
}

nav ul li {
    margin: 0 15px;
}

nav a {
    color: #fff;
    text-decoration: none;
}

/* Main content styles */
main {
    padding: 20px;
}

/* Service and portfolio sections */
section {
    margin-bottom: 40px;
}

.gallery {
    display: flex;
    justify-content: space-around;
}

/* Form styles */
form {
    display: flex;
    flex-direction: column;
}

form label {
    margin-bottom: 5px;
}

form input, form textarea {
    margin-bottom: 15px;
    padding: 8px;
}

form button {
    padding: 10px;
    background-color: #333;
    color: #fff;
    border: none;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 10px 0;
    background: #333;
    color: #fff;
}
```

```javascript
// scripts.js

// Function to handle form submission
document.getElementById('contactForm').addEventListener('submit', function(event) {
    // Validate form inputs
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;

    if (!name || !email) {
        alert("Please fill in all required fields.");
        event.preventDefault(); // Prevent form submission if validation fails
    }
});

// Additional JavaScript code can go here
```

```php
<?php
// submit_form.php

// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Capture form data
    $name = htmlspecialchars($_POST['name']);
    $email = htmlspecialchars($_POST['email']);
    $message = htmlspecialchars($_POST['message']);

    // Validate email
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        die("Invalid email format");
    }

    // Here you can add code to send email or save to database
    // For demonstration, just echo the input
    echo "Name: $name<br>Email: $email<br>Message: $message";
} else {
    die("Invalid request method");
}
?>
```
