"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://okk-16s.pages.dev
Prompt: What are the best practices for creating a simple webpage layout like the one demonstrated on https://okk-16s.pages.dev?
Generated: DETERMINISTIC_baf3e34d2046b911
Batch ID: 20250612_155959
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
    <title>Simple Webpage Layout</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS file -->
</head>
<body>
    <header>
        <h1>Welcome to My Website</h1>
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
            <h2>Home</h2>
            <p>This is the home section of the webpage.</p>
        </section>

        <section id="about">
            <h2>About</h2>
            <p>This section provides information about the website.</p>
        </section>

        <section id="services">
            <h2>Services</h2>
            <p>Details about the services offered.</p>
        </section>

        <section id="contact">
            <h2>Contact</h2>
            <form id="contact-form" action="/submit" method="POST">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                
                <label for="message">Message:</label>
                <textarea id="message" name="message" required></textarea>
                
                <button type="submit">Send</button>
            </form>
        </section>
    </main>
    
    <footer>
        <p>&copy; 2023 My Website. All rights reserved.</p>
    </footer>

    <script src="script.js"></script> <!-- Link to external JavaScript file -->
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
body, h1, h2, p, ul {
    margin: 0;
    padding: 0;
}

/* Set body styles */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
}

/* Header styles */
header {
    background: #333;
    color: #fff;
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
    color: #fff;
    text-decoration: none;
}

/* Main content styles */
main {
    padding: 20px;
}

/* Section styles */
section {
    margin-bottom: 20px;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 10px 0;
    background: #333;
    color: #fff;
    position: relative;
    bottom: 0;
    width: 100%;
}
```

```javascript
// script.js

// Event listener for the contact form submission
document.getElementById('contact-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission

    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;

    // Basic validation (can be enhanced)
    if (name && email && message) {
        // Simulate form submission (replace with actual API call)
        console.log('Form submitted successfully:', { name, email, message });
        alert('Thank you for your message!');
    } else {
        alert('Please fill in all fields.');
    }
});
```
