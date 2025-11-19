"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digistrategy.in
Prompt: Generate a code snippet for a custom website design that enhances user engagement based on the services offered by DigiStrategy.
Generated: DETERMINISTIC_40b7f2203249073d
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap": {
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
    <meta name="description" content="DigiStrategy - Comprehensive Digital Solutions to Boost Engagement">
    <title>DigiStrategy - Enhance Your Digital Engagement</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="icon" href="favicon.ico" type="image/x-icon">
    <!-- Google Font: Roboto for clean typography -->
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet">
</head>
<body>
    <!-- Header Section -->
    <header>
        <div class="container header-container">
            <div class="logo">
                <a href="/">
                    <img src="logo.png" alt="DigiStrategy Logo" width="150">
                </a>
            </div>
            <nav class="navbar">
                <ul>
                    <li><a href="#services">Services</a></li>
                    <li><a href="#team">Our Team</a></li>
                    <li><a href="#contact">Contact</a></li>
                </ul>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <div class="container">
            <h1>Welcome to DigiStrategy</h1>
            <p>Providing cutting-edge digital solutions to maximize your engagement and drive results.</p>
            <a href="#services" class="cta-button">Explore Our Services</a>
        </div>
    </section>

    <!-- Services Section -->
    <section id="services">
        <div class="container">
            <h2>Our Services</h2>
            <div class="service-cards">
                <div class="service-card">
                    <h3>SEO Optimization</h3>
                    <p>Improve your search rankings and increase organic traffic.</p>
                </div>
                <div class="service-card">
                    <h3>Social Media Management</h3>
                    <p>Engage with your audience across popular social platforms.</p>
                </div>
                <div class="service-card">
                    <h3>Content Creation</h3>
                    <p>Create impactful content that drives conversions.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Team Section -->
    <section id="team">
        <div class="container">
            <h2>Meet Our Team</h2>
            <div class="team-grid">
                <div class="team-member">
                    <img src="team1.jpg" alt="Team Member 1" width="100">
                    <h3>John Doe</h3>
                    <p>SEO Specialist</p>
                </div>
                <div class="team-member">
                    <img src="team2.jpg" alt="Team Member 2" width="100">
                    <h3>Jane Smith</h3>
                    <p>Content Strategist</p>
                </div>
                <div class="team-member">
                    <img src="team3.jpg" alt="Team Member 3" width="100">
                    <h3>Mike Lee</h3>
                    <p>Social Media Manager</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section id="contact">
        <div class="container">
            <h2>Contact Us</h2>
            <form id="contact-form">
                <label for="name">Name</label>
                <input type="text" id="name" name="name" required>

                <label for="email">Email</label>
                <input type="email" id="email" name="email" required>

                <label for="message">Message</label>
                <textarea id="message" name="message" rows="4" required></textarea>

                <button type="submit">Submit</button>
            </form>
        </div>
    </section>

    <!-- Footer Section -->
    <footer>
        <div class="container footer-container">
            <p>&copy; 2023 DigiStrategy. All rights reserved.</p>
            <nav class="footer-nav">
                <ul>
                    <li><a href="#privacy">Privacy Policy</a></li>
                    <li><a href="#terms">Terms of Service</a></li>
                </ul>
            </nav>
        </div>
    </footer>

    <!-- External JS File -->
    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* General Styles */
body {
    font-family: 'Roboto', sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
    color: #333;
}

.container {
    width: 90%;
    max-width: 1200px;
    margin: 0 auto;
}

h1, h2, h3 {
    margin: 0;
}

a {
    text-decoration: none;
    color: inherit;
}

/* Header */
header {
    background-color: #333;
    color: #fff;
    padding: 10px 0;
}

.header-container {
    display: flex;
    align-items: center;
    justify-content: space-between;
}

.navbar ul {
    list-style: none;
    display: flex;
    gap: 20px;
}

.navbar a {
    color: #fff;
    font-weight: bold;
}

/* Hero Section */
.hero {
    background-color: #0073e6;
    color: #fff;
    text-align: center;
    padding: 50px 20px;
}

.cta-button {
    display: inline-block;
    margin-top: 20px;
    padding: 10px 20px;
    background-color: #ff6600;
    color: #fff;
    border-radius: 5px;
    font-weight: bold;
}

/* Services Section */
.service-cards {
    display: flex;
    gap: 20px;
    margin-top: 20px;
}

.service-card {
    background-color: #fff;
    border-radius: 5px;
    padding: 20px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    flex: 1;
}

/* Team Section */
.team-grid {
    display: flex;
    gap: 20px;
    margin-top: 20px;
}

.team-member {
    text-align: center;
}

.team-member img {
    border-radius: 50%;
}

/* Contact Section */
form {
    display: flex;
    flex-direction: column;
    gap: 10px;
}

input, textarea, button {
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

/button {
    background-color: #0073e6;
    color: #fff;
    font-weight: bold;
}

/* Footer */
footer {
    background-color: #333;
    color: #fff;
    text-align: center;
    padding: 10px 0;
}

/footer-nav ul {
    list-style: none;
    display: flex;
    gap: 20px;
    justify-content: center;
}

.footer-nav a {
    color: #fff;
}
```

```javascript
// script.js

document.getElementById('contact-form').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent form submission

    // Retrieve form data
    const name = document.getElementById('name').value.trim();
    const email = document.getElementById('email').value.trim();
    const message = document.getElementById('message').value.trim();

    // Basic validation
    if (!name || !email || !message) {
        alert('Please fill out all fields.');
        return;
    }

    // Simulate form submission (replace with actual API call in production)
    alert('Thank you for contacting us, ' + name + '! We will get back to you soon.');
    document.getElementById('contact-form').reset();
});
```
