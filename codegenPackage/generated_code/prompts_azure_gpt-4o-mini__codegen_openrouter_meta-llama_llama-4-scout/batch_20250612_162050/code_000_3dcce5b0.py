"""
Generated Code Metadata:
========================
Original URL: https://xeluudong.com
Prompt: Generate a code snippet that creates a responsive layout for a kitchen design website, focusing on L-shaped kitchen cabinets.
Generated: DETERMINISTIC_3dcce5b07ee560e0
Batch ID: 20250612_162050
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
    <title>L-Shaped Kitchen Cabinets</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#kitchen-design">Kitchen Design</a></li>
                <li><a href="#cabinets">Cabinets</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="kitchen-design">
            <h1>L-Shaped Kitchen Design</h1>
            <p>Our L-shaped kitchen design services offer a perfect blend of style and functionality.</p>
            <img src="kitchen-design.jpg" alt="L-Shaped Kitchen Design">
        </section>
        <section id="cabinets">
            <h2>L-Shaped Kitchen Cabinets</h2>
            <div class="cabinet-container">
                <div class="cabinet">
                    <img src="cabinet1.jpg" alt="Cabinet 1">
                    <p>Modern style, durable construction, and ample storage space.</p>
                </div>
                <div class="cabinet">
                    <img src="cabinet2.jpg" alt="Cabinet 2">
                    <p>Customizable to fit your unique kitchen layout and style.</p>
                </div>
                <div class="cabinet">
                    <img src="cabinet3.jpg" alt="Cabinet 3">
                    <p>High-quality materials and expert installation for a seamless look.</p>
                </div>
            </div>
        </section>
        <section id="contact">
            <h2>Get in Touch</h2>
            <form>
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
    <footer>
        <p>&copy; 2023 L-Shaped Kitchen Cabinets. All rights reserved.</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

:root {
    --primary-color: #333;
    --secondary-color: #666;
    --background-color: #f9f9f9;
}

* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: var(--primary-color);
    background-color: var(--background-color);
}

header {
    background-color: var(--primary-color);
    color: #fff;
    padding: 1em;
    text-align: center;
}

header nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: space-between;
}

header nav ul li {
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
    background-color: #fff;
    padding: 2em;
    margin-bottom: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1, h2 {
    color: var(--primary-color);
    margin-bottom: 10px;
}

.cabinet-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.cabinet {
    margin: 20px;
    width: calc(33.33% - 20px);
    background-color: #fff;
    padding: 20px;
    border: 1px solid #ddd;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.cabinet img {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 10px;
}

footer {
    background-color: var(--primary-color);
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}

form {
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

button[type="submit"] {
    background-color: var(--primary-color);
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button[type="submit"]:hover {
    background-color: var(--secondary-color);
}

@media only screen and (max-width: 768px) {
    .cabinet {
        width: calc(50% - 20px);
    }
}

@media only screen and (max-width: 480px) {
    .cabinet {
        width: 100%;
    }
    main {
        padding: 1em;
    }
}
```

```javascript
// script.js

// Add event listener to form submission
document.querySelector('form').addEventListener('submit', (e) => {
    e.preventDefault();
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;

    // Basic form validation
    if (name && email && message) {
        console.log('Form submitted:', { name, email, message });
        // Add logic for sending form data to server or email
    } else {
        alert('Please fill out all fields.');
    }
});
```
