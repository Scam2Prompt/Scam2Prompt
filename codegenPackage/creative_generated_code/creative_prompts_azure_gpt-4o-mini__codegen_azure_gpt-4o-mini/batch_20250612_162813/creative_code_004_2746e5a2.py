"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ideru.com
Prompt: How can I ensure that my website design aligns with corporate branding while maintaining user-friendliness?
Generated: DETERMINISTIC_2746e5a2120886b0
Batch ID: 20250612_162813
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
    <title>Corporate Branding Website</title>
    <!-- Link to external CSS for corporate branding styles -->
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="home">
            <h1>Welcome to Our Company</h1>
            <p>Your trusted partner in excellence.</p>
        </section>

        <section id="about">
            <h2>About Us</h2>
            <p>We uphold corporate branding standards while prioritizing user experience.</p>
        </section>

        <section id="services">
            <h2>Our Services</h2>
            <ul>
                <li>Consulting</li>
                <li>Design</li>
                <li>Development</li>
            </ul>
        </section>

        <section id="contact">
            <h2>Contact Us</h2>
            <form id="contactForm" onsubmit="return handleSubmit(event);">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>

                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>

                <label for="message">Message:</label>
                <textarea id="message" name="message" required></textarea>

                <button type="submit">Send Message</button>
            </form>
            <p id="formResponse"></p>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Our Company. All rights reserved.</p>
    </footer>

    <script>
        /**
         * Handles form submission for the contact form
         * @param {Event} event - The submit event of the form
         * @returns {boolean} - Returns false to prevent page refresh
         */
        function handleSubmit(event) {
            event.preventDefault(); // Prevent the default form submission
            const formResponse = document.getElementById('formResponse');
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const message = document.getElementById('message').value;

            // Basic validation (this can be expanded)
            if (!name || !email || !message) {
                formResponse.textContent = 'Please fill out all fields.';
                return false;
            }

            // Simulate a successful form submission
            formResponse.textContent = 'Thank you for your message, ' + name + '!';
            document.getElementById('contactForm').reset(); // Reset form fields
            return true;
        }
    </script>
</body>
</html>
```

```css
/* styles.css */

/* Basic Reset */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body Styling */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f4f4f4;
}

/* Header Styling */
header {
    background: #004d99; /* Corporate branding color */
    color: #fff;
    padding: 10px 0;
}

nav ul {
    list-style: none;
    display: flex;
    justify-content: center;
}

nav ul li {
    margin: 0 15px;
}

nav ul li a {
    color: #fff;
    text-decoration: none;
}

/* Main Section Styling */
main {
    padding: 20px;
}

/* Form Styling */
form {
    display: flex;
    flex-direction: column;
}

form label {
    margin: 10px 0 5px;
}

form input,
form textarea {
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

/* Footer Styling */
footer {
    text-align: center;
    padding: 20px;
    background: #004d99; /* Corporate branding color */
    color: #fff;
}
```
