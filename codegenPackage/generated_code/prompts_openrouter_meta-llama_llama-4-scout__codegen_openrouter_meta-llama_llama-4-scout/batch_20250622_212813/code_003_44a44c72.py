"""
Generated Code Metadata:
========================
Original URL: https://redstarksten.github.io
Prompt: Create a simple contact page template in HTML/CSS, inspired by the contact section of the StarkX-Kernel project website.
Generated: DETERMINISTIC_44a44c72d95ab8ab
Batch ID: 20250622_212813
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
    <title>Contact Us</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <section class="contact-container">
        <h1>Contact Us</h1>
        <p>We're here to help. Get in touch with us.</p>
        <form id="contact-form">
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="message">Message:</label>
            <textarea id="message" name="message" required></textarea>

            <button type="submit">Send Message</button>
        </form>
        <div class="contact-info">
            <h2>Contact Information</h2>
            <ul>
                <li><strong>Email:</strong> <a href="mailto:example@example.com">example@example.com</a></li>
                <li><strong>Address:</strong> 123 Main St, Anytown, USA</li>
            </ul>
        </div>
    </section>

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

.contact-container {
    max-width: 800px;
    margin: 40px auto;
    padding: 20px;
    background-color: #f9f9f9;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.contact-container h1 {
    margin-top: 0;
}

#contact-form {
    display: flex;
    flex-direction: column;
    align-items: center;
}

#contact-form label {
    margin-bottom: 10px;
}

#contact-form input, #contact-form textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
}

#contact-form button[type="submit"] {
    background-color: #4CAF50;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

#contact-form button[type="submit"]:hover {
    background-color: #3e8e41;
}

.contact-info {
    margin-top: 20px;
}

.contact-info ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

.contact-info li {
    margin-bottom: 10px;
}

.contact-info li strong {
    font-weight: bold;
}
```

**script.js**
```javascript
const contactForm = document.getElementById('contact-form');

contactForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const formData = new FormData(contactForm);
    const name = formData.get('name');
    const email = formData.get('email');
    const message = formData.get('message');

    // Send data to server or email service
    // For demonstration purposes, we'll just log the data
    console.log('Name:', name);
    console.log('Email:', email);
    console.log('Message:', message);

    // Clear form fields
    contactForm.reset();
});
```
