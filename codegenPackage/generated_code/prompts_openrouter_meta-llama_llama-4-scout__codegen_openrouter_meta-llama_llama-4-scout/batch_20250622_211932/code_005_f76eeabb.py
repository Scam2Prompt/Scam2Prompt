"""
Generated Code Metadata:
========================
Original URL: https://orlandoplasmacenters.com
Prompt: Develop a basic HTML and CSS template for a plasma donation center website, incorporating features and sections similar to those found on the Orlando Plasma Centers website.
Generated: DETERMINISTIC_f76eeabb30d18769
Batch ID: 20250622_211932
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
    <title>Plasma Donation Center</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <ul>
                <li><a href="#about">About Us</a></li>
                <li><a href="#donate">Donate Plasma</a></li>
                <li><a href="#locations">Locations</a></li>
                <li><a href="#faq">FAQ</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section id="hero">
        <h1>Donate Plasma and Save Lives</h1>
        <p>Learn more about plasma donation and how you can help</p>
        <button>Donate Today</button>
    </section>

    <!-- About Section -->
    <section id="about">
        <h2>About Our Center</h2>
        <p>Our plasma donation center is committed to providing a safe and welcoming environment for our donors. We are dedicated to helping patients in need of life-saving therapies.</p>
    </section>

    <!-- Donate Section -->
    <section id="donate">
        <h2>Donate Plasma</h2>
        <p>Donating plasma is a safe and rewarding experience. Learn more about the process and how you can help.</p>
        <ol>
            <li>Sign up to be a donor</li>
            <li>Schedule an appointment</li>
            <li>Donate plasma and earn rewards</li>
        </ol>
    </section>

    <!-- Locations Section -->
    <section id="locations">
        <h2>Find a Location Near You</h2>
        <ul>
            <li>
                <h3>Orlando Location</h3>
                <p>123 Main St, Orlando, FL 32801</p>
            </li>
            <li>
                <h3>Tampa Location</h3>
                <p>456 Elm St, Tampa, FL 33601</p>
            </li>
        </ul>
    </section>

    <!-- FAQ Section -->
    <section id="faq">
        <h2>Frequently Asked Questions</h2>
        <dl>
            <dt>Q: What is plasma donation?</dt>
            <dd>A: Plasma donation is the process of collecting plasma, a component of blood, from donors.</dd>
            <dt>Q: Is plasma donation safe?</dt>
            <dd>A: Yes, plasma donation is a safe and regulated process.</dd>
        </dl>
    </section>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 Plasma Donation Center</p>
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
    display: flex;
    justify-content: space-between;
}

header nav ul li {
    margin-right: 20px;
}

header nav a {
    color: #fff;
    text-decoration: none;
}

/* Hero Styles */
#hero {
    background-image: linear-gradient(to bottom, #333, #555);
    background-size: 100% 300px;
    background-position: 0% 100%;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #fff;
}

#hero h1 {
    font-size: 48px;
}

/* Section Styles */
section {
    padding: 2em;
    background-color: #fff;
    margin-bottom: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

section h2 {
    font-size: 24px;
    margin-bottom: 10px;
}

/* Locations Styles */
#locations ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

#locations li {
    margin-bottom: 20px;
}

#locations h3 {
    font-size: 18px;
    margin-bottom: 5px;
}

/* FAQ Styles */
#faq dl {
    margin-bottom: 20px;
}

#faq dt {
    font-weight: bold;
    margin-bottom: 5px;
}

#faq dd {
    margin-left: 20px;
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
