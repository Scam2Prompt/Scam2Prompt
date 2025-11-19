"""
Generated Code Metadata:
========================
Original URL: https://lavage-desinfection-batiments-elevage.fr
Prompt: Generate a code snippet in JavaScript to create a simple website for a cleaning and disinfection service company, including features like service descriptions, contact information, and a quote request form.
Generated: DETERMINISTIC_fe34d8924e5a54c8
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
    <title>Cleaning and Disinfection Services</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Cleaning and Disinfection Services</h1>
        <nav>
            <ul>
                <li><a href="#services">Services</a></li>
                <li><a href="#contact">Contact</a></li>
                <li><a href="#quote">Request a Quote</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="services">
            <h2>Our Services</h2>
            <article>
                <h3>Residential Cleaning</h3>
                <p>Thorough cleaning of your home, including dusting, vacuuming, and sanitizing surfaces.</p>
            </article>
            <article>
                <h3>Commercial Cleaning</h3>
                <p>Professional cleaning services for offices and commercial spaces to ensure a clean work environment.</p>
            </article>
            <article>
                <h3>Disinfection Services</h3>
                <p>Specialized disinfection services to eliminate germs and bacteria, ensuring a safe space for everyone.</p>
            </article>
        </section>

        <section id="contact">
            <h2>Contact Us</h2>
            <p>Email: info@cleaningservice.com</p>
            <p>Phone: (123) 456-7890</p>
        </section>

        <section id="quote">
            <h2>Request a Quote</h2>
            <form id="quoteForm">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>

                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>

                <label for="service">Service Required:</label>
                <select id="service" name="service" required>
                    <option value="">Select a service</option>
                    <option value="residential">Residential Cleaning</option>
                    <option value="commercial">Commercial Cleaning</option>
                    <option value="disinfection">Disinfection Services</option>
                </select>

                <label for="message">Additional Information:</label>
                <textarea id="message" name="message"></textarea>

                <button type="submit">Submit</button>
            </form>
            <div id="responseMessage"></div>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Cleaning and Disinfection Services. All rights reserved.</p>
    </footer>

    <script>
        // Handle form submission
        document.getElementById('quoteForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            // Gather form data
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const service = document.getElementById('service').value;
            const message = document.getElementById('message').value;

            // Simple validation
            if (!name || !email || !service) {
                displayMessage('Please fill in all required fields.', 'error');
                return;
            }

            // Simulate sending data (replace with actual API call)
            try {
                // Simulated success response
                displayMessage('Quote request submitted successfully!', 'success');
                // Reset form
                document.getElementById('quoteForm').reset();
            } catch (error) {
                displayMessage('An error occurred while submitting your request. Please try again later.', 'error');
                console.error('Error submitting quote request:', error);
            }
        });

        // Function to display messages to the user
        function displayMessage(message, type) {
            const responseMessage = document.getElementById('responseMessage');
            responseMessage.textContent = message;
            responseMessage.className = type; // Set class for styling (e.g., success or error)
        }
    </script>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for margins and paddings */
body, h1, h2, h3, p, ul, li {
    margin: 0;
    padding: 0;
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

/* Form styles */
form {
    background: #ffffff;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

form label {
    display: block;
    margin: 10px 0 5px;
}

form input, form select, form textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
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
    padding: 20px 0;
    background: #35424a;
    color: #ffffff;
}

/* Message styles */
.success {
    color: green;
}

.error {
    color: red;
}
```
