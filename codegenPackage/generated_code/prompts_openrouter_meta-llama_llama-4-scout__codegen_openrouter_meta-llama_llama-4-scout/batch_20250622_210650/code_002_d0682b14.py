"""
Generated Code Metadata:
========================
Original URL: https://sosmenuiserie.fr
Prompt: Generate a code snippet in JavaScript to create a simple webpage for a local business, similar to SOS Menuiserie's website, with sections for services and contact information.
Generated: DETERMINISTIC_d0682b14fcee6932
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// index.html and script.js will be generated

// index.html
const indexHtml = `
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SOS Menuiserie</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#services">Services</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="services">
            <h1>Our Services</h1>
            <ul id="services-list"></ul>
        </section>
        <section id="contact">
            <h1>Get in Touch</h1>
            <form id="contact-form">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name"><br><br>
                <label for="email">Email:</label>
                <input type="email" id="email" name="email"><br><br>
                <label for="message">Message:</label>
                <textarea id="message" name="message"></textarea><br><br>
                <input type="submit" value="Submit">
            </form>
        </section>
    </main>
    <script src="script.js"></script>
</body>
</html>
`;

// style.css
const styleCss = `
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

nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

nav li {
    display: inline-block;
    margin-right: 20px;
}

nav a {
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

#services-list {
    list-style: none;
    padding: 0;
    margin: 0;
}

#services-list li {
    margin-bottom: 10px;
}

#contact-form {
    display: flex;
    flex-direction: column;
    align-items: center;
}

label {
    margin-bottom: 10px;
}

input, textarea {
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
}

input[type="submit"] {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    cursor: pointer;
}

input[type="submit"]:hover {
    background-color: #444;
}
`;

// script.js
const scriptJs = `
class SosMenuiserie {
    constructor() {
        this.services = [
            "Menuiserie",
            "Charpente",
            "Agencement",
            "Rénovation",
        ];
        this.contactForm = document.getElementById('contact-form');
        this.servicesList = document.getElementById('services-list');

        this.init();
    }

    init() {
        this.renderServices();
        this.addEventListeners();
    }

    renderServices() {
        this.services.forEach((service) => {
            const li = document.createElement('li');
            li.textContent = service;
            this.servicesList.appendChild(li);
        });
    }

    addEventListeners() {
        this.contactForm.addEventListener('submit', (e) => this.handleSubmit(e));
    }

    handleSubmit(e) {
        e.preventDefault();
        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;
        const message = document.getElementById('message').value;

        // Basic validation
        if (!name || !email || !message) {
            alert('Please fill out all fields.');
            return;
        }

        // Send data to server or handle as needed
        console.log('Form submitted:', { name, email, message });

        // Reset form
        this.contactForm.reset();
    }
}

document.addEventListener('DOMContentLoaded', () => {
    new SosMenuiserie();
});
`;

// Create files
const fs = require('fs');

fs.writeFileSync('index.html', indexHtml);
fs.writeFileSync('style.css', styleCss);
fs.writeFileSync('script.js', scriptJs);

console.log('Files created successfully.');
```
