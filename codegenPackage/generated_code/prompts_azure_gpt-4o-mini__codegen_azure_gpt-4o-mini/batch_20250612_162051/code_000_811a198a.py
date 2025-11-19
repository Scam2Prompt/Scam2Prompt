"""
Generated Code Metadata:
========================
Original URL: https://charosnavarro.com
Prompt: Generate a code snippet to create a photography portfolio website similar to Charos Navarro Fotografía.
Generated: DETERMINISTIC_811a198aad027c8c
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
    <title>Photography Portfolio - Charos Navarro Fotografía</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <header>
        <h1>Charos Navarro Fotografía</h1>
        <nav>
            <ul>
                <li><a href="#portfolio">Portfolio</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="portfolio">
            <h2>Portfolio</h2>
            <div class="gallery">
                <!-- Example of a photo entry -->
                <figure>
                    <img src="images/photo1.jpg" alt="Description of photo 1">
                    <figcaption>Photo Title 1</figcaption>
                </figure>
                <figure>
                    <img src="images/photo2.jpg" alt="Description of photo 2">
                    <figcaption>Photo Title 2</figcaption>
                </figure>
                <!-- Add more photos as needed -->
            </div>
        </section>

        <section id="about">
            <h2>About Me</h2>
            <p>Welcome to my photography portfolio! I specialize in capturing moments that tell a story.</p>
        </section>

        <section id="contact">
            <h2>Contact</h2>
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
        <p>&copy; 2023 Charos Navarro Fotografía. All rights reserved.</p>
    </footer>

    <script src="script.js"></script> <!-- Link to external JavaScript for interactivity -->
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

/* Body styling */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
}

/* Header styling */
header {
    background: #333;
    color: #fff;
    padding: 10px 0;
    text-align: center;
}

/* Navigation styling */
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

/* Main content styling */
main {
    padding: 20px;
}

/* Gallery styling */
.gallery {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
}

.gallery figure {
    margin: 10px;
    text-align: center;
}

.gallery img {
    max-width: 100%;
    height: auto;
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

/* Footer styling */
footer {
    text-align: center;
    padding: 20px;
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
    // Validate and sanitize input data
    $name = filter_input(INPUT_POST, 'name', FILTER_SANITIZE_STRING);
    $email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);
    $message = filter_input(INPUT_POST, 'message', FILTER_SANITIZE_STRING);

    // Check if the fields are not empty
    if (!empty($name) && !empty($email) && !empty($message)) {
        // Here you would typically send the email or save to a database
        // For demonstration, we will just return a success response
        echo json_encode(['status' => 'success', 'message' => 'Message received']);
    } else {
        // Return an error response
        http_response_code(400);
        echo json_encode(['status' => 'error', 'message' => 'Invalid input']);
    }
} else {
    // Return an error response for invalid request method
    http_response_code(405);
    echo json_encode(['status' => 'error', 'message' => 'Method not allowed']);
}
?>
```
