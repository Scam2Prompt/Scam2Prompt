"""
Generated Code Metadata:
========================
Original URL: https://happyboarding.edu.np
Prompt: Create a simple web page using HTML, CSS, and JavaScript to showcase school facilities, similar to Happy Boarding School's website.
Generated: DETERMINISTIC_57765f6c5c7d7078
Batch ID: 20250622_204903
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
    <title>Happy Boarding School Facilities</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Welcome to Happy Boarding School</h1>
        <nav>
            <ul>
                <li><a href="#facilities">Facilities</a></li>
                <li><a href="#about">About Us</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="facilities">
            <h2>Our Facilities</h2>
            <div class="facility" id="library">
                <h3>Library</h3>
                <p>Our library is equipped with a vast collection of books and study materials.</p>
            </div>
            <div class="facility" id="sports">
                <h3>Sports Complex</h3>
                <p>We have a state-of-the-art sports complex for various athletic activities.</p>
            </div>
            <div class="facility" id="dormitory">
                <h3>Dormitory</h3>
                <p>Comfortable and safe dormitory facilities for all students.</p>
            </div>
        </section>

        <section id="about">
            <h2>About Us</h2>
            <p>Happy Boarding School is dedicated to providing a nurturing environment for students.</p>
        </section>

        <section id="contact">
            <h2>Contact Us</h2>
            <form id="contactForm" onsubmit="return handleSubmit(event)">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                
                <label for="message">Message:</label>
                <textarea id="message" name="message" required></textarea>
                
                <button type="submit">Send Message</button>
            </form>
            <div id="formResponse"></div>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Happy Boarding School. All rights reserved.</p>
    </footer>

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

/* Body styles */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
}

/* Header styles */
header {
    background: #35424a;
    color: #ffffff;
    padding: 20px 0;
    text-align: center;
}

nav ul {
    list-style: none;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav ul li a {
    color: #ffffff;
    text-decoration: none;
}

/* Main section styles */
main {
    padding: 20px;
}

/* Facility section styles */
.facility {
    background: #ffffff;
    border: 1px solid #dddddd;
    margin: 10px 0;
    padding: 15px;
}

/* Form styles */
form {
    background: #ffffff;
    padding: 20px;
    border: 1px solid #dddddd;
    margin-top: 20px;
}

form label {
    display: block;
    margin: 10px 0 5px;
}

form input, form textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #cccccc;
}

form button {
    background: #35424a;
    color: #ffffff;
    border: none;
    padding: 10px 15px;
    cursor: pointer;
}

form button:hover {
    background: #2c3e50;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 10px 0;
    background: #35424a;
    color: #ffffff;
    position: relative;
    bottom: 0;
    width: 100%;
}
```

```javascript
// script.js

/**
 * Handles the form submission.
 * @param {Event} event - The event object.
 * @returns {boolean} - Returns false to prevent default form submission.
 */
function handleSubmit(event) {
    event.preventDefault(); // Prevent default form submission

    // Get form values
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;

    // Simple validation (could be expanded)
    if (!name || !email || !message) {
        displayResponse("Please fill in all fields.", false);
        return false;
    }

    // Simulate form submission (e.g., send to server)
    // In a real application, you would use fetch or XMLHttpRequest here
    displayResponse("Thank you for your message, " + name + "!", true);

    // Clear form fields
    document.getElementById('contactForm').reset();
    return false; // Prevent default form submission
}

/**
 * Displays the response message to the user.
 * @param {string} message - The message to display.
 * @param {boolean} isSuccess - Indicates if the submission was successful.
 */
function displayResponse(message, isSuccess) {
    const responseDiv = document.getElementById('formResponse');
    responseDiv.textContent = message;
    responseDiv.style.color = isSuccess ? 'green' : 'red';
}
```
