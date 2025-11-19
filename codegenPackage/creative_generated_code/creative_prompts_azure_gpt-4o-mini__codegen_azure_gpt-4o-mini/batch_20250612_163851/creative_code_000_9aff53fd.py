"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamaks.xyz
Prompt: Generate a code snippet for a web application that showcases professional interior design services, similar to those offered by AYOFT.
Generated: DETERMINISTIC_9aff53fdc6c5a6dd
Batch ID: 20250612_163851
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
    <title>Professional Interior Design Services</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>AYOFT Interior Design</h1>
        <nav>
            <ul>
                <li><a href="#services">Services</a></li>
                <li><a href="#portfolio">Portfolio</a></li>
                <li><a href="#about">About Us</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="services">
            <h2>Our Services</h2>
            <div class="service">
                <h3>Residential Design</h3>
                <p>Transform your home into a stunning living space with our expert residential design services.</p>
            </div>
            <div class="service">
                <h3>Commercial Design</h3>
                <p>Enhance your business environment with our professional commercial design solutions.</p>
            </div>
            <div class="service">
                <h3>Consultation</h3>
                <p>Get expert advice on your design projects through our one-on-one consultation services.</p>
            </div>
        </section>

        <section id="portfolio">
            <h2>Our Portfolio</h2>
            <div class="portfolio-item">
                <img src="project1.jpg" alt="Living Room Design">
                <h3>Modern Living Room</h3>
            </div>
            <div class="portfolio-item">
                <img src="project2.jpg" alt="Office Space Design">
                <h3>Chic Office Space</h3>
            </div>
            <div class="portfolio-item">
                <img src="project3.jpg" alt="Cozy Bedroom Design">
                <h3>Cozy Bedroom</h3>
            </div>
        </section>

        <section id="about">
            <h2>About Us</h2>
            <p>AYOFT is a premier interior design firm with a passion for creating beautiful, functional spaces.</p>
        </section>

        <section id="contact">
            <h2>Contact Us</h2>
            <form id="contact-form" method="POST" action="/submit">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>

                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>

                <label for="message">Message:</label>
                <textarea id="message" name="message" required></textarea>

                <button type="submit">Send Message</button>
            </form>
            <div id="form-response" aria-live="polite"></div>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 AYOFT Interior Design. All rights reserved.</p>
    </footer>

    <script>
        // Handle form submission
        document.getElementById('contact-form').addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent the default form submission

            const formData = new FormData(this);
            fetch('/submit', {
                method: 'POST',
                body: formData
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                return response.text();
            })
            .then(data => {
                document.getElementById('form-response').textContent = 'Message sent successfully!';
                this.reset(); // Reset the form fields
            })
            .catch(error => {
                document.getElementById('form-response').textContent = 'Error: ' + error.message;
            });
        });
    </script>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for margin and padding */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
    color: #333;
}

header {
    background: #333;
    color: #fff;
    padding: 1rem;
    text-align: center;
}

nav ul {
    list-style: none;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav a {
    color: #fff;
    text-decoration: none;
}

main {
    padding: 20px;
}

.service, .portfolio-item {
    background: #fff;
    margin: 15px 0;
    padding: 15px;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

footer {
    text-align: center;
    padding: 1rem;
    background: #333;
    color: #fff;
    position: relative;
    bottom: 0;
    width: 100%;
}
```
