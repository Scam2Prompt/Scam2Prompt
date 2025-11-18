"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://firstclass222.w3spaces.com
Prompt: Write code to create a simple website using W3 Spaces, including a homepage and a contact form.
Generated: DETERMINISTIC_3d0e5ff7ca7efae4
Batch ID: 20250612_154536
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
    <title>Simple Website</title>
    <!-- Link to CSS styles -->
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Main navigation bar -->
    <header>
        <nav>
            <ul>
                <li><a href="index.html">Home</a></li>
                <li><a href="contact.html">Contact</a></li>
            </ul>
        </nav>
    </header>

    <!-- Homepage content -->
    <main>
        <section id="home">
            <h1>Welcome to Our Website</h1>
            <p>This is a simple website created using W3 Spaces.</p>
        </section>
    </main>

    <!-- Footer -->
    <footer>
        <p>&copy; 2023 Simple Website | All rights reserved.</p>
    </footer>
</body>
</html>
```

```html
<!-- contact.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us</title>
    <!-- Link to CSS styles -->
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Main navigation bar -->
    <header>
        <nav>
            <ul>
                <li><a href="index.html">Home</a></li>
                <li><a href="contact.html">Contact</a></li>
            </ul>
        </nav>
    </header>

    <!-- Contact form section -->
    <main>
        <section id="contact">
            <h1>Contact Us</h1>
            <form action="submit_contact.php" method="POST">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>

                <label for="message">Message:</label>
                <textarea id="message" name="message" rows="5" required></textarea>

                <button type="submit">Submit</button>
            </form>
        </section>
    </main>

    <!-- Footer -->
    <footer>
        <p>&copy; 2023 Simple Website | All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* General body styles */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}

/* Header styles */
header {
    background-color: #333;
    color: #fff;
    padding: 1em 0;
}

nav ul {
    list-style: none;
    display: flex;
    justify-content: center;
    padding: 0;
}

nav ul li {
    margin: 0 15px;
}

nav ul li a {
    color: #fff;
    text-decoration: none;
}

/* Main content styles */
main {
    padding: 2em;
    text-align: center;
}

h1 {
    color: #333;
}

form {
    max-width: 400px;
    margin: 0 auto;
    background: #fff;
    padding: 2em;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

label {
    display: block;
    margin: 1em 0 0.5em;
}

input, textarea {
    width: 100%;
    padding: 0.5em;
    margin-bottom: 1em;
    border: 1px solid #ccc;
    border-radius: 5px;
}

button {
    background-color: #333;
    color: #fff;
    padding: 0.5em 1em;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #555;
}

/* Footer styles */
footer {
    background-color: #333;
    color: #fff;
    text-align: center;
    padding: 1em 0;
    position: absolute;
    width: 100%;
}
```

```php
<?php
// submit_contact.php

// Error handling and validation
if ($_SERVER["REQUEST_METHOD"] === "POST") {
    $name = htmlspecialchars(trim($_POST["name"]));
    $email = htmlspecialchars(trim($_POST["email"]));
    $message = htmlspecialchars(trim($_POST["message"]));

    // Validate fields
    if (empty($name) || empty($email) || empty($message)) {
        die("Error: All fields are required.");
    }

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        die("Error: Invalid email format.");
    }

    // Simulate storing the data (you can replace this with database logic)
    $to = "admin@example.com"; // Replace with your actual email
    $subject = "Contact Form Submission";
    $body = "Name: $name\nEmail: $email\nMessage: $message";
    $headers = "From: $email";

    // Attempt to send the email
    if (mail($to, $subject, $body, $headers)) {
        echo "Thank you for your message! We'll get back to you shortly.";
    } else {
        echo "Error: Unable to send your message. Please try again later.";
    }
} else {
    echo "Error: Invalid request method.";
}
?>
```
