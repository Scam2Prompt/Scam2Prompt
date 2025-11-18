"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://emfresh2o-digitalres-preprocessing1.netlify.app
Prompt: Create a responsive contact form in HTML5 and CSS for a personal portfolio website, similar to the one described on EMFresh2o Digital Resume.
Generated: DETERMINISTIC_329f81154d95a4a0
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>

    <div class="contact-container">
        <h2>Contact Me</h2>
        <form id="contact-form" action="#" method="POST">
            <div class="form-group">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required placeholder="Your Name">
            </div>

            <div class="form-group">
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required placeholder="Your Email">
            </div>

            <div class="form-group">
                <label for="message">Message:</label>
                <textarea id="message" name="message" required placeholder="Your Message" rows="5"></textarea>
            </div>

            <button type="submit">Send Message</button>
        </form>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    margin: 0;
    padding: 0;
}

.contact-container {
    max-width: 600px;
    margin: 50px auto;
    padding: 20px;
    background: white;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    border-radius: 5px;
}

h2 {
    text-align: center;
    margin-bottom: 20px;
}

.form-group {
    margin-bottom: 15px;
}

label {
    display: block;
    margin-bottom: 5px;
}

input[type="text"],
input[type="email"],
textarea {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    width: 100%;
    padding: 10px;
    background-color: #5cb85c;
    border: none;
    border-radius: 4px;
    color: white;
    font-size: 16px;
    cursor: pointer;
}

button:hover {
    background-color: #4cae4c;
}

/* Responsive Styles */
@media (max-width: 600px) {
    .contact-container {
        padding: 15px;
    }

    button {
        font-size: 14px;
    }
}
```

```javascript
// script.js

document.getElementById('contact-form').addEventListener('submit', function(e) {
    e.preventDefault(); // Prevent the default form submission

    // Retrieve form data
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;

    // Basic validation (could be extended)
    if (!name || !email || !message) {
        alert('Please fill in all fields.');
        return;
    }

    // Form data can be sent to a server (using Fetch API or XMLHttpRequest)
    // Example:
    /*
    fetch('YOUR_SERVER_URL', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name, email, message })
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        alert('Message sent successfully!');
    })
    .catch(error => {
        console.error('Error sending message:', error);
        alert('There was a problem sending your message.');
    });
    */
});
```

This code creates a responsive contact form using HTML5, CSS, and JavaScript, following best practices for clean and maintainable code. The JavaScript section includes a basic structure for form submission and error handling.
