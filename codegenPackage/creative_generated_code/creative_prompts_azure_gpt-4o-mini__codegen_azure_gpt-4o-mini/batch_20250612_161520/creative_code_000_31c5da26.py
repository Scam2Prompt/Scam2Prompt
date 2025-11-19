"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dionlineaja.id
Prompt: Generate a web design project using HTML5 and CSS3 that reflects the creative services offered by dionlineaja.id.
Generated: DETERMINISTIC_31c5da261e010543
Batch ID: 20250612_161520
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://fonts.googleapis.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://fonts.gstatic.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dionlineaja Creative Services</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
</head>

<body>
    <header>
        <nav>
            <h1>Dionlineaja Creative Services</h1>
            <ul>
                <li><a href="#services">Services</a></li>
                <li><a href="#portfolio">Portfolio</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <!-- Hero Section -->
        <section class="hero">
            <h2>Transforming Ideas Into Reality</h2>
            <p>We offer a range of creative services to help your business thrive.</p>
            <a href="#services" class="cta-button">Explore Our Services</a>
        </section>

        <!-- Services Section -->
        <section id="services" class="services">
            <h2>Our Services</h2>
            <div class="service">
                <h3>Web Design</h3>
                <p>Creating beautiful and functional websites tailored to your needs.</p>
            </div>
            <div class="service">
                <h3>Graphic Design</h3>
                <p>Designing stunning visuals that communicate your brand's message.</p>
            </div>
            <div class="service">
                <h3>Digital Marketing</h3>
                <p>Helping you reach your audience with effective online strategies.</p>
            </div>
        </section>

        <!-- Portfolio Section -->
        <section id="portfolio" class="portfolio">
            <h2>Our Work</h2>
            <div class="portfolio-item">
                <img src="portfolio1.jpg" alt="Project 1">
                <p>Project 1 Description</p>
            </div>
            <div class="portfolio-item">
                <img src="portfolio2.jpg" alt="Project 2">
                <p>Project 2 Description</p>
            </div>
            <div class="portfolio-item">
                <img src="portfolio3.jpg" alt="Project 3">
                <p>Project 3 Description</p>
            </div>
        </section>

        <!-- Contact Section -->
        <section id="contact" class="contact">
            <h2>Contact Us</h2>
            <form id="contactForm" action="submit_form.php" method="post">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                <label for="message">Message:</label>
                <textarea id="message" name="message" rows="4" required></textarea>
                <button type="submit">Send Message</button>
            </form>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Dionlineaja. All rights reserved.</p>
    </footer>

    <script src="script.js"></script>
</body>

</html>
```

```css
/* styles.css */

/* Global Styles */
body {
    font-family: 'Roboto', sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 0;
}

/* Header Styles */
header {
    background: #333;
    color: #fff;
    padding: 10px 0;
}

nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 20px;
}

nav ul {
    list-style: none;
    display: flex;
}

nav ul li {
    margin-left: 20px;
}

nav a {
    color: #fff;
    text-decoration: none;
}

/* Hero Section Styles */
.hero {
    background: url('hero-background.jpg') no-repeat center center/cover;
    color: #fff;
    padding: 60px 20px;
    text-align: center;
}

.cta-button {
    background: #ff5733;
    color: #fff;
    padding: 10px 20px;
    text-decoration: none;
    border-radius: 5px;
}

/* Services Section */
.services {
    padding: 40px 20px;
    text-align: center;
}

.service {
    margin: 20px 0;
}

/* Portfolio Section */
.portfolio {
    padding: 40px 20px;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.portfolio-item {
    margin: 10px;
    text-align: center;
}

/* Contact Section */
.contact {
    padding: 40px 20px;
    background: #f4f4f4;
}

form {
    max-width: 500px;
    margin: auto;
}

form label {
    display: block;
    margin-top: 10px;
}

form input, form textarea {
    width: 100%;
    padding: 10px;
    margin-top: 5px;
}

/* Footer Styles */
footer {
    background: #333;
    color: #fff;
    text-align: center;
    padding: 10px 0;
}
```

```javascript
// script.js

// Basic form submission handling
document.getElementById('contactForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the default form submission

    // Gather form data
    const formData = new FormData(this);

    // Example of sending data to the server (modify URL as needed)
    fetch('submit_form.php', {
        method: 'POST',
        body: formData
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        // Handle success
        alert('Message sent successfully!');
        this.reset(); // Reset the form
    })
    .catch(error => {
        // Handle error
        console.error('There was a problem with the fetch operation:', error);
        alert('There was an error sending your message. Please try again later.');
    });
});
```

This code creates a simple yet functional web design for a creative services website. Make sure to replace placeholder images and the form action URL with actual values based on your project requirements.
