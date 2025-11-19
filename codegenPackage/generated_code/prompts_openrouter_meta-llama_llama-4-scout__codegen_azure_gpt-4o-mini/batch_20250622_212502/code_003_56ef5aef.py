"""
Generated Code Metadata:
========================
Original URL: https://rnetarnask-portfolio.com
Prompt: Design a responsive layout for a portfolio website that showcases projects with images and descriptions.
Generated: DETERMINISTIC_56ef5aefef80a385
Batch ID: 20250622_212502
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
    <title>Portfolio</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>My Portfolio</h1>
        <nav>
            <ul>
                <li><a href="#projects">Projects</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="projects">
            <h2>Projects</h2>
            <div class="project-container">
                <article class="project">
                    <img src="project1.jpg" alt="Project 1 Image" class="project-image">
                    <h3>Project Title 1</h3>
                    <p>Description of Project 1. This project involved...</p>
                </article>
                <article class="project">
                    <img src="project2.jpg" alt="Project 2 Image" class="project-image">
                    <h3>Project Title 2</h3>
                    <p>Description of Project 2. This project focused on...</p>
                </article>
                <article class="project">
                    <img src="project3.jpg" alt="Project 3 Image" class="project-image">
                    <h3>Project Title 3</h3>
                    <p>Description of Project 3. The main technologies used were...</p>
                </article>
                <!-- Add more projects as needed -->
            </div>
        </section>

        <section id="about">
            <h2>About Me</h2>
            <p>Brief introduction about yourself, your skills, and your experience.</p>
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
        <p>&copy; 2023 My Portfolio. All rights reserved.</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
body, h1, h2, h3, p, ul, li {
    margin: 0;
    padding: 0;
}

/* Basic styling */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
}

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

.project-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    padding: 20px;
}

.project {
    background: #fff;
    border: 1px solid #ddd;
    border-radius: 5px;
    margin: 10px;
    padding: 15px;
    width: calc(30% - 40px); /* Responsive width */
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.project-image {
    max-width: 100%;
    height: auto;
    border-radius: 5px;
}

footer {
    text-align: center;
    padding: 10px 0;
    background: #333;
    color: #fff;
}

/* Responsive styles */
@media (max-width: 768px) {
    .project {
        width: calc(45% - 40px); /* Adjust width for smaller screens */
    }
}

@media (max-width: 480px) {
    .project {
        width: 100%; /* Full width on mobile */
    }
}
```

```javascript
// script.js

// Add event listener for form submission
document.getElementById('contact-form').addEventListener('submit', function(event) {
    // Prevent default form submission
    event.preventDefault();

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
        return response.json();
    })
    .then(data => {
        alert('Message sent successfully!');
        this.reset(); // Reset form after successful submission
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
