"""
Generated Code Metadata:
========================
Original URL: https://orlandoplasmacenters.com
Prompt: Develop a basic HTML and CSS template for a plasma donation center website, incorporating features and sections similar to those found on the Orlando Plasma Centers website.
Generated: DETERMINISTIC_f76eeabb30d18769
Batch ID: 20250622_211932
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
    <title>Plasma Donation Center</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Welcome to Our Plasma Donation Center</h1>
        <nav>
            <ul>
                <li><a href="#about">About Us</a></li>
                <li><a href="#donate">How to Donate</a></li>
                <li><a href="#locations">Locations</a></li>
                <li><a href="#contact">Contact Us</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="about">
            <h2>About Us</h2>
            <p>We are dedicated to providing a safe and welcoming environment for plasma donation. Your contributions help save lives.</p>
        </section>

        <section id="donate">
            <h2>How to Donate</h2>
            <ol>
                <li>Check eligibility requirements.</li>
                <li>Schedule an appointment online.</li>
                <li>Visit our center for your donation.</li>
            </ol>
        </section>

        <section id="locations">
            <h2>Our Locations</h2>
            <p>Find a donation center near you:</p>
            <ul>
                <li>Location 1: 123 Plasma St, Orlando, FL</li>
                <li>Location 2: 456 Donation Ave, Orlando, FL</li>
                <li>Location 3: 789 Health Blvd, Orlando, FL</li>
            </ul>
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
    </main>

    <footer>
        <p>&copy; 2023 Plasma Donation Center. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
body, h1, h2, p, ul, ol {
    margin: 0;
    padding: 0;
}

/* Basic styling for the body */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
    color: #333;
}

/* Header styles */
header {
    background: #007bff;
    color: #fff;
    padding: 20px 0;
    text-align: center;
}

nav ul {
    list-style: none;
    padding: 0;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav ul li a {
    color: #fff;
    text-decoration: none;
}

/* Main section styles */
main {
    padding: 20px;
}

/* Section styles */
section {
    margin-bottom: 20px;
    background: #fff;
    padding: 15px;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

/* Form styles */
form {
    display: flex;
    flex-direction: column;
}

form label {
    margin-bottom: 5px;
}

form input, form textarea {
    margin-bottom: 15px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

form button {
    padding: 10px;
    background: #007bff;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

form button:hover {
    background: #0056b3;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 10px 0;
    background: #007bff;
    color: #fff;
    position: relative;
    bottom: 0;
    width: 100%;
}
```
