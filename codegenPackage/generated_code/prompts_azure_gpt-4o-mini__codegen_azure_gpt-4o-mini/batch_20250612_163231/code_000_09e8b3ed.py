"""
Generated Code Metadata:
========================
Original URL: https://phantomslens.com
Prompt: Generate a code snippet for a portfolio website that showcases a freelance artist's work in music and horror, similar to Dulce Mendes' PhantomsLens.
Generated: DETERMINISTIC_09e8b3edd910b7a8
Batch ID: 20250612_163231
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
    <title>Freelance Artist Portfolio</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Welcome to My Portfolio</h1>
        <nav>
            <ul>
                <li><a href="#music">Music</a></li>
                <li><a href="#horror">Horror Art</a></li>
                <li><a href="#about">About Me</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="music">
            <h2>Music</h2>
            <div class="gallery">
                <!-- Music pieces showcased here -->
                <figure>
                    <img src="music1.jpg" alt="Music Piece 1">
                    <figcaption>Title: Melancholy Tune</figcaption>
                </figure>
                <figure>
                    <img src="music2.jpg" alt="Music Piece 2">
                    <figcaption>Title: Nightfall Symphony</figcaption>
                </figure>
                <!-- Add more music pieces as needed -->
            </div>
        </section>

        <section id="horror">
            <h2>Horror Art</h2>
            <div class="gallery">
                <!-- Horror artworks showcased here -->
                <figure>
                    <img src="horror1.jpg" alt="Horror Art 1">
                    <figcaption>Title: Shadows in the Dark</figcaption>
                </figure>
                <figure>
                    <img src="horror2.jpg" alt="Horror Art 2">
                    <figcaption>Title: The Haunting</figcaption>
                </figure>
                <!-- Add more horror artworks as needed -->
            </div>
        </section>

        <section id="about">
            <h2>About Me</h2>
            <p>
                I am a freelance artist specializing in music compositions and horror-themed artwork. 
                My passion lies in creating immersive experiences through sound and visuals.
            </p>
        </section>

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
        <p>&copy; 2023 Freelance Artist. All rights reserved.</p>
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
    background-color: #f4f4f4;
    color: #333;
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

/* Main section styles */
main {
    padding: 20px;
}

/* Gallery styles */
.gallery {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
}

figure {
    background: #fff;
    border: 1px solid #ddd;
    border-radius: 5px;
    overflow: hidden;
    width: calc(50% - 20px);
}

figure img {
    width: 100%;
    height: auto;
}

/* Form styles */
form {
    display: flex;
    flex-direction: column;
    gap: 10px;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 1rem 0;
    background: #333;
    color: #fff;
    position: relative;
    bottom: 0;
    width: 100%;
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
    if ($name && filter_var($email, FILTER_VALIDATE_EMAIL) && $message) {
        // Here you would typically send the email or save to a database
        // For demonstration, we'll just return a success response
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
