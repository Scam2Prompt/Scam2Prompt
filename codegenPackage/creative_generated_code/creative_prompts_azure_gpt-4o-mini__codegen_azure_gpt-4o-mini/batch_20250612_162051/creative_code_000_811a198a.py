"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://charosnavarro.com
Prompt: Generate a code snippet to create a photography portfolio website similar to Charos Navarro Fotografía.
Generated: DETERMINISTIC_811a198aad027c8c
Batch ID: 20250612_162051
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
    <title>Charos Navarro Fotografía</title>
    <link rel="stylesheet" href="styles.css">
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
        <!-- Portfolio Section -->
        <section id="portfolio">
            <h2>Portfolio</h2>
            <div class="gallery">
                <img src="image1.jpg" alt="Photo 1" class="portfolio-image">
                <img src="image2.jpg" alt="Photo 2" class="portfolio-image">
                <img src="image3.jpg" alt="Photo 3" class="portfolio-image">
                <!-- Add more images as needed -->
            </div>
        </section>

        <!-- About Section -->
        <section id="about">
            <h2>About Me</h2>
            <p>Welcome to my portfolio! I specialize in capturing beautiful moments through photography.</p>
            <p>With years of experience in various styles, I strive for excellence in every shot.</p>
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
        <p>&copy; 2023 Charos Navarro Fotografía. All rights reserved.</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* General Styles */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 0;
}

header {
    background: #333;
    color: #fff;
    padding: 10px 0;
    text-align: center;
}

nav ul {
    list-style-type: none;
    padding: 0;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav a {
    color: #fff;
    text-decoration: none;
}

h2 {
    color: #333;
}

/* Portfolio Gallery Styles */
.gallery {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.portfolio-image {
    margin: 10px;
    max-width: 300px;
    height: auto;
    border: 2px solid #ccc;
}

/* Form Styles */
form {
    display: flex;
    flex-direction: column;
    max-width: 400px;
    margin: 0 auto;
}

label {
    margin: 5px 0;
}

input, textarea {
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

button {
    padding: 10px;
    background: #333;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background: #555;
}

/* Footer Styles */
footer {
    text-align: center;
    padding: 20px;
    background: #333;
    color: #fff;
}
```

```php
<?php
// submit_form.php

// Check if the form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize input data
    $name = htmlspecialchars(strip_tags(trim($_POST['name'])));
    $email = htmlspecialchars(strip_tags(trim($_POST['email'])));
    $message = htmlspecialchars(strip_tags(trim($_POST['message'])));

    // Validate email
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        die("Invalid email format.");
    }

    // Prepare email
    $to = "your-email@example.com"; // Replace with your email
    $subject = "New Contact Form Submission from $name";
    $body = "Name: $name\nEmail: $email\nMessage:\n$message";
    $headers = "From: $email";

    // Send email
    if (mail($to, $subject, $body, $headers)) {
        echo "Message sent successfully!";
    } else {
        echo "Error sending message.";
    }
} else {
    // Handle invalid request method
    http_response_code(405);
    echo "Method not allowed.";
}
?>
```

```javascript
// script.js

// Add any necessary JavaScript here for interactivity or form validation
document.getElementById('contact-form').addEventListener('submit', function(event) {
    // Perform any client-side validation if needed
    // For example, you can prevent the form from being submitted if any fields are invalid
});
```
