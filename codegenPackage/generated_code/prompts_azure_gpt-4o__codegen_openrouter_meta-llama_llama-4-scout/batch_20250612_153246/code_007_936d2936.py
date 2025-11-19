"""
Generated Code Metadata:
========================
Original URL: https://taniphones.com
Prompt: Develop a responsive design for an e-commerce website with store locations and contact details, inspired by the "Adresa" section on TaniPhone.com.
Generated: DETERMINISTIC_936d2936d54723a8
Batch ID: 20250612_153246
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
    <title>E-commerce Website</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">About</a></li>
                <li><a href="#">Contact</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section class="adresa">
            <h2>Store Locations</h2>
            <div class="store-locations">
                <div class="store-location">
                    <h3>New York</h3>
                    <p>123 Main St, New York, NY 10001</p>
                    <p>Phone: +1 123 456 7890</p>
                    <p>Email: <a href="mailto:ny@taniPhone.com">ny@taniPhone.com</a></p>
                </div>
                <div class="store-location">
                    <h3>Los Angeles</h3>
                    <p>456 Broadway, Los Angeles, CA 90013</p>
                    <p>Phone: +1 987 654 3210</p>
                    <p>Email: <a href="mailto:la@taniPhone.com">la@taniPhone.com</a></p>
                </div>
                <div class="store-location">
                    <h3>Chicago</h3>
                    <p>789 Michigan Ave, Chicago, IL 60601</p>
                    <p>Phone: +1 555 123 4567</p>
                    <p>Email: <a href="mailto:chicago@taniPhone.com">chicago@taniPhone.com</a></p>
                </div>
            </div>
            <h2>Contact Us</h2>
            <form id="contact-form">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                <label for="message">Message:</label>
                <textarea id="message" name="message" required></textarea>
                <button type="submit">Send</button>
            </form>
        </section>
    </main>
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

.adresa {
    max-width: 800px;
    margin: 40px auto;
    padding: 20px;
    background-color: #f9f9f9;
    border: 1px solid #ddd;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.store-locations {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
}

.store-location {
    margin: 20px;
    padding: 20px;
    background-color: #fff;
    border: 1px solid #ddd;
    width: calc(33.33% - 20px);
}

.store-location h3 {
    margin-top: 0;
}

#contact-form {
    margin-top: 40px;
}

label {
    display: block;
    margin-bottom: 10px;
}

input, textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
}

button[type="submit"] {
    background-color: #333;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button[type="submit"]:hover {
    background-color: #444;
}

@media only screen and (max-width: 768px) {
    .store-location {
        width: calc(50% - 20px);
    }
}

@media only screen and (max-width: 480px) {
    .store-location {
        width: 100%;
    }
}
```

```javascript
// script.js

const contactForm = document.getElementById('contact-form');

contactForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;

    // Send data to server or handle form submission
    console.log(`Name: ${name}, Email: ${email}, Message: ${message}`);

    // Reset form
    contactForm.reset();
});
```
