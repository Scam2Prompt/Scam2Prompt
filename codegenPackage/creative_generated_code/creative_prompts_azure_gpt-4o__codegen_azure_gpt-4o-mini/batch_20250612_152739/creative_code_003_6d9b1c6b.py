"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dionlineaja.id
Prompt: Provide code examples for integrating a contact form into a web design project using HTML5, CSS3, and JavaScript, similar to the "Get in Touch" section on dionlineaja.id.
Generated: DETERMINISTIC_6d9b1c6b47be0ea6
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact Form</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <section id="contact" class="contact-section">
        <h2>Get in Touch</h2>
        <form id="contactForm" class="contact-form" novalidate>
            <div class="form-group">
                <label for="name">Name <span class="required">*</span></label>
                <input type="text" id="name" name="name" required>
            </div>
            <div class="form-group">
                <label for="email">Email <span class="required">*</span></label>
                <input type="email" id="email" name="email" required>
            </div>
            <div class="form-group">
                <label for="message">Message <span class="required">*</span></label>
                <textarea id="message" name="message" required></textarea>
            </div>
            <button type="submit">Send Message</button>
            <div id="responseMessage" class="response-message"></div>
        </form>
    </section>
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
    background-color: #f8f9fa;
}

.contact-section {
    max-width: 600px;
    margin: 50px auto;
    padding: 20px;
    background-color: #fff;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

h2 {
    text-align: center;
}

.form-group {
    margin-bottom: 15px;
}

label {
    display: block;
    margin-bottom: 5px;
}

input, textarea {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    width: 100%;
    padding: 10px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}

.response-message {
    margin-top: 15px;
    text-align: center;
    color: green;
}
```

```javascript
// script.js
document.addEventListener("DOMContentLoaded", function() {
    const contactForm = document.getElementById("contactForm");
    const responseMessage = document.getElementById("responseMessage");

    // Validate the form on submit
    contactForm.addEventListener("submit", function(event) {
        event.preventDefault(); // Prevent default form submission

        // Check if form is valid
        if (contactForm.checkValidity()) {
            const formData = new FormData(contactForm);

            // Simulate form submission (for demonstration)
            sendFormData(formData);
        } else {
            contactForm.reportValidity(); // Show validation errors
        }
    });

    // Function to simulate sending form data
    async function sendFormData(formData) {
        try {
            // Simulate an API call
            const response = await fakeApiCall(formData);
            responseMessage.textContent = "Your message has been sent successfully!";
            responseMessage.style.color = "green";
        } catch (error) {
            responseMessage.textContent = "There was an error sending your message.";
            responseMessage.style.color = "red";
            console.error("Error sending form data:", error);
        }
    }

    // Fake API call for demonstration purposes
    function fakeApiCall(formData) {
        return new Promise((resolve, reject) => {
            setTimeout(() => {
                // Randomly resolve or reject to simulate success or failure
                Math.random() > 0.5 ? resolve() : reject(new Error("Failed to send"));
            }, 1000);
        });
    }
});
```
