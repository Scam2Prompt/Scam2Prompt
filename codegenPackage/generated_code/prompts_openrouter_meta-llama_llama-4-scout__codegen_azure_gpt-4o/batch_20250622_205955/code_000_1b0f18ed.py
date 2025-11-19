"""
Generated Code Metadata:
========================
Original URL: https://westpoint-construction.co.uk
Prompt: "Generate a code snippet for a construction company's website, including sections for about, sectors, and contact us, with a focus on groundworks solutions and health and safety."
Generated: DETERMINISTIC_1b0f18ede2a347f5
Batch ID: 20250622_205955
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
    <meta name="description" content="Construction company specializing in groundworks solutions and health and safety.">
    <title>Construction Company</title>
    <link rel="stylesheet" href="styles.css"> <!-- External CSS file for styling -->
</head>
<body>
    <!-- Header Section -->
    <header>
        <div class="container">
            <h1>Construction Company</h1>
            <nav>
                <ul>
                    <li><a href="#about">About</a></li>
                    <li><a href="#sectors">Sectors</a></li>
                    <li><a href="#contact">Contact Us</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- About Section -->
    <section id="about" class="section">
        <div class="container">
            <h2>About Us</h2>
            <p>Welcome to our construction company, where we specialize in groundworks solutions and prioritize health and safety in every project. With years of experience, we deliver reliable and efficient services tailored to your needs.</p>
        </div>
    </section>

    <!-- Sectors Section -->
    <section id="sectors" class="section">
        <div class="container">
            <h2>Sectors</h2>
            <ul>
                <li>Residential Construction</li>
                <li>Commercial Construction</li>
                <li>Infrastructure Development</li>
                <li>Groundworks Solutions</li>
            </ul>
        </div>
    </section>

    <!-- Contact Us Section -->
    <section id="contact" class="section">
        <div class="container">
            <h2>Contact Us</h2>
            <form id="contact-form" action="/submit-form" method="POST">
                <!-- Name Input -->
                <div class="form-group">
                    <label for="name">Name:</label>
                    <input type="text" id="name" name="name" required>
                </div>
                <!-- Email Input -->
                <div class="form-group">
                    <label for="email">Email:</label>
                    <input type="email" id="email" name="email" required>
                </div>
                <!-- Message Input -->
                <div class="form-group">
                    <label for="message">Message:</label>
                    <textarea id="message" name="message" rows="5" required></textarea>
                </div>
                <!-- Submit Button -->
                <button type="submit">Send Message</button>
            </form>
        </div>
    </section>

    <!-- Footer Section -->
    <footer>
        <div class="container">
            <p>&copy; 2023 Construction Company. All rights reserved.</p>
        </div>
    </footer>

    <!-- External JavaScript file for interactivity -->
    <script src="scripts.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
body, h1, h2, p, ul, li, form, input, textarea, button {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body Styling */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f9f9f9;
}

/* Container */
.container {
    width: 90%;
    max-width: 1200px;
    margin: 0 auto;
}

/* Header */
header {
    background-color: #0044cc;
    color: #fff;
    padding: 1rem 0;
}
header h1 {
    text-align: center;
}
header nav ul {
    display: flex;
    justify-content: center;
    list-style: none;
    margin-top: 0.5rem;
}
header nav ul li {
    margin: 0 1rem;
}
header nav ul li a {
    color: #fff;
    text-decoration: none;
}

/* Section Styling */
.section {
    padding: 2rem 0;
    background-color: #fff;
    margin-bottom: 1rem;
}
.section h2 {
    text-align: center;
    margin-bottom: 1rem;
}
.section p, .section ul {
    text-align: center;
}

/* Form Styling */
form {
    max-width: 600px;
    margin: 0 auto;
}
.form-group {
    margin-bottom: 1rem;
}
label {
    display: block;
    margin-bottom: 0.5rem;
}
input, textarea {
    width: 100%;
    padding: 0.5rem;
    border: 1px solid #ccc;
    border-radius: 4px;
}
button {
    display: block;
    width: 100%;
    padding: 0.5rem;
    background-color: #0044cc;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}
button:hover {
    background-color: #003399;
}

/* Footer */
footer {
    background-color: #333;
    color: #fff;
    text-align: center;
    padding: 1rem 0;
}
```

```javascript
// scripts.js

// Add event listener for form submission
document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    // Collect form data
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const message = document.getElementById('message').value.trim();

    // Basic validation
    if (!name || !email || !message) {
        alert('Please fill out all fields.');
        return;
    }

    // Simulate form submission (replace with actual API call in production)
    alert('Thank you for your message! We will get back to you shortly.');

    // Reset form fields
    document.getElementById('contact-form').reset();
});
```
