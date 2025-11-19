"""
Generated Code Metadata:
========================
Original URL: https://alshehhi.net
Prompt: Create a web application template for showcasing completed projects, similar to the "اعمالنا" (Our Work) section on Alshehhi.Net.
Generated: DETERMINISTIC_208c12b3aef7c545
Batch ID: 20250612_151553
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
    <title>Our Work - Project Showcase</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <header>
        <h1>Our Completed Projects</h1>
        <nav>
            <ul>
                <li><a href="#projects">Projects</a></li>
                <li><a href="#about">About Us</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main id="projects">
        <section>
            <h2>Featured Projects</h2>
            <div class="project-container">
                <!-- Project Item Template -->
                <article class="project-item">
                    <img src="project1.jpg" alt="Project 1 Image" class="project-image">
                    <h3>Project Title 1</h3>
                    <p>Short description of Project 1. This project involved...</p>
                    <a href="project1-details.html" class="project-link">View Details</a>
                </article>
                <article class="project-item">
                    <img src="project2.jpg" alt="Project 2 Image" class="project-image">
                    <h3>Project Title 2</h3>
                    <p>Short description of Project 2. This project focused on...</p>
                    <a href="project2-details.html" class="project-link">View Details</a>
                </article>
                <!-- Add more project items as needed -->
            </div>
        </section>
    </main>

    <footer>
        <section id="about">
            <h2>About Us</h2>
            <p>We are a team of dedicated professionals committed to delivering high-quality projects...</p>
        </section>
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
        </section>
        <p>&copy; 2023 Our Company. All rights reserved.</p>
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

/* Main content styling */
main {
    padding: 20px;
}

.project-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
}

.project-item {
    background: #fff;
    border: 1px solid #ddd;
    border-radius: 5px;
    margin: 10px;
    padding: 15px;
    width: 300px;
    text-align: center;
}

.project-image {
    max-width: 100%;
    height: auto;
}

/* Footer styling */
footer {
    background: #333;
    color: #fff;
    padding: 20px;
    text-align: center;
}

/* Form styling */
form {
    display: flex;
    flex-direction: column;
    max-width: 400px;
    margin: 0 auto;
}

form label {
    margin: 10px 0 5px;
}

form input, form textarea {
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
}

form button {
    padding: 10px;
    background: #333;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

form button:hover {
    background: #555;
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
    // If the request method is not POST, return a 405 Method Not Allowed response
    http_response_code(405);
    echo json_encode(['error' => 'Method not allowed.']);
}
?>
```
