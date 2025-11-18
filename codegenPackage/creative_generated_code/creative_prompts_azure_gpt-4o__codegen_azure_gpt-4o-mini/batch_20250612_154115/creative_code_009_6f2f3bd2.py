"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://infinitiai.in
Prompt: Generate code to build a high-performing landing page with custom menus and lead capture forms using InfinitiAI's page builder.
Generated: DETERMINISTIC_6f2f3bd275af1a20
Batch ID: 20250612_154115
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
    <title>Landing Page</title>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js" defer></script>
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <ul class="custom-menu">
                <li><a href="#home">Home</a></li>
                <li><a href="#about">About</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <!-- Main Content Section -->
    <main>
        <section id="home">
            <h1>Welcome to Our Landing Page</h1>
            <p>Your one-stop solution for your needs.</p>
        </section>

        <section id="about">
            <h2>About Us</h2>
            <p>We are dedicated to providing the best service.</p>
        </section>

        <section id="services">
            <h2>Our Services</h2>
            <ul>
                <li>Service 1</li>
                <li>Service 2</li>
                <li>Service 3</li>
            </ul>
        </section>

        <!-- Lead Capture Form Section -->
        <section id="contact">
            <h2>Get in Touch</h2>
            <form id="leadCaptureForm" onsubmit="return handleSubmit(event)">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>

                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>

                <label for="message">Message:</label>
                <textarea id="message" name="message" required></textarea>

                <button type="submit">Submit</button>
            </form>
            <p id="formResponse"></p>
        </section>
    </main>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 Your Company. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Reset some basic elements */
body, h1, h2, p, ul {
    margin: 0;
    padding: 0;
}

/* Basic styling for body */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
}

/* Header styling */
header {
    background: #333;
    color: #fff;
    padding: 10px 0;
}

/* Menu styling */
.custom-menu {
    list-style: none;
    display: flex;
    justify-content: center;
}

.custom-menu li {
    margin: 0 15px;
}

.custom-menu a {
    color: #fff;
    text-decoration: none;
}

/* Main content styling */
main {
    padding: 20px;
}

/* Form styling */
form {
    display: flex;
    flex-direction: column;
}

form label {
    margin-bottom: 5px;
}

form input, form textarea {
    margin-bottom: 15px;
    padding: 10px;
    border: 1px solid #ccc;
}

/* Footer styling */
footer {
    text-align: center;
    padding: 10px 0;
    background: #f4f4f4;
}
```

```javascript
// script.js

/**
 * Handles the submission of the lead capture form.
 * @param {Event} event - The submit event from the form.
 * @returns {boolean} - False to prevent default form submission.
 */
function handleSubmit(event) {
    event.preventDefault(); // Prevent default form submission

    // Retrieve form data
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;

    // Validate email format
    if (!validateEmail(email)) {
        showFormResponse("Please enter a valid email address.", false);
        return false;
    }

    // Simulate sending data to server (replace with actual API call)
    try {
        // Here you would typically make an API call to send the data.
        console.log("Sending data:", { name, email, message });
        showFormResponse("Thank you for your message!", true);
        // Reset form fields
        document.getElementById('leadCaptureForm').reset();
    } catch (error) {
        showFormResponse("There was an error submitting your form. Please try again later.", false);
    }
    return false; // Prevent default form submission
}

/**
 * Validates the email format using a regular expression.
 * @param {string} email - The email address to validate.
 * @returns {boolean} - True if valid, otherwise false.
 */
function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(String(email).toLowerCase());
}

/**
 * Displays a response message to the user.
 * @param {string} message - The message to display.
 * @param {boolean} isSuccess - Indicates if the message is a success message.
 */
function showFormResponse(message, isSuccess) {
    const responseElement = document.getElementById('formResponse');
    responseElement.textContent = message;
    responseElement.style.color = isSuccess ? 'green' : 'red';
}
```
