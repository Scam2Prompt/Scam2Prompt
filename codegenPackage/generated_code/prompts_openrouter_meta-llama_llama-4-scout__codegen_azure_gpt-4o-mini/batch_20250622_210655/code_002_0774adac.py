"""
Generated Code Metadata:
========================
Original URL: https://al-afdel.com
Prompt: Generate a code snippet in JavaScript for creating a simple website like Al-Afdel for Home Maintenance, incorporating services such as pest control, cleaning, and insulation.
Generated: DETERMINISTIC_0774adac076dd650
Batch ID: 20250622_210655
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
    <title>Home Maintenance Services</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Al-Afdel Home Maintenance</h1>
        <nav>
            <ul>
                <li><a href="#services">Services</a></li>
                <li><a href="#contact">Contact Us</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="services">
            <h2>Our Services</h2>
            <div class="service" id="pest-control">
                <h3>Pest Control</h3>
                <p>Effective pest control solutions for your home.</p>
                <button onclick="bookService('Pest Control')">Book Now</button>
            </div>
            <div class="service" id="cleaning">
                <h3>Cleaning</h3>
                <p>Professional cleaning services to keep your home spotless.</p>
                <button onclick="bookService('Cleaning')">Book Now</button>
            </div>
            <div class="service" id="insulation">
                <h3>Insulation</h3>
                <p>Quality insulation services for energy efficiency.</p>
                <button onclick="bookService('Insulation')">Book Now</button>
            </div>
        </section>

        <section id="contact">
            <h2>Contact Us</h2>
            <form id="contact-form" onsubmit="submitForm(event)">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                
                <label for="message">Message:</label>
                <textarea id="message" name="message" required></textarea>
                
                <button type="submit">Send Message</button>
            </form>
            <div id="form-response"></div>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Al-Afdel Home Maintenance. All rights reserved.</p>
    </footer>

    <script>
        /**
         * Function to handle service booking
         * @param {string} serviceName - The name of the service to book
         */
        function bookService(serviceName) {
            alert(`You have booked the ${serviceName} service!`);
        }

        /**
         * Function to handle form submission
         * @param {Event} event - The form submission event
         */
        function submitForm(event) {
            event.preventDefault(); // Prevent default form submission

            // Gather form data
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const message = document.getElementById('message').value;

            // Simple validation
            if (!name || !email || !message) {
                displayResponse('Please fill in all fields.', 'error');
                return;
            }

            // Simulate form submission (replace with actual API call)
            setTimeout(() => {
                displayResponse('Your message has been sent successfully!', 'success');
                document.getElementById('contact-form').reset(); // Reset form
            }, 1000);
        }

        /**
         * Function to display response messages
         * @param {string} message - The message to display
         * @param {string} type - The type of message ('success' or 'error')
         */
        function displayResponse(message, type) {
            const responseDiv = document.getElementById('form-response');
            responseDiv.textContent = message;
            responseDiv.className = type; // Set class for styling
        }
    </script>
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
    padding: 10px 0;
    text-align: center;
}

/* Navigation styles */
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

/* Service section styles */
.service {
    background: #ffffff;
    border: 1px solid #dddddd;
    margin: 10px 0;
    padding: 15px;
}

/* Form styles */
form {
    background: #ffffff;
    padding: 15px;
    border: 1px solid #dddddd;
    margin-top: 20px;
}

/* Response message styles */
.success {
    color: green;
}

.error {
    color: red;
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
