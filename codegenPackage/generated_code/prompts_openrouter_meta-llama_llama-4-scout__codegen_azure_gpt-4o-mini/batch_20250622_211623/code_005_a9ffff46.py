"""
Generated Code Metadata:
========================
Original URL: https://backontrackpsych.com
Prompt: Create a basic webpage template for a psychology clinic that provides information on services like psychology, neuropsychology, speech pathology, and occupational therapy.
Generated: DETERMINISTIC_a9ffff4602695f87
Batch ID: 20250622_211623
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
    <title>Psychology Clinic</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <header>
        <h1>Welcome to Our Psychology Clinic</h1>
        <nav>
            <ul>
                <li><a href="#services">Services</a></li>
                <li><a href="#about">About Us</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="services">
            <h2>Our Services</h2>
            <ul>
                <li>
                    <h3>Psychology</h3>
                    <p>We provide comprehensive psychological assessments and therapy for individuals and families.</p>
                </li>
                <li>
                    <h3>Neuropsychology</h3>
                    <p>Our neuropsychologists specialize in diagnosing and treating cognitive and behavioral issues.</p>
                </li>
                <li>
                    <h3>Speech Pathology</h3>
                    <p>We offer speech and language therapy for children and adults with communication disorders.</p>
                </li>
                <li>
                    <h3>Occupational Therapy</h3>
                    <p>Our occupational therapists help clients develop, recover, and improve the skills needed for daily living.</p>
                </li>
            </ul>
        </section>

        <section id="about">
            <h2>About Us</h2>
            <p>Our clinic is dedicated to providing high-quality psychological services to our community. Our team of experienced professionals is committed to helping individuals achieve their mental health goals.</p>
        </section>

        <section id="contact">
            <h2>Contact Us</h2>
            <p>If you have any questions or would like to schedule an appointment, please reach out to us:</p>
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
        <p>&copy; 2023 Psychology Clinic. All rights reserved.</p>
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
    color: #333;
}

/* Header styling */
header {
    background: #007BFF;
    color: #fff;
    padding: 20px 0;
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

/* Section styling */
section {
    margin-bottom: 20px;
    background: #fff;
    padding: 15px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

/* Footer styling */
footer {
    text-align: center;
    padding: 10px 0;
    background: #007BFF;
    color: #fff;
    position: relative;
    bottom: 0;
    width: 100%;
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
    border: 1px solid #ccc;
    border-radius: 5px;
}

form button {
    padding: 10px;
    background: #007BFF;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

form button:hover {
    background: #0056b3;
}
```

```javascript
// script.js

// This script can be used for form validation or other interactivity in the future

document.getElementById('contact-form').addEventListener('submit', function(event) {
    // Prevent default form submission
    event.preventDefault();

    // Simple client-side validation (can be expanded)
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;

    if (name && email && message) {
        // Here you can add AJAX call to submit the form without reloading
        alert('Form submitted successfully!');
        // Reset the form
        this.reset();
    } else {
        alert('Please fill in all fields.');
    }
});
```
