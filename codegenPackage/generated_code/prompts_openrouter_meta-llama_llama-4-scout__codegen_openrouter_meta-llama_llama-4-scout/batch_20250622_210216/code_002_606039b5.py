"""
Generated Code Metadata:
========================
Original URL: https://lestersplace.com
Prompt: Generate a code snippet to create a simple website for an assisted living facility, including pages for About Us, Services, and Contact Us, with a focus on compassion and empowerment.
Generated: DETERMINISTIC_606039b583e27bef
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Assisted Living Facility</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#about">About Us</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#contact">Contact Us</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="about">
            <h1>About Us</h1>
            <p>Welcome to our assisted living facility, where we provide compassionate care and support to our residents. Our mission is to empower individuals to live their best lives, with dignity and respect.</p>
            <p>Our team is dedicated to providing personalized care and services, tailored to meet the unique needs of each resident. We strive to create a warm and welcoming community, where everyone feels valued and supported.</p>
        </section>
        <section id="services">
            <h1>Services</h1>
            <ul>
                <li>Personalized care and support</li>
                <li>Medication management</li>
                <li>Nutritional meals and snacks</li>
                <li>Recreational activities and events</li>
                <li>Transportation services</li>
            </ul>
        </section>
        <section id="contact">
            <h1>Contact Us</h1>
            <p>Phone: 555-555-5555</p>
            <p>Email: <a href="mailto:info@assistedliving.com">info@assistedliving.com</a></p>
            <p>Address: 123 Main St, Anytown, USA 12345</p>
            <form id="contact-form">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name"><br><br>
                <label for="email">Email:</label>
                <input type="email" id="email" name="email"><br><br>
                <label for="message">Message:</label>
                <textarea id="message" name="message"></textarea><br><br>
                <input type="submit" value="Send">
            </form>
            <script>
                // Get the contact form element
                const contactForm = document.getElementById('contact-form');

                // Add event listener to handle form submission
                contactForm.addEventListener('submit', (e) => {
                    e.preventDefault();
                    try {
                        // Get the form data
                        const formData = new FormData(contactForm);

                        // Send the form data to the server
                        fetch('/contact', {
                            method: 'POST',
                            body: formData,
                        })
                        .then((response) => response.json())
                        .then((data) => console.log(data))
                        .catch((error) => console.error(error));
                    } catch (error) {
                        console.error(error);
                    }
                });
            </script>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Assisted Living Facility</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

header nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

header nav ul li {
    display: inline-block;
    margin-right: 20px;
}

header nav a {
    color: #fff;
    text-decoration: none;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

section {
    background-color: #f7f7f7;
    padding: 1em;
    margin-bottom: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
    margin-top: 0;
}

#contact-form {
    width: 50%;
    margin: 0 auto;
}

label {
    display: block;
    margin-bottom: 10px;
}

input[type="text"], input[type="email"] {
    width: 100%;
    height: 40px;
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ccc;
}

textarea {
    width: 100%;
    height: 100px;
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ccc;
}

input[type="submit"] {
    background-color: #333;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

input[type="submit"]:hover {
    background-color: #444;
}

footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}
```

```javascript
// server.js

const express = require('express');
const app = express();
const port = 3000;

app.use(express.static('public'));
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.post('/contact', (req, res) => {
    try {
        const { name, email, message } = req.body;
        console.log(`Received message from ${name} (${email}): ${message}`);
        res.json({ message: 'Message sent successfully!' });
    } catch (error) {
        console.error(error);
        res.status(500).json({ message: 'Error sending message' });
    }
});

app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```

```json
// package.json

{
    "name": "assisted-living-facility",
    "version": "1.0.0",
    "scripts": {
        "start": "node server.js"
    },
    "dependencies": {
        "express": "^4.18.2"
    }
}
```
