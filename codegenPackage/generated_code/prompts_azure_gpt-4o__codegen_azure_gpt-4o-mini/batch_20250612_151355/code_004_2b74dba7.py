"""
Generated Code Metadata:
========================
Original URL: https://metamaks.xyz
Prompt: Generate HTML and CSS code for a responsive contact form, including fields for name, email, phone number, and message, inspired by the contact section on Ayoft's website.
Generated: DETERMINISTIC_2b74dba734fc706d
Batch ID: 20250612_151355
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
    <title>Contact Form</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="contact-container">
        <h1>Contact Us</h1>
        <form id="contactForm" action="#" method="POST">
            <div class="form-group">
                <label for="name">Name</label>
                <input type="text" id="name" name="name" required placeholder="Your Name">
            </div>
            <div class="form-group">
                <label for="email">Email</label>
                <input type="email" id="email" name="email" required placeholder="Your Email">
            </div>
            <div class="form-group">
                <label for="phone">Phone Number</label>
                <input type="tel" id="phone" name="phone" required placeholder="Your Phone Number">
            </div>
            <div class="form-group">
                <label for="message">Message</label>
                <textarea id="message" name="message" required placeholder="Your Message"></textarea>
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

/* Basic reset for margins and paddings */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body styling */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    color: #333;
}

/* Container for the contact form */
.contact-container {
    max-width: 600px;
    margin: 50px auto;
    padding: 20px;
    background: white;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

/* Heading styling */
h1 {
    text-align: center;
    margin-bottom: 20px;
}

/* Form group styling */
.form-group {
    margin-bottom: 15px;
}

/* Label styling */
label {
    display: block;
    margin-bottom: 5px;
}

/* Input and textarea styling */
input[type="text"],
input[type="email"],
input[type="tel"],
textarea {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

/* Button styling */
button {
    width: 100%;
    padding: 10px;
    background-color: #5cb85c;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
}

/* Button hover effect */
button:hover {
    background-color: #4cae4c;
}

/* Responsive design */
@media (max-width: 600px) {
    .contact-container {
        padding: 15px;
    }
}
```

```javascript
// script.js

// Function to handle form submission
document.getElementById('contactForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    // Gather form data
    const formData = new FormData(this);

    // Example of handling form data (e.g., sending to a server)
    fetch('/submit', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        alert('Message sent successfully!');
        this.reset(); // Reset the form after successful submission
    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
        alert('There was an error sending your message. Please try again later.');
    });
});
```
