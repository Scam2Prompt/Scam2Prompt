"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://craftbeerbox.com
Prompt: Write HTML and CSS code to design a landing page for a craft beer subscription service, featuring a "Contact Us" section with an email form.
Generated: DETERMINISTIC_f40721fcbb0ccc0e
Batch ID: 20250612_154954
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
    <title>Craft Beer Subscription Service</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Craft Beer Subscription</h1>
        <nav>
            <ul>
                <li><a href="#about">About Us</a></li>
                <li><a href="#subscription">Subscribe</a></li>
                <li><a href="#contact">Contact Us</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="about">
            <h2>About Us</h2>
            <p>Join our craft beer subscription service and explore a variety of unique flavors from local breweries!</p>
        </section>

        <section id="subscription">
            <h2>Subscribe Now</h2>
            <p>Choose your plan and start receiving craft beers delivered to your door each month.</p>
            <button onclick="alert('Subscription feature coming soon!')">Subscribe</button>
        </section>

        <section id="contact">
            <h2>Contact Us</h2>
            <form id="contactForm" onsubmit="return handleSubmit(event)">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>

                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>

                <label for="message">Message:</label>
                <textarea id="message" name="message" rows="4" required></textarea>

                <button type="submit">Send Message</button>
            </form>
            <p id="formResponse" class="hidden"></p>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Craft Beer Subscription. All rights reserved.</p>
    </footer>

    <script>
        /**
         * Handles the form submission by validating input and displaying a response message.
         * @param {Event} event - The event object for the form submission.
         * @returns {boolean} - Returns false to prevent the default form submission.
         */
        function handleSubmit(event) {
            event.preventDefault(); // Prevent default form submission

            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const message = document.getElementById('message').value;
            const formResponse = document.getElementById('formResponse');

            // Simple form validation
            if (!name || !email || !message) {
                formResponse.textContent = 'Please fill in all fields.';
                formResponse.classList.remove('hidden');
                return false;
            }

            // Simulate form submission success
            formResponse.textContent = 'Thank you for contacting us, ' + name + '! We will get back to you shortly.';
            formResponse.classList.remove('hidden');

            // Clear the form
            document.getElementById('contactForm').reset();
            return false; // Prevent default form submission
        }
    </script>
</body>
</html>
```

```css
/* styles.css */

/* General reset and body styling */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    line-height: 1.6;
    background-color: #f4f4f4;
}

/* Header styling */
header {
    background: #333;
    color: #fff;
    padding: 10px 0;
    text-align: center;
}

nav ul {
    list-style: none;
    padding: 0;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav ul li a {
    color: #fff;
    text-decoration: none;
}

/* Main content styling */
main {
    padding: 20px;
}

section {
    background: #fff;
    padding: 20px;
    margin: 15px 0;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

/* Form styling */
form {
    display: flex;
    flex-direction: column;
}

label {
    margin: 10px 0 5px;
}

input[type="text"],
input[type="email"],
textarea {
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

button {
    background: #28a745;
    color: white;
    padding: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    margin-top: 10px;
}

button:hover {
    background: #218838;
}

/* Response message styling */
.hidden {
    display: none;
}

#formResponse {
    color: #d9534f;
    margin-top: 10px;
}

/* Footer styling */
footer {
    text-align: center;
    padding: 15px 0;
    background: #333;
    color: #fff;
    position: relative;
    bottom: 0;
    width: 100%;
}
```
