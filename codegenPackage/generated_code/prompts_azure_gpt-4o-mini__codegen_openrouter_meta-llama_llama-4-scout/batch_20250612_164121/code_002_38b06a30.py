"""
Generated Code Metadata:
========================
Original URL: https://aibanshee.com
Prompt: Create an HTML structure for a simple contact page that includes a form and follows the design principles of simplicity and clarity highlighted on the IMST Telehealth site.
Generated: DETERMINISTIC_38b06a3057459409
Batch ID: 20250612_164121
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
    <title>Contact Us</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <!-- Optional navigation links can go here -->
        </nav>
    </header>
    <main>
        <section class="contact-hero">
            <h1>Get in Touch</h1>
            <p>We're here to help. Contact us with any questions or concerns.</p>
        </section>
        <section class="contact-form">
            <form id="contact-form" action="/submit" method="post">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>

                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>

                <label for="message">Message:</label>
                <textarea id="message" name="message" required></textarea>

                <button type="submit">Send Message</button>
            </form>
        </section>
        <section class="contact-info">
            <h2>Contact Information</h2>
            <ul>
                <li><strong>Phone:</strong> <a href="tel:123-456-7890">123-456-7890</a></li>
                <li><strong>Email:</strong> <a href="mailto:info@example.com">info@example.com</a></li>
                <li><strong>Address:</strong> 123 Main St, Anytown, USA 12345</li>
            </ul>
        </section>
    </main>
    <footer>
        <!-- Optional footer content can go here -->
    </footer>

    <script src="script.js"></script>
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

header, footer {
    background-color: #f0f0f0;
    padding: 1em;
    text-align: center;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

.contact-hero {
    background-image: linear-gradient(to bottom, #f7f7f7, #fff);
    padding: 2em;
    text-align: center;
    margin-bottom: 2em;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

.contact-form {
    background-color: #f9f9f9;
    padding: 2em;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
    margin-bottom: 2em;
}

label {
    display: block;
    margin-bottom: 0.5em;
}

input, textarea {
    width: 100%;
    padding: 0.5em;
    margin-bottom: 1em;
    border: 1px solid #ccc;
}

button[type="submit"] {
    background-color: #4CAF50;
    color: #fff;
    padding: 0.5em 1em;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button[type="submit"]:hover {
    background-color: #3e8e41;
}

.contact-info {
    background-color: #f9f9f9;
    padding: 2em;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

li {
    margin-bottom: 0.5em;
}

a {
    text-decoration: none;
    color: #337ab7;
}

a:hover {
    color: #23527c;
}
```

```javascript
// script.js

const form = document.getElementById('contact-form');

form.addEventListener('submit', (e) => {
    e.preventDefault();
    const formData = new FormData(form);
    fetch('/submit', {
        method: 'POST',
        body: formData,
    })
    .then((response) => response.json())
    .then((data) => console.log(data))
    .catch((error) => console.error(error));
});
```
