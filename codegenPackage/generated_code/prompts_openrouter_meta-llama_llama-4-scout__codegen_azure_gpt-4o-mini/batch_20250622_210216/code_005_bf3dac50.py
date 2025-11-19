"""
Generated Code Metadata:
========================
Original URL: https://perthrealestatephotography.com.au
Prompt: Write a code snippet to design a simple web gallery, similar to the one on the Perth Real Estate Photography website, to showcase a photographer's work and client testimonials.
Generated: DETERMINISTIC_bf3dac50e59072fa
Batch ID: 20250622_210216
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
    <title>Photography Gallery</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Photographer's Gallery</h1>
        <nav>
            <ul>
                <li><a href="#gallery">Gallery</a></li>
                <li><a href="#testimonials">Testimonials</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <!-- Gallery Section -->
        <section id="gallery">
            <h2>Gallery</h2>
            <div class="gallery-container">
                <img src="image1.jpg" alt="Description of image 1" class="gallery-item">
                <img src="image2.jpg" alt="Description of image 2" class="gallery-item">
                <img src="image3.jpg" alt="Description of image 3" class="gallery-item">
                <img src="image4.jpg" alt="Description of image 4" class="gallery-item">
                <!-- Add more images as needed -->
            </div>
        </section>

        <!-- Testimonials Section -->
        <section id="testimonials">
            <h2>Client Testimonials</h2>
            <div class="testimonial-container">
                <blockquote>
                    <p>"Amazing work! The photos captured our property beautifully."</p>
                    <cite>- Client Name</cite>
                </blockquote>
                <blockquote>
                    <p>"Professional and creative. Highly recommend!"</p>
                    <cite>- Client Name</cite>
                </blockquote>
                <!-- Add more testimonials as needed -->
            </div>
        </section>

        <!-- Contact Section -->
        <section id="contact">
            <h2>Contact Me</h2>
            <form id="contact-form" action="submit_form.php" method="POST">
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
        <p>&copy; 2023 Photographer's Name. All rights reserved.</p>
    </footer>

    <script src="script.js"></script>
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

nav a {
    color: #fff;
    text-decoration: none;
}

/* Gallery styles */
.gallery-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    margin: 20px 0;
}

.gallery-item {
    width: 300px;
    margin: 10px;
    border: 2px solid #ccc;
}

/* Testimonials styles */
.testimonial-container {
    margin: 20px 0;
}

blockquote {
    border-left: 4px solid #333;
    margin: 10px 0;
    padding-left: 10px;
}

/* Contact form styles */
form {
    display: flex;
    flex-direction: column;
    max-width: 400px;
    margin: 20px auto;
}

form label {
    margin-bottom: 5px;
}

form input, form textarea {
    margin-bottom: 15px;
    padding: 10px;
    border: 1px solid #ccc;
}

form button {
    padding: 10px;
    background: #333;
    color: #fff;
    border: none;
    cursor: pointer;
}

form button:hover {
    background: #555;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 1rem 0;
    background: #333;
    color: #fff;
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

    // Check for empty fields
    if (empty($name) || empty($email) || empty($message)) {
        http_response_code(400);
        echo json_encode(['error' => 'All fields are required.']);
        exit;
    }

    // Here you would typically send the email or save to a database
    // For demonstration, we will just return a success response
    http_response_code(200);
    echo json_encode(['success' => 'Message sent successfully!']);
} else {
    // If not a POST request, return a 405 Method Not Allowed
    http_response_code(405);
    echo json_encode(['error' => 'Method not allowed.']);
}
?>
```
