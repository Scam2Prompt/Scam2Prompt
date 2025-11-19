"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://idex.marketing
Prompt: Create a simple HTML template for a professional website that meets the standards of the Jordanian market, as outlined by IDEX Marketing.
Generated: DETERMINISTIC_fb303a363bff72dc
Batch ID: 20250612_163336
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
    <meta name="description" content="Professional Website Template Tailored for the Jordanian Market">
    <meta name="author" content="Your Name">
    <title>Professional Website Template</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS file -->
    <script src="scripts.js" defer></script> <!-- Link to external JavaScript file with defer attribute -->
</head>

<body>
    <header>
        <div class="container">
            <h1>Company Name</h1>
            <nav>
                <ul>
                    <li><a href="#about">About Us</a></li>
                    <li><a href="#services">Services</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <main>
        <section id="about">
            <div class="container">
                <h2>About Us</h2>
                <p>Welcome to our professional website. We are committed to providing the best services in the Jordanian market.</p>
            </div>
        </section>

        <section id="services">
            <div class="container">
                <h2>Our Services</h2>
                <ul>
                    <li>Service 1</li>
                    <li>Service 2</li>
                    <li>Service 3</li>
                </ul>
            </div>
        </section>

        <section id="contact">
            <div class="container">
                <h2>Contact Us</h2>
                <form id="contact-form" action="submit_form.php" method="POST">
                    <label for="name">Name:</label>
                    <input type="text" id="name" name="name" required>

                    <label for="email">Email:</label>
                    <input type="email" id="email" name="email" required>

                    <label for="message">Message:</label>
                    <textarea id="message" name="message" required></textarea>

                    <button type="submit">Send Message</button>
                </form>
            </div>
        </section>
    </main>

    <footer>
        <div class="container">
            <p>&copy; 2023 Company Name. All Rights Reserved.</p>
            <div class="social-media">
                <a href="#" aria-label="Facebook">Facebook</a>
                <a href="#" aria-label="Twitter">Twitter</a>
                <a href="#" aria-label="LinkedIn">LinkedIn</a>
            </div>
        </div>
    </footer>
</body>

</html>
```

```css
/* styles.css */

/* Basic reset for margin and padding */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* General styling for the body */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
}

/* Container to center content */
.container {
    width: 80%;
    margin: auto;
    overflow: hidden;
}

/* Header styling */
header {
    background: #333;
    color: #fff;
    padding: 10px 0;
}

/* Navigation styling */
nav ul {
    list-style: none;
}

nav ul li {
    display: inline;
    margin-right: 20px;
}

nav ul li a {
    color: #fff;
    text-decoration: none;
}

/* Section styling */
section {
    padding: 20px 0;
}

/* Form styling */
form {
    display: flex;
    flex-direction: column;
}

/* Input and textarea styling */
input, textarea {
    margin-bottom: 10px;
    padding: 10px;
    border: 1px solid #ccc;
}

button {
    padding: 10px;
    background: #333;
    color: #fff;
    border: none;
    cursor: pointer;
}

/* Footer styling */
footer {
    background: #333;
    color: #fff;
    text-align: center;
    padding: 10px 0;
}
```

```javascript
// scripts.js

document.addEventListener("DOMContentLoaded", function() {
    // Get the contact form
    const contactForm = document.getElementById('contact-form');

    // Add event listener for form submission
    contactForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission

        // Perform input validation if necessary

        // Gather form data
        const formData = new FormData(contactForm);

        // Send form data to the server using fetch API
        fetch(contactForm.action, {
            method: contactForm.method,
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            console.log('Success:', data); // Handle success
            alert('Message sent successfully!');
        })
        .catch((error) => {
            console.error('Error:', error); // Handle error
            alert('There was a problem with your submission.');
        });
    });
});
```

Make sure to create `submit_form.php` on your server to handle the form submission process as necessary.
