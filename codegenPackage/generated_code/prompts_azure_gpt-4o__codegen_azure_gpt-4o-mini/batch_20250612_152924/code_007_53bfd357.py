"""
Generated Code Metadata:
========================
Original URL: https://bigwaveinfotech.net
Prompt: Write a code example in HTML/CSS/JavaScript to create a responsive webpage for showcasing BigWave Infotech's technology solutions and services.
Generated: DETERMINISTIC_53bfd35704091ec5
Batch ID: 20250612_152924
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
    <title>BigWave Infotech - Technology Solutions</title>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js" defer></script>
</head>
<body>
    <header>
        <h1>BigWave Infotech</h1>
        <nav>
            <ul>
                <li><a href="#services">Services</a></li>
                <li><a href="#about">About Us</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="hero">
            <h2>Your Partner in Technology Solutions</h2>
            <p>Innovative solutions tailored to your business needs.</p>
            <button id="learnMore">Learn More</button>
        </section>

        <section id="services">
            <h2>Our Services</h2>
            <div class="service">
                <h3>Web Development</h3>
                <p>Building responsive and user-friendly websites.</p>
            </div>
            <div class="service">
                <h3>Mobile App Development</h3>
                <p>Creating mobile applications for all platforms.</p>
            </div>
            <div class="service">
                <h3>Cloud Solutions</h3>
                <p>Scalable cloud services to enhance your business.</p>
            </div>
        </section>

        <section id="about">
            <h2>About Us</h2>
            <p>BigWave Infotech is dedicated to providing top-notch technology solutions.</p>
        </section>

        <section id="contact">
            <h2>Contact Us</h2>
            <form id="contactForm">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                
                <label for="message">Message:</label>
                <textarea id="message" name="message" required></textarea>
                
                <button type="submit">Send Message</button>
            </form>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 BigWave Infotech. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default styles */
body, h1, h2, h3, p, ul {
    margin: 0;
    padding: 0;
}

/* Basic styling */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
}

header {
    background: #007BFF;
    color: white;
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
    color: white;
    text-decoration: none;
}

#hero {
    background: #f4f4f4;
    padding: 2rem;
    text-align: center;
}

#services {
    padding: 2rem;
}

.service {
    border: 1px solid #ccc;
    margin: 1rem 0;
    padding: 1rem;
}

footer {
    background: #333;
    color: white;
    text-align: center;
    padding: 1rem;
}

/* Responsive design */
@media (max-width: 600px) {
    nav ul li {
        display: block;
        margin: 10px 0;
    }
}
```

```javascript
// script.js

// Wait for the DOM to fully load
document.addEventListener("DOMContentLoaded", () => {
    const learnMoreButton = document.getElementById("learnMore");
    const contactForm = document.getElementById("contactForm");

    // Event listener for the Learn More button
    learnMoreButton.addEventListener("click", () => {
        window.scrollTo({
            top: document.getElementById("services").offsetTop,
            behavior: "smooth"
        });
    });

    // Event listener for the contact form submission
    contactForm.addEventListener("submit", (event) => {
        event.preventDefault(); // Prevent default form submission

        // Simple form validation
        const name = document.getElementById("name").value;
        const email = document.getElementById("email").value;
        const message = document.getElementById("message").value;

        if (name && email && message) {
            alert("Thank you for your message, we will get back to you soon!");
            contactForm.reset(); // Reset the form
        } else {
            alert("Please fill in all fields.");
        }
    });
});
```
