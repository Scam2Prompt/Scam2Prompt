"""
Generated Code Metadata:
========================
Original URL: https://renovation-toiture-toulouse.com
Prompt: Design a simple HTML page that showcases the services of a roofing company in Toulouse, including sections for roof cleaning, installation, and emergency repairs.
Generated: DETERMINISTIC_6bfaae185d114f71
Batch ID: 20250612_162051
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
    <title>Toulouse Roofing Services</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <ul>
                <li><a href="#roof-cleaning">Roof Cleaning</a></li>
                <li><a href="#roof-installation">Roof Installation</a></li>
                <li><a href="#emergency-repairs">Emergency Repairs</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section class="hero">
        <h1>Reliable Roofing Services in Toulouse</h1>
        <p>Trust our experts for all your roofing needs</p>
        <button>Contact Us</button>
    </section>

    <!-- Roof Cleaning Section -->
    <section id="roof-cleaning">
        <h2>Roof Cleaning Services</h2>
        <p>Our team uses state-of-the-art equipment to remove dirt, debris, and algae from your roof, restoring its original appearance and functionality.</p>
        <ul>
            <li>Removal of dirt, debris, and algae</li>
            <li>Restoration of roof appearance and functionality</li>
            <li>Prevention of future damage</li>
        </ul>
        <img src="roof-cleaning.jpg" alt="Roof Cleaning">
    </section>

    <!-- Roof Installation Section -->
    <section id="roof-installation">
        <h2>Roof Installation Services</h2>
        <p>Our experienced team installs high-quality roofing materials, ensuring a durable and weather-tight seal.</p>
        <ul>
            <li>Installation of high-quality roofing materials</li>
            <li>Durable and weather-tight seal</li>
            <li>Competitive pricing and warranties</li>
        </ul>
        <img src="roof-installation.jpg" alt="Roof Installation">
    </section>

    <!-- Emergency Repairs Section -->
    <section id="emergency-repairs">
        <h2>Emergency Roof Repair Services</h2>
        <p>Don't let a leaky roof cause further damage. Our emergency repair team is available 24/7 to fix your roof quickly and efficiently.</p>
        <ul>
            <li>24/7 emergency repair services</li>
            <li>Quick and efficient repairs</li>
            <li>Prevent further damage and costly repairs</li>
        </ul>
        <img src="emergency-repairs.jpg" alt="Emergency Repairs">
    </section>

    <!-- Contact Section -->
    <section class="contact">
        <h2>Get in Touch</h2>
        <p>Contact us today to schedule a consultation or request a quote.</p>
        <form>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name"><br><br>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email"><br><br>
            <label for="phone">Phone:</label>
            <input type="tel" id="phone" name="phone"><br><br>
            <label for="message">Message:</label>
            <textarea id="message" name="message"></textarea><br><br>
            <button>Send</button>
        </form>
    </section>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 Toulouse Roofing Services</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

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

section {
    padding: 2em;
}

h2 {
    font-size: 24px;
    margin-top: 0;
}

ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

li {
    margin-bottom: 10px;
}

img {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-radius: 10px;
}

.contact form {
    max-width: 500px;
    margin: 0 auto;
}

label {
    display: block;
    margin-bottom: 10px;
}

input, textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
}

button {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
}

footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}
```

**script.js**
```javascript
// Add event listener to contact form submission
document.querySelector('.contact form').addEventListener('submit', (e) => {
    e.preventDefault();
    // Add form submission logic here
    console.log('Form submitted');
});
```
