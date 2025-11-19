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

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Company website template for showcasing upcoming launches and contact information.">
    <meta name="author" content="Your Company Name">
    <title>Your Company Name</title>
    <!-- Link to external CSS -->
    <link rel="stylesheet" href="styles.css">
    <!-- Favicon -->
    <link rel="icon" href="favicon.ico" type="image/x-icon">
</head>
<body>
    <!-- Header Section -->
    <header>
        <div class="container">
            <h1>Your Company Name</h1>
            <nav>
                <ul>
                    <li><a href="#launches">Upcoming Launches</a></li>
                    <li><a href="#contact">Contact Us</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Main Content -->
    <main>
        <!-- Upcoming Launches Section -->
        <section id="launches" class="section">
            <div class="container">
                <h2>Upcoming Launches</h2>
                <p>Stay tuned for our exciting new products and services!</p>
                <div class="launch-list">
                    <div class="launch-item">
                        <h3>Launch 1</h3>
                        <p>Details about the first launch.</p>
                    </div>
                    <div class="launch-item">
                        <h3>Launch 2</h3>
                        <p>Details about the second launch.</p>
                    </div>
                </div>
            </div>
        </section>

        <!-- Contact Section -->
        <section id="contact" class="section">
            <div class="container">
                <h2>Contact Us</h2>
                <form id="contact-form">
                    <div class="form-group">
                        <label for="name">Name:</label>
                        <input type="text" id="name" name="name" required>
                    </div>
                    <div class="form-group">
                        <label for="email">Email:</label>
                        <input type="email" id="email" name="email" required>
                    </div>
                    <div class="form-group">
                        <label for="message">Message:</label>
                        <textarea id="message" name="message" rows="5" required></textarea>
                    </div>
                    <button type="submit">Submit</button>
                </form>
            </div>
        </section>
    </main>

    <!-- Footer Section -->
    <footer>
        <div class="container">
            <p>&copy; 2023 Your Company Name. All rights reserved.</p>
        </div>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
body, h1, h2, h3, p, ul, li, form, input, textarea, button {
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
    padding: 20px 0;
}

header h1 {
    text-align: center;
    margin-bottom: 10px;
}

header nav ul {
    list-style: none;
    text-align: center;
}

header nav ul li {
    display: inline;
    margin: 0 15px;
}

header nav ul li a {
    color: #fff;
    text-decoration: none;
    font-weight: bold;
}

/* Section Styling */
.section {
    padding: 40px 0;
    background-color: #fff;
    margin-bottom: 20px;
}

.section h2 {
    text-align: center;
    margin-bottom: 20px;
}

/* Launch List */
.launch-list {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    justify-content: center;
}

.launch-item {
    background-color: #f1f1f1;
    padding: 20px;
    border-radius: 5px;
    width: 300px;
    text-align: center;
}

/* Contact Form */
form {
    max-width: 600px;
    margin: 0 auto;
}

.form-group {
    margin-bottom: 15px;
}

label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
}

input, textarea {
    width: 100%;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

button {
    display: block;
    width: 100%;
    padding: 10px;
    background-color: #0044cc;
    color: #fff;
    border: none;
    border-radius: 5px;
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
    padding: 10px 0;
}
```
