"""
Generated Code Metadata:
========================
Original URL: https://celestia.solutions
Prompt: Develop a basic HTML/CSS template for a company website similar to celestia.solutions, incorporating sections for upcoming launches and contact information.
Generated: DETERMINISTIC_2329dfa8114e47b2
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Company Website</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <ul>
                <li><a href="#upcoming-launches">Upcoming Launches</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <h1>Welcome to Our Company</h1>
        <p>We are a team of experts dedicated to delivering innovative solutions.</p>
        <button>Learn More</button>
    </section>

    <!-- Upcoming Launches Section -->
    <section id="upcoming-launches" class="upcoming-launches">
        <h2>Upcoming Launches</h2>
        <div class="launch-cards">
            <div class="launch-card">
                <h3>Launch 1</h3>
                <p>Date: <span>2024-09-01</span></p>
                <p>Description: This is the description of launch 1.</p>
            </div>
            <div class="launch-card">
                <h3>Launch 2</h3>
                <p>Date: <span>2024-10-01</span></p>
                <p>Description: This is the description of launch 2.</p>
            </div>
            <div class="launch-card">
                <h3>Launch 3</h3>
                <p>Date: <span>2024-11-01</span></p>
                <p>Description: This is the description of launch 3.</p>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact" class="contact">
        <h2>Get in Touch</h2>
        <form>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name" required>

            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="message">Message:</label>
            <textarea id="message" name="message" required></textarea>

            <button>Send</button>
        </form>
    </section>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2024 Company Name. All Rights Reserved.</p>
    </footer>
</body>
</html>
```

**styles.css**
```css
/* Global Styles */
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f9f9f9;
}

/* Header Styles */
header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

header nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

header nav ul li {
    display: inline-block;
    margin-right: 20px;
}

header nav a {
    color: #fff;
    text-decoration: none;
}

/* Hero Styles */
.hero {
    background-image: linear-gradient(to bottom, #333, #555);
    background-size: 100% 300px;
    background-position: 0% 100%;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #fff;
}

.hero h1 {
    font-size: 48px;
}

/* Upcoming Launches Styles */
.upcoming-launches {
    padding: 2em;
}

.upcoming-launches h2 {
    margin-bottom: 10px;
}

.launch-cards {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.launch-card {
    background-color: #fff;
    padding: 1em;
    margin: 10px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    width: calc(33.33% - 20px);
}

.launch-card h3 {
    margin-top: 0;
}

/* Contact Styles */
.contact {
    padding: 2em;
}

.contact form {
    max-width: 500px;
    margin: 0 auto;
}

.contact label {
    display: block;
    margin-bottom: 10px;
}

.contact input, .contact textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
}

.contact button {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
}

/* Footer Styles */
footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}
```
