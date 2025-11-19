"""
Generated Code Metadata:
========================
Original URL: https://marinendtbd.com
Prompt: "What are the key features of a company profile page for a NDT service provider in Bangladesh, and how can it be implemented using HTML and CSS?"
Generated: DETERMINISTIC_761251695d08ec95
Batch ID: 20250622_211142
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NDT Service Provider Company Profile</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <ul>
                <li><a href="#about">About Us</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#contact">Contact Us</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section id="hero">
        <h1>Welcome to [Company Name]</h1>
        <p>Leading NDT Service Provider in Bangladesh</p>
        <button>Learn More</button>
    </section>

    <!-- About Section -->
    <section id="about">
        <h2>About Us</h2>
        <p>[Company Name] is a leading provider of Non-Destructive Testing (NDT) services in Bangladesh. Our team of experts provides high-quality services to ensure the integrity and reliability of your assets.</p>
    </section>

    <!-- Services Section -->
    <section id="services">
        <h2>Our Services</h2>
        <ul>
            <li>Radiography Testing</li>
            <li>Ultrasonic Testing</li>
            <li>Magnaflux Testing</li>
            <li>Acoustic Emission Testing</li>
        </ul>
    </section>

    <!-- Contact Section -->
    <section id="contact">
        <h2>Get in Touch</h2>
        <p>Phone: +880 1234 567890</p>
        <p>Email: <a href="mailto:info@company.com">info@company.com</a></p>
        <p>Address: [Company Address]</p>
    </section>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 [Company Name]. All Rights Reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

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

#hero p {
    font-size: 18px;
}

#hero button {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 18px;
    cursor: pointer;
}

#about, #services, #contact {
    padding: 2em;
}

#about h2, #services h2, #contact h2 {
    font-size: 24px;
    margin-bottom: 10px;
}

footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}
```
