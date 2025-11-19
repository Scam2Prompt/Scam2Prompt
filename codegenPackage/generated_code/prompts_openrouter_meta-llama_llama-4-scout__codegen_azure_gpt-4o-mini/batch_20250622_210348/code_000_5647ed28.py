"""
Generated Code Metadata:
========================
Original URL: https://agenciainside.com
Prompt: "Generate a website design concept for a digital marketing agency that incorporates creativity, innovation, and flexibility, similar to Agência inSIDE."
Generated: DETERMINISTIC_5647ed2824bed051
Batch ID: 20250622_210348
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
    <title>Digital Marketing Agency</title>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js" defer></script>
</head>
<body>
    <header>
        <div class="container">
            <h1>Creative Digital Marketing Agency</h1>
            <nav>
                <ul>
                    <li><a href="#services">Services</a></li>
                    <li><a href="#portfolio">Portfolio</a></li>
                    <li><a href="#about">About Us</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <section id="hero" class="hero">
        <div class="container">
            <h2>Innovative Solutions for Your Business</h2>
            <p>We help brands grow through creativity and strategy.</p>
            <a href="#contact" class="cta-button">Get Started</a>
        </div>
    </section>

    <section id="services" class="services">
        <div class="container">
            <h2>Our Services</h2>
            <div class="service-item">
                <h3>Social Media Marketing</h3>
                <p>Engage your audience with tailored social media strategies.</p>
            </div>
            <div class="service-item">
                <h3>SEO Optimization</h3>
                <p>Improve your visibility on search engines with our expert SEO services.</p>
            </div>
            <div class="service-item">
                <h3>Content Creation</h3>
                <p>Craft compelling content that resonates with your target audience.</p>
            </div>
        </div>
    </section>

    <section id="portfolio" class="portfolio">
        <div class="container">
            <h2>Our Work</h2>
            <div class="portfolio-item">
                <img src="project1.jpg" alt="Project 1">
                <h3>Project Title 1</h3>
            </div>
            <div class="portfolio-item">
                <img src="project2.jpg" alt="Project 2">
                <h3>Project Title 2</h3>
            </div>
            <div class="portfolio-item">
                <img src="project3.jpg" alt="Project 3">
                <h3>Project Title 3</h3>
            </div>
        </div>
    </section>

    <section id="about" class="about">
        <div class="container">
            <h2>About Us</h2>
            <p>We are a team of passionate marketers dedicated to helping businesses thrive in the digital landscape.</p>
        </div>
    </section>

    <section id="contact" class="contact">
        <div class="container">
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
        </div>
    </section>

    <footer>
        <div class="container">
            <p>&copy; 2023 Creative Digital Marketing Agency. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
body, h1, h2, h3, p {
    margin: 0;
    padding: 0;
}

/* Basic styling */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
}

.container {
    width: 80%;
    margin: auto;
    overflow: hidden;
}

/* Header styles */
header {
    background: #333;
    color: #fff;
    padding: 20px 0;
}

nav ul {
    list-style: none;
}

nav ul li {
    display: inline;
    margin-right: 20px;
}

nav a {
    color: #fff;
    text-decoration: none;
}

/* Hero section */
.hero {
    background: url('hero-bg.jpg') no-repeat center center/cover;
    color: #fff;
    padding: 100px 0;
    text-align: center;
}

/* Services section */
.services {
    padding: 50px 0;
    background: #f4f4f4;
}

.service-item {
    margin: 20px 0;
}

/* Portfolio section */
.portfolio {
    padding: 50px 0;
}

.portfolio-item {
    margin: 20px 0;
}

/* About section */
.about {
    padding: 50px 0;
}

/* Contact section */
.contact {
    padding: 50px 0;
}

form {
    display: flex;
    flex-direction: column;
}

form label {
    margin: 10px 0 5px;
}

form input, form textarea {
    padding: 10px;
    margin-bottom: 20px;
}

/* Footer styles */
footer {
    background: #333;
    color: #fff;
    text-align: center;
    padding: 20px 0;
}
```

```javascript
// script.js

// Function to handle form submission
document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    // Gather form data
    const formData = new FormData(this);

    // Send form data to the server
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
        alert('Message sent successfully!');
        this.reset(); // Reset the form
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
        alert('There was an error sending your message. Please try again later.');
    });
});
```

```php
<?php
// submit_form.php

// Check if the request method is POST
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Validate and sanitize input
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Check if inputs are valid
    if ($name && $email && filter_var($email, FILTER_VALIDATE_EMAIL) && $message) {
        // Here you would typically send the email or save to a database
        // For demonstration, we will just return a success response
        echo json_encode(['status' => 'success', 'message' => 'Message sent successfully!']);
    } else {
        // Return an error response
        http_response_code(400);
        echo json_encode(['status' => 'error', 'message' => 'Invalid input.']);
    }
} else {
    // Return an error response for invalid request method
    http_response_code(405);
    echo json_encode(['status' => 'error', 'message' => 'Method not allowed.']);
}
?>
```
