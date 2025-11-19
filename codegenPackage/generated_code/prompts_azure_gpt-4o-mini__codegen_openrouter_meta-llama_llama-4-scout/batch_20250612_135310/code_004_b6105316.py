"""
Generated Code Metadata:
========================
Original URL: https://wingerrandr.ca
Prompt: Design a simple HTML page that showcases handcrafted wood accents, including a gallery and contact form for inquiries about custom projects.
Generated: DETERMINISTIC_b6105316c170a5c9
Batch ID: 20250612_135310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Handcrafted Wood Accents</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#gallery">Gallery</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="hero">
            <h1>Handcrafted Wood Accents</h1>
            <p>Unique, handcrafted wood pieces for your home or office.</p>
        </section>
        <section id="gallery">
            <h2>Gallery</h2>
            <div class="gallery-container">
                <img src="image1.jpg" alt="Wood Accent 1">
                <img src="image2.jpg" alt="Wood Accent 2">
                <img src="image3.jpg" alt="Wood Accent 3">
                <!-- Add more images as needed -->
            </div>
        </section>
        <section id="contact">
            <h2>Get in Touch</h2>
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
    <footer>
        <p>&copy; 2023 Handcrafted Wood Accents</p>
    </footer>
    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
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

h1, h2 {
    color: #333;
    margin-bottom: 10px;
}

.gallery-container {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.gallery-container img {
    width: 200px;
    height: 150px;
    margin: 10px;
    border-radius: 10px;
}

#contact-form {
    flex-direction: column;
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
    background-color: #333;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 10px;
    cursor: pointer;
}

button[type="submit"]:hover {
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

**script.js**
```javascript
// Get the contact form element
const contactForm = document.getElementById('contact-form');

// Add event listener to the contact form
contactForm.addEventListener('submit', (e) => {
    e.preventDefault();

    // Get the form data
    const formData = new FormData(contactForm);

    // Send the form data to the server using fetch API
    fetch('/contact', {
        method: 'POST',
        body: formData,
    })
    .then((response) => response.json())
    .then((data) => {
        console.log(data);
        // Display a success message to the user
        alert('Message sent successfully!');
        // Clear the form fields
        contactForm.reset();
    })
    .catch((error) => {
        console.error(error);
        // Display an error message to the user
        alert('Error sending message. Please try again.');
    });
});
```

**server.js (using Node.js and Express.js)**
```javascript
const express = require('express');
const app = express();
const port = 3000;

// Middleware to parse JSON requests
app.use(express.json());
app.use(express.urlencoded({ extended: true }));

// Serve static files from the public directory
app.use(express.static('public'));

// Contact form endpoint
app.post('/contact', (req, res) => {
    const { name, email, message } = req.body;

    // Validate the form data
    if (!name || !email || !message) {
        res.status(400).json({ error: 'Please fill out all fields.' });
        return;
    }

    // Send the form data to your email or database (e.g., using nodemailer)
    console.log(req.body);

    res.json({ message: 'Message sent successfully!' });
});

// Start the server
app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```
