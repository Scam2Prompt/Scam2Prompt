"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrium.legal
Prompt: Generate HTML and CSS code for a "Contact Us" page that aligns with the design and structure of the "Legal Arbitrium" website.
Generated: DETERMINISTIC_01981a593d57f908
Batch ID: 20250612_145706
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!-- contact.html -->
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Us - Legal Arbitrium</title>
    <link rel="stylesheet" href="styles.css">
</head>

<body>
    <header>
        <nav>
            <ul>
                <li><a href="index.html">Home</a></li>
                <li><a href="services.html">Services</a></li>
                <li><a href="about.html">About</a></li>
                <li><a href="contact.html" class="active">Contact Us</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section class="contact-section">
            <h1>Contact Us</h1>
            <p>If you have any questions or need further information, please fill out the form below.</p>
            <form id="contact-form" action="submit_form.php" method="POST">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>

                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>

                <label for="message">Message:</label>
                <textarea id="message" name="message" rows="4" required></textarea>

                <button type="submit">Send Message</button>
            </form>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Legal Arbitrium. All rights reserved.</p>
    </footer>
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
    background-color: #f5f5f5;
}

header {
    background: #003366; /* Dark Blue */
    color: #ffffff;
    padding: 15px 0;
}

nav ul {
    list-style: none;
    padding: 0;
    text-align: center;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav ul li a {
    color: #ffffff;
    text-decoration: none;
}

nav ul li a.active {
    text-decoration: underline;
}

.contact-section {
    max-width: 600px;
    margin: 50px auto;
    background: #ffffff; /* White background for the contact form */
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.contact-section h1 {
    text-align: center;
    color: #003366; /* Dark Blue */
}

.contact-section form {
    display: flex;
    flex-direction: column;
}

.contact-section label {
    margin: 10px 0 5px;
}

.contact-section input, 
.contact-section textarea {
    padding: 10px;
    border: 1px solid #cccccc;
    border-radius: 5px;
}

.contact-section button {
    margin-top: 15px;
    padding: 10px;
    border: none;
    border-radius: 5px;
    background: #003366; /* Dark Blue */
    color: #ffffff;
    cursor: pointer;
}

.contact-section button:hover {
    background: #00509e; /* Lighter Blue for hover effect */
}

footer {
    text-align: center;
    padding: 15px;
    background: #003366; /* Dark Blue */
    color: #ffffff;
    position: relative;
    bottom: 0;
    width: 100%;
}
```
